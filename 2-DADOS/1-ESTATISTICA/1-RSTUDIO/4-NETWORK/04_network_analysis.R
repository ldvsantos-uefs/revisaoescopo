################################################################################
# ANÁLISE DE REDES (NETWORK ANALYSIS) - GGPLOT2
# Machine Learning para Indicações Geográficas
#
# Este script realiza análise de redes de co-ocorrências usando igraph/ggraph
# e gera visualizações com ggplot2
#
# Outputs:
#   - network_completa.png (Rede completa de co-ocorrências)
#   - network_algoritmo_produto.png (Rede específica)
#   - network_instrumento_produto.png (Rede específica)
#   - network_centrality_metrics.png (Métricas de centralidade)
#   - network_communities.png (Detecção de comunidades)
#   - network_relatorio.txt (Métricas de rede)
#   - network_*.graphml (Arquivos para importar em Gephi)
################################################################################

rm(list = ls())
gc()

packages <- c("bib2df", "tidyverse", "igraph", "ggraph", "tidygraph", 
              "viridis", "patchwork", "scales")

for (pkg in packages) {
  if (!require(pkg, character.only = TRUE, quietly = TRUE)) {
    install.packages(pkg, dependencies = TRUE, repos = "https://cloud.r-project.org")
    library(pkg, character.only = TRUE)
  }
}

cat("\n")
cat("================================================================================\n")
cat("ANÁLISE DE REDES (NETWORK ANALYSIS) - GGRAPH + GGPLOT2\n")
cat("Machine Learning para Indicações Geográficas\n")
cat("================================================================================\n\n")

################################################################################
# FUNÇÃO: Extrair co-ocorrências
################################################################################
extrair_coocorrencias <- function(caminho_bib) {
  cat("📚 Extraindo co-ocorrências do arquivo .bib...\n")
  
  bib_data <- bib2df(caminho_bib)
  texto_completo <- tolower(paste(bib_data$TITLE, bib_data$ABSTRACT, bib_data$KEYWORDS, sep = " "))
  
  # Definir categorias
  algoritmos <- c("RandomForest", "SVM", "NeuralNetwork", "KNN", "DecisionTree", 
                  "GradientBoosting", "NaiveBayes", "LogisticRegression")
  instrumentos <- c("NIR", "FTIR", "GCMS", "LCMS", "ICPMS", "NMR", "Sensor")
  produtos <- c("Wine", "Coffee", "Olive", "Honey", "Cheese", "Tea", "Meat")
  regioes <- c("Europe", "Asia", "Americas", "Africa")
  
  # Detectar presença
  presenca <- data.frame(
    # Algoritmos
    RandomForest = grepl("random forest", texto_completo),
    SVM = grepl("svm|support vector", texto_completo),
    NeuralNetwork = grepl("neural|deep learning|cnn|lstm", texto_completo),
    KNN = grepl("k-nearest|knn", texto_completo),
    DecisionTree = grepl("decision tree", texto_completo),
    GradientBoosting = grepl("gradient boosting|xgboost", texto_completo),
    NaiveBayes = grepl("naive bayes", texto_completo),
    LogisticRegression = grepl("logistic regression", texto_completo),
    
    # Instrumentos
    NIR = grepl("nir\\b|near infrared", texto_completo),
    FTIR = grepl("ftir|fourier transform", texto_completo),
    GCMS = grepl("gc-ms|gas chromatography", texto_completo),
    LCMS = grepl("lc-ms|hplc|liquid chromatography", texto_completo),
    ICPMS = grepl("icp-ms|icp\\b", texto_completo),
    NMR = grepl("nmr|nuclear magnetic", texto_completo),
    Sensor = grepl("sensor|e-nose", texto_completo),
    
    # Produtos
    Wine = grepl("wine|vinho", texto_completo),
    Coffee = grepl("coffee|café", texto_completo),
    Olive = grepl("olive|azeite", texto_completo),
    Honey = grepl("honey|mel", texto_completo),
    Cheese = grepl("cheese|queijo", texto_completo),
    Tea = grepl("tea|chá", texto_completo),
    Meat = grepl("meat|carne", texto_completo),
    
    # Regiões
    Europe = grepl("europe|italy|france|spain|portugal", texto_completo),
    Asia = grepl("asia|china|japan|korea", texto_completo),
    Americas = grepl("america|usa|brazil|canada", texto_completo),
    Africa = grepl("africa", texto_completo)
  )
  
  cat(sprintf("✓ Total de estudos analisados: %d\n\n", nrow(presenca)))
  
  return(list(presenca = presenca, 
              algoritmos = algoritmos, 
              instrumentos = instrumentos, 
              produtos = produtos,
              regioes = regioes))
}

################################################################################
# FUNÇÃO: Construir rede de co-ocorrências
################################################################################
construir_rede <- function(presenca_data, min_coocorrencia = 3) {
  cat(sprintf("🔬 Construindo rede de co-ocorrências (mínimo: %d)...\n", min_coocorrencia))
  
  # Calcular matriz de co-ocorrências
  cooc_matrix <- t(as.matrix(presenca_data)) %*% as.matrix(presenca_data)
  
  # Remover diagonal (auto-conexões)
  diag(cooc_matrix) <- 0
  
  # Filtrar por mínimo de co-ocorrências
  cooc_matrix[cooc_matrix < min_coocorrencia] <- 0
  
  # Criar grafo
  g <- graph_from_adjacency_matrix(cooc_matrix, mode = "undirected", 
                                    weighted = TRUE, diag = FALSE)
  
  # Remover nós isolados
  g <- delete.vertices(g, degree(g) == 0)
  
  cat(sprintf("✓ Rede construída: %d nós, %d arestas\n\n", vcount(g), ecount(g)))
  
  return(g)
}

################################################################################
# FUNÇÃO: Calcular métricas de rede
################################################################################
calcular_metricas_rede <- function(g) {
  cat("📊 Calculando métricas de rede...\n")
  
  metricas <- data.frame(
    Node = V(g)$name,
    Degree = degree(g),
    Betweenness = betweenness(g, normalized = TRUE),
    Closeness = closeness(g, normalized = TRUE),
    Eigenvector = eigen_centrality(g)$vector,
    stringsAsFactors = FALSE
  )
  
  metricas <- metricas %>% arrange(desc(Degree))
  
  cat("✓ Métricas calculadas\n\n")
  
  return(metricas)
}

################################################################################
# FUNÇÃO: Detectar comunidades
################################################################################
detectar_comunidades <- function(g) {
  cat("🔬 Detectando comunidades (Louvain)...\n")
  
  communities <- cluster_louvain(g)
  V(g)$community <- membership(communities)
  
  cat(sprintf("✓ Comunidades detectadas: %d\n", length(unique(V(g)$community))))
  cat(sprintf("  Modularidade: %.3f\n\n", modularity(communities)))
  
  return(g)
}

################################################################################
# FUNÇÃO: Plot da rede completa
################################################################################
plot_network_completa <- function(g, output_file = "network_completa.png") {
  cat("📊 Gerando visualização da rede completa...\n")
  
  # Converter para tidygraph
  tg <- as_tbl_graph(g)
  
  p <- ggraph(tg, layout = "fr") +
    geom_edge_link(aes(width = weight, alpha = weight), color = "gray50") +
    geom_node_point(aes(size = degree(g), color = as.factor(V(g)$community)), alpha = 0.8) +
    geom_node_text(aes(label = name), repel = TRUE, size = 3.5, fontface = "bold") +
    scale_edge_width(range = c(0.5, 3)) +
    scale_edge_alpha(range = c(0.3, 0.8)) +
    scale_size_continuous(range = c(3, 12)) +
    scale_color_viridis_d(option = "plasma", begin = 0.1, end = 0.9) +
    labs(
      title = "Rede de Co-ocorrências - Machine Learning para IG",
      subtitle = sprintf("%d nós, %d arestas | Comunidades detectadas: %d", 
                         vcount(g), ecount(g), length(unique(V(g)$community))),
      color = "Comunidade",
      size = "Grau"
    ) +
    theme_graph(base_family = "sans") +
    theme(
      plot.title = element_text(face = "bold", size = 16, hjust = 0.5),
      plot.subtitle = element_text(hjust = 0.5, color = "gray40", size = 12),
      legend.position = "right"
    )
  
  ggsave(output_file, plot = p, width = 16, height = 12, dpi = 300)
  cat(sprintf("✓ Rede completa salva: %s\n", output_file))
}

################################################################################
# FUNÇÃO: Plot de rede específica (Algoritmo × Produto)
################################################################################
plot_network_especifica <- function(presenca_data, categorias1, categorias2, 
                                     titulo, output_file, min_cooc = 2) {
  cat(sprintf("📊 Gerando rede: %s...\n", titulo))
  
  # Selecionar apenas categorias relevantes (remover espaços do nome GC-MS)
  categorias1 <- gsub("-", "", categorias1)
  categorias2 <- gsub("-", "", categorias2)
  
  # Verificar quais colunas existem
  cols <- c(categorias1, categorias2)
  cols_existentes <- cols[cols %in% colnames(presenca_data)]
  
  if (length(cols_existentes) < 2) {
    cat(sprintf("⚠️  Pulando %s - colunas insuficientes\n", output_file))
    return(invisible(NULL))
  }
  
  presenca_sub <- presenca_data[, cols_existentes]
  
  # Construir rede
  cooc_matrix <- t(as.matrix(presenca_sub)) %*% as.matrix(presenca_sub)
  diag(cooc_matrix) <- 0
  cooc_matrix[cooc_matrix < min_cooc] <- 0
  
  g_sub <- graph_from_adjacency_matrix(cooc_matrix, mode = "undirected", 
                                       weighted = TRUE, diag = FALSE)
  g_sub <- delete.vertices(g_sub, degree(g_sub) == 0)
  
  # Adicionar atributos de tipo
  V(g_sub)$type <- ifelse(V(g_sub)$name %in% categorias1, "Tipo1", "Tipo2")
  
  # Plot
  tg <- as_tbl_graph(g_sub)
  
  p <- ggraph(tg, layout = "kk") +
    geom_edge_link(aes(width = weight, alpha = weight), color = "gray40") +
    geom_node_point(aes(size = degree(g_sub), color = V(g_sub)$type), alpha = 0.8) +
    geom_node_text(aes(label = name), repel = TRUE, size = 4, fontface = "bold") +
    scale_edge_width(range = c(0.5, 4)) +
    scale_edge_alpha(range = c(0.3, 0.9)) +
    scale_size_continuous(range = c(4, 15)) +
    scale_color_manual(values = c("Tipo1" = "#2E86AB", "Tipo2" = "#FC4E07")) +
    labs(
      title = titulo,
      subtitle = sprintf("%d nós, %d arestas", vcount(g_sub), ecount(g_sub)),
      color = "Categoria",
      size = "Grau"
    ) +
    theme_graph(base_family = "sans") +
    theme(
      plot.title = element_text(face = "bold", size = 14, hjust = 0.5),
      plot.subtitle = element_text(hjust = 0.5, color = "gray40"),
      legend.position = "right"
    )
  
  ggsave(output_file, plot = p, width = 12, height = 9, dpi = 300)
  cat(sprintf("✓ Rede salva: %s\n", output_file))
}

################################################################################
# FUNÇÃO: Plot de métricas de centralidade
################################################################################
plot_centrality_metrics <- function(metricas, output_file = "network_centrality_metrics.png") {
  cat("📊 Gerando visualização de métricas de centralidade...\n")
  
  # Top 15 nós por grau
  top_nodes <- head(metricas, 15)
  
  # Preparar dados
  metricas_long <- top_nodes %>%
    select(Node, Degree, Betweenness, Closeness, Eigenvector) %>%
    pivot_longer(-Node, names_to = "Metric", values_to = "Value")
  
  p <- ggplot(metricas_long, aes(x = reorder(Node, Value), y = Value, fill = Metric)) +
    geom_col(alpha = 0.8) +
    coord_flip() +
    facet_wrap(~Metric, scales = "free_x") +
    scale_fill_viridis_d(option = "plasma") +
    labs(
      title = "Métricas de Centralidade - Top 15 Nós",
      subtitle = "Degree | Betweenness | Closeness | Eigenvector",
      x = "Nó",
      y = "Valor"
    ) +
    theme_minimal(base_size = 12) +
    theme(
      plot.title = element_text(face = "bold", size = 14, hjust = 0.5),
      plot.subtitle = element_text(hjust = 0.5, color = "gray40"),
      legend.position = "none",
      strip.text = element_text(face = "bold", size = 12)
    )
  
  ggsave(output_file, plot = p, width = 14, height = 10, dpi = 300)
  cat(sprintf("✓ Métricas de centralidade salvas: %s\n", output_file))
}

################################################################################
# FUNÇÃO: Plot de comunidades
################################################################################
plot_communities <- function(g, output_file = "network_communities.png") {
  cat("📊 Gerando visualização de comunidades...\n")
  
  tg <- as_tbl_graph(g)
  
  p <- ggraph(tg, layout = "fr") +
    geom_edge_link(aes(alpha = weight), color = "gray60", width = 0.5) +
    geom_node_point(aes(size = degree(g), color = as.factor(V(g)$community)), alpha = 0.9) +
    geom_node_text(aes(label = name, color = as.factor(V(g)$community)), 
                   repel = TRUE, size = 3, fontface = "bold", show.legend = FALSE) +
    scale_size_continuous(range = c(4, 14)) +
    scale_color_viridis_d(option = "turbo", begin = 0.1, end = 0.9) +
    labs(
      title = "Detecção de Comunidades - Algoritmo de Louvain",
      subtitle = sprintf("%d comunidades identificadas", length(unique(V(g)$community))),
      color = "Comunidade",
      size = "Grau"
    ) +
    theme_graph(base_family = "sans") +
    theme(
      plot.title = element_text(face = "bold", size = 16, hjust = 0.5),
      plot.subtitle = element_text(hjust = 0.5, color = "gray40"),
      legend.position = "right"
    )
  
  ggsave(output_file, plot = p, width = 16, height = 12, dpi = 300)
  cat(sprintf("✓ Comunidades salvas: %s\n", output_file))
}

################################################################################
# FUNÇÃO: Relatório
################################################################################
gerar_relatorio <- function(g, metricas, output_file = "network_relatorio.txt") {
  cat("\n📝 Gerando relatório estatístico...\n")
  
  sink(output_file)
  cat("================================================================================\n")
  cat("RELATÓRIO DE ANÁLISE DE REDES - ML PARA INDICAÇÕES GEOGRÁFICAS\n")
  cat("================================================================================\n\n")
  cat(sprintf("Data de execução: %s\n\n", Sys.time()))
  
  cat("--------------------------------------------------------------------------------\n")
  cat("ESTATÍSTICAS GERAIS DA REDE\n")
  cat("--------------------------------------------------------------------------------\n")
  cat(sprintf("Número de nós: %d\n", vcount(g)))
  cat(sprintf("Número de arestas: %d\n", ecount(g)))
  cat(sprintf("Densidade: %.4f\n", edge_density(g)))
  cat(sprintf("Transitividade (clustering coefficient): %.4f\n", transitivity(g)))
  cat(sprintf("Diâmetro da rede: %d\n", diameter(g)))
  cat(sprintf("Distância média: %.2f\n\n", mean_distance(g)))
  
  cat("--------------------------------------------------------------------------------\n")
  cat("TOP 15 NÓS POR GRAU (DEGREE CENTRALITY)\n")
  cat("--------------------------------------------------------------------------------\n")
  print(head(metricas %>% select(Node, Degree) %>% arrange(desc(Degree)), 15))
  cat("\n")
  
  cat("--------------------------------------------------------------------------------\n")
  cat("TOP 15 NÓS POR BETWEENNESS CENTRALITY\n")
  cat("--------------------------------------------------------------------------------\n")
  print(head(metricas %>% select(Node, Betweenness) %>% arrange(desc(Betweenness)), 15))
  cat("\n")
  
  cat("--------------------------------------------------------------------------------\n")
  cat("TOP 15 NÓS POR EIGENVECTOR CENTRALITY\n")
  cat("--------------------------------------------------------------------------------\n")
  print(head(metricas %>% select(Node, Eigenvector) %>% arrange(desc(Eigenvector)), 15))
  cat("\n")
  
  cat("--------------------------------------------------------------------------------\n")
  cat("COMUNIDADES DETECTADAS (LOUVAIN)\n")
  cat("--------------------------------------------------------------------------------\n")
  communities_table <- table(V(g)$community)
  print(communities_table)
  cat("\n")
  
  for (comm in sort(unique(V(g)$community))) {
    cat(sprintf("\n=== COMUNIDADE %d (n=%d) ===\n", comm, sum(V(g)$community == comm)))
    nodes_comm <- V(g)$name[V(g)$community == comm]
    cat(paste(nodes_comm, collapse = ", "), "\n")
  }
  
  cat("\n================================================================================\n")
  sink()
  
  cat(sprintf("✓ Relatório estatístico salvo: %s\n", output_file))
}

################################################################################
# FUNÇÃO: Salvar grafo
################################################################################
salvar_grafo <- function(g, filename = "network_completa.graphml") {
  write_graph(g, filename, format = "graphml")
  cat(sprintf("✓ Grafo salvo: %s (importável em Gephi)\n", filename))
}

################################################################################
# EXECUÇÃO PRINCIPAL
################################################################################
main <- function() {
  caminho_bib <- "../../1-RSTUDIO/corpus.bib"
  
  if (!file.exists(caminho_bib)) {
    stop("❌ Erro: Arquivo .bib não encontrado em: ", caminho_bib)
  }
  
  # 1. Extrair co-ocorrências
  dados <- extrair_coocorrencias(caminho_bib)
  
  # 2. Construir rede completa
  g <- construir_rede(dados$presenca, min_coocorrencia = 3)
  
  # 3. Calcular métricas
  metricas <- calcular_metricas_rede(g)
  
  # 4. Detectar comunidades
  g <- detectar_comunidades(g)
  
  # 5. Visualizações
  cat("📊 Gerando visualizações...\n")
  plot_network_completa(g)
  plot_network_especifica(dados$presenca, dados$algoritmos, dados$produtos,
                          "Rede Algoritmo × Produto", "network_algoritmo_produto.png")
  plot_network_especifica(dados$presenca, dados$instrumentos, dados$produtos,
                          "Rede Instrumento × Produto", "network_instrumento_produto.png")
  plot_centrality_metrics(metricas)
  plot_communities(g)
  
  # 6. Relatório
  gerar_relatorio(g, metricas)
  
  # 7. Salvar grafo
  cat("\n")
  salvar_grafo(g)
  
  cat("\n")
  cat("================================================================================\n")
  cat("✅ ANÁLISE DE REDES CONCLUÍDA COM SUCESSO!\n")
  cat("================================================================================\n")
}

tryCatch({
  main()
}, error = function(e) {
  cat("\n❌ ERRO durante a execução:\n")
  cat(conditionMessage(e), "\n")
})
