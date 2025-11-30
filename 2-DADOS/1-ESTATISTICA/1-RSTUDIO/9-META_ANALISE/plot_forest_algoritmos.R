# =============================================================================
# FOREST PLOT: META-ANÁLISE POR ALGORITMO
# Script independente para gerar forest plot limpo e organizado
# =============================================================================

# Carregar pacotes
library(metafor)
library(meta)
library(dplyr)

# Limpar ambiente
rm(list = ls())
gc()

# Definir diretório
setwd("C:/Users/vidal/OneDrive/Documentos/13 - CLONEGIT/revisaoescopo/2-DADOS/1-ESTATISTICA/1-RSTUDIO/9-META_ANALISE")

# -----------------------------------------------------------------------------
# 1. PREPARAR DADOS DE ACURÁCIAS POR ALGORITMO
# -----------------------------------------------------------------------------

# Ler dados consolidados (substitua pelo arquivo real se necessário)
acuracias_algoritmo <- data.frame(
  algoritmo = c("PLS-DA", "Random Forest", "Neural Network", "Deep Learning", 
                "SVM", "XGBoost", "Decision Tree"),
  acuracia_pooled = c(92.9, 91.3, 90.8, 90.5, 90.3, 89.8, 81.0),
  ic_inferior = c(89.3, 89.7, 88.8, 87.1, 88.8, 85.6, 68.6),
  ic_superior = c(95.4, 92.7, 92.5, 93.1, 91.6, 92.9, 89.3),
  n_estudos = c(8, 37, 32, 15, 47, 7, 2)
)

# Ordenar por acurácia decrescente
acuracias_algoritmo <- acuracias_algoritmo %>%
  arrange(desc(acuracia_pooled))

# Categorizar grupos funcionais
acuracias_algoritmo <- acuracias_algoritmo %>%
  mutate(
    grupo = case_when(
      algoritmo %in% c("Random Forest", "XGBoost", "Decision Tree") ~ "Ensemble",
      algoritmo == "PLS-DA" ~ "Quimiometria",
      algoritmo %in% c("SVM", "Neural Network", "Deep Learning") ~ "Kernel/Neural"
    ),
    grupo = factor(grupo, levels = c("Ensemble", "Quimiometria", "Kernel/Neural"))
  )

# -----------------------------------------------------------------------------
# 2. PREPARAR PARA metafor (transformação logit)
# -----------------------------------------------------------------------------

acuracias_algoritmo <- acuracias_algoritmo %>%
  mutate(
    yi = transf.logit(acuracia_pooled / 100),
    sei = (transf.logit(ic_superior / 100) - transf.logit(ic_inferior / 100)) / (2 * 1.96),
    studlab = paste0(algoritmo, " (n=", n_estudos, ")"),
    peso_pct = (n_estudos / sum(n_estudos)) * 100
  )

# Criar modelo meta
meta_alg <- rma(yi, sei = sei, data = acuracias_algoritmo, method = "REML")

# -----------------------------------------------------------------------------
# 3. CORES E SÍMBOLOS POR GRUPO
# -----------------------------------------------------------------------------

cores_grupo <- c(
  "Ensemble" = "#0072B2",
  "Quimiometria" = "#009E73",
  "Kernel/Neural" = "#D55E00"
)

# Mapear cores por algoritmo
cores_por_algo <- sapply(acuracias_algoritmo$grupo, function(g) cores_grupo[as.character(g)])

# Mapear símbolos: quadrado=Ensemble, diamante=Quimiometria, triângulo=Kernel/Neural
shapes_por_algo <- sapply(acuracias_algoritmo$grupo, function(g) {
  switch(as.character(g),
         "Ensemble" = 15,
         "Quimiometria" = 18,
         "Kernel/Neural" = 17)
})

# -----------------------------------------------------------------------------
# 4. FOREST PLOT LIMPO (estilo OLD)
# -----------------------------------------------------------------------------

png("plot_forest_algoritmos_limpo.png", width = 12, height = 7.5, units = "in", res = 300)

# Margens mais compactas (reduz espaço ocioso)
par(mar = c(4, 11, 3.2, 1.2))
par(cex = 0.70, font = 1)

# Forest plot
forest(meta_alg,
       slab = acuracias_algoritmo$studlab,
       atransf = transf.ilogit,
       xlim = c(-1.9, 2.2),
       alim = c(0.75, 0.98),
       at = transf.logit(c(0.80, 0.85, 0.90, 0.95)),
       xlab = "Acurácia Consolidada (proporção)",
       
       # Colunas extras (reduzidas e mais próximas)
       ilab = cbind(
         acuracias_algoritmo$n_estudos,
         sprintf("%.1f%%", acuracias_algoritmo$acuracia_pooled),
         sprintf("[%.1f; %.1f]", acuracias_algoritmo$ic_inferior, acuracias_algoritmo$ic_superior),
         sprintf("%.1f%%", acuracias_algoritmo$peso_pct)
       ),
       ilab.xpos = c(-1.60, -1.30, -1.02, -0.74),
       ilab.pos = 4,
       
       # Símbolos por grupo (bordas pretas para legibilidade)
       pch = shapes_por_algo,
       col = "black",
       bg = cores_por_algo,
       psize = 1.15,
       
       # Sem diamante automático
       refline = transf.logit(transf.ilogit(meta_alg$beta)),
       addfit = FALSE,
       showweights = FALSE,
       
       # Posicionamento: linhas de cima para baixo (mais compacto)
       rows = seq(nrow(acuracias_algoritmo), 1, by = -1),
       ylim = c(0.3, nrow(acuracias_algoritmo) + 2.2),
       
       # Cabeçalhos
       header = c("Algoritmo", "Estimativa [IC 95%]"),
       top = 1.3,
       
       # Ajustes tipográficos
       cex = 0.70,
       cex.lab = 0.90,
       cex.axis = 0.70,
       digits = 3)

# Cabeçalhos das colunas extras
text(c(-1.60, -1.30, -1.02, -0.74), nrow(acuracias_algoritmo) + 1.6,
  c("n", "% Acurácia", "IC 95%", "Peso (%)"),
  cex = 0.70, font = 2, pos = 4)

# Linha vertical pontilhada de referência
# Linha leve na posição da estimativa global para referência
abline(v = meta_alg$beta, lty = 3, col = "gray60")

# Diamante do modelo consolidado NO TOPO
addpoly(meta_alg,
  row = nrow(acuracias_algoritmo) + 0.2,
  atransf = transf.ilogit,
  mlab = "Modelo (REML)",
  col = "gray80",
  border = "black",
  cex = 0.70)

# Legenda
legend("bottomleft",
  legend = c("Ensemble", "Quimiometria (PLS-DA)", "Kernel/Neural"),
  pch = c(15, 18, 17),
  pt.bg = c(cores_grupo["Ensemble"], cores_grupo["Quimiometria"], cores_grupo["Kernel/Neural"]),
  col = "black",
  pt.cex = 1.1,
  bty = "n",
  cex = 0.65)

dev.off()

cat("\n✓ Forest plot salvo: plot_forest_algoritmos_limpo.png\n")

# -----------------------------------------------------------------------------
# 5. TABELA DE RESUMO (estilo OLD)
# -----------------------------------------------------------------------------

library(kableExtra)

# Linha do modelo global
resumo_global <- tibble::tibble(
  `Algoritmo (n, obs)` = "Modelo de Efeitos Aleatórios",
  `% Acurácia` = sprintf("%.1f", transf.ilogit(meta_alg$beta) * 100),
  `IC 95%` = sprintf("[%.1f, %.1f]", 
                     transf.ilogit(meta_alg$ci.lb) * 100,
                     transf.ilogit(meta_alg$ci.ub) * 100),
  `Peso (%)` = "",
  `p-valor` = sprintf("%.3f", meta_alg$pval)
)

# Linhas por algoritmo
tabela_algoritmos <- tibble::tibble(
  `Algoritmo (n, obs)` = acuracias_algoritmo$studlab,
  `% Acurácia` = sprintf("%.1f", acuracias_algoritmo$acuracia_pooled),
  `IC 95%` = sprintf("[%.1f, %.1f]", acuracias_algoritmo$ic_inferior, acuracias_algoritmo$ic_superior),
  `Peso (%)` = sprintf("%.1f", acuracias_algoritmo$peso_pct),
  `p-valor` = "-"
)

# Combinar
tabela_final <- bind_rows(resumo_global, tabela_algoritmos)

# Caption
caption_meta <- sprintf(
  "Meta-Análise de Acurácias por Algoritmo (k = %d estudos)\nI² = %.1f%%, Tau² = %.3f, Q(df=%d) = %.2f, p(Q) = %.3f",
  meta_alg$k, meta_alg$I2, meta_alg$tau2, meta_alg$k - 1, meta_alg$QE, meta_alg$QEp
)

# Exibir tabela
print(kable(tabela_final,
            align = c("l", "r", "c", "r", "r"),
            caption = caption_meta) %>%
        kable_styling(bootstrap_options = "striped", full_width = FALSE))

cat("\n✓ Análise concluída!\n")
