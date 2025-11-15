#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para gerar arquivos Word com referências a partir do Markdown
Uso: python gerar-docx.py
Gera artigo.docx (Português) e artigo_ENGLISH.docx (English)
"""

import os
import subprocess
import sys
from pathlib import Path
import time

def gerar_docx(md_file, output_file, bib_file, csl_file, apendices_file=None):
    """
    Gera arquivo DOCX usando Pandoc
    
    Args:
        md_file: Arquivo Markdown de entrada
        output_file: Arquivo DOCX de saída
        bib_file: Arquivo de bibliografia
        csl_file: Arquivo de estilo de citação
        apendices_file: Arquivo de apêndices (opcional)
    
    Returns:
        0 se sucesso, 1 se erro
    """
    print(f"\n🔄 Gerando {output_file.name}...")
    
    # Remover arquivo antigo se existir
    if output_file.exists():
        print(f"📝 Removendo arquivo antigo: {output_file.name}")
        max_attempts = 5
        for attempt in range(max_attempts):
            try:
                output_file.unlink()
                break
            except PermissionError:
                if attempt < max_attempts - 1:
                    print(f"⚠️  Tentativa {attempt + 1}/{max_attempts}: Arquivo em uso, aguardando...")
                    time.sleep(0.6)
                else:
                    print(f"❌ Erro: Não foi possível remover '{output_file.name}'.")
                    print("   Certifique-se de que o arquivo não está aberto no Word ou OneDrive.")
                    return 1
    
    # Comando Pandoc
    cmd = [
        "pandoc",
        str(md_file),
    ]
    
    # Adicionar apêndices ANTES do --citeproc
    if apendices_file and apendices_file.exists():
        cmd.append(str(apendices_file))
        print(f"📎 Incluindo apêndices: {apendices_file.name}")
    
    # Adicionar processamento de citações
    # Temporariamente desabilitado devido a problemas no arquivo .bib
    # cmd.extend([
    #     "--citeproc",
    #     "--bibliography", str(bib_file),
    #     "--csl", str(csl_file),
    # ])
    
    # Adicionar modelo de formatação se existir
    modelo = Path("modelo_formatacao.docx")
    if modelo.exists():
        cmd.extend(["--reference-doc", str(modelo)])
    
    cmd.extend(["-o", str(output_file)])
    
    print(f"� Executando Pandoc...")
    
    try:
        # Executar Pandoc
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace'
        )
        
        # Mostrar warnings/erros do Pandoc
        if result.stderr:
            print(f"\n⚠️  Avisos do Pandoc para {output_file.name}:")
            print(result.stderr)
        
        # Verificar se o arquivo foi criado
        if output_file.exists():
            print(f"\n✅ Arquivo {output_file.name} gerado com sucesso!")
            print(f"📍 Localização: {output_file.absolute()}")
            print(f"📊 Tamanho: {output_file.stat().st_size / 1024:.1f} KB")
            return 0
        else:
            print(f"\n❌ Erro: O arquivo {output_file.name} não foi gerado!")
            if result.stdout:
                print("Saída:", result.stdout)
            return 1
            
    except FileNotFoundError:
        print("\n❌ Erro: Pandoc não está instalado ou não está no PATH do sistema!")
        print("   Instale o Pandoc em: https://pandoc.org/installing.html")
        return 1
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        return 1

def main():
    # Mudar para o diretório do script
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    print("=" * 70)
    print("📚 GERADOR DE REVISÃO DE ESCOPO - WORD")
    print("=" * 70)
    
    # Arquivos comuns
    bib_file = Path("referencias.bib")
    csl_file = Path("apa.csl")
    apendices_pt = Path("apendices.md")
    
    # Verificar arquivos necessários
    arquivos_necessarios = [bib_file, csl_file]
    arquivos_faltando = [f for f in arquivos_necessarios if not f.exists()]
    
    if arquivos_faltando:
        print("\n❌ Erro: Arquivos necessários não encontrados:")
        for arquivo in arquivos_faltando:
            print(f"   - {arquivo}")
        return 1
    
    # Contador de sucesso
    sucessos = 0
    total = 1
    
    # ========================================================================
    # GERAR REVISÃO DE ESCOPO
    # ========================================================================
    md_rs = Path("revisao_escopo.md")
    docx_rs = Path("revisao_escopo.docx")
    
    if not md_rs.exists():
        print(f"\n⚠️  Arquivo {md_rs} não encontrado, pulando...")
    else:
        result = gerar_docx(md_rs, docx_rs, bib_file, csl_file)
        if result == 0:
            sucessos += 1
    
    # ========================================================================
    # RESUMO FINAL
    # ========================================================================
    print("\n" + "=" * 70)
    print("📊 RESUMO DA GERAÇÃO")
    print("=" * 70)
    print(f"✅ Arquivos gerados com sucesso: {sucessos}/{total}")
    
    if sucessos == total:
        print("\n🎉 Todos os arquivos foram gerados com sucesso!")
        return 0
    elif sucessos > 0:
        print(f"\n⚠️  Alguns arquivos não foram gerados ({total - sucessos} falharam)")
        return 1
    else:
        print("\n❌ Nenhum arquivo foi gerado!")
        return 1

if __name__ == "__main__":
    sys.exit(main())
