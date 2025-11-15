#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SISTEMA INTEGRADO DE VERIFICAÇÃO - REVISÃO DE ESCOPO
Tema: Machine Learning aplicado a Indicações Geográficas
Combina: Filtragem + Verificação de Citações
"""

import re
import os
from typing import List, Set, Dict, Tuple

# ============================================================================
# PARTE 1: EXTRAÇÃO E VERIFICAÇÃO DE CITAÇÕES
# ============================================================================

def extrair_citacoes_markdown(arquivo_md: str) -> Set[str]:
    """
    Extrai citações do formato Markdown: [@Autor2020] ou [@Autor2020; @Autor2021]
    """
    citacoes = set()
    
    print(f"📖 Extraindo citações de {arquivo_md}...")
    
    try:
        with open(arquivo_md, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
        
        # Padrão para [@Autor2020] ou [@Autor2020; @Autor2021; ...]
        padrao_cite = r'\[@([^\]]+)\]'
        matches = re.findall(padrao_cite, conteudo)
        
        for match in matches:
            # Separar múltiplas citações separadas por ;
            refs = [ref.strip().lstrip('@') for ref in match.split(';')]
            citacoes.update(refs)
        
        print(f"   ✅ {len(citacoes)} citações únicas encontradas")
        return citacoes
    
    except FileNotFoundError:
        print(f"   ❌ {arquivo_md} não encontrado!")
        return set()

def extrair_chaves_bib(arquivo_bib: str) -> Dict[str, Dict[str, str]]:
    """
    Extrai chaves e informações básicas do arquivo BibTeX
    """
    referencias = {}
    ref_atual = None
    
    print(f"\n📚 Processando {arquivo_bib}...")
    
    try:
        with open(arquivo_bib, 'r', encoding='utf-8', errors='ignore') as arquivo:
            for linha in arquivo:
                # Nova entrada começa com @
                if linha.strip().startswith('@'):
                    match = re.match(r'@(\w+)\{([^,]+),', linha)
                    if match:
                        tipo, chave = match.groups()
                        chave = chave.strip()
                        referencias[chave] = {
                            'tipo': tipo,
                            'chave': chave,
                            'title': '',
                            'author': '',
                            'year': ''
                        }
                        ref_atual = chave
                
                elif ref_atual:
                    # Extrair campos title, author, year
                    for campo in ['title', 'author', 'year']:
                        padrao = rf'{campo}\s*=\s*\{{(.+?)}},'
                        match = re.search(padrao, linha, re.IGNORECASE)
                        if match:
                            referencias[ref_atual][campo] = match.group(1).strip()
        
        print(f"   ✅ {len(referencias)} referências processadas")
        return referencias
    
    except FileNotFoundError:
        print(f"   ❌ {arquivo_bib} não encontrado!")
        return {}

def verificar_cobertura_citacoes(citacoes: Set[str], referencias: Dict[str, Dict]) -> Tuple[Set[str], Set[str]]:
    """
    Verifica quais citações estão presentes no corpus bibliográfico
    """
    chaves_disponiveis = set(referencias.keys())
    
    citacoes_encontradas = citacoes.intersection(chaves_disponiveis)
    citacoes_faltantes = citacoes - chaves_disponiveis
    
    return citacoes_encontradas, citacoes_faltantes

# ============================================================================
# PARTE 2: ESTATÍSTICAS DO CORPUS
# ============================================================================

def analisar_distribuicao_temporal(referencias: Dict[str, Dict]) -> Dict[str, int]:
    """
    Analisa distribuição temporal das referências
    """
    distribuicao = {}
    
    for ref in referencias.values():
        year = ref.get('year', 'N/A')[:4]
        if year and year.isdigit():
            distribuicao[year] = distribuicao.get(year, 0) + 1
    
    return dict(sorted(distribuicao.items()))

def identificar_top_autores(referencias: Dict[str, Dict], top_n: int = 10) -> List[Tuple[str, int]]:
    """
    Identifica autores mais citados no corpus
    """
    autores = {}
    
    for ref in referencias.values():
        autor_str = ref.get('author', '')
        if autor_str:
            # Pegar primeiro autor (antes da vírgula ou 'and')
            primeiro_autor = re.split(r',|and', autor_str)[0].strip()
            if primeiro_autor:
                autores[primeiro_autor] = autores.get(primeiro_autor, 0) + 1
    
    return sorted(autores.items(), key=lambda x: x[1], reverse=True)[:top_n]

# ============================================================================
# PARTE 3: RELATÓRIOS
# ============================================================================

def gerar_relatorio_completo(
    arquivo_manuscrito: str,
    arquivo_corpus: str,
    citacoes: Set[str],
    referencias: Dict[str, Dict],
    citacoes_encontradas: Set[str],
    citacoes_faltantes: Set[str]
):
    """
    Gera relatório completo de verificação
    """
    arquivo_relatorio = '../relatorios/relatorio_verificacao_escopo.txt'
    
    # Análises adicionais
    distribuicao_temporal = analisar_distribuicao_temporal(referencias)
    top_autores = identificar_top_autores(referencias)
    
    with open(arquivo_relatorio, 'w', encoding='utf-8') as rel:
        rel.write("=" * 80 + "\n")
        rel.write("RELATÓRIO DE VERIFICAÇÃO - REVISÃO DE ESCOPO\n")
        rel.write("Tema: Machine Learning aplicado a Indicações Geográficas\n")
        rel.write("=" * 80 + "\n\n")
        
        # Seção 1: Cobertura de Citações
        rel.write("📊 COBERTURA DE CITAÇÕES\n")
        rel.write("-" * 80 + "\n")
        rel.write(f"Manuscrito analisado: {arquivo_manuscrito}\n")
        rel.write(f"Corpus bibliográfico: {arquivo_corpus}\n\n")
        rel.write(f"Total de citações no manuscrito: {len(citacoes)}\n")
        rel.write(f"Citações encontradas no corpus: {len(citacoes_encontradas)} ({len(citacoes_encontradas)/len(citacoes)*100:.1f}%)\n")
        rel.write(f"Citações faltantes: {len(citacoes_faltantes)} ({len(citacoes_faltantes)/len(citacoes)*100 if citacoes else 0:.1f}%)\n\n")
        
        if citacoes_encontradas:
            rel.write(f"✅ CITAÇÕES PRESENTES ({len(citacoes_encontradas)}):\n")
            for cit in sorted(citacoes_encontradas):
                ref = referencias[cit]
                titulo = ref.get('title', 'Sem título')[:60]
                ano = ref.get('year', 'N/A')[:4]
                rel.write(f"  • [{ano}] {cit}\n")
                rel.write(f"    {titulo}...\n")
        
        if citacoes_faltantes:
            rel.write(f"\n❌ CITAÇÕES FALTANTES ({len(citacoes_faltantes)}):\n")
            for cit in sorted(citacoes_faltantes):
                rel.write(f"  • {cit}\n")
            rel.write("\n⚠️  AÇÃO NECESSÁRIA: Adicionar estas referências ao corpus ou remover do manuscrito\n")
        
        # Seção 2: Estatísticas do Corpus
        rel.write("\n\n📚 ESTATÍSTICAS DO CORPUS BIBLIOGRÁFICO\n")
        rel.write("-" * 80 + "\n")
        rel.write(f"Total de referências no corpus: {len(referencias)}\n")
        rel.write(f"Referências citadas no manuscrito: {len(citacoes_encontradas)}\n")
        rel.write(f"Referências NÃO citadas: {len(referencias) - len(citacoes_encontradas)}\n\n")
        
        # Seção 3: Distribuição Temporal
        rel.write("📅 DISTRIBUIÇÃO TEMPORAL DAS REFERÊNCIAS\n")
        rel.write("-" * 80 + "\n")
        for ano, count in distribuicao_temporal.items():
            barra = "█" * (count // 2)
            rel.write(f"{ano}: {barra} ({count})\n")
        
        # Seção 4: Top Autores
        rel.write(f"\n\n👥 TOP {len(top_autores)} AUTORES MAIS PRESENTES NO CORPUS\n")
        rel.write("-" * 80 + "\n")
        for i, (autor, count) in enumerate(top_autores, 1):
            rel.write(f"{i:2d}. {autor:<40} ({count} refs)\n")
        
        # Seção 5: Recomendações
        rel.write("\n\n💡 RECOMENDAÇÕES\n")
        rel.write("-" * 80 + "\n")
        
        taxa_cobertura = len(citacoes_encontradas) / len(citacoes) * 100 if citacoes else 0
        
        if taxa_cobertura == 100:
            rel.write("✅ EXCELENTE: Todas as citações estão no corpus!\n")
        elif taxa_cobertura >= 95:
            rel.write("✅ MUITO BOM: Cobertura quase completa.\n")
            rel.write(f"   → Revisar {len(citacoes_faltantes)} citação(ões) faltante(s)\n")
        elif taxa_cobertura >= 80:
            rel.write("⚠️  BOM: Boa cobertura, mas há espaço para melhoria.\n")
            rel.write(f"   → Adicionar {len(citacoes_faltantes)} referências ao corpus\n")
        else:
            rel.write("❌ ATENÇÃO: Cobertura insuficiente!\n")
            rel.write(f"   → Revisar e adicionar {len(citacoes_faltantes)} referências\n")
        
        taxa_uso = len(citacoes_encontradas) / len(referencias) * 100 if referencias else 0
        rel.write(f"\n📈 Taxa de uso do corpus: {taxa_uso:.1f}%\n")
        
        if taxa_uso < 50:
            rel.write("   → Considerar revisão do corpus (muitas refs não utilizadas)\n")
        elif taxa_uso > 80:
            rel.write("   → Corpus bem aproveitado!\n")
        
        rel.write("\n" + "=" * 80 + "\n")
    
    print(f"\n💾 Relatório salvo em: {arquivo_relatorio}")

def exibir_resumo_terminal(
    citacoes: Set[str],
    referencias: Dict[str, Dict],
    citacoes_encontradas: Set[str],
    citacoes_faltantes: Set[str]
):
    """
    Exibe resumo no terminal
    """
    print("\n" + "=" * 80)
    print("📋 RESUMO DA VERIFICAÇÃO")
    print("=" * 80)
    
    print(f"\n📊 COBERTURA DE CITAÇÕES:")
    print(f"  • Total de citações: {len(citacoes)}")
    print(f"  • Encontradas: {len(citacoes_encontradas)} ({len(citacoes_encontradas)/len(citacoes)*100 if citacoes else 0:.1f}%)")
    print(f"  • Faltantes: {len(citacoes_faltantes)} ({len(citacoes_faltantes)/len(citacoes)*100 if citacoes else 0:.1f}%)")
    
    print(f"\n📚 CORPUS BIBLIOGRÁFICO:")
    print(f"  • Total de referências: {len(referencias)}")
    print(f"  • Citadas no manuscrito: {len(citacoes_encontradas)}")
    print(f"  • Taxa de uso: {len(citacoes_encontradas)/len(referencias)*100 if referencias else 0:.1f}%")
    
    if citacoes_faltantes:
        print(f"\n❌ CITAÇÕES FALTANTES NO CORPUS:")
        for cit in sorted(list(citacoes_faltantes)[:10]):
            print(f"  • {cit}")
        if len(citacoes_faltantes) > 10:
            print(f"  ... e mais {len(citacoes_faltantes) - 10}")
    else:
        print(f"\n✅ TODAS AS CITAÇÕES ESTÃO NO CORPUS!")

# ============================================================================
# FUNÇÃO PRINCIPAL
# ============================================================================

def main():
    """
    Executa verificação completa da revisão de escopo
    """
    print("=" * 80)
    print("🔍 SISTEMA INTEGRADO DE VERIFICAÇÃO - REVISÃO DE ESCOPO")
    print("Tema: Machine Learning aplicado a Indicações Geográficas")
    print("=" * 80 + "\n")
    
    # Configuração de arquivos
    arquivo_manuscrito = '../../1-MANUSCRITO/revisao_escopo.md'
    arquivo_corpus = '../scopus_export_Nov 4-2025_d3228730-6773-48d3-8a0c-1aa5ad56f628.bib'
    
    # Verificar existência dos arquivos
    if not os.path.exists(arquivo_manuscrito):
        print(f"❌ Manuscrito não encontrado: {arquivo_manuscrito}")
        return
    
    if not os.path.exists(arquivo_corpus):
        print(f"❌ Corpus não encontrado: {arquivo_corpus}")
        return
    
    # ETAPA 1: Extrair citações do manuscrito
    citacoes = extrair_citacoes_markdown(arquivo_manuscrito)
    
    if not citacoes:
        print("\n⚠️  Nenhuma citação encontrada no manuscrito!")
        print("    Verifique se o formato está correto: [@Autor2020]")
        return
    
    # ETAPA 2: Processar corpus bibliográfico
    referencias = extrair_chaves_bib(arquivo_corpus)
    
    if not referencias:
        print("\n❌ Erro ao processar corpus bibliográfico!")
        return
    
    # ETAPA 3: Verificar cobertura
    print("\n🔎 Verificando cobertura das citações...")
    citacoes_encontradas, citacoes_faltantes = verificar_cobertura_citacoes(citacoes, referencias)
    
    # ETAPA 4: Gerar relatórios
    gerar_relatorio_completo(
        arquivo_manuscrito,
        arquivo_corpus,
        citacoes,
        referencias,
        citacoes_encontradas,
        citacoes_faltantes
    )
    
    exibir_resumo_terminal(citacoes, referencias, citacoes_encontradas, citacoes_faltantes)
    
    print("\n✅ Verificação concluída!")
    print("=" * 80 + "\n")

if __name__ == '__main__':
    main()
