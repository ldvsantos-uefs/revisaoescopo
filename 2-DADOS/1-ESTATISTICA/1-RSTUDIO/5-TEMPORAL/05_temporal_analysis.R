################################################################################
# ANÁLISE DE SÉRIES TEMPORAIS (2010-2025) - GGPLOT2
# Machine Learning para Indicações Geográficas
#
# Este script realiza análise temporal usando ggplot2
# e gera visualizações elegantes
#
# Outputs:
#   - temporal_publicacoes.png (Evolução de publicações)
#   - temporal_algoritmos.png (Adoção de algoritmos)
#   - temporal_produtos.png (Evolução de produtos)
#   - temporal_regioes.png (Distribuição geográfica)
#   - temporal_heatmap.png (Heatmap de evolução)
#   - temporal_tendencias.png (Análise de tendências)
#   - temporal_relatorio.txt (Análise completa)
#   - temporal_*.csv (Dados processados)
################################################################################

rm(list = ls())
gc()

packages <- c("bib2df", "tidyverse", "viridis", "patchwork", "scales", 
              "ggrepel", "pheatmap", "lubridate")

for (pkg in packages) {
  if (!require(pkg, character.only = TRUE, quietly = TRUE)) {
    install.packages(pkg, dependencies = TRUE, repos = "https://cloud.r-project.org")
    library(pkg, character.only = TRUE)
  }
}

cat("\n")
cat("================================================================================\n")
cat("ANÁLISE DE SÉRIES TEMPORAIS (2010-2025) - GGPLOT2\n")
cat("Machine Learning para Indicações Geográficas\n")
cat("================================================================================\n\n")

################################################################################
# FUNÇÃO: Extrair dados temporais
################################################################################
extrair_dados_temporais <- function(caminho_bib) {
  cat("📚 Extraindo dados temporais do arquivo .bib...\n")
  
  bib_data <- bib2df(caminho_bib)
  texto_completo <- tolower(paste(bib_data$TITLE, bib_data$ABSTRACT, bib_data$KEYWORDS, sep = " "))
  
  dados <- data.frame(
    ID = 1:nrow(bib_data),
    Ano = as.numeric(bib_data$YEAR),
    
    # Algoritmos
    RandomForest = as.integer(grepl("random forest", texto_completo)),
    SVM = as.integer(grepl("svm|support vector", texto_completo)),
    NeuralNetwork = as.integer(grepl("neural|deep learning|cnn|lstm", texto_completo)),
    KNN = as.integer(grepl("k-nearest|knn", texto_completo)),
    DecisionTree = as.integer(grepl("decision tree", texto_completo)),
    GradientBoosting = as.integer(grepl("gradient boosting|xgboost", texto_completo)),
    
    # Instrumentos
    NIR = as.integer(grepl("nir\\b|near infrared", texto_completo)),
    FTIR = as.integer(grepl("ftir|fourier transform", texto_completo)),
    GCMS = as.integer(grepl("gc-ms|gas chromatography", texto_completo)),
    LCMS = as.integer(grepl("lc-ms|hplc", texto_completo)),
    ICPMS = as.integer(grepl("icp-ms|icp\\b", texto_completo)),
    NMR = as.integer(grepl("nmr|nuclear magnetic", texto_completo)),
    
    # Produtos
    Wine = as.integer(grepl("wine|vinho", texto_completo)),
    Coffee = as.integer(grepl("coffee|café", texto_completo)),
    Olive = as.integer(grepl("olive|azeite", texto_completo)),
    Honey = as.integer(grepl("honey|mel", texto_completo)),
    Cheese = as.integer(grepl("cheese|queijo", texto_completo)),
    
    # Regiões
    Europe = as.integer(grepl("europe|italy|france|spain|portugal", texto_completo)),
    Asia = as.integer(grepl("asia|china|japan|korea", texto_completo)),
    Americas = as.integer(grepl("america|usa|brazil|canada", texto_completo)),
    
    stringsAsFactors = FALSE
  )
  
  # Filtrar anos válidos
  dados <- dados %>% filter(Ano >= 2010, Ano <= 2025)
  
  cat(sprintf("✓ Total de estudos extraídos: %d (2010-2025)\n\n", nrow(dados)))
  
  return(dados)
}

################################################################################
# FUNÇÃO: Agregar por ano
################################################################################
agregar_por_ano <- function(dados) {
  cat("🔬 Agregando dados por ano...\n")
  
  # Total de publicações por ano
  publicacoes_ano <- dados %>%
    group_by(Ano) %>%
    summarise(Total = n(), .groups = "drop")
  
  # Algoritmos por ano
  algoritmos_ano <- dados %>%
    group_by(Ano) %>%
    summarise(
      RandomForest = sum(RandomForest),
      SVM = sum(SVM),
      NeuralNetwork = sum(NeuralNetwork),
      KNN = sum(KNN),
      DecisionTree = sum(DecisionTree),
      GradientBoosting = sum(GradientBoosting),
      .groups = "drop"
    )
  
  # Instrumentos por ano
  instrumentos_ano <- dados %>%
    group_by(Ano) %>%
    summarise(
      NIR = sum(NIR),
      FTIR = sum(FTIR),
      GCMS = sum(GCMS),
      LCMS = sum(LCMS),
      ICPMS = sum(ICPMS),
      NMR = sum(NMR),
      .groups = "drop"
    )
  
  # Produtos por ano
  produtos_ano <- dados %>%
    group_by(Ano) %>%
    summarise(
      Wine = sum(Wine),
      Coffee = sum(Coffee),
      Olive = sum(Olive),
      Honey = sum(Honey),
      Cheese = sum(Cheese),
      .groups = "drop"
    )
  
  # Regiões por ano
  regioes_ano <- dados %>%
    group_by(Ano) %>%
    summarise(
      Europe = sum(Europe),
      Asia = sum(Asia),
      Americas = sum(Americas),
      .groups = "drop"
    )
  
  cat("✓ Agregação concluída\n\n")
  
  return(list(
    publicacoes = publicacoes_ano,
    algoritmos = algoritmos_ano,
    instrumentos = instrumentos_ano,
    produtos = produtos_ano,
    regioes = regioes_ano
  ))
}

################################################################################
# FUNÇÃO: Plot de publicações ao longo do tempo
################################################################################
plot_publicacoes_tempo <- function(publicacoes_ano, output_file = "temporal_publicacoes.png") {
  cat("📊 Gerando gráfico de publicações...\n")
  
  p <- ggplot(publicacoes_ano, aes(x = Ano, y = Total)) +
    geom_line(color = "#2E86AB", size = 1.5) +
    geom_point(color = "#2E86AB", size = 4, alpha = 0.8) +
    geom_smooth(method = "loess", se = TRUE, color = "#FC4E07", 
                fill = "#FC4E07", alpha = 0.2, linetype = "dashed") +
    scale_x_continuous(breaks = seq(2010, 2025, 2)) +
    labs(
      title = "Evolução das Publicações em ML para Indicações Geográficas",
      subtitle = "Período: 2010-2025",
      x = "Ano",
      y = "Número de Publicações",
      caption = "Linha tracejada: tendência LOESS"
    ) +
    theme_minimal(base_size = 14) +
    theme(
      plot.title = element_text(face = "bold", size = 16, hjust = 0.5),
      plot.subtitle = element_text(hjust = 0.5, color = "gray40"),
      panel.grid.minor = element_blank()
    )
  
  ggsave(output_file, plot = p, width = 12, height = 7, dpi = 300)
  cat(sprintf("✓ Gráfico de publicações salvo: %s\n", output_file))
}

################################################################################
# FUNÇÃO: Plot de algoritmos ao longo do tempo
################################################################################
plot_algoritmos_tempo <- function(algoritmos_ano, output_file = "temporal_algoritmos.png") {
  cat("📊 Gerando gráfico de algoritmos...\n")
  
  algoritmos_long <- algoritmos_ano %>%
    pivot_longer(-Ano, names_to = "Algoritmo", values_to = "Frequencia")
  
  p <- ggplot(algoritmos_long, aes(x = Ano, y = Frequencia, color = Algoritmo, group = Algoritmo)) +
    geom_line(size = 1.2, alpha = 0.8) +
    geom_point(size = 2.5, alpha = 0.7) +
    scale_x_continuous(breaks = seq(2010, 2025, 2)) +
    scale_color_viridis_d(option = "plasma", begin = 0.1, end = 0.9) +
    labs(
      title = "Temporal Evolution of Machine Learning Algorithm Adoption (2010–2025)",
      subtitle = "Frequency of use in Geographical Indications studies by year",
      x = "Publication Year",
      y = "Absolute Frequency",
      color = "Algorithm"
    ) +
    theme_minimal(base_size = 14) +
    theme(
      plot.title = element_text(face = "bold", size = 16, hjust = 0.5),
      plot.subtitle = element_text(hjust = 0.5, color = "gray40"),
      legend.position = "right",
      panel.grid.minor = element_blank()
    )
  
  ggsave(output_file, plot = p, width = 14, height = 8, dpi = 300)
  cat(sprintf("✓ Gráfico de algoritmos salvo: %s\n", output_file))
}

################################################################################
# FUNÇÃO: Plot de produtos ao longo do tempo
################################################################################
plot_produtos_tempo <- function(produtos_ano, output_file = "temporal_produtos.png") {
  cat("📊 Gerando gráfico de produtos...\n")
  
  produtos_long <- produtos_ano %>%
    pivot_longer(-Ano, names_to = "Produto", values_to = "Frequencia")
  
  p <- ggplot(produtos_long, aes(x = Ano, y = Frequencia, fill = Produto)) +
    geom_area(alpha = 0.7, position = "stack") +
    scale_x_continuous(breaks = seq(2010, 2025, 2)) +
    scale_fill_viridis_d(option = "turbo") +
    labs(
      title = "Temporal Evolution of Products Investigated in GI Studies (2010–2025)",
      subtitle = "Cumulative frequency distribution by product category and year",
      x = "Publication Year",
      y = "Cumulative Frequency",
      fill = "Product Category"
    ) +
    theme_minimal(base_size = 14) +
    theme(
      plot.title = element_text(face = "bold", size = 16, hjust = 0.5),
      plot.subtitle = element_text(hjust = 0.5, color = "gray40"),
      legend.position = "right",
      panel.grid.minor = element_blank()
    )
  
  ggsave(output_file, plot = p, width = 14, height = 8, dpi = 300)
  cat(sprintf("✓ Gráfico de produtos salvo: %s\n", output_file))
}

################################################################################
# FUNÇÃO: Plot de regiões ao longo do tempo
################################################################################
plot_regioes_tempo <- function(regioes_ano, output_file = "temporal_regioes.png") {
  cat("📊 Gerando gráfico de regiões...\n")
  
  regioes_long <- regioes_ano %>%
    pivot_longer(-Ano, names_to = "Regiao", values_to = "Frequencia")
  
  p <- ggplot(regioes_long, aes(x = Ano, y = Frequencia, color = Regiao, group = Regiao)) +
    geom_line(size = 1.3, alpha = 0.8) +
    geom_point(size = 3, alpha = 0.7) +
    scale_x_continuous(breaks = seq(2010, 2025, 2)) +
    scale_color_manual(values = c("Europe" = "#2E86AB", "Asia" = "#FC4E07", 
                                   "Americas" = "#A23B72"),
                       labels = c("Europe" = "Europe", "Asia" = "Asia", 
                                  "Americas" = "Americas")) +
    labs(
      title = "Geographic Distribution of ML in GI Studies (2010–2025)",
      subtitle = "Absolute frequency of publications by region and year",
      x = "Publication Year",
      y = "Absolute Frequency",
      color = "Geographic Region"
    ) +
    theme_minimal(base_size = 14) +
    theme(
      plot.title = element_text(face = "bold", size = 16, hjust = 0.5),
      plot.subtitle = element_text(hjust = 0.5, color = "gray40"),
      legend.position = "right",
      panel.grid.minor = element_blank()
    )
  
  ggsave(output_file, plot = p, width = 12, height = 7, dpi = 300)
  cat(sprintf("✓ Gráfico de regiões salvo: %s\n", output_file))
}

################################################################################
# FUNÇÃO: Heatmap de evolução
################################################################################
plot_heatmap_evolucao <- function(dados_temporais, output_file = "temporal_heatmap.png") {
  cat("📊 Gerando heatmap de evolução...\n")
  
  # Combinar algoritmos e produtos
  combined <- dados_temporais$algoritmos %>%
    left_join(dados_temporais$produtos, by = "Ano") %>%
    pivot_longer(-Ano, names_to = "Feature", values_to = "Frequencia")
  
  p <- ggplot(combined, aes(x = Ano, y = Feature, fill = Frequencia)) +
    geom_tile(color = "white", size = 0.5) +
    geom_text(aes(label = Frequencia), color = "white", size = 2.5, fontface = "bold") +
    scale_fill_viridis_c(option = "magma", direction = -1) +
    scale_x_continuous(breaks = seq(2010, 2025, 2)) +
    labs(
      title = "Heatmap of Temporal Evolution: Algorithms and Products",
      subtitle = "Frequency of use in Geographical Indications studies by year (2010–2025)",
      x = "Publication Year",
      y = "Feature (Algorithm or Product)",
      fill = "Absolute Frequency"
    ) +
    theme_minimal(base_size = 12) +
    theme(
      plot.title = element_text(face = "bold", size = 14, hjust = 0.5),
      plot.subtitle = element_text(hjust = 0.5, color = "gray40"),
      axis.text.y = element_text(size = 10),
      legend.position = "right",
      panel.grid = element_blank()
    )
  
  ggsave(output_file, plot = p, width = 14, height = 10, dpi = 300)
  cat(sprintf("✓ Heatmap de evolução salvo: %s\n", output_file))
}

################################################################################
# FUNÇÃO: Análise de tendências
################################################################################
calcular_tendencias <- function(dados_temporais) {
  cat("🔬 Calculando tendências temporais...\n")
  
  tendencias <- list()
  
  # Algoritmos
  for (col in setdiff(names(dados_temporais$algoritmos), "Ano")) {
    df <- dados_temporais$algoritmos %>% select(Ano, all_of(col))
    colnames(df) <- c("Ano", "Valor")
    
    if (sum(df$Valor) >= 5) {  # Mínimo de 5 ocorrências
      cor_test <- cor.test(df$Ano, df$Valor, method = "spearman")
      tendencias[[col]] <- data.frame(
        Feature = col,
        Tipo = "Algoritmo",
        Correlacao = cor_test$estimate,
        PValue = cor_test$p.value,
        Significativo = cor_test$p.value < 0.05,
        Tendencia = ifelse(cor_test$estimate > 0, "Crescente", "Decrescente"),
        stringsAsFactors = FALSE
      )
    }
  }
  
  # Produtos
  for (col in setdiff(names(dados_temporais$produtos), "Ano")) {
    df <- dados_temporais$produtos %>% select(Ano, all_of(col))
    colnames(df) <- c("Ano", "Valor")
    
    if (sum(df$Valor) >= 5) {
      cor_test <- cor.test(df$Ano, df$Valor, method = "spearman")
      tendencias[[col]] <- data.frame(
        Feature = col,
        Tipo = "Produto",
        Correlacao = cor_test$estimate,
        PValue = cor_test$p.value,
        Significativo = cor_test$p.value < 0.05,
        Tendencia = ifelse(cor_test$estimate > 0, "Crescente", "Decrescente"),
        stringsAsFactors = FALSE
      )
    }
  }
  
  tendencias_df <- bind_rows(tendencias)
  tendencias_df <- tendencias_df %>% arrange(desc(abs(Correlacao)))
  
  cat("✓ Tendências calculadas\n\n")
  
  return(tendencias_df)
}

################################################################################
# FUNÇÃO: Plot de tendências significativas
################################################################################
plot_tendencias <- function(tendencias, output_file = "temporal_tendencias.png") {
  cat("📊 Gerando gráfico de tendências...\n")
  
  # Filtrar apenas tendências significativas
  tend_sig <- tendencias %>%
    filter(Significativo == TRUE) %>%
    mutate(Feature = reorder(Feature, Correlacao))
  
  if (nrow(tend_sig) == 0) {
    cat("⚠️  Nenhuma tendência significativa detectada (p < 0.05)\n")
    return(NULL)
  }
  
  p <- ggplot(tend_sig, aes(x = Correlacao, y = Feature, fill = Tipo)) +
    geom_col(alpha = 0.8) +
    geom_vline(xintercept = 0, linetype = "dashed", color = "gray30") +
    scale_fill_viridis_d(option = "plasma", begin = 0.2, end = 0.8) +
    labs(
      title = "Statistically Significant Temporal Trends (p < 0.05)",
      subtitle = "Spearman correlation coefficient (ρ) between frequency and publication year",
      x = "Spearman Correlation (ρ)",
      y = "Feature (Algorithm or Product)",
      fill = "Category"
    ) +
    theme_minimal(base_size = 14) +
    theme(
      plot.title = element_text(face = "bold", size = 16, hjust = 0.5),
      plot.subtitle = element_text(hjust = 0.5, color = "gray40"),
      legend.position = "right",
      panel.grid.minor = element_blank()
    )
  
  ggsave(output_file, plot = p, width = 12, height = 8, dpi = 300)
  cat(sprintf("✓ Gráfico de tendências salvo: %s\n", output_file))
}

################################################################################
# FUNÇÃO: Relatório
################################################################################
gerar_relatorio <- function(dados_temporais, tendencias, output_file = "temporal_relatorio.txt") {
  cat("\n📝 Gerando relatório estatístico...\n")
  
  sink(output_file)
  cat("================================================================================\n")
  cat("RELATÓRIO DE ANÁLISE TEMPORAL - ML PARA INDICAÇÕES GEOGRÁFICAS\n")
  cat("================================================================================\n\n")
  cat(sprintf("Data de execução: %s\n", Sys.time()))
  cat(sprintf("Período analisado: 2010-2025\n\n"))
  
  cat("--------------------------------------------------------------------------------\n")
  cat("EVOLUÇÃO DAS PUBLICAÇÕES\n")
  cat("--------------------------------------------------------------------------------\n")
  print(dados_temporais$publicacoes)
  cat("\n")
  
  cat("--------------------------------------------------------------------------------\n")
  cat("TENDÊNCIAS TEMPORAIS SIGNIFICATIVAS (p < 0.05)\n")
  cat("--------------------------------------------------------------------------------\n")
  tend_sig <- tendencias %>% filter(Significativo == TRUE)
  if (nrow(tend_sig) > 0) {
    print(tend_sig)
  } else {
    cat("Nenhuma tendência significativa detectada.\n")
  }
  cat("\n")
  
  cat("--------------------------------------------------------------------------------\n")
  cat("ALGORITMOS MAIS UTILIZADOS (2020-2025)\n")
  cat("--------------------------------------------------------------------------------\n")
  alg_recente <- dados_temporais$algoritmos %>%
    filter(Ano >= 2020) %>%
    summarise(across(-Ano, sum)) %>%
    pivot_longer(everything(), names_to = "Algoritmo", values_to = "Total") %>%
    arrange(desc(Total))
  print(alg_recente)
  cat("\n")
  
  cat("--------------------------------------------------------------------------------\n")
  cat("PRODUTOS MAIS ESTUDADOS (2020-2025)\n")
  cat("--------------------------------------------------------------------------------\n")
  prod_recente <- dados_temporais$produtos %>%
    filter(Ano >= 2020) %>%
    summarise(across(-Ano, sum)) %>%
    pivot_longer(everything(), names_to = "Produto", values_to = "Total") %>%
    arrange(desc(Total))
  print(prod_recente)
  cat("\n")
  
  cat("================================================================================\n")
  sink()
  
  cat(sprintf("✓ Relatório estatístico salvo: %s\n", output_file))
}

################################################################################
# FUNÇÃO: Salvar dados
################################################################################
salvar_dados <- function(dados_temporais, tendencias) {
  write.csv(dados_temporais$publicacoes, "temporal_publicacoes.csv", row.names = FALSE)
  write.csv(dados_temporais$algoritmos, "temporal_algoritmos.csv", row.names = FALSE)
  write.csv(dados_temporais$produtos, "temporal_produtos.csv", row.names = FALSE)
  write.csv(tendencias, "temporal_tendencias.csv", row.names = FALSE)
  
  cat("\n✓ Dados salvos: temporal_*.csv\n")
}

################################################################################
# EXECUÇÃO PRINCIPAL
################################################################################
main <- function() {
  caminho_bib <- "../corpus.bib"
  
  if (!file.exists(caminho_bib)) {
    stop("❌ Erro: Arquivo .bib não encontrado em: ", caminho_bib)
  }
  
  # 1. Extrair dados
  dados <- extrair_dados_temporais(caminho_bib)
  
  # 2. Agregar por ano
  dados_temporais <- agregar_por_ano(dados)
  
  # 3. Calcular tendências
  tendencias <- calcular_tendencias(dados_temporais)
  
  # 4. Visualizações
  cat("📊 Gerando visualizações...\n")
  plot_publicacoes_tempo(dados_temporais$publicacoes)
  plot_algoritmos_tempo(dados_temporais$algoritmos)
  plot_produtos_tempo(dados_temporais$produtos)
  plot_regioes_tempo(dados_temporais$regioes)
  plot_heatmap_evolucao(dados_temporais)
  plot_tendencias(tendencias)
  
  # 5. Relatório
  gerar_relatorio(dados_temporais, tendencias)
  
  # 6. Salvar dados
  salvar_dados(dados_temporais, tendencias)
  
  cat("\n")
  cat("================================================================================\n")
  cat("✅ ANÁLISE TEMPORAL CONCLUÍDA COM SUCESSO!\n")
  cat("================================================================================\n")
}

tryCatch({
  main()
}, error = function(e) {
  cat("\n❌ ERRO durante a execução:\n")
  cat(conditionMessage(e), "\n")
})
