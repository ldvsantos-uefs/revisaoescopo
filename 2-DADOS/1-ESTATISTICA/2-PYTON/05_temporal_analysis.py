#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ANÁLISE DE SÉRIES TEMPORAIS
Corpus: Machine Learning aplicado a Indicações Geográficas
Objetivo: Analisar evolução temporal de técnicas, produtos e aplicações (2010-2025)
"""

import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr, spearmanr
from scipy.signal import savgol_filter
import warnings
warnings.filterwarnings('ignore')

# Configuração
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("tab10")

# ============================================================================
# EXTRAÇÃO DE DADOS TEMPORAIS
# ============================================================================

def extrair_dados_temporais(caminho_bib):
    """
    Extrai dados anuais do corpus
    """
    with open(caminho_bib, 'r', encoding='utf-8', errors='ignore') as f:
        conteudo = f.read()
    
    entradas = re.split(r'\n\n% Score:', conteudo)
    dados = []
    
    for entrada in entradas[1:]:
        try:
            score_match = re.search(r'^([\d.]+)', entrada)
            score = float(score_match.group(1)) if score_match else 0
            
            ano_match = re.search(r'year = \{(\d{4})\}', entrada)
            ano = int(ano_match.group(1)) if ano_match else 0
            
            if ano < 2010 or ano > 2025:
                continue
            
            id_match = re.search(r'@ARTICLE\{([^,]+),', entrada)
            id_ref = id_match.group(1) if id_match else "Unknown"
            
            titulo_match = re.search(r'title = \{([^}]+)\}', entrada)
            titulo = titulo_match.group(1) if titulo_match else ""
            
            keywords_match = re.search(r'keywords = \{([^}]+)\}', entrada)
            keywords = keywords_match.group(1).lower() if keywords_match else ""
            
            abstract_match = re.search(r'abstract = \{([^}]+)\}', entrada)
            abstract = abstract_match.group(1).lower() if abstract_match else ""
            
            texto = f"{titulo} {keywords} {abstract}".lower()
            
            # Classificar características
            caracteristicas = {
                'ano': ano,
                'id': id_ref,
                'score': score,
                
                # Algoritmos
                'random_forest': int(bool(re.search(r'random forest', texto))),
                'svm': int(bool(re.search(r'support vector machine|svm', texto))),
                'neural_network': int(bool(re.search(r'neural network|ann|deep learning|cnn', texto))),
                'pls_da': int(bool(re.search(r'pls-da|partial least squares', texto))),
                
                # Instrumentos
                'nir': int(bool(re.search(r'nir|near.infrared', texto))),
                'gc_ms': int(bool(re.search(r'gc-ms|gas chromatography', texto))),
                'icp_ms': int(bool(re.search(r'icp-ms|inductively coupled', texto))),
                'nmr': int(bool(re.search(r'nmr|nuclear magnetic', texto))),
                
                # Produtos
                'wine': int(bool(re.search(r'wine|vinho', texto))),
                'tea': int(bool(re.search(r'\btea\b|chá', texto))),
                'meat': int(bool(re.search(r'meat|carne|lamb|beef', texto))),
                'oil': int(bool(re.search(r'oil|olive|azeite', texto))),
                
                # Aplicações
                'authentication': int(bool(re.search(r'authentication', texto))),
                'traceability': int(bool(re.search(r'traceability', texto))),
                'fraud': int(bool(re.search(r'fraud|adulteration', texto))),
                
                # Regiões
                'asia': int(bool(re.search(r'china|japan|korea', texto))),
                'europe': int(bool(re.search(r'italy|spain|france|portugal', texto))),
                'americas': int(bool(re.search(r'brazil|america|usa', texto))),
                
                # Técnicas avançadas
                'metabolomics': int(bool(re.search(r'metabolomics|metabolômica', texto))),
                'deep_learning': int(bool(re.search(r'deep learning', texto))),
                'transfer_learning': int(bool(re.search(r'transfer learning', texto))),
            }
            
            dados.append(caracteristicas)
            
        except Exception as e:
            print(f"Erro: {e}")
            continue
    
    return pd.DataFrame(dados)

# ============================================================================
# ANÁLISE TEMPORAL
# ============================================================================

def agregar_por_ano(df):
    """
    Agrega dados por ano
    """
    # Total de publicações por ano
    pub_por_ano = df.groupby('ano').size().reset_index(name='total_publicacoes')
    
    # Características por ano (somatório e proporção)
    features = [col for col in df.columns if col not in ['ano', 'id', 'score']]
    
    agregado = df.groupby('ano')[features].agg(['sum', 'mean']).reset_index()
    agregado.columns = ['_'.join(col).strip('_') for col in agregado.columns]
    
    # Merge
    resultado = pub_por_ano.merge(agregado, on='ano')
    
    return resultado

def calcular_tendencias(df_temporal):
    """
    Calcula tendências lineares (correlação com tempo)
    """
    anos = df_temporal['ano'].values
    
    tendencias = {}
    
    for col in df_temporal.columns:
        if col == 'ano':
            continue
        
        valores = df_temporal[col].values
        
        # Correlação de Pearson
        corr_pearson, p_pearson = pearsonr(anos, valores)
        
        # Correlação de Spearman (monotônica, robusta a outliers)
        corr_spearman, p_spearman = spearmanr(anos, valores)
        
        # Regressão linear simples
        coef = np.polyfit(anos, valores, 1)
        
        tendencias[col] = {
            'pearson_r': corr_pearson,
            'pearson_p': p_pearson,
            'spearman_r': corr_spearman,
            'spearman_p': p_spearman,
            'inclinacao': coef[0],
            'intercepto': coef[1]
        }
    
    return pd.DataFrame(tendencias).T

# ============================================================================
# VISUALIZAÇÕES
# ============================================================================

def plot_publicacoes_tempo(df_temporal, output_path):
    """
    Evolução do número de publicações ao longo do tempo
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    
    anos = df_temporal['ano'].values
    pubs = df_temporal['total_publicacoes'].values
    
    # Gráfico de barras
    ax.bar(anos, pubs, color='steelblue', alpha=0.7, edgecolor='black', label='Publicações Anuais')
    
    # Linha de tendência
    z = np.polyfit(anos, pubs, 2)
    p = np.poly1d(z)
    anos_fit = np.linspace(anos.min(), anos.max(), 100)
    ax.plot(anos_fit, p(anos_fit), color='red', linewidth=3, linestyle='--', label='Tendência Polinomial')
    
    ax.set_xlabel('Ano', fontsize=12, fontweight='bold')
    ax.set_ylabel('Número de Publicações', fontsize=12, fontweight='bold')
    ax.set_title('Evolução Temporal do Corpus (2010-2025)', fontsize=14, fontweight='bold')
    ax.legend(fontsize=11)
    ax.grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Gráfico de publicações salvo: {output_path}")

def plot_algoritmos_tempo(df, output_path):
    """
    Evolução da adoção de algoritmos ML
    """
    # Agrupar por ano
    algoritmos = ['random_forest', 'svm', 'neural_network', 'pls_da']
    dados_alg = df.groupby('ano')[algoritmos].sum()
    
    fig, ax = plt.subplots(figsize=(14, 7))
    
    for alg in algoritmos:
        ax.plot(dados_alg.index, dados_alg[alg], marker='o', linewidth=2.5, 
                label=alg.replace('_', ' ').title())
    
    ax.set_xlabel('Ano', fontsize=12, fontweight='bold')
    ax.set_ylabel('Número de Estudos', fontsize=12, fontweight='bold')
    ax.set_title('Evolução da Adoção de Algoritmos ML (2010-2025)', fontsize=14, fontweight='bold')
    ax.legend(fontsize=11, loc='upper left')
    ax.grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Gráfico de algoritmos salvo: {output_path}")

def plot_produtos_tempo(df, output_path):
    """
    Evolução de produtos estudados
    """
    produtos = ['wine', 'tea', 'meat', 'oil']
    dados_prod = df.groupby('ano')[produtos].sum()
    
    fig, ax = plt.subplots(figsize=(14, 7))
    
    for prod in produtos:
        ax.plot(dados_prod.index, dados_prod[prod], marker='s', linewidth=2.5, 
                label=prod.capitalize())
    
    ax.set_xlabel('Ano', fontsize=12, fontweight='bold')
    ax.set_ylabel('Número de Estudos', fontsize=12, fontweight='bold')
    ax.set_title('Evolução de Produtos Estudados (2010-2025)', fontsize=14, fontweight='bold')
    ax.legend(fontsize=11, loc='upper left')
    ax.grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Gráfico de produtos salvo: {output_path}")

def plot_regioes_tempo(df, output_path):
    """
    Evolução geográfica das publicações
    """
    regioes = ['asia', 'europe', 'americas']
    dados_reg = df.groupby('ano')[regioes].sum()
    
    fig, ax = plt.subplots(figsize=(14, 7))
    
    cores = ['orange', 'blue', 'green']
    for i, reg in enumerate(regioes):
        ax.plot(dados_reg.index, dados_reg[reg], marker='D', linewidth=2.5, 
                color=cores[i], label=reg.capitalize())
    
    ax.set_xlabel('Ano', fontsize=12, fontweight='bold')
    ax.set_ylabel('Número de Estudos', fontsize=12, fontweight='bold')
    ax.set_title('Distribuição Geográfica das Publicações (2010-2025)', fontsize=14, fontweight='bold')
    ax.legend(fontsize=11, loc='upper left')
    ax.grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Gráfico de regiões salvo: {output_path}")

def plot_heatmap_temporal(df, output_path):
    """
    Heatmap de evolução temporal de todas características
    """
    features = ['random_forest', 'svm', 'neural_network', 'pls_da',
                'nir', 'gc_ms', 'icp_ms', 'nmr',
                'wine', 'tea', 'meat', 'oil',
                'authentication', 'traceability', 'fraud',
                'metabolomics', 'deep_learning']
    
    dados_heat = df.groupby('ano')[features].sum().T
    
    # Normalizar por linha (0-1)
    dados_heat_norm = dados_heat.div(dados_heat.max(axis=1), axis=0)
    
    fig, ax = plt.subplots(figsize=(16, 10))
    
    sns.heatmap(
        dados_heat_norm, cmap='YlGnBu', annot=False,
        linewidths=0.5, cbar_kws={'label': 'Intensidade Normalizada'}, ax=ax
    )
    
    ax.set_xlabel('Ano', fontsize=12, fontweight='bold')
    ax.set_ylabel('Características', fontsize=12, fontweight='bold')
    ax.set_title('Heatmap Temporal: Evolução de Características (2010-2025)', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Heatmap temporal salvo: {output_path}")

def plot_tendencias_significativas(tendencias_df, output_path):
    """
    Gráfico de barras de tendências significativas (p < 0.05)
    """
    # Filtrar por p-valor significativo
    tendencias_sig = tendencias_df[tendencias_df['pearson_p'] < 0.05].copy()
    tendencias_sig = tendencias_sig.sort_values('pearson_r', ascending=False)
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    cores = ['green' if r > 0 else 'red' for r in tendencias_sig['pearson_r']]
    
    ax.barh(range(len(tendencias_sig)), tendencias_sig['pearson_r'], color=cores, alpha=0.7, edgecolor='black')
    ax.set_yticks(range(len(tendencias_sig)))
    ax.set_yticklabels(tendencias_sig.index)
    ax.set_xlabel('Correlação de Pearson (r)', fontsize=12, fontweight='bold')
    ax.set_title('Tendências Temporais Significativas (p < 0.05)', fontsize=14, fontweight='bold')
    ax.axvline(0, color='black', linewidth=1)
    ax.grid(alpha=0.3, axis='x')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Gráfico de tendências salvo: {output_path}")

def plot_acumulado_stackplot(df, output_path):
    """
    Gráfico de área empilhada (stackplot) para algoritmos
    """
    algoritmos = ['random_forest', 'svm', 'neural_network', 'pls_da']
    dados_alg = df.groupby('ano')[algoritmos].sum()
    
    fig, ax = plt.subplots(figsize=(14, 7))
    
    ax.stackplot(
        dados_alg.index, 
        [dados_alg[alg] for alg in algoritmos],
        labels=[alg.replace('_', ' ').title() for alg in algoritmos],
        alpha=0.8
    )
    
    ax.set_xlabel('Ano', fontsize=12, fontweight='bold')
    ax.set_ylabel('Número Acumulado de Estudos', fontsize=12, fontweight='bold')
    ax.set_title('Distribuição Acumulada de Algoritmos ML (2010-2025)', fontsize=14, fontweight='bold')
    ax.legend(loc='upper left', fontsize=11)
    ax.grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Stackplot salvo: {output_path}")

# ============================================================================
# RELATÓRIO
# ============================================================================

def gerar_relatorio(df, df_temporal, tendencias_df, output_path):
    """
    Relatório de análise temporal
    """
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("="*80 + "\n")
        f.write("RELATÓRIO DE ANÁLISE DE SÉRIES TEMPORAIS\n")
        f.write("Corpus: Machine Learning para Indicações Geográficas (2010-2025)\n")
        f.write("="*80 + "\n\n")
        
        f.write(f"Total de estudos: {len(df)}\n")
        f.write(f"Período: {df['ano'].min()} - {df['ano'].max()}\n")
        f.write(f"Publicações médias por ano: {len(df) / (df['ano'].max() - df['ano'].min() + 1):.2f}\n\n")
        
        f.write("-"*80 + "\n")
        f.write("PUBLICAÇÕES POR ANO\n")
        f.write("-"*80 + "\n")
        for _, row in df_temporal.iterrows():
            f.write(f"{int(row['ano'])}: {int(row['total_publicacoes'])} publicações\n")
        
        f.write("\n" + "-"*80 + "\n")
        f.write("TENDÊNCIAS TEMPORAIS SIGNIFICATIVAS (p < 0.05)\n")
        f.write("-"*80 + "\n")
        
        tendencias_sig = tendencias_df[tendencias_df['pearson_p'] < 0.05].copy()
        tendencias_sig = tendencias_sig.sort_values('pearson_r', ascending=False)
        
        f.write("\nTENDÊNCIAS CRESCENTES:\n")
        for idx, row in tendencias_sig[tendencias_sig['pearson_r'] > 0].iterrows():
            f.write(f"  {idx:25s}: r={row['pearson_r']:+.3f}, p={row['pearson_p']:.4f}\n")
        
        f.write("\nTENDÊNCIAS DECRESCENTES:\n")
        for idx, row in tendencias_sig[tendencias_sig['pearson_r'] < 0].iterrows():
            f.write(f"  {idx:25s}: r={row['pearson_r']:+.3f}, p={row['pearson_p']:.4f}\n")
        
        f.write("\n" + "-"*80 + "\n")
        f.write("ANÁLISE POR PERÍODO\n")
        f.write("-"*80 + "\n")
        
        periodos = {
            '2010-2014': (2010, 2014),
            '2015-2019': (2015, 2019),
            '2020-2025': (2020, 2025)
        }
        
        for nome, (inicio, fim) in periodos.items():
            subset = df[(df['ano'] >= inicio) & (df['ano'] <= fim)]
            f.write(f"\nPeríodo {nome}:\n")
            f.write(f"  Total de publicações: {len(subset)}\n")
            f.write(f"  Score médio: {subset['score'].mean():.2f}\n")
            f.write(f"  Principais algoritmos:\n")
            for alg in ['random_forest', 'svm', 'neural_network']:
                freq = subset[alg].sum()
                pct = (freq / len(subset)) * 100
                f.write(f"    {alg:20s}: {freq:3d} ({pct:5.1f}%)\n")
        
        f.write("\n" + "="*80 + "\n")
        f.write("FIM DO RELATÓRIO\n")
        f.write("="*80 + "\n")
    
    print(f"✓ Relatório salvo: {output_path}")

# ============================================================================
# MAIN
# ============================================================================

def main():
    """
    Função principal
    """
    print("\n" + "="*80)
    print("ANÁLISE DE SÉRIES TEMPORAIS")
    print("Machine Learning para Indicações Geográficas (2010-2025)")
    print("="*80 + "\n")
    
    caminho_bib = "../referencias_filtradas/referencias_ML_IG_filtradas.bib"
    output_dir = "."
    
    # 1. Extrair dados
    print("📚 Extraindo dados temporais...")
    df = extrair_dados_temporais(caminho_bib)
    print(f"✓ Total de estudos (2010-2025): {len(df)}")
    
    # 2. Agregar por ano
    print("\n📊 Agregando dados por ano...")
    df_temporal = agregar_por_ano(df)
    print(f"✓ Dados agregados para {len(df_temporal)} anos")
    
    # 3. Calcular tendências
    print("\n📈 Calculando tendências temporais...")
    tendencias_df = calcular_tendencias(df_temporal)
    n_sig = len(tendencias_df[tendencias_df['pearson_p'] < 0.05])
    print(f"✓ Tendências calculadas: {n_sig} significativas (p < 0.05)")
    
    # 4. Visualizações
    print("\n🎨 Gerando visualizações...")
    plot_publicacoes_tempo(df_temporal, f"{output_dir}/temporal_publicacoes.png")
    plot_algoritmos_tempo(df, f"{output_dir}/temporal_algoritmos.png")
    plot_produtos_tempo(df, f"{output_dir}/temporal_produtos.png")
    plot_regioes_tempo(df, f"{output_dir}/temporal_regioes.png")
    plot_heatmap_temporal(df, f"{output_dir}/temporal_heatmap.png")
    plot_tendencias_significativas(tendencias_df, f"{output_dir}/temporal_tendencias_sig.png")
    plot_acumulado_stackplot(df, f"{output_dir}/temporal_stackplot.png")
    
    # 5. Relatório
    print("\n📝 Gerando relatório...")
    gerar_relatorio(df, df_temporal, tendencias_df, f"{output_dir}/temporal_relatorio.txt")
    
    # 6. Salvar dados
    df.to_csv(f"{output_dir}/temporal_dados_completos.csv", index=False)
    df_temporal.to_csv(f"{output_dir}/temporal_agregado_anual.csv", index=False)
    tendencias_df.to_csv(f"{output_dir}/temporal_tendencias.csv")
    print(f"\n✓ Dados salvos: temporal_*.csv")
    
    print("\n" + "="*80)
    print("✅ ANÁLISE TEMPORAL CONCLUÍDA COM SUCESSO!")
    print("="*80 + "\n")

if __name__ == "__main__":
    main()
