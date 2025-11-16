# ANÁLISES ESTATÍSTICAS - CORPUS ML PARA INDICAÇÕES GEOGRÁFICAS

Este diretório contém scripts Python para análises estatísticas multivariadas do corpus bibliográfico.

## 📊 Scripts Disponíveis

### 1. **01_pca_analysis.py** - Análise de Componentes Principais (PCA)
**Objetivo:** Identificar padrões latentes e estrutura de variação no corpus  
**Outputs:**
- `pca_scree_plot.png` - Variância explicada por componente
- `pca_biplot.png` - Scores e loadings projetados
- `pca_loadings_heatmap.png` - Contribuição de variáveis
- `pca_temporal_evolution.png` - Evolução no espaço PCA
- `pca_relatorio.txt` - Relatório estatístico completo
- `pca_scores.csv` e `pca_loadings.csv` - Dados processados

**Como executar:**
```bash
cd 2-DADOS/1-ESTATISTICA
python 01_pca_analysis.py
```

---

### 2. **02_mca_analysis.py** - Análise de Correspondência Múltipla (MCA)
**Objetivo:** Analisar associações entre variáveis categóricas (algoritmo, produto, região, etc.)  
**Outputs:**
- `mca_scree_plot.png` - Inércia explicada
- `mca_biplot.png` - Observações e categorias
- `mca_categorias.png` - Visualização separada por tipo
- `mca_contingency_heatmaps.png` - Tabelas de contingência
- `mca_relatorio.txt` - Relatório de associações
- `mca_dados_categoricos.csv` e `mca_coordenadas_categorias.csv`

**Como executar:**
```bash
python 02_mca_analysis.py
```

---

### 3. **03_cluster_analysis.py** - Análise de Clusters (K-Means e Hierárquico)
**Objetivo:** Identificar grupos naturais de estudos por similaridade metodológica  
**Outputs:**
- `cluster_elbow_silhouette.png` - Determinação do k ótimo
- `cluster_kmeans_scatter.png` - Visualização dos clusters (PCA)
- `cluster_dendrogram.png` - Dendrograma hierárquico
- `cluster_heatmap_profiles.png` - Perfil de características por cluster
- `cluster_relatorio.txt` - Análise detalhada dos clusters
- `cluster_resultados.csv` - Dados com atribuição de clusters

**Como executar:**
```bash
python 03_cluster_analysis.py
```

---

### 4. **04_network_analysis.py** - Análise de Redes (Network Analysis)
**Objetivo:** Mapear co-ocorrências e relações entre técnicas, produtos e regiões  
**Outputs:**
- `network_completa.png` - Rede completa de co-ocorrências
- `network_algoritmo_produto.png` - Rede específica
- `network_instrumento_produto.png` - Rede específica
- `network_degree_distribution.png` - Distribuição de graus
- `network_centrality_heatmap.png` - Métricas de centralidade
- `network_adjacency_matrix.png` - Matriz de adjacência
- `network_communities.png` - Detecção de comunidades
- `network_relatorio.txt` - Métricas de rede
- `network_*.gexf` - Arquivos para importar em Gephi

**Como executar:**
```bash
python 04_network_analysis.py
```

---

### 5. **05_temporal_analysis.py** - Análise de Séries Temporais (2010-2025)
**Objetivo:** Analisar evolução temporal de técnicas, produtos e aplicações  
**Outputs:**
- `temporal_publicacoes.png` - Evolução do número de publicações
- `temporal_algoritmos.png` - Adoção de algoritmos ao longo do tempo
- `temporal_produtos.png` - Evolução de produtos estudados
- `temporal_regioes.png` - Distribuição geográfica temporal
- `temporal_heatmap.png` - Heatmap de evolução de características
- `temporal_tendencias_sig.png` - Tendências significativas (p < 0.05)
- `temporal_stackplot.png` - Distribuição acumulada
- `temporal_relatorio.txt` - Análise temporal completa
- `temporal_*.csv` - Dados temporais processados

**Como executar:**
```bash
python 05_temporal_analysis.py
```

---

### 6. **06_predictive_modeling.py** - Modelagem Preditiva
**Objetivo:** Modelar relações preditivas entre características dos estudos  
**Modelos:**
- **Regressão:** Predizer score (Linear, Ridge, Lasso, Random Forest)
- **Classificação:** Predizer high_score (Logistic, Random Forest)

**Outputs:**
- `model_regressao_comparacao.png` - Comparação de modelos de regressão
- `model_feature_importance_reg.png` - Importância de features (regressão)
- `model_feature_importance_clf.png` - Importância de features (classificação)
- `model_confusion_matrix.png` - Matriz de confusão
- `model_metricas_comparacao.png` - Comparação de desempenho
- `model_relatorio.txt` - Relatório de modelagem
- `model_dados_completos.csv` - Dados com features extraídas

**Como executar:**
```bash
python 06_predictive_modeling.py
```

---

## 📦 Dependências

Instale as bibliotecas necessárias:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn scipy networkx prince bioinfokit
```

**Lista detalhada:**
- `numpy` - Computação numérica
- `pandas` - Manipulação de dados
- `matplotlib` - Visualizações básicas
- `seaborn` - Visualizações estatísticas
- `scikit-learn` - Machine Learning e análises multivariadas
- `scipy` - Funções estatísticas e hierárquicas
- `networkx` - Análise de redes
- `prince` - MCA (Multiple Correspondence Analysis)
- `bioinfokit` - Visualizações avançadas (opcional para PCA)

---

## 🎯 Fluxo Recomendado de Análise

1. **PCA** → Exploração inicial de estrutura de dados
2. **MCA** → Compreensão de associações categóricas
3. **Clustering** → Identificação de subgrupos metodológicos
4. **Network Analysis** → Mapeamento de relações e ecossistema
5. **Temporal Analysis** → Compreensão de evolução temporal
6. **Predictive Modeling** → Modelagem de relações preditivas

---

## 📄 Integração com Manuscrito

Os gráficos e tabelas gerados podem ser integrados diretamente no manuscrito:

- **Seção 3.1-3.2:** Figuras de PCA e MCA (estrutura do corpus)
- **Seção 3.3:** Network Analysis (ecossistema algorítmico)
- **Seção 3.7:** Temporal Analysis (tendências metodológicas)
- **Discussão:** Clustering e Modeling (padrões emergentes)

### Exemplo de citação no manuscrito:

```markdown
A análise de componentes principais (Figura X) revelou que os dois primeiros 
componentes explicam 67.3% da variância total do corpus, com PC1 associado 
predominantemente a técnicas espectroscópicas (NIR, FTIR) e PC2 a métodos 
cromatográficos (GC-MS, ICP-MS).
```

---

## 🔧 Personalização

Todos os scripts podem ser personalizados editando os parâmetros no início de cada arquivo:

```python
# Exemplo: Alterar número de clusters em 03_cluster_analysis.py
k_otimo = 6  # Altere conforme necessário

# Exemplo: Alterar período temporal em 05_temporal_analysis.py
ano_inicio = 2015
ano_fim = 2025
```

---

## 📊 Outputs Esperados

Cada script gera:
1. **Visualizações PNG** (alta resolução, 300 dpi) para publicação
2. **Relatórios TXT** com estatísticas descritivas e interpretações
3. **Dados CSV** para análises complementares em R ou Excel

Total de arquivos gerados: **~40 arquivos** (gráficos + relatórios + dados)

---

## 🐛 Troubleshooting

**Erro: "No module named 'prince'"**
```bash
pip install prince
```

**Erro: "bioinfokit not found"**
```bash
pip install bioinfokit
```

**Erro: "Arquivo .bib não encontrado"**
- Verifique se o caminho `../referencias_filtradas/referencias_ML_IG_filtradas.bib` está correto
- Ajuste o caminho no início de cada script se necessário

---

## 📞 Suporte

Para dúvidas ou problemas:
1. Verifique se todas as dependências estão instaladas
2. Certifique-se de estar executando no diretório correto
3. Consulte os comentários dentro de cada script para detalhes técnicos

---

**Última atualização:** Novembro 2025  
**Versão:** 1.0
