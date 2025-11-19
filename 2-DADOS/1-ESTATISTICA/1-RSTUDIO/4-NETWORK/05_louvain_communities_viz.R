################################################################################
# VISUALIZAÇÃO AVANÇADA DAS COMUNIDADES DE LOUVAIN
# Machine Learning para Indicações Geográficas
#
# Este script gera visualizações detalhadas dos três módulos identificados
# pelo algoritmo de Louvain, criando uma figura composta que complementa
# a Tabela 5 do manuscrito.
#
# Outputs:
#   - louvain_modules_detailed.png (Figura detalhada dos 3 módulos)
#   - louvain_modules_summary.png (Figura resumo para o manuscrito)
################################################################################

rm(list = ls())
gc()

packages <- c("bib2df", "tidyverse", "igraph", "ggraph", "tidygraph", 
              "viridis", "patchwork", "scales", "ggforce")

for (pkg in packages) {
  if (!require(pkg, character.only = TRUE, quietly = TRUE)) {
    install.packages(pkg, dependencies = TRUE, repos = "https://cloud.r-project.org")
    library(pkg, character.only = TRUE)
  }
}

cat("\n")
cat("================================================================================\n")
cat("VISUALIZAÇÃO DETALHADA DAS COMUNIDADES DE LOUVAIN\n")
cat("Machine Learning para Indicações Geográficas\n")
cat("================================================================================\n\n")

################################################################################
# CARREGAR DADOS E REDE (reutilizando funções do script anterior)
################################################################################
source("04_network_analysis.R", encoding = "UTF-8")

# Construir rede
caminho_bib <- "../../1-RSTUDIO/corpus.bib"
dados <- extrair_coocorrencias(caminho_bib)
g <- construir_rede(dados$presenca, min_coocorrencia = 3)
g <- detectar_comunidades(g)

################################################################################
# FUNÇÃO: Criar visualização detalhada de um módulo específico
################################################################################
plot_module_detail <- function(g, module_id, module_name, module_color) {
  # Extrair nós do módulo
  nodes_in_module <- V(g)$name[V(g)$community == module_id]
  
  # Criar subgrafo
  g_sub <- induced_subgraph(g, V(g)[V(g)$community == module_id])
  
  # Adicionar categoria aos nós
  algoritmos <- c("RandomForest", "SVM", "NeuralNetwork", "KNN", "DecisionTree", 
                  "GradientBoosting")
  instrumentos <- c("NIR", "FTIR", "GCMS", "LCMS", "Sensor")
  produtos <- c("Wine", "Honey", "Meat", "Olive", "Cheese", "Tea")
  regioes <- c("Africa", "Asia", "Europe")
  
  V(g_sub)$category <- case_when(
    V(g_sub)$name %in% algoritmos ~ "Algoritmo",
    V(g_sub)$name %in% instrumentos ~ "Instrumento",
    V(g_sub)$name %in% produtos ~ "Produto",
    V(g_sub)$name %in% regioes ~ "Região",
    TRUE ~ "Outro"
  )
  
  # Converter para tidygraph
  tg <- as_tbl_graph(g_sub)
  
  # Plot
  p <- ggraph(tg, layout = "stress") +
    geom_edge_link(aes(width = weight), alpha = 0.6, color = "gray50") +
    geom_node_point(aes(size = degree(g_sub), color = V(g_sub)$category), 
                    alpha = 0.85, stroke = 1.5) +
    geom_node_text(aes(label = name), repel = TRUE, size = 3.5, 
                   fontface = "bold", max.overlaps = 20) +
    scale_edge_width(range = c(0.8, 3.5), guide = "none") +
    scale_size_continuous(range = c(5, 12), guide = "none") +
    scale_color_manual(
      values = c(
        "Algoritmo" = "#E63946",
        "Instrumento" = "#457B9D",
        "Produto" = "#2A9D8F",
        "Região" = "#F4A261"
      )
    ) +
    labs(
      title = module_name,
      subtitle = sprintf("n=%d | Densidade=%.2f", 
                        vcount(g_sub), edge_density(g_sub)),
      color = "Categoria"
    ) +
    theme_graph(base_family = "sans") +
    theme(
      plot.title = element_text(face = "bold", size = 14, hjust = 0.5),
      plot.subtitle = element_text(hjust = 0.5, color = "gray40", size = 10),
      legend.position = "bottom",
      legend.title = element_text(face = "bold", size = 10),
      plot.background = element_rect(fill = "white", color = NA),
      panel.background = element_rect(fill = "white", color = NA)
    )
  
  return(p)
}

################################################################################
# FUNÇÃO: Criar figura composta dos três módulos
################################################################################
plot_three_modules <- function(g) {
  cat("📊 Gerando visualização dos três módulos de Louvain...\n")
  
  # Plotar cada módulo
  p1 <- plot_module_detail(g, 1, "Módulo 1: Árvores + Espectroscopia", "#E76F51")
  p2 <- plot_module_detail(g, 2, "Módulo 2: SVM/KNN + Cromatografia", "#2A9D8F")
  p3 <- plot_module_detail(g, 3, "Módulo 3: Redes Neurais + Sensores", "#264653")
  
  # Combinar com patchwork
  combined <- (p1 | p2 | p3) +
    plot_annotation(
      title = "Módulos Tecnológicos Identificados pelo Algoritmo de Louvain",
      subtitle = "Rede de Coocorrências: 20 nós, 58 arestas | Densidade=0.305 | Clustering=0.595",
      theme = theme(
        plot.title = element_text(face = "bold", size = 18, hjust = 0.5),
        plot.subtitle = element_text(hjust = 0.5, color = "gray40", size = 12)
      )
    ) &
    theme(legend.position = "bottom")
  
  # Salvar
  ggsave("louvain_modules_detailed.png", plot = combined, 
         width = 20, height = 7, dpi = 300)
  
  cat("✓ Figura detalhada dos módulos salva: louvain_modules_detailed.png\n")
  
  return(combined)
}

################################################################################
# FUNÇÃO: Criar figura resumo com anotações para manuscrito
################################################################################
plot_modules_summary <- function(g) {
  cat("📊 Gerando figura resumo para o manuscrito...\n")
  
  # Adicionar mais informações aos nós
  V(g)$size_scaled <- degree(g)
  V(g)$module_name <- case_when(
    V(g)$community == 1 ~ "M1: Árvores",
    V(g)$community == 2 ~ "M2: SVM/KNN",
    V(g)$community == 3 ~ "M3: Redes Neurais",
    TRUE ~ "Outro"
  )
  
  # Converter para tidygraph
  tg <- as_tbl_graph(g)
  
  # Plot principal
  p <- ggraph(tg, layout = "fr") +
    geom_edge_link(aes(width = weight, alpha = weight), color = "gray60") +
    geom_node_point(aes(size = size_scaled, fill = as.factor(V(g)$community)),
                    shape = 21, color = "white", stroke = 1.2, alpha = 0.9) +
    geom_node_text(aes(label = name), repel = TRUE, size = 3.2,
                   fontface = "bold", max.overlaps = 25,
                   segment.color = "gray70", segment.size = 0.3) +
    scale_edge_width(range = c(0.3, 2.5), guide = "none") +
    scale_edge_alpha(range = c(0.3, 0.7), guide = "none") +
    scale_size_continuous(range = c(3, 15), guide = "none") +
    scale_fill_manual(
      name = "Módulo Tecnológico",
      values = c(
        "1" = "#E76F51",
        "2" = "#2A9D8F", 
        "3" = "#264653"
      ),
      labels = c(
        "1" = "M1: Árvores + Espectroscopia (n=6)",
        "2" = "M2: SVM/KNN + Cromatografia (n=6)",
        "3" = "M3: Redes Neurais + Sensores (n=8)"
      )
    ) +
    labs(
      title = "Estrutura Modular da Rede de ML para Indicações Geográficas",
      subtitle = "Comunidades detectadas pelo algoritmo de Louvain | Tamanhos proporcionais ao grau de centralidade",
      caption = "Densidade da rede = 0.305 | Coeficiente de clustering = 0.595\nNós mais centrais: NeuralNetwork (degree=15), SVM (degree=12), RandomForest (degree=11)"
    ) +
    theme_graph(base_family = "sans") +
    theme(
      plot.title = element_text(face = "bold", size = 16, hjust = 0.5, 
                                margin = margin(b = 5)),
      plot.subtitle = element_text(hjust = 0.5, color = "gray40", size = 11,
                                   margin = margin(b = 10)),
      plot.caption = element_text(hjust = 0.5, color = "gray50", size = 9,
                                 margin = margin(t = 10)),
      legend.position = "bottom",
      legend.title = element_text(face = "bold", size = 11),
      legend.text = element_text(size = 10),
      plot.background = element_rect(fill = "white", color = NA),
      panel.background = element_rect(fill = "white", color = NA),
      plot.margin = margin(15, 15, 15, 15)
    ) +
    guides(fill = guide_legend(override.aes = list(size = 6)))
  
  # Salvar
  ggsave("louvain_modules_summary.png", plot = p,
         width = 14, height = 10, dpi = 300, bg = "white")
  
  cat("✓ Figura resumo salva: louvain_modules_summary.png\n")
  
  return(p)
}

################################################################################
# FUNÇÃO: Criar tabela visual dos módulos (complemento à Tabela 5)
################################################################################
create_module_table_visual <- function(g) {
  cat("📊 Criando visualização em tabela dos módulos...\n")
  
  # Preparar dados
  modules_data <- tibble(
    Module = c("M1", "M2", "M3"),
    Size = c(6, 6, 8),
    Algorithms = c(
      "RandomForest\nDecisionTree\nGradient Boosting",
      "SVM\nKNN",
      "Neural Networks\nCNN\nDeep Learning"
    ),
    Techniques = c(
      "NIR\nQuimiometria",
      "GC-MS\nLC-MS\nHPLC",
      "NIR, FTIR\ne-nose"
    ),
    Products = c(
      "Vinho\nMel",
      "Carnes\nProdutos\nRegionais",
      "Azeite\nQueijo\nChá"
    ),
    Region = c("África\nEuropa", "Ásia", "Europa\nÁsia"),
    Color = c("#E76F51", "#2A9D8F", "#264653")
  )
  
  # Criar visualização
  p <- ggplot(modules_data, aes(x = 1, y = Module)) +
    geom_tile(aes(fill = Color), color = "white", size = 2, alpha = 0.3) +
    geom_text(aes(x = 0.7, label = paste0(Module, "\n(n=", Size, ")")),
              fontface = "bold", size = 5) +
    geom_text(aes(x = 1.3, label = Algorithms), size = 3.5, hjust = 0) +
    geom_text(aes(x = 2.0, label = Techniques), size = 3.5, hjust = 0) +
    geom_text(aes(x = 2.7, label = Products), size = 3.5, hjust = 0) +
    geom_text(aes(x = 3.3, label = Region), size = 3.5, hjust = 0) +
    scale_fill_identity() +
    scale_x_continuous(
      breaks = c(0.7, 1.3, 2.0, 2.7, 3.3),
      labels = c("Módulo", "Algoritmos", "Técnicas", "Produtos", "Região")
    ) +
    labs(
      title = "Composição dos Três Módulos Tecnológicos",
      subtitle = "Análise de Comunidades de Louvain"
    ) +
    theme_minimal(base_size = 12) +
    theme(
      plot.title = element_text(face = "bold", size = 16, hjust = 0.5),
      plot.subtitle = element_text(hjust = 0.5, color = "gray40"),
      axis.title = element_blank(),
      axis.text.y = element_blank(),
      axis.text.x = element_text(face = "bold", size = 11),
      panel.grid = element_blank(),
      plot.background = element_rect(fill = "white", color = NA)
    )
  
  ggsave("louvain_modules_table_visual.png", plot = p,
         width = 14, height = 6, dpi = 300, bg = "white")
  
  cat("✓ Tabela visual salva: louvain_modules_table_visual.png\n")
  
  return(p)
}

################################################################################
# EXECUÇÃO PRINCIPAL
################################################################################
main_viz <- function() {
  cat("\n📊 Gerando visualizações avançadas das comunidades...\n\n")
  
  # 1. Figura detalhada dos três módulos lado a lado
  p_detailed <- plot_three_modules(g)
  
  # 2. Figura resumo para o manuscrito
  p_summary <- plot_modules_summary(g)
  
  # 3. Tabela visual
  p_table <- create_module_table_visual(g)
  
  cat("\n")
  cat("================================================================================\n")
  cat("✅ VISUALIZAÇÕES AVANÇADAS CONCLUÍDAS!\n")
  cat("================================================================================\n")
  cat("\nArquivos gerados:\n")
  cat("  1. louvain_modules_detailed.png - Figura detalhada dos 3 módulos\n")
  cat("  2. louvain_modules_summary.png - Figura resumo para manuscrito\n")
  cat("  3. louvain_modules_table_visual.png - Tabela visual complementar\n")
  cat("\nRecomendação: Use louvain_modules_summary.png como Figura 9\n")
  cat("              A Tabela 5 (markdown) permanece no texto\n")
  cat("================================================================================\n")
}

tryCatch({
  main_viz()
}, error = function(e) {
  cat("\n❌ ERRO durante a execução:\n")
  cat(conditionMessage(e), "\n")
})
