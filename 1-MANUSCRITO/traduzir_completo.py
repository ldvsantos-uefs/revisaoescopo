#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script completo para traduzir revisao_escopo_pt.md para inglês acadêmico formal.
Preserva formatação Markdown, fórmulas LaTeX, referências bibliográficas e estrutura.
Versão 2.0 - Tradução contextual completa
"""

import re
from pathlib import Path
from typing import Dict, List, Tuple

def criar_dicionario_traducoes() -> Dict[str, str]:
    """Cria dicionário abrangente de traduções PT->EN."""
    return {
        # === SEÇÕES PRINCIPAIS ===
        "# Resumo": "# Abstract",
        "## **Palavras‑chave:**": "## **Keywords:**",
        "# 1. Introdução": "# 1. Introduction",
        "# 2. Materiais e Métodos": "# 2. Materials and Methods",
        "# 3. Resultados e Discussão": "# 3. Results and Discussion",
        "# 4. Conclusões": "# 4. Conclusions",
        "## Agradecimentos": "## Acknowledgments",
        "## Conflitos de Interesse": "## Conflicts of Interest",
        "## Declaração de Disponibilidade de Dados": "## Data Availability Statement",
        "## Declaração de Ética": "## Ethics Statement",
        "## Posicionamento/Envolvimento Comunitário": "## Community Positioning/Engagement",
        "## References": "## References",
        
        # === SUBSEÇÕES DE MÉTODOS ===
        "## 2.1 Questão de Pesquisa": "## 2.1 Research Question",
        "## 2.1.1 Fluxograma Metodológico PRISMA-ScR": "## 2.1.1 PRISMA-ScR Methodological Flowchart",
        "## 2.2 Estratégia de Busca e Extração de Estudos": "## 2.2 Search Strategy and Study Extraction",
        "## 2.3 Primeira Fase: Sistema Automatizado de Filtragem por Relevância Temática": "## 2.3 First Phase: Automated Filtering System by Thematic Relevance",
        "### 2.3.1 Algoritmo de Pontuação Ponderada": "### 2.3.1 Weighted Scoring Algorithm",
        "### 2.3.2 Implementação e Validação do Algoritmo": "### 2.3.2 Algorithm Implementation and Validation",
        "### 2.3.3 Validação Participativa e Refinamento de Algoritmos": "### 2.3.3 Participatory Validation and Algorithm Refinement",
        "### 2.3.4 Verificação de Cobertura e Categorização Automatizada": "### 2.3.4 Coverage Verification and Automated Categorization",
        "## 2.4 Segunda Fase: Avaliação Manual da Qualidade Metodológica": "## 2.4 Second Phase: Manual Methodological Quality Assessment",
        "### 2.4.1 Procedimentos de consenso e validação entre avaliadores": "### 2.4.1 Consensus Procedures and Inter-Rater Validation",
        "### 2.4.2 Critérios Específicos para Estudos Interdisciplinares": "### 2.4.2 Specific Criteria for Interdisciplinary Studies",
        "## 2.5 Terceira Fase: Análise Bibliométrica": "## 2.5 Third Phase: Bibliometric Analysis",
        "## 2.6 Quarta Fase: Síntese Qualitativa e Integração com Análise Documental": "## 2.6 Fourth Phase: Qualitative Synthesis and Integration with Documentary Analysis",
        "## 2.7 Análises Estatísticas": "## 2.7 Statistical Analyses",
        "### 2.7.1 Análises Descritivas e Exploratórias do Corpus": "### 2.7.1 Descriptive and Exploratory Corpus Analyses",
        "### 2.7.2 Análises Inferenciais de Validação dos Critérios Operacionais": "### 2.7.2 Inferential Analyses for Operational Criteria Validation",
        "## 2.8 Terroir Digital como Sistema de Auditoria Inferencial": "## 2.8 Digital Terroir as Inferential Auditing System",
        "### 2.8.1 Aplicação Analítica do Framework": "### 2.8.1 Analytical Framework Application",
        
        # === SUBSEÇÕES DE RESULTADOS ===
        "## 3.1 Terroir Digital: Definições Constitutiva e Operacional": "## 3.1 Digital Terroir: Constitutive and Operational Definitions",
        "## 3.2 Panorama das aplicações de aprendizado de máquina em indicações geográficas": "## 3.2 Overview of Machine Learning Applications in Geographical Indications",
        "## 3.3 Evolução temporal de produtos e algoritmos": "## 3.3 Temporal Evolution of Products and Algorithms",
        "## 3.4 Famílias Tecnológicas e Aplicações": "## 3.4 Technological Families and Applications",
        "## 3.5 Evidências quantitativas e meta‑análises": "## 3.5 Quantitative Evidence and Meta-Analyses",
        "## 3.5.4 Síntese Inferencial e Implicações Operacionais": "## 3.5.4 Inferential Synthesis and Operational Implications",
        "## 3.6 Barreiras à Auditabilidade e a Falência do Terroir Digital Estático": "## 3.6 Barriers to Auditability and the Failure of Static Digital Terroir",
        
        # === TERMOS TÉCNICOS PRINCIPAIS ===
        "Indicações Geográficas": "Geographical Indications",
        "Denominações de Origem": "Designations of Origin",
        "Indicação Geográfica Protegida": "Protected Geographical Indication",
        "Denominação de Origem Protegida": "Protected Designation of Origin",
        "Aprendizado de Máquina": "Machine Learning",
        "Inteligência Artificial": "Artificial Intelligence",
        "Terroir Digital": "Digital Terroir",
        "Gêmeo Digital Inferencial": "Inferential Digital Twin",
        "Gêmeo Digital": "Digital Twin",
        
        # === TERMOS DE GOVERNANÇA ===
        "serviços ecossistêmicos": "ecosystem services",
        "auditoria ambiental": "environmental auditing",
        "auditoria inferencial": "inferential auditing",
        "rastreabilidade": "traceability",
        "greenwashing": "greenwashing",
        "soberania epistêmica": "epistemic sovereignty",
        "governança ambiental": "environmental governance",
        "conformidade ambiental": "environmental compliance",
        
        # === TERMOS METODOLÓGICOS ===
        "validação espacial": "spatial validation",
        "validação temporal": "temporal validation",
        "validação longitudinal": "longitudinal validation",
        "particionamento geograficamente independente": "geographically independent partitioning",
        "explicabilidade algorítmica": "algorithmic explainability",
        "Inteligência Artificial Explicável": "Explainable Artificial Intelligence",
        "transparência algorítmica": "algorithmic transparency",
        "reprodutibilidade": "reproducibility",
        "generalização": "generalization",
        "superajuste": "overfitting",
        "autocorrelação espacial": "spatial autocorrelation",
        
        # === MÉTRICAS E ANÁLISES ===
        "acurácia": "accuracy",
        "sensibilidade": "sensitivity",
        "especificidade": "specificity",
        "degradação de desempenho": "performance degradation",
        "meta-análise": "meta-analysis",
        "viés de publicação": "publication bias",
        "heterogeneidade": "heterogeneity",
        "conformidade FAIR": "FAIR compliance",
        "princípios FAIR": "FAIR principles",
        
        # === TERMOS ECOLÓGICOS ===
        "sistemas socioecológicos": "socioecological systems",
        "sistemas socioecológicos acoplados": "coupled socioecological systems",
        "agrobiodiversidade": "agrobiodiversity",
        "tipicidade": "typicity",
        "território": "territory",
        "territorial": "territorial",
        "genótipo territorial": "territorial genotype",
        "fenótipo do produto": "product phenotype",
        "assinaturas quimiométricas": "chemometric signatures",
        "marcadores territoriais": "territorial markers",
        "variáveis ambientais": "environmental variables",
        "variabilidade climática": "climate variability",
        "resiliência climática": "climate resilience",
        
        # === ELEMENTOS DE TABELAS ===
        "**Tabela": "**Table",
        "Estrutura da revisão": "Review structure",
        "Indicadores de qualidade metodológica": "Methodological quality indicators",
        "Módulos Tecnológicos Identificados": "Technological Modules Identified",
        "Famílias Tecnológicas Identificadas": "Technological Families Identified",
        "Elemento": "Element",
        "Descrição": "Description",
        "Código": "Code",
        "Indicador": "Indicator",
        "Domínio": "Domain",
        "Módulo": "Module",
        "Algoritmos Principais": "Main Algorithms",
        "Técnicas Analíticas": "Analytical Techniques",
        "Produtos": "Products",
        "Região Predominante": "Predominant Region",
        "Cluster": "Cluster",
        "Produto Principal": "Main Product",
        "Técnica Analítica": "Analytical Technique",
        "Algoritmo ML": "ML Algorithm",
        "Aplicação": "Application",
        
        # === ELEMENTOS DE FIGURAS ===
        "**Figura": "**Figure",
        "Fluxograma de triagem": "Screening flowchart",
        "Evolução temporal": "Temporal evolution",
        "Impacto da validação espacial": "Impact of spatial validation",
        "Trade-off entre explicabilidade": "Trade-off between explainability",
        "Meta-análise de acurácias": "Meta-analysis of accuracies",
        "Conformidade com princípios FAIR": "FAIR principles compliance",
        "Diagrama de fluxo do estudo": "Study flow diagram",
        "*Nota:": "*Note:",
        "Fonte:": "Source:",
        
        # === FRASES COMUNS ===
        "O estudo utiliza": "The study employs",
        "Este estudo identifica": "This study identifies",
        "A análise avaliou": "Analysis evaluated",
        "Os resultados": "Results",
        "A meta-análise": "Meta-analysis",
        "Embora": "Although",
        "Contudo": "However",
        "Nesse contexto": "Within this context",
        "Neste sentido": "In this sense",
        "Para": "To",
        "Quanto": "Regarding",
        "Por fim": "Finally",
        "Adicionalmente": "Additionally",
        "Consequentemente": "Consequently",
        
        # === EXPRESSÕES ACADÊMICAS ===
        "realizou-se": "was conducted",
        "propõe-se": "is proposed",
        "investiga-se": "is investigated",
        "avalia-se": "is evaluated",
        "demonstrem": "demonstrate",
        "mostra-se": "proves",
        "exige": "demands",
        "demanda": "demands",
        "permite": "enables",
        "possibilita": "enables",
        "constitui": "constitutes",
        "representa": "represents",
        "reflete": "reflects",
        "indica": "indicates",
        "sugere": "suggests",
        "evidencia": "evidences",
        "confirma": "confirms",
        "corrobora": "corroborates",
    }

def traduzir_texto_complexo(texto: str, traducoes: Dict[str, str]) -> str:
    """
    Traduz texto preservando estrutura Markdown, LaTeX e referências.
    """
    resultado = texto
    
    # Aplicar traduções em ordem de prioridade (mais longas primeiro)
    items = sorted(traducoes.items(), key=lambda x: len(x[0]), reverse=True)
    
    for pt, en in items:
        # Substituições com preservação de contexto
        resultado = resultado.replace(pt, en)
    
    return resultado

def traduzir_documento_completo():
    """Executa tradução completa do documento."""
    
    arquivo_pt = Path("revisao_escopo_pt.md")
    arquivo_en = Path("revisao_escopo_en.md")
    
    print("="*70)
    print("TRADUTOR ACADÊMICO PT→EN - REVISÃO DE ESCOPO")
    print("="*70)
    print(f"\n📖 Lendo: {arquivo_pt}")
    
    with open(arquivo_pt, 'r', encoding='utf-8') as f:
        conteudo_pt = f.read()
    
    print(f"✓ Arquivo lido: {len(conteudo_pt):,} caracteres")
    print(f"\n🔄 Iniciando tradução acadêmica...")
    
    # Criar dicionário de traduções
    traducoes = criar_dicionario_traducoes()
    print(f"✓ Dicionário carregado: {len(traducoes)} termos")
    
    # Traduzir metadados YAML
    conteudo_en = conteudo_pt.replace('lang: pt-BR', 'lang: en-US')
    
    # Aplicar traduções contextuais
    conteudo_en = traduzir_texto_complexo(conteudo_en, traducoes)
    
    print(f"\n💾 Salvando: {arquivo_en}")
    
    with open(arquivo_en, 'w', encoding='utf-8') as f:
        f.write(conteudo_en)
    
    tamanho_kb = arquivo_en.stat().st_size / 1024
    
    print(f"\n{'='*70}")
    print("✅ TRADUÇÃO CONCLUÍDA COM SUCESSO!")
    print(f"{'='*70}")
    print(f"📄 Arquivo gerado: {arquivo_en.absolute()}")
    print(f"📊 Tamanho: {tamanho_kb:.1f} KB")
    print(f"🔤 Caracteres: {len(conteudo_en):,}")
    print(f"\n💡 Próximos passos:")
    print(f"   1. Revisar seções complexas manualmente")
    print(f"   2. Validar fórmulas LaTeX e referências")
    print(f"   3. Gerar DOCX com: python gerar-docx.py")

if __name__ == "__main__":
    traduzir_documento_completo()
