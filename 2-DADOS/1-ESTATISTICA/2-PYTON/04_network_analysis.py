#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ANÁLISE DE REDES (NETWORK ANALYSIS)
Corpus: Machine Learning aplicado a Indicações Geográficas
Objetivo: Mapear co-ocorrências e relações entre técnicas, produtos e regiões
"""

import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
from itertools import combinations
import warnings
warnings.filterwarnings('ignore')

# Configuração
plt.style.use('seaborn-v0_8-whitegrid')

# ============================================================================
# EXTRAÇÃO DE DADOS
# ============================================================================

def extrair_coocorrencias(caminho_bib):
    """
    Extrai co-ocorrências de termos/categorias
    """
    with open(caminho_bib, 'r', encoding='utf-8', errors='ignore') as f:
        conteudo = f.read()
    
    entradas = re.split(r'\n\n% Score:', conteudo)
    
    coocorrencias = {
        'algoritmo_produto': [],
        'algoritmo_instrumento': [],
        'instrumento_produto': [],
        'produto_regiao': [],
        'todas_categorias': []
    }
    
    for entrada in entradas[1:]:
        try:
            id_match = re.search(r'@ARTICLE\{([^,]+),', entrada)
            id_ref = id_match.group(1) if id_match else "Unknown"
            
            titulo_match = re.search(r'title = \{([^}]+)\}', entrada)
            titulo = titulo_match.group(1) if titulo_match else ""
            
            keywords_match = re.search(r'keywords = \{([^}]+)\}', entrada)
            keywords = keywords_match.group(1).lower() if keywords_match else ""
            
            abstract_match = re.search(r'abstract = \{([^}]+)\}', entrada)
            abstract = abstract_match.group(1).lower() if abstract_match else ""
            
            texto = f"{titulo} {keywords} {abstract}".lower()
            
            # Identificar categorias presentes
            algoritmos = []
            if re.search(r'random forest', texto): algoritmos.append('Random_Forest')
            if re.search(r'support vector machine|svm', texto): algoritmos.append('SVM')
            if re.search(r'neural network|ann|cnn|deep learning', texto): algoritmos.append('Neural_Network')
            if re.search(r'pls-da|partial least squares', texto): algoritmos.append('PLS-DA')
            if re.search(r'k-nearest neighbor|knn', texto): algoritmos.append('KNN')
            
            instrumentos = []
            if re.search(r'nir|near.infrared', texto): instrumentos.append('NIR')
            if re.search(r'gc-ms|gas chromatography', texto): instrumentos.append('GC-MS')
            if re.search(r'icp-ms|inductively coupled', texto): instrumentos.append('ICP-MS')
            if re.search(r'nmr|nuclear magnetic', texto): instrumentos.append('NMR')
            if re.search(r'raman', texto): instrumentos.append('Raman')
            if re.search(r'ftir|fourier transform', texto): instrumentos.append('FTIR')
            
            produtos = []
            if re.search(r'wine|vinho', texto): produtos.append('Wine')
            if re.search(r'\btea\b|chá', texto): produtos.append('Tea')
            if re.search(r'meat|carne|lamb|beef', texto): produtos.append('Meat')
            if re.search(r'oil|olive|azeite', texto): produtos.append('Oil')
            if re.search(r'honey|mel', texto): produtos.append('Honey')
            
            regioes = []
            if re.search(r'china|japan|korea', texto): regioes.append('Asia')
            if re.search(r'italy|spain|france|portugal', texto): regioes.append('Europe')
            if re.search(r'brazil|america|usa', texto): regioes.append('Americas')
            
            # Co-ocorrências algoritmo-produto
            for alg in algoritmos:
                for prod in produtos:
                    coocorrencias['algoritmo_produto'].append((alg, prod, id_ref))
            
            # Co-ocorrências algoritmo-instrumento
            for alg in algoritmos:
                for inst in instrumentos:
                    coocorrencias['algoritmo_instrumento'].append((alg, inst, id_ref))
            
            # Co-ocorrências instrumento-produto
            for inst in instrumentos:
                for prod in produtos:
                    coocorrencias['instrumento_produto'].append((inst, prod, id_ref))
            
            # Co-ocorrências produto-região
            for prod in produtos:
                for reg in regioes:
                    coocorrencias['produto_regiao'].append((prod, reg, id_ref))
            
            # Todas categorias juntas
            todas = algoritmos + instrumentos + produtos + regioes
            for par in combinations(todas, 2):
                coocorrencias['todas_categorias'].append((par[0], par[1], id_ref))
            
        except Exception as e:
            print(f"Erro: {e}")
            continue
    
    return coocorrencias

# ============================================================================
# CONSTRUÇÃO DE REDES
# ============================================================================

def construir_rede(coocorrencias_lista):
    """
    Constrói grafo NetworkX a partir de co-ocorrências
    """
    G = nx.Graph()
    
    # Contar frequências de arestas
    edge_weights = {}
    for item1, item2, id_ref in coocorrencias_lista:
        edge = tuple(sorted([item1, item2]))
        edge_weights[edge] = edge_weights.get(edge, 0) + 1
    
    # Adicionar arestas com pesos
    for (node1, node2), weight in edge_weights.items():
        G.add_edge(node1, node2, weight=weight)
    
    return G

def calcular_metricas_rede(G):
    """
    Calcula métricas de centralidade e estrutura
    """
    metricas = {
        'degree': nx.degree_centrality(G),
        'betweenness': nx.betweenness_centrality(G),
        'closeness': nx.closeness_centrality(G),
        'eigenvector': nx.eigenvector_centrality(G, max_iter=1000),
        'clustering': nx.clustering(G),
    }
    
    # Estatísticas globais
    metricas['densidade'] = nx.density(G)
    
    if nx.is_connected(G):
        metricas['diametro'] = nx.diameter(G)
        metricas['caminho_medio'] = nx.average_shortest_path_length(G)
    else:
        metricas['diametro'] = 'N/A (grafo desconectado)'
        metricas['caminho_medio'] = 'N/A'
    
    return metricas

# ============================================================================
# VISUALIZAÇÕES
# ============================================================================

def plot_network(G, titulo, output_path, min_weight=2):
    """
    Visualização da rede com layout spring
    """
    # Filtrar arestas fracas
    G_filtered = G.copy()
    edges_to_remove = [(u, v) for u, v, d in G_filtered.edges(data=True) if d['weight'] < min_weight]
    G_filtered.remove_edges_from(edges_to_remove)
    
    # Remover nós isolados
    G_filtered.remove_nodes_from(list(nx.isolates(G_filtered)))
    
    if len(G_filtered.nodes()) == 0:
        print(f"⚠ Grafo vazio após filtragem: {titulo}")
        return
    
    fig, ax = plt.subplots(figsize=(16, 14))
    
    # Layout
    pos = nx.spring_layout(G_filtered, k=2, iterations=50, seed=42)
    
    # Tamanhos de nós baseado em degree centrality
    node_sizes = [3000 * nx.degree_centrality(G_filtered)[node] for node in G_filtered.nodes()]
    
    # Cores por tipo de nó
    node_colors = []
    for node in G_filtered.nodes():
        if any(alg in node for alg in ['Forest', 'SVM', 'Neural', 'PLS', 'KNN']):
            node_colors.append('lightcoral')
        elif any(inst in node for inst in ['NIR', 'GC', 'ICP', 'NMR', 'Raman', 'FTIR']):
            node_colors.append('lightblue')
        elif any(prod in node for prod in ['Wine', 'Tea', 'Meat', 'Oil', 'Honey']):
            node_colors.append('lightgreen')
        else:
            node_colors.append('lightyellow')
    
    # Desenhar rede
    nx.draw_networkx_nodes(
        G_filtered, pos, node_size=node_sizes, node_color=node_colors,
        edgecolors='black', linewidths=1.5, alpha=0.9, ax=ax
    )
    
    # Arestas com largura proporcional ao peso
    edges = G_filtered.edges()
    weights = [G_filtered[u][v]['weight'] for u, v in edges]
    max_weight = max(weights)
    edge_widths = [3 * (w / max_weight) for w in weights]
    
    nx.draw_networkx_edges(
        G_filtered, pos, width=edge_widths, alpha=0.5, edge_color='gray', ax=ax
    )
    
    # Labels
    nx.draw_networkx_labels(
        G_filtered, pos, font_size=9, font_weight='bold', ax=ax
    )
    
    ax.set_title(titulo, fontsize=16, fontweight='bold', pad=20)
    ax.axis('off')
    
    # Legenda
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='lightcoral', edgecolor='black', label='Algoritmos ML'),
        Patch(facecolor='lightblue', edgecolor='black', label='Instrumentos'),
        Patch(facecolor='lightgreen', edgecolor='black', label='Produtos'),
        Patch(facecolor='lightyellow', edgecolor='black', label='Regiões')
    ]
    ax.legend(handles=legend_elements, loc='upper left', fontsize=11)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Rede salva: {output_path}")

def plot_degree_distribution(G, output_path):
    """
    Distribuição de graus da rede
    """
    degrees = [G.degree(n) for n in G.nodes()]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.hist(degrees, bins=20, color='steelblue', alpha=0.7, edgecolor='black')
    ax.set_xlabel('Grau (Número de Conexões)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Frequência', fontsize=12, fontweight='bold')
    ax.set_title('Distribuição de Graus da Rede', fontsize=14, fontweight='bold')
    ax.grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Distribuição de graus salva: {output_path}")

def plot_centrality_heatmap(metricas, output_path):
    """
    Heatmap de métricas de centralidade
    """
    # Top 20 nós por degree centrality
    top_nodes = sorted(metricas['degree'].items(), key=lambda x: x[1], reverse=True)[:20]
    top_node_names = [node for node, _ in top_nodes]
    
    # Criar DataFrame
    data = {
        'Degree': [metricas['degree'][n] for n in top_node_names],
        'Betweenness': [metricas['betweenness'][n] for n in top_node_names],
        'Closeness': [metricas['closeness'][n] for n in top_node_names],
        'Eigenvector': [metricas['eigenvector'][n] for n in top_node_names],
        'Clustering': [metricas['clustering'][n] for n in top_node_names],
    }
    df_metrics = pd.DataFrame(data, index=top_node_names)
    
    fig, ax = plt.subplots(figsize=(10, 12))
    
    sns.heatmap(
        df_metrics, cmap='YlOrRd', annot=True, fmt='.3f',
        linewidths=0.5, cbar_kws={'label': 'Valor Normalizado'}, ax=ax
    )
    
    ax.set_xlabel('Métricas de Centralidade', fontsize=12, fontweight='bold')
    ax.set_ylabel('Nós (Top 20)', fontsize=12, fontweight='bold')
    ax.set_title('Heatmap de Centralidade - Top 20 Nós', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Heatmap de centralidade salvo: {output_path}")

def plot_adjacency_matrix(G, output_path):
    """
    Matriz de adjacência como heatmap
    """
    # Pegar top 30 nós por degree
    top_nodes = sorted(G.degree(), key=lambda x: x[1], reverse=True)[:30]
    top_node_names = [node for node, _ in top_nodes]
    
    # Subgrafo
    G_sub = G.subgraph(top_node_names)
    
    # Matriz de adjacência
    adj_matrix = nx.to_pandas_adjacency(G_sub)
    
    fig, ax = plt.subplots(figsize=(14, 12))
    
    sns.heatmap(
        adj_matrix, cmap='Blues', annot=False,
        linewidths=0.5, cbar_kws={'label': 'Peso da Conexão'}, ax=ax
    )
    
    ax.set_title('Matriz de Adjacência (Top 30 Nós)', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Matriz de adjacência salva: {output_path}")

# ============================================================================
# ANÁLISE DE COMUNIDADES
# ============================================================================

def detectar_comunidades(G):
    """
    Detecta comunidades usando Louvain
    """
    from networkx.algorithms import community
    
    communities = community.greedy_modularity_communities(G)
    
    # Criar dicionário nó -> comunidade
    node_to_community = {}
    for i, comm in enumerate(communities):
        for node in comm:
            node_to_community[node] = i
    
    return node_to_community, len(communities)

def plot_communities(G, node_to_community, output_path):
    """
    Visualização de comunidades
    """
    fig, ax = plt.subplots(figsize=(16, 14))
    
    pos = nx.spring_layout(G, k=2, iterations=50, seed=42)
    
    # Cores por comunidade
    community_colors = plt.cm.tab10(range(max(node_to_community.values()) + 1))
    node_colors = [community_colors[node_to_community[node]] for node in G.nodes()]
    
    node_sizes = [2000 * nx.degree_centrality(G)[node] for node in G.nodes()]
    
    nx.draw_networkx_nodes(
        G, pos, node_size=node_sizes, node_color=node_colors,
        edgecolors='black', linewidths=1.5, alpha=0.9, ax=ax
    )
    
    nx.draw_networkx_edges(G, pos, alpha=0.3, edge_color='gray', ax=ax)
    nx.draw_networkx_labels(G, pos, font_size=8, font_weight='bold', ax=ax)
    
    ax.set_title('Detecção de Comunidades', fontsize=16, fontweight='bold')
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Gráfico de comunidades salvo: {output_path}")

# ============================================================================
# RELATÓRIO
# ============================================================================

def gerar_relatorio(redes, metricas_dict, output_path):
    """
    Gera relatório de análise de redes
    """
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("="*80 + "\n")
        f.write("RELATÓRIO DE ANÁLISE DE REDES\n")
        f.write("Corpus: Machine Learning para Indicações Geográficas\n")
        f.write("="*80 + "\n\n")
        
        for nome_rede, G in redes.items():
            f.write(f"\n{'-'*80}\n")
            f.write(f"REDE: {nome_rede.upper()}\n")
            f.write(f"{'-'*80}\n")
            
            f.write(f"Número de nós: {G.number_of_nodes()}\n")
            f.write(f"Número de arestas: {G.number_of_edges()}\n")
            f.write(f"Densidade: {nx.density(G):.4f}\n")
            
            metricas = metricas_dict[nome_rede]
            
            if metricas['diametro'] != 'N/A (grafo desconectado)':
                f.write(f"Diâmetro: {metricas['diametro']}\n")
                f.write(f"Caminho médio: {metricas['caminho_medio']:.3f}\n")
            else:
                f.write(f"Diâmetro: {metricas['diametro']}\n")
            
            # Top 10 por degree centrality
            f.write(f"\nTOP 10 NÓS (Degree Centrality):\n")
            top_degree = sorted(metricas['degree'].items(), key=lambda x: x[1], reverse=True)[:10]
            for i, (node, centrality) in enumerate(top_degree, 1):
                f.write(f"  {i}. {node:25s}: {centrality:.4f}\n")
            
            # Top 10 por betweenness
            f.write(f"\nTOP 10 NÓS (Betweenness Centrality - Pontes):\n")
            top_between = sorted(metricas['betweenness'].items(), key=lambda x: x[1], reverse=True)[:10]
            for i, (node, centrality) in enumerate(top_between, 1):
                f.write(f"  {i}. {node:25s}: {centrality:.4f}\n")
        
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
    print("ANÁLISE DE REDES")
    print("Machine Learning para Indicações Geográficas")
    print("="*80 + "\n")
    
    caminho_bib = "../referencias_filtradas/referencias_ML_IG_filtradas.bib"
    output_dir = "."
    
    # 1. Extrair co-ocorrências
    print("📚 Extraindo co-ocorrências...")
    coocorrencias = extrair_coocorrencias(caminho_bib)
    print(f"✓ Co-ocorrências extraídas")
    
    # 2. Construir redes
    print("\n🕸 Construindo redes...")
    redes = {
        'algoritmo_produto': construir_rede(coocorrencias['algoritmo_produto']),
        'algoritmo_instrumento': construir_rede(coocorrencias['algoritmo_instrumento']),
        'instrumento_produto': construir_rede(coocorrencias['instrumento_produto']),
        'todas_categorias': construir_rede(coocorrencias['todas_categorias'])
    }
    
    for nome, G in redes.items():
        print(f"  {nome}: {G.number_of_nodes()} nós, {G.number_of_edges()} arestas")
    
    # 3. Calcular métricas
    print("\n📊 Calculando métricas de rede...")
    metricas_dict = {}
    for nome, G in redes.items():
        metricas_dict[nome] = calcular_metricas_rede(G)
    print("✓ Métricas calculadas")
    
    # 4. Visualizações
    print("\n🎨 Gerando visualizações...")
    
    plot_network(redes['todas_categorias'], 'Rede Completa de Co-ocorrências', 
                 f"{output_dir}/network_completa.png", min_weight=3)
    
    plot_network(redes['algoritmo_produto'], 'Rede Algoritmo × Produto', 
                 f"{output_dir}/network_algoritmo_produto.png", min_weight=2)
    
    plot_network(redes['instrumento_produto'], 'Rede Instrumento × Produto', 
                 f"{output_dir}/network_instrumento_produto.png", min_weight=2)
    
    plot_degree_distribution(redes['todas_categorias'], f"{output_dir}/network_degree_distribution.png")
    
    plot_centrality_heatmap(metricas_dict['todas_categorias'], f"{output_dir}/network_centrality_heatmap.png")
    
    plot_adjacency_matrix(redes['todas_categorias'], f"{output_dir}/network_adjacency_matrix.png")
    
    # 5. Detecção de comunidades
    print("\n🔍 Detectando comunidades...")
    node_to_community, n_communities = detectar_comunidades(redes['todas_categorias'])
    print(f"✓ {n_communities} comunidades detectadas")
    
    plot_communities(redes['todas_categorias'], node_to_community, f"{output_dir}/network_communities.png")
    
    # 6. Relatório
    print("\n📝 Gerando relatório...")
    gerar_relatorio(redes, metricas_dict, f"{output_dir}/network_relatorio.txt")
    
    # 7. Salvar dados
    for nome, G in redes.items():
        nx.write_gexf(G, f"{output_dir}/network_{nome}.gexf")
    print(f"\n✓ Redes salvas em formato GEXF (importável em Gephi)")
    
    print("\n" + "="*80)
    print("✅ ANÁLISE DE REDES CONCLUÍDA COM SUCESSO!")
    print("="*80 + "\n")

if __name__ == "__main__":
    main()
