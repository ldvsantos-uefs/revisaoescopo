#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ANÁLISE DE CORRESPONDÊNCIA MÚLTIPLA (MCA)
Corpus: Machine Learning aplicado a Indicações Geográficas
Objetivo: Analisar associações entre variáveis categóricas
"""

import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from prince import MCA
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings('ignore')

# Configuração de estilo
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("Set2")

# ============================================================================
# EXTRAÇÃO DE DADOS DO ARQUIVO BIB
# ============================================================================

def extrair_dados_categoricos(caminho_bib):
    """
    Extrai variáveis categóricas do arquivo .bib
    """
    with open(caminho_bib, 'r', encoding='utf-8', errors='ignore') as f:
        conteudo = f.read()
    
    entradas = re.split(r'\n\n% Score:', conteudo)
    
    dados = []
    
    for entrada in entradas[1:]:
        try:
            # Extrair metadados
            score_match = re.search(r'^([\d.]+)', entrada)
            score = float(score_match.group(1)) if score_match else 0
            
            ano_match = re.search(r'year = \{(\d{4})\}', entrada)
            ano = int(ano_match.group(1)) if ano_match else 0
            
            id_match = re.search(r'@ARTICLE\{([^,]+),', entrada)
            id_ref = id_match.group(1) if id_match else "Unknown"
            
            # Extrair texto
            titulo_match = re.search(r'title = \{([^}]+)\}', entrada)
            titulo = titulo_match.group(1) if titulo_match else ""
            
            keywords_match = re.search(r'keywords = \{([^}]+)\}', entrada)
            keywords = keywords_match.group(1).lower() if keywords_match else ""
            
            abstract_match = re.search(r'abstract = \{([^}]+)\}', entrada)
            abstract = abstract_match.group(1).lower() if abstract_match else ""
            
            texto_completo = f"{titulo} {keywords} {abstract}".lower()
            
            # Categorizar algoritmo ML (único dominante)
            algoritmo = 'Other'
            if re.search(r'random forest', texto_completo):
                algoritmo = 'Random_Forest'
            elif re.search(r'support vector machine|svm', texto_completo):
                algoritmo = 'SVM'
            elif re.search(r'neural network|ann|cnn|deep learning', texto_completo):
                algoritmo = 'Neural_Network'
            elif re.search(r'pls-da|partial least squares', texto_completo):
                algoritmo = 'PLS-DA'
            elif re.search(r'k-nearest neighbor|knn', texto_completo):
                algoritmo = 'KNN'
            
            # Categorizar instrumento (único dominante)
            instrumento = 'Other'
            if re.search(r'nir|near.infrared|near infrared', texto_completo):
                instrumento = 'NIR'
            elif re.search(r'gc-ms|gas chromatography', texto_completo):
                instrumento = 'GC-MS'
            elif re.search(r'icp-ms|inductively coupled plasma', texto_completo):
                instrumento = 'ICP-MS'
            elif re.search(r'nmr|nuclear magnetic', texto_completo):
                instrumento = 'NMR'
            elif re.search(r'raman', texto_completo):
                instrumento = 'Raman'
            elif re.search(r'ftir|fourier transform', texto_completo):
                instrumento = 'FTIR'
            
            # Categorizar produto (único dominante)
            produto = 'Other'
            if re.search(r'wine|vinho|vin\b', texto_completo):
                produto = 'Wine'
            elif re.search(r'\btea\b|chá|thé', texto_completo):
                produto = 'Tea'
            elif re.search(r'meat|carne|lamb|beef|pork', texto_completo):
                produto = 'Meat'
            elif re.search(r'oil|olive|azeite', texto_completo):
                produto = 'Oil'
            elif re.search(r'honey|mel', texto_completo):
                produto = 'Honey'
            
            # Categorizar aplicação (único dominante)
            aplicacao = 'Other'
            if re.search(r'authentication|autenticação', texto_completo):
                aplicacao = 'Authentication'
            elif re.search(r'traceability|rastreabilidade', texto_completo):
                aplicacao = 'Traceability'
            elif re.search(r'fraud|adulteration|falsif', texto_completo):
                aplicacao = 'Fraud_Detection'
            elif re.search(r'quality control|quality assessment', texto_completo):
                aplicacao = 'Quality'
            
            # Região geográfica
            regiao = 'Other'
            if re.search(r'china|japan|korea', texto_completo):
                regiao = 'Asia'
            elif re.search(r'italy|spain|france|portugal|greece', texto_completo):
                regiao = 'Europe'
            elif re.search(r'brazil|america|usa|canada', texto_completo):
                regiao = 'Americas'
            
            # Período
            if ano >= 2020:
                periodo = '2020-2025'
            elif ano >= 2015:
                periodo = '2015-2019'
            elif ano >= 2010:
                periodo = '2010-2014'
            else:
                periodo = 'Pre-2010'
            
            # Categoria de score
            if score >= 50:
                categoria_score = 'High'
            elif score >= 35:
                categoria_score = 'Medium'
            else:
                categoria_score = 'Low'
            
            dados.append({
                'id': id_ref,
                'score': score,
                'ano': ano,
                'algoritmo': algoritmo,
                'instrumento': instrumento,
                'produto': produto,
                'aplicacao': aplicacao,
                'regiao': regiao,
                'periodo': periodo,
                'categoria_score': categoria_score
            })
            
        except Exception as e:
            print(f"Erro: {e}")
            continue
    
    return pd.DataFrame(dados)

# ============================================================================
# ANÁLISE MCA
# ============================================================================

def executar_mca(df, n_componentes=5):
    """
    Executa Multiple Correspondence Analysis
    """
    # Selecionar variáveis categóricas
    categoricas = ['algoritmo', 'instrumento', 'produto', 'aplicacao', 
                   'regiao', 'periodo', 'categoria_score']
    
    df_cat = df[categoricas].copy()
    
    # Executar MCA
    mca = MCA(
        n_components=n_componentes,
        n_iter=10,
        copy=True,
        check_input=True,
        engine='sklearn',
        random_state=42
    )
    
    mca = mca.fit(df_cat)
    
    # Coordenadas das linhas (observações)
    row_coords = mca.row_coordinates(df_cat)
    
    # Coordenadas das colunas (categorias)
    col_coords = mca.column_coordinates(df_cat)
    
    # Inércia (variância explicada)
    inercia = mca.explained_inertia_
    
    return mca, row_coords, col_coords, inercia

# ============================================================================
# VISUALIZAÇÕES
# ============================================================================

def plot_scree_mca(inercia, output_path):
    """
    Scree plot para MCA
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    n_dims = len(inercia)
    x_pos = np.arange(1, n_dims + 1)
    
    ax.bar(x_pos, inercia * 100, alpha=0.7, color='teal', label='Inércia Individual')
    
    inercia_acum = np.cumsum(inercia) * 100
    ax.plot(x_pos, inercia_acum, marker='o', color='crimson', 
            linewidth=2, label='Inércia Acumulada')
    
    ax.set_xlabel('Dimensão', fontsize=12, fontweight='bold')
    ax.set_ylabel('Inércia Explicada (%)', fontsize=12, fontweight='bold')
    ax.set_title('Scree Plot MCA - Inércia Explicada por Dimensão', 
                 fontsize=14, fontweight='bold')
    ax.set_xticks(x_pos)
    ax.legend(fontsize=10)
    ax.grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Scree Plot MCA salvo: {output_path}")

def plot_mca_biplot(row_coords, col_coords, df, output_path):
    """
    Biplot MCA: observações + categorias
    """
    fig, ax = plt.subplots(figsize=(14, 12))
    
    # Plot observações (pontos pequenos por período)
    for periodo in df['periodo'].unique():
        mask = df['periodo'] == periodo
        subset_rows = row_coords[mask]
        ax.scatter(
            subset_rows[0], subset_rows[1],
            label=f'Estudos {periodo}',
            s=50, alpha=0.5, edgecolors='black', linewidth=0.3
        )
    
    # Plot categorias (labels grandes)
    for idx, categoria in enumerate(col_coords.index):
        ax.scatter(
            col_coords.iloc[idx, 0], col_coords.iloc[idx, 1],
            s=200, marker='D', color='red', alpha=0.8, 
            edgecolors='black', linewidth=1.5
        )
        ax.text(
            col_coords.iloc[idx, 0] * 1.05, col_coords.iloc[idx, 1] * 1.05,
            categoria, fontsize=9, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='yellow', alpha=0.7)
        )
    
    ax.set_xlabel('Dimensão 1', fontsize=12, fontweight='bold')
    ax.set_ylabel('Dimensão 2', fontsize=12, fontweight='bold')
    ax.set_title('Biplot MCA: Estudos e Categorias', fontsize=14, fontweight='bold')
    ax.axhline(0, color='gray', linewidth=0.5, linestyle='--')
    ax.axvline(0, color='gray', linewidth=0.5, linestyle='--')
    ax.legend(fontsize=9, loc='upper right')
    ax.grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Biplot MCA salvo: {output_path}")

def plot_categorias_separadas(col_coords, output_path):
    """
    Plot separado para cada tipo de categoria
    """
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    axes = axes.flatten()
    
    categorias_grupos = {
        'Algoritmo': [cat for cat in col_coords.index if any(
            alg in cat for alg in ['Random_Forest', 'SVM', 'Neural_Network', 'PLS-DA', 'KNN', 'Other'])],
        'Instrumento': [cat for cat in col_coords.index if any(
            inst in cat for inst in ['NIR', 'GC-MS', 'ICP-MS', 'NMR', 'Raman', 'FTIR'])],
        'Produto': [cat for cat in col_coords.index if any(
            prod in cat for prod in ['Wine', 'Tea', 'Meat', 'Oil', 'Honey'])],
        'Aplicação': [cat for cat in col_coords.index if any(
            app in cat for app in ['Authentication', 'Traceability', 'Fraud_Detection', 'Quality'])],
        'Região': [cat for cat in col_coords.index if any(
            reg in cat for reg in ['Asia', 'Europe', 'Americas'])],
        'Período': [cat for cat in col_coords.index if any(
            per in cat for per in ['2020-2025', '2015-2019', '2010-2014', 'Pre-2010'])]
    }
    
    for idx, (titulo, categorias) in enumerate(categorias_grupos.items()):
        ax = axes[idx]
        
        for cat in categorias:
            if cat in col_coords.index:
                ax.scatter(
                    col_coords.loc[cat, 0], col_coords.loc[cat, 1],
                    s=200, alpha=0.7, edgecolors='black', linewidth=1.5
                )
                ax.text(
                    col_coords.loc[cat, 0], col_coords.loc[cat, 1],
                    cat.split('_')[-1] if '_' in cat else cat,
                    fontsize=9, ha='center', va='center'
                )
        
        ax.set_xlabel('Dimensão 1', fontsize=10)
        ax.set_ylabel('Dimensão 2', fontsize=10)
        ax.set_title(titulo, fontsize=12, fontweight='bold')
        ax.axhline(0, color='gray', linewidth=0.5, linestyle='--')
        ax.axvline(0, color='gray', linewidth=0.5, linestyle='--')
        ax.grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Gráficos de Categorias salvos: {output_path}")

def plot_contingency_heatmaps(df, output_path):
    """
    Heatmaps de tabelas de contingência
    """
    fig, axes = plt.subplots(2, 2, figsize=(16, 14))
    
    # 1. Algoritmo vs Produto
    cont1 = pd.crosstab(df['algoritmo'], df['produto'])
    sns.heatmap(cont1, annot=True, fmt='d', cmap='YlGnBu', ax=axes[0, 0], cbar_kws={'label': 'Frequência'})
    axes[0, 0].set_title('Algoritmo ML × Produto', fontsize=12, fontweight='bold')
    
    # 2. Instrumento vs Produto
    cont2 = pd.crosstab(df['instrumento'], df['produto'])
    sns.heatmap(cont2, annot=True, fmt='d', cmap='YlOrRd', ax=axes[0, 1], cbar_kws={'label': 'Frequência'})
    axes[0, 1].set_title('Instrumento Analítico × Produto', fontsize=12, fontweight='bold')
    
    # 3. Região vs Produto
    cont3 = pd.crosstab(df['regiao'], df['produto'])
    sns.heatmap(cont3, annot=True, fmt='d', cmap='BuPu', ax=axes[1, 0], cbar_kws={'label': 'Frequência'})
    axes[1, 0].set_title('Região Geográfica × Produto', fontsize=12, fontweight='bold')
    
    # 4. Período vs Algoritmo
    cont4 = pd.crosstab(df['periodo'], df['algoritmo'])
    sns.heatmap(cont4, annot=True, fmt='d', cmap='RdYlGn', ax=axes[1, 1], cbar_kws={'label': 'Frequência'})
    axes[1, 1].set_title('Período × Algoritmo ML', fontsize=12, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Heatmaps de Contingência salvos: {output_path}")

# ============================================================================
# RELATÓRIO ESTATÍSTICO
# ============================================================================

def gerar_relatorio(df, mca, col_coords, inercia, output_path):
    """
    Gera relatório textual MCA
    """
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("="*80 + "\n")
        f.write("RELATÓRIO DE ANÁLISE DE CORRESPONDÊNCIA MÚLTIPLA (MCA)\n")
        f.write("Corpus: Machine Learning para Indicações Geográficas\n")
        f.write("="*80 + "\n\n")
        
        f.write(f"Total de estudos: {len(df)}\n")
        f.write(f"Número de variáveis categóricas: 7\n")
        f.write(f"Total de categorias: {len(col_coords)}\n\n")
        
        f.write("-"*80 + "\n")
        f.write("INÉRCIA EXPLICADA POR DIMENSÃO\n")
        f.write("-"*80 + "\n")
        for i, inert in enumerate(inercia):
            acum = np.sum(inercia[:i+1]) * 100
            f.write(f"Dimensão {i+1}: {inert*100:.2f}% (Acumulado: {acum:.2f}%)\n")
        
        f.write("\n" + "-"*80 + "\n")
        f.write("DISTRIBUIÇÃO DE FREQUÊNCIAS\n")
        f.write("-"*80 + "\n")
        
        for col in ['algoritmo', 'instrumento', 'produto', 'aplicacao', 'regiao', 'periodo']:
            f.write(f"\n{col.upper()}:\n")
            freq = df[col].value_counts()
            for cat, count in freq.items():
                pct = (count / len(df)) * 100
                f.write(f"  {cat:20s}: {count:3d} ({pct:5.1f}%)\n")
        
        f.write("\n" + "-"*80 + "\n")
        f.write("COORDENADAS DAS CATEGORIAS (Dimensão 1 e 2)\n")
        f.write("-"*80 + "\n")
        f.write(col_coords.iloc[:, :2].to_string())
        
        f.write("\n\n" + "-"*80 + "\n")
        f.write("ASSOCIAÇÕES PRINCIPAIS\n")
        f.write("-"*80 + "\n")
        
        # Top associações produto-algoritmo
        f.write("\nProduto × Algoritmo:\n")
        cont = pd.crosstab(df['produto'], df['algoritmo'])
        f.write(cont.to_string())
        
        # Top associações instrumento-produto
        f.write("\n\nInstrumento × Produto:\n")
        cont2 = pd.crosstab(df['instrumento'], df['produto'])
        f.write(cont2.to_string())
        
        f.write("\n\n" + "="*80 + "\n")
        f.write("FIM DO RELATÓRIO MCA\n")
        f.write("="*80 + "\n")
    
    print(f"✓ Relatório MCA salvo: {output_path}")

# ============================================================================
# MAIN
# ============================================================================

def main():
    """
    Função principal
    """
    print("\n" + "="*80)
    print("ANÁLISE DE CORRESPONDÊNCIA MÚLTIPLA (MCA)")
    print("Machine Learning para Indicações Geográficas")
    print("="*80 + "\n")
    
    caminho_bib = "../referencias_filtradas/referencias_ML_IG_filtradas.bib"
    output_dir = "."
    
    # 1. Extrair dados
    print("📚 Extraindo dados categóricos...")
    df = extrair_dados_categoricos(caminho_bib)
    print(f"✓ Total de estudos: {len(df)}")
    
    # 2. Executar MCA
    print("\n🔬 Executando MCA...")
    mca, row_coords, col_coords, inercia = executar_mca(df, n_componentes=5)
    print(f"✓ MCA concluída")
    print(f"  Inércia explicada (Dim1+Dim2): {sum(inercia[:2])*100:.2f}%")
    
    # 3. Visualizações
    print("\n📊 Gerando visualizações...")
    plot_scree_mca(inercia, f"{output_dir}/mca_scree_plot.png")
    plot_mca_biplot(row_coords, col_coords, df, f"{output_dir}/mca_biplot.png")
    plot_categorias_separadas(col_coords, f"{output_dir}/mca_categorias.png")
    plot_contingency_heatmaps(df, f"{output_dir}/mca_contingency_heatmaps.png")
    
    # 4. Relatório
    print("\n📝 Gerando relatório...")
    gerar_relatorio(df, mca, col_coords, inercia, f"{output_dir}/mca_relatorio.txt")
    
    # 5. Salvar dados
    df.to_csv(f"{output_dir}/mca_dados_categoricos.csv", index=False)
    col_coords.to_csv(f"{output_dir}/mca_coordenadas_categorias.csv")
    print(f"\n✓ Dados salvos: mca_dados_categoricos.csv, mca_coordenadas_categorias.csv")
    
    print("\n" + "="*80)
    print("✅ ANÁLISE MCA CONCLUÍDA COM SUCESSO!")
    print("="*80 + "\n")

if __name__ == "__main__":
    main()
