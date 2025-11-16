#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ANÁLISE DE CLUSTERS (K-MEANS E HIERÁRQUICO)
Corpus: Machine Learning aplicado a Indicações Geográficas
Objetivo: Identificar grupos naturais de estudos por similaridade metodológica
"""

import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import pdist, squareform
import warnings
warnings.filterwarnings('ignore')

# Configuração
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("tab10")

# ============================================================================
# EXTRAÇÃO DE DADOS
# ============================================================================

def extrair_dados_clustering(caminho_bib):
    """
    Extrai features para clustering
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
            
            id_match = re.search(r'@ARTICLE\{([^,]+),', entrada)
            id_ref = id_match.group(1) if id_match else "Unknown"
            
            titulo_match = re.search(r'title = \{([^}]+)\}', entrada)
            titulo = titulo_match.group(1)[:50] if titulo_match else "Unknown"
            
            keywords_match = re.search(r'keywords = \{([^}]+)\}', entrada)
            keywords = keywords_match.group(1).lower() if keywords_match else ""
            
            abstract_match = re.search(r'abstract = \{([^}]+)\}', entrada)
            abstract = abstract_match.group(1).lower() if abstract_match else ""
            
            texto = f"{titulo} {keywords} {abstract}".lower()
            
            # Features numéricas para clustering
            features = {
                'id': id_ref,
                'titulo': titulo,
                'score': score,
                'ano_normalizado': (ano - 2010) / 15,  # Normalizar 2010-2025
                
                # Algoritmos ML
                'rf': int(bool(re.search(r'random forest', texto))),
                'svm': int(bool(re.search(r'support vector machine|svm', texto))),
                'nn': int(bool(re.search(r'neural network|ann|cnn|deep learning', texto))),
                'knn': int(bool(re.search(r'k-nearest neighbor|knn', texto))),
                'dt': int(bool(re.search(r'decision tree', texto))),
                'plsda': int(bool(re.search(r'pls-da|partial least squares', texto))),
                'nb': int(bool(re.search(r'naive bayes', texto))),
                
                # Instrumentos
                'nir': int(bool(re.search(r'nir|near.infrared', texto))),
                'gcms': int(bool(re.search(r'gc-ms|gas chromatography', texto))),
                'icpms': int(bool(re.search(r'icp-ms|inductively coupled', texto))),
                'nmr': int(bool(re.search(r'nmr|nuclear magnetic', texto))),
                'raman': int(bool(re.search(r'raman', texto))),
                'ftir': int(bool(re.search(r'ftir|fourier transform', texto))),
                
                # Produtos
                'wine': int(bool(re.search(r'wine|vinho', texto))),
                'tea': int(bool(re.search(r'\btea\b|chá', texto))),
                'meat': int(bool(re.search(r'meat|carne|lamb|beef', texto))),
                'oil': int(bool(re.search(r'oil|olive|azeite', texto))),
                'honey': int(bool(re.search(r'honey|mel', texto))),
                
                # Aplicações
                'authentication': int(bool(re.search(r'authentication', texto))),
                'traceability': int(bool(re.search(r'traceability', texto))),
                'quality': int(bool(re.search(r'quality control', texto))),
                'fraud': int(bool(re.search(r'fraud|adulteration', texto))),
                
                # Regiões
                'asia': int(bool(re.search(r'china|japan|korea', texto))),
                'europe': int(bool(re.search(r'italy|spain|france|portugal', texto))),
                'americas': int(bool(re.search(r'brazil|america|usa', texto))),
                
                # Técnicas avançadas
                'metabolomics': int(bool(re.search(r'metabolomics|metabolômica', texto))),
                'chemometrics': int(bool(re.search(r'chemometrics|quimiometria', texto))),
                'fingerprinting': int(bool(re.search(r'fingerprinting', texto))),
            }
            
            dados.append(features)
            
        except Exception as e:
            print(f"Erro: {e}")
            continue
    
    return pd.DataFrame(dados)

# ============================================================================
# ANÁLISE K-MEANS
# ============================================================================

def encontrar_k_otimo(X_scaled, max_k=10):
    """
    Método do cotovelo + Silhouette Score
    """
    inertias = []
    silhouettes = []
    k_range = range(2, max_k + 1)
    
    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(X_scaled)
        inertias.append(kmeans.inertia_)
        silhouettes.append(silhouette_score(X_scaled, kmeans.labels_))
    
    return k_range, inertias, silhouettes

def plot_elbow_silhouette(k_range, inertias, silhouettes, output_path):
    """
    Gráfico de Cotovelo + Silhouette Score
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Método do cotovelo
    axes[0].plot(k_range, inertias, marker='o', linewidth=2, color='steelblue')
    axes[0].set_xlabel('Número de Clusters (k)', fontsize=12, fontweight='bold')
    axes[0].set_ylabel('Inércia (Within-Cluster Sum of Squares)', fontsize=11)
    axes[0].set_title('Método do Cotovelo', fontsize=13, fontweight='bold')
    axes[0].grid(alpha=0.3)
    
    # Silhouette Score
    axes[1].plot(k_range, silhouettes, marker='s', linewidth=2, color='coral')
    axes[1].set_xlabel('Número de Clusters (k)', fontsize=12, fontweight='bold')
    axes[1].set_ylabel('Silhouette Score', fontsize=11)
    axes[1].set_title('Silhouette Score por Número de Clusters', fontsize=13, fontweight='bold')
    axes[1].grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Gráfico de Cotovelo e Silhouette salvo: {output_path}")

def executar_kmeans(X_scaled, k_otimo):
    """
    Executa K-Means com k otimizado
    """
    kmeans = KMeans(n_clusters=k_otimo, random_state=42, n_init=20)
    labels = kmeans.fit_predict(X_scaled)
    
    # Métricas de qualidade
    silhouette = silhouette_score(X_scaled, labels)
    davies_bouldin = davies_bouldin_score(X_scaled, labels)
    calinski = calinski_harabasz_score(X_scaled, labels)
    
    return kmeans, labels, silhouette, davies_bouldin, calinski

def plot_kmeans_scatter(df, labels, output_path):
    """
    Scatter plot dos clusters (PCA-reduzido para visualização)
    """
    from sklearn.decomposition import PCA
    
    X = df.drop(['id', 'titulo', 'score', 'ano_normalizado'], axis=1).values
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)
    
    fig, ax = plt.subplots(figsize=(12, 10))
    
    scatter = ax.scatter(
        X_pca[:, 0], X_pca[:, 1],
        c=labels, cmap='tab10',
        s=df['score']*5, alpha=0.7,
        edgecolors='black', linewidth=0.5
    )
    
    # Centroides
    centroides_pca = pca.transform(
        df.groupby(labels).mean().drop(['score', 'ano_normalizado'], axis=1).values
    )
    ax.scatter(
        centroides_pca[:, 0], centroides_pca[:, 1],
        marker='X', s=500, c='red', edgecolors='black', linewidth=2,
        label='Centroides'
    )
    
    # Colorbar
    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label('Cluster', fontsize=11, fontweight='bold')
    
    ax.set_xlabel('PC1', fontsize=12, fontweight='bold')
    ax.set_ylabel('PC2', fontsize=12, fontweight='bold')
    ax.set_title('K-Means Clustering (Projeção PCA)', fontsize=14, fontweight='bold')
    ax.legend(fontsize=11)
    ax.grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Scatter K-Means salvo: {output_path}")

# ============================================================================
# ANÁLISE HIERÁRQUICA
# ============================================================================

def executar_clustering_hierarquico(X_scaled, n_clusters=5):
    """
    Clustering hierárquico aglomerativo
    """
    hc = AgglomerativeClustering(n_clusters=n_clusters, linkage='ward')
    labels = hc.fit_predict(X_scaled)
    
    # Métricas
    silhouette = silhouette_score(X_scaled, labels)
    davies_bouldin = davies_bouldin_score(X_scaled, labels)
    calinski = calinski_harabasz_score(X_scaled, labels)
    
    return labels, silhouette, davies_bouldin, calinski

def plot_dendrogram(X_scaled, df, output_path):
    """
    Dendrograma do clustering hierárquico
    """
    fig, ax = plt.subplots(figsize=(16, 10))
    
    # Calcular linkage
    Z = linkage(X_scaled, method='ward')
    
    # Plotar dendrograma
    dendrogram(
        Z,
        labels=df['id'].values,
        leaf_font_size=7,
        leaf_rotation=90,
        color_threshold=0.7*max(Z[:,2]),
        ax=ax
    )
    
    ax.set_xlabel('Estudos (IDs)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Distância (Ward)', fontsize=12, fontweight='bold')
    ax.set_title('Dendrograma - Clustering Hierárquico', fontsize=14, fontweight='bold')
    ax.axhline(y=0.7*max(Z[:,2]), color='red', linestyle='--', linewidth=2, label='Corte Sugerido')
    ax.legend(fontsize=11)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Dendrograma salvo: {output_path}")

def plot_heatmap_clusters(df, labels, output_path):
    """
    Heatmap de características médias por cluster
    """
    df_com_cluster = df.copy()
    df_com_cluster['cluster'] = labels
    
    # Médias por cluster (variáveis binárias)
    features_binarias = [col for col in df.columns if col not in ['id', 'titulo', 'score', 'ano_normalizado']]
    medias = df_com_cluster.groupby('cluster')[features_binarias].mean()
    
    fig, ax = plt.subplots(figsize=(14, 10))
    
    sns.heatmap(
        medias.T,
        cmap='YlGnBu', annot=True, fmt='.2f',
        linewidths=0.5, cbar_kws={'label': 'Proporção'},
        ax=ax
    )
    
    ax.set_xlabel('Cluster', fontsize=12, fontweight='bold')
    ax.set_ylabel('Características', fontsize=12, fontweight='bold')
    ax.set_title('Perfil de Características por Cluster', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Heatmap de Clusters salvo: {output_path}")

# ============================================================================
# ANÁLISE DE PERFIL DOS CLUSTERS
# ============================================================================

def analisar_perfil_clusters(df, labels):
    """
    Analisa características dominantes de cada cluster
    """
    df_com_cluster = df.copy()
    df_com_cluster['cluster'] = labels
    
    perfis = {}
    
    for cluster_id in sorted(set(labels)):
        subset = df_com_cluster[df_com_cluster['cluster'] == cluster_id]
        
        # Top características
        features = [col for col in df.columns if col not in ['id', 'titulo', 'score', 'ano_normalizado']]
        medias = subset[features].mean().sort_values(ascending=False)
        
        perfis[cluster_id] = {
            'tamanho': len(subset),
            'score_medio': subset['score'].mean(),
            'ano_medio': subset['ano_normalizado'].mean() * 15 + 2010,
            'top_features': medias.head(10).to_dict()
        }
    
    return perfis

# ============================================================================
# RELATÓRIO
# ============================================================================

def gerar_relatorio(df, labels_kmeans, labels_hc, perfis, metricas_kmeans, metricas_hc, output_path):
    """
    Relatório de clustering
    """
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("="*80 + "\n")
        f.write("RELATÓRIO DE ANÁLISE DE CLUSTERS\n")
        f.write("Corpus: Machine Learning para Indicações Geográficas\n")
        f.write("="*80 + "\n\n")
        
        f.write(f"Total de estudos: {len(df)}\n")
        f.write(f"Número de features: {len([c for c in df.columns if c not in ['id', 'titulo']])}\n\n")
        
        f.write("-"*80 + "\n")
        f.write("RESULTADOS K-MEANS\n")
        f.write("-"*80 + "\n")
        f.write(f"Número de clusters: {len(set(labels_kmeans))}\n")
        f.write(f"Silhouette Score: {metricas_kmeans[0]:.4f}\n")
        f.write(f"Davies-Bouldin Index: {metricas_kmeans[1]:.4f} (menor é melhor)\n")
        f.write(f"Calinski-Harabasz Score: {metricas_kmeans[2]:.2f} (maior é melhor)\n\n")
        
        f.write("-"*80 + "\n")
        f.write("RESULTADOS CLUSTERING HIERÁRQUICO\n")
        f.write("-"*80 + "\n")
        f.write(f"Número de clusters: {len(set(labels_hc))}\n")
        f.write(f"Silhouette Score: {metricas_hc[0]:.4f}\n")
        f.write(f"Davies-Bouldin Index: {metricas_hc[1]:.4f}\n")
        f.write(f"Calinski-Harabasz Score: {metricas_hc[2]:.2f}\n\n")
        
        f.write("-"*80 + "\n")
        f.write("PERFIL DOS CLUSTERS (K-Means)\n")
        f.write("-"*80 + "\n")
        for cluster_id, perfil in perfis.items():
            f.write(f"\nCLUSTER {cluster_id}:\n")
            f.write(f"  Tamanho: {perfil['tamanho']} estudos\n")
            f.write(f"  Score médio: {perfil['score_medio']:.2f}\n")
            f.write(f"  Ano médio: {perfil['ano_medio']:.0f}\n")
            f.write(f"  Características dominantes:\n")
            for feat, val in list(perfil['top_features'].items())[:5]:
                f.write(f"    - {feat}: {val:.2f}\n")
        
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
    print("ANÁLISE DE CLUSTERS")
    print("Machine Learning para Indicações Geográficas")
    print("="*80 + "\n")
    
    caminho_bib = "../referencias_filtradas/referencias_ML_IG_filtradas.bib"
    output_dir = "."
    
    # 1. Extrair dados
    print("📚 Extraindo features para clustering...")
    df = extrair_dados_clustering(caminho_bib)
    print(f"✓ Total de estudos: {len(df)}")
    
    # Preparar dados
    X = df.drop(['id', 'titulo', 'score', 'ano_normalizado'], axis=1).values
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # 2. Encontrar k ótimo
    print("\n🔍 Determinando número ótimo de clusters...")
    k_range, inertias, silhouettes = encontrar_k_otimo(X_scaled, max_k=10)
    k_otimo = k_range[np.argmax(silhouettes)]
    print(f"✓ k ótimo (Silhouette): {k_otimo}")
    
    plot_elbow_silhouette(k_range, inertias, silhouettes, f"{output_dir}/cluster_elbow_silhouette.png")
    
    # 3. K-Means
    print(f"\n🔬 Executando K-Means (k={k_otimo})...")
    kmeans, labels_kmeans, sil_km, db_km, ch_km = executar_kmeans(X_scaled, k_otimo)
    print(f"✓ K-Means concluído - Silhouette: {sil_km:.4f}")
    
    plot_kmeans_scatter(df, labels_kmeans, f"{output_dir}/cluster_kmeans_scatter.png")
    
    # 4. Clustering Hierárquico
    print(f"\n🌳 Executando Clustering Hierárquico (n={k_otimo})...")
    labels_hc, sil_hc, db_hc, ch_hc = executar_clustering_hierarquico(X_scaled, n_clusters=k_otimo)
    print(f"✓ Hierárquico concluído - Silhouette: {sil_hc:.4f}")
    
    plot_dendrogram(X_scaled, df, f"{output_dir}/cluster_dendrogram.png")
    
    # 5. Heatmap
    print("\n📊 Gerando heatmap de perfis...")
    plot_heatmap_clusters(df, labels_kmeans, f"{output_dir}/cluster_heatmap_profiles.png")
    
    # 6. Análise de perfis
    print("\n📋 Analisando perfis dos clusters...")
    perfis = analisar_perfil_clusters(df, labels_kmeans)
    
    # 7. Relatório
    print("\n📝 Gerando relatório...")
    gerar_relatorio(
        df, labels_kmeans, labels_hc, perfis,
        (sil_km, db_km, ch_km), (sil_hc, db_hc, ch_hc),
        f"{output_dir}/cluster_relatorio.txt"
    )
    
    # 8. Salvar dados
    df['cluster_kmeans'] = labels_kmeans
    df['cluster_hierarquico'] = labels_hc
    df.to_csv(f"{output_dir}/cluster_resultados.csv", index=False)
    print(f"\n✓ Dados salvos: cluster_resultados.csv")
    
    print("\n" + "="*80)
    print("✅ ANÁLISE DE CLUSTERS CONCLUÍDA COM SUCESSO!")
    print("="*80 + "\n")

if __name__ == "__main__":
    main()
