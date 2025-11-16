#!/usr/bin/env Rscript
# GERADOR DE FLUXOGRAMA PRISMA 2020 - VERSÃO R OFICIAL
# Script para gerar diagramas PRISMA 2020 profissionais usando o pacote R oficial
# PRISMA2020 baseado no repositório: https://github.com/prisma-flowdiagram/PRISMA2020
# Author: Adaptado para português
# Data: 2025

# Supprimir avisos
options(warn = -1)

# Configurar CRAN mirror
options(repos = c(CRAN = "https://cran.rstudio.com"))

# Verificar e instalar pacotes necessários
pacotes_necessarios <- c("devtools", "htmlwidgets", "DiagrammeR")

# Forçar reinstalação do magrittr
install.packages("magrittr", quiet = TRUE)

for (pacote in pacotes_necessarios) {
  if (!require(pacote, character.only = TRUE)) {
    cat(sprintf("📦 Instalando pacote: %s\n", pacote))
    install.packages(pacote, quiet = TRUE)
  }
}

# Forçar reinstalação do PRISMA2020
if (!require("PRISMA2020", character.only = TRUE)) {
    cat("📦 Instalando PRISMA2020 do GitHub...\n")
    devtools::install_github("prisma-flowdiagram/PRISMA2020", quiet = TRUE, force = TRUE)
}


library(PRISMA2020, quietly = TRUE)
library(htmlwidgets, quietly = TRUE)
library(DiagrammeR, quietly = TRUE)

# Carregar dados do CSV
cat("======================================================================\n")
cat("🔄 GERADOR DE FLUXOGRAMA PRISMA 2020 - VERSÃO R OFICIAL\n")
cat("======================================================================\n\n")

csv_file <- "PRISMA.csv"

if (!file.exists(csv_file)) {
  cat(sprintf("❌ Arquivo %s não encontrado!\n", csv_file))
  quit(status = 1)
}

cat(sprintf("📂 Carregando dados de: %s\n", csv_file))

# Ler os dados
data <- read.csv(csv_file, stringsAsFactors = FALSE)

cat("✅ Dados carregados com sucesso\n\n")

# Processar dados para formato correto
cat("📊 Processando dados PRISMA...\n")
prisma_data <- PRISMA_data(data)

# Gerar o fluxograma PRISMA 2020
cat("🎨 Gerando fluxograma PRISMA 2020...\n")

plot <- PRISMA_flowdiagram(
  prisma_data,
  fontsize = 12,
  font = "Helvetica",
  title_colour = "Goldenrod1",
  greybox_colour = "Gainsboro",
  main_colour = "Black",
  arrow_colour = "Black",
  arrow_head = "normal",
  arrow_tail = "none",
  interactive = TRUE,
  previous = FALSE,
  other = TRUE,
  detail_databases = TRUE,
  detail_registers = FALSE,
  meta_analysis = FALSE,
  side_boxes = TRUE
)

# Salvar em diferentes formatos
output_html <- "prisma_flowdiagram_interativo.html"
output_pdf <- "prisma_flowdiagram.pdf"
output_png <- "prisma_flowdiagram.png"
output_svg <- "prisma_flowdiagram.svg"

cat("\n📥 Salvando arquivos...\n")

# HTML (com interatividade)
tryCatch({
  PRISMA_save(plot, filename = output_html, filetype = "HTML", overwrite = TRUE)
  cat(sprintf("✅ HTML: %s\n", output_html))
}, error = function(e) {
  cat(sprintf("❌ Erro ao salvar HTML: %s\n", e$message))
})

# PDF
tryCatch({
  PRISMA_save(plot, filename = output_pdf, filetype = "PDF", overwrite = TRUE)
  cat(sprintf("✅ PDF: %s\n", output_pdf))
}, error = function(e) {
  cat(sprintf("⚠️  Aviso ao salvar PDF: %s\n", e$message))
})

# PNG
tryCatch({
  PRISMA_save(plot, filename = output_png, filetype = "PNG", overwrite = TRUE)
  cat(sprintf("✅ PNG: %s\n", output_png))
}, error = function(e) {
  cat(sprintf("⚠️  Aviso ao salvar PNG: %s\n", e$message))
})

# SVG
tryCatch({
  PRISMA_save(plot, filename = output_svg, filetype = "SVG", overwrite = TRUE)
  cat(sprintf("✅ SVG: %s\n", output_svg))
}, error = function(e) {
  cat(sprintf("⚠️  Aviso ao salvar SVG: %s\n", e$message))
})

cat("\n======================================================================\n")
cat("✨ FLUXOGRAMA PRISMA 2020 GERADO COM SUCESSO!\n")
cat("======================================================================\n")
cat(sprintf("📁 Arquivos de saída disponíveis no diretório atual\n"))
cat(sprintf("🌐 Arquivo HTML interativo: %s\n", output_html))
cat("📖 Para visualizar, abra o arquivo HTML em seu navegador\n\n")
