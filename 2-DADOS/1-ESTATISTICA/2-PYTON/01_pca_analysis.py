#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ANÁLISE DE COMPONENTES PRINCIPAIS (PCA)
Corpus: Machine Learning aplicado a Indicações Geográficas
Objetivo: Identificar padrões latentes e estrutura de variação no corpus
"""

import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from bioinfokit.visuz import cluster
import warnings
warnings.filterwarnings('ignore')

# Configuração de estilo
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# ============================================================================
# EXTRAÇÃO DE DADOS DO ARQUIVO BIB
# ============================================================================

def extrair_dados_bib(caminho_bib):
    """
    Extrai informações estruturadas do arquivo .bib
    """
    with open(caminho_bib, 'r', encoding='utf-8', errors='ignore') as f:
        conteudo = f.read()
    
    # Dividir por entradas
    entradas = re.split(r'\n\n% Score:', conteudo)
    
    dados = []
    
    for entrada in entradas[1:]:  # Pular cabeçalho
        try:
            # Extrair score
            score_match = re.search(r'^([\d.]+)', entrada)
            score = float(score_match.group(1)) if score_match else 0
            
            # Extrair ano
            ano_match = re.search(r'year = \{(\d{4})\}', entrada)
            ano = int(ano_match.group(1)) if ano_match else 0
            
            # Extrair ID
            id_match = re.search(r'@ARTICLE\{([^,]+),', entrada)
            id_ref = id_match.group(1) if id_match else "Unknown"
            
            # Extrair título
            titulo_match = re.search(r'title = \{([^}]+)\}', entrada)
            titulo = titulo_match.group(1) if titulo_match else ""
            
            # Extrair keywords e abstract
            keywords_match = re.search(r'keywords = \{([^}]+)\}', entrada)
            keywords = keywords_match.group(1).lower() if keywords_match else ""
            
            abstract_match = re.search(r'abstract = \{([^}]+)\}', entrada)
            abstract = abstract_match.group(1).lower() if abstract_match else ""
            
            texto_completo = f"{titulo} {keywords} {abstract}".lower()
            
            # Categorizar algoritmos ML
            ml_algorithms = {
                'random_forest': int(bool(re.search(r'random forest', texto_completo))),
                'svm': int(bool(re.search(r'support vector machine|svm', texto_completo))),
                'neural_network': int(bool(re.search(r'neural network|ann|cnn|deep learning', texto_completo))),
                'knn': int(bool(re.search(r'k-nearest neighbor|knn', texto_completo))),
                'decision_tree': int(bool(re.search(r'decision tree', texto_completo))),
                'pls_da': int(bool(re.search(r'pls-da|partial least squares', texto_completo))),
                'naive_bayes': int(bool(re.search(r'naive bayes', texto_completo))),
            }
            
            # Categorizar técnicas instrumentais
            instrumentos = {
                'nir': int(bool(re.search(r'nir|near.infrared|near infrared', texto_completo))),
                'gc_ms': int(bool(re.search(r'gc-ms|gas chromatography', texto_completo))),
                'icp_ms': int(bool(re.search(r'icp-ms|inductively coupled plasma', texto_completo))),
                'nmr': int(bool(re.search(r'nmr|nuclear magnetic', texto_completo))),
                'raman': int(bool(re.search(r'raman', texto_completo))),
                'ftir': int(bool(re.search(r'ftir|infrared spectroscopy', texto_completo))),
            }
            
            # Categorizar produtos
            produtos = {
                'wine': int(bool(re.search(r'wine|vinho|vin\b', texto_completo))),
                'tea': int(bool(re.search(r'\btea\b|chá|thé', texto_completo))),
                'meat': int(bool(re.search(r'meat|carne|lamb|beef|pork', texto_completo))),
                'oil': int(bool(re.search(r'oil|olive|azeite', texto_completo))),
                'honey': int(bool(re.search(r'honey|mel', texto_completo))),
                'other': 1  # sempre presente como categoria residual
            }
            
            # Categorizar aplicações
            aplicacoes = {
                'authentication': int(bool(re.search(r'authentication|autenticação', texto_completo))),
                'traceability': int(bool(re.search(r'traceability|rastreabilidade', texto_completo))),
                'quality': int(bool(re.search(r'quality control|quality assessment', texto_completo))),
                'fraud': int(bool(re.search(r'fraud|adulteration|falsif', texto_completo))),
            }
            
            # Regiões geográficas
            regioes = {
                'asia': int(bool(re.search(r'china|japan|korea|asia', texto_completo))),
                'europe': int(bool(re.search(r'italy|spain|france|portugal|europe', texto_completo))),
                'americas': int(bool(re.search(r'brazil|america|usa|canada', texto_completo))),
            }
            
            dados.append({
                'id': id_ref,
                'score': score,
                'ano': ano,
                **ml_algorithms,
                **instrumentos,
                **produtos,
                **aplicacoes,
                **regioes
            })
            
        except Exception as e:
            print(f"Erro ao processar entrada: {e}")
            continue
    
    return pd.DataFrame(dados)

# ============================================================================
# ANÁLISE PCA
# ============================================================================

def executar_pca(df, n_componentes=5):
    """
    Executa PCA e retorna componentes principais
    """
    # Selecionar apenas variáveis numéricas (exceto id, score, ano)
    X = df.drop(['id', 'score', 'ano'], axis=1)
    
    # Padronizar dados
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Executar PCA
    pca = PCA(n_components=n_componentes)
    componentes = pca.fit_transform(X_scaled)
    
    # Criar DataFrame com componentes
    df_pca = pd.DataFrame(
        componentes,
        columns=[f'PC{i+1}' for i in range(n_componentes)]
    )
    
    # Adicionar metadados
    df_pca['id'] = df['id'].values
    df_pca['score'] = df['score'].values
    df_pca['ano'] = df['ano'].values
    
    # Calcular loadings
    loadings = pd.DataFrame(
        pca.components_.T,
        columns=[f'PC{i+1}' for i in range(n_componentes)],
        index=X.columns
    )
    
    # Variância explicada
    var_explicada = pca.explained_variance_ratio_
    
    return df_pca, loadings, var_explicada, pca

# ============================================================================
# VISUALIZAÇÕES
# ============================================================================

def plot_scree(var_explicada, output_path):
    """
    Gráfico de Scree Plot (variância explicada)
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    n_components = len(var_explicada)
    x_pos = np.arange(1, n_components + 1)
    
    # Variância por componente
    ax.bar(x_pos, var_explicada * 100, alpha=0.7, color='steelblue', label='Variância Individual')
    
    # Variância acumulada
    var_acumulada = np.cumsum(var_explicada) * 100
    ax.plot(x_pos, var_acumulada, marker='o', color='crimson', 
            linewidth=2, label='Variância Acumulada')
    
    ax.set_xlabel('Componente Principal', fontsize=12, fontweight='bold')
    ax.set_ylabel('Variância Explicada (%)', fontsize=12, fontweight='bold')
    ax.set_title('Scree Plot - Variância Explicada por Componente Principal', 
                 fontsize=14, fontweight='bold')
    ax.set_xticks(x_pos)
    ax.legend(fontsize=10)
    ax.grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Scree Plot salvo: {output_path}")

def plot_biplot(df_pca, loadings, output_path):
    """
    Biplot: PCA scores + loadings
    """
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # Scatter dos scores colorido por ano
    scatter = ax.scatter(
        df_pca['PC1'], df_pca['PC2'],
        c=df_pca['ano'], cmap='viridis',
        s=df_pca['score']*3,  # Tamanho proporcional ao score
        alpha=0.6, edgecolors='black', linewidth=0.5
    )
    
    # Colorbar para ano
    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label('Ano de Publicação', fontsize=10, fontweight='bold')
    
    # Plotar loadings (setas)
    scale_factor = 3
    for i, var in enumerate(loadings.index):
        ax.arrow(
            0, 0,
            loadings.loc[var, 'PC1'] * scale_factor,
            loadings.loc[var, 'PC2'] * scale_factor,
            head_width=0.15, head_length=0.15,
            fc='red', ec='red', alpha=0.6, linewidth=1.5
        )
        ax.text(
            loadings.loc[var, 'PC1'] * scale_factor * 1.1,
            loadings.loc[var, 'PC2'] * scale_factor * 1.1,
            var, fontsize=9, ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.5)
        )
    
    ax.set_xlabel('PC1', fontsize=12, fontweight='bold')
    ax.set_ylabel('PC2', fontsize=12, fontweight='bold')
    ax.set_title('Biplot PCA: Scores (pontos) e Loadings (setas)', 
                 fontsize=14, fontweight='bold')
    ax.axhline(0, color='gray', linewidth=0.5, linestyle='--')
    ax.axvline(0, color='gray', linewidth=0.5, linestyle='--')
    ax.grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Biplot salvo: {output_path}")

def plot_loadings_heatmap(loadings, output_path):
    """
    Heatmap dos loadings
    """
    fig, ax = plt.subplots(figsize=(10, 12))
    
    sns.heatmap(
        loadings.iloc[:, :5],  # Primeiros 5 PCs
        cmap='RdBu_r', center=0,
        annot=True, fmt='.2f',
        linewidths=0.5, cbar_kws={'label': 'Loading'},
        ax=ax
    )
    
    ax.set_title('Heatmap de Loadings (5 primeiros PCs)', 
                 fontsize=14, fontweight='bold')
    ax.set_xlabel('Componente Principal', fontsize=12, fontweight='bold')
    ax.set_ylabel('Variável', fontsize=12, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Heatmap de Loadings salvo: {output_path}")

def plot_temporal_evolution(df_pca, output_path):
    """
    Evolução temporal no espaço PC1 vs PC2
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Agrupar por década
    df_pca['decada'] = (df_pca['ano'] // 5) * 5
    
    for decada in sorted(df_pca['decada'].unique()):
        subset = df_pca[df_pca['decada'] == decada]
        ax.scatter(
            subset['PC1'], subset['PC2'],
            label=f'{decada}s',
            s=100, alpha=0.7, edgecolors='black', linewidth=0.5
        )
    
    ax.set_xlabel('PC1', fontsize=12, fontweight='bold')
    ax.set_ylabel('PC2', fontsize=12, fontweight='bold')
    ax.set_title('Evolução Temporal no Espaço de Componentes Principais', 
                 fontsize=14, fontweight='bold')
    ax.legend(title='Período', fontsize=10)
    ax.axhline(0, color='gray', linewidth=0.5, linestyle='--')
    ax.axvline(0, color='gray', linewidth=0.5, linestyle='--')
    ax.grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Evolução Temporal salva: {output_path}")

# ============================================================================
# RELATÓRIO ESTATÍSTICO
# ============================================================================

def gerar_relatorio(df, df_pca, loadings, var_explicada, output_path):
    """
    Gera relatório textual com resultados estatísticos
    """
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("="*80 + "\n")
        f.write("RELATÓRIO DE ANÁLISE DE COMPONENTES PRINCIPAIS (PCA)\n")
        f.write("Corpus: Machine Learning para Indicações Geográficas\n")
        f.write("="*80 + "\n\n")
        
        f.write(f"Total de estudos analisados: {len(df)}\n")
        f.write(f"Número de variáveis: {len(loadings)}\n")
        f.write(f"Período: {df['ano'].min()} - {df['ano'].max()}\n\n")
        
        f.write("-"*80 + "\n")
        f.write("VARIÂNCIA EXPLICADA POR COMPONENTE\n")
        f.write("-"*80 + "\n")
        for i, var in enumerate(var_explicada):
            f.write(f"PC{i+1}: {var*100:.2f}%")
            if i == 0:
                f.write(f" (Acumulado: {var*100:.2f}%)\n")
            else:
                acum = np.sum(var_explicada[:i+1]) * 100
                f.write(f" (Acumulado: {acum:.2f}%)\n")
        
        f.write("\n" + "-"*80 + "\n")
        f.write("TOP 10 LOADINGS - PC1 (Eixo Principal)\n")
        f.write("-"*80 + "\n")
        top_pc1 = loadings['PC1'].abs().sort_values(ascending=False).head(10)
        for var, loading in top_pc1.items():
            f.write(f"{var:25s}: {loadings.loc[var, 'PC1']:+.3f}\n")
        
        f.write("\n" + "-"*80 + "\n")
        f.write("TOP 10 LOADINGS - PC2 (Segundo Eixo)\n")
        f.write("-"*80 + "\n")
        top_pc2 = loadings['PC2'].abs().sort_values(ascending=False).head(10)
        for var, loading in top_pc2.items():
            f.write(f"{var:25s}: {loadings.loc[var, 'PC2']:+.3f}\n")
        
        f.write("\n" + "-"*80 + "\n")
        f.write("ESTATÍSTICAS DESCRITIVAS DOS COMPONENTES PRINCIPAIS\n")
        f.write("-"*80 + "\n")
        f.write(df_pca[['PC1', 'PC2', 'PC3', 'PC4', 'PC5']].describe().to_string())
        
        f.write("\n\n" + "-"*80 + "\n")
        f.write("CORRELAÇÃO ENTRE PCs E VARIÁVEIS ORIGINAIS (Score e Ano)\n")
        f.write("-"*80 + "\n")
        corr_score = df_pca[['PC1', 'PC2', 'PC3', 'score']].corr()['score']
        corr_ano = df_pca[['PC1', 'PC2', 'PC3', 'ano']].corr()['ano']
        
        f.write("\nCorrelação com Score:\n")
        for pc in ['PC1', 'PC2', 'PC3']:
            f.write(f"  {pc}: {corr_score[pc]:+.3f}\n")
        
        f.write("\nCorrelação com Ano:\n")
        for pc in ['PC1', 'PC2', 'PC3']:
            f.write(f"  {pc}: {corr_ano[pc]:+.3f}\n")
        
        f.write("\n" + "="*80 + "\n")
        f.write("FIM DO RELATÓRIO\n")
        f.write("="*80 + "\n")
    
    print(f"✓ Relatório estatístico salvo: {output_path}")

# ============================================================================
# MAIN
# ============================================================================

def main():
    """
    Função principal
    """
    print("\n" + "="*80)
    print("ANÁLISE DE COMPONENTES PRINCIPAIS (PCA)")
    print("Machine Learning para Indicações Geográficas")
    print("="*80 + "\n")
    
    # Caminhos
    caminho_bib = "../referencias_filtradas/referencias_ML_IG_filtradas.bib"
    output_dir = "."
    
    # 1. Extrair dados
    print("📚 Extraindo dados do arquivo .bib...")
    df = extrair_dados_bib(caminho_bib)
    print(f"✓ Total de estudos extraídos: {len(df)}")
    
    # 2. Executar PCA
    print("\n🔬 Executando PCA...")
    df_pca, loadings, var_explicada, pca = executar_pca(df, n_componentes=5)
    print(f"✓ PCA concluída: {len(var_explicada)} componentes principais")
    print(f"  Variância explicada (PC1+PC2): {sum(var_explicada[:2])*100:.2f}%")
    
    # 3. Gerar visualizações
    print("\n📊 Gerando visualizações...")
    plot_scree(var_explicada, f"{output_dir}/pca_scree_plot.png")
    plot_biplot(df_pca, loadings, f"{output_dir}/pca_biplot.png")
    plot_loadings_heatmap(loadings, f"{output_dir}/pca_loadings_heatmap.png")
    plot_temporal_evolution(df_pca, f"{output_dir}/pca_temporal_evolution.png")
    
    # 4. Gerar relatório
    print("\n📝 Gerando relatório estatístico...")
    gerar_relatorio(df, df_pca, loadings, var_explicada, 
                    f"{output_dir}/pca_relatorio.txt")
    
    # 5. Salvar dados processados
    df_pca.to_csv(f"{output_dir}/pca_scores.csv", index=False)
    loadings.to_csv(f"{output_dir}/pca_loadings.csv")
    print(f"\n✓ Dados salvos: pca_scores.csv e pca_loadings.csv")
    
    print("\n" + "="*80)
    print("✅ ANÁLISE PCA CONCLUÍDA COM SUCESSO!")
    print("="*80 + "\n")

if __name__ == "__main__":
    main()
