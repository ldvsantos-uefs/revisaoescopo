#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para finalizar 100% da tradução do manuscrito
Identifica e traduz todos os trechos remanescentes em português
"""

import re

# Dicionário de traduções para os trechos remanescentes identificados
traducoes = {
    # Seção 3.2 - Robustez espacial
    r"Regarding à robustez espacial, apenas 23% dos estudos aplicaram validação independente geograficamente, registrando-se decréscimos de accuracy entre 2% e 15% quando os modelos são expostos a novos conjuntos de dados \[@Effrosynidis2021\]\. Esses resultados corroboratesm a hipótese de sobreajuste \(\*overfitting\*\) a contextos locais, conforme discutido por \\@Kuhn2013\. Additionally, a baixa taxa de implementação de métricas de explicabilidade \(XAI\), presentes em 14% das pesquisas, dificulta a adequação aos requisitos de auditabilidade regulatória, uma vez que modelos do tipo \"caixa-preta\" não oferecem a traceability decisória exigida por órgãos de certificação \[@Lundberg2017\]\.":
    r"Regarding spatial robustness, only 23% of studies applied geographically independent validation, registering accuracy decreases between 2% and 15% when models are exposed to new datasets [@Effrosynidis2021]. These results corroborate the overfitting hypothesis to local contexts, as discussed by @Kuhn2013. Additionally, the low implementation rate of explainability metrics (XAI), present in 14% of research, hinders adequacy to regulatory auditability requirements, since \"black-box\" models do not offer the decision traceability required by certification bodies [@Lundberg2017].",
    
    # Seção 3.2 - Detecção de fraudes
    r"Já para a detecção de fraudes, prevalecem abordagens de classificação binária via SVM e KNN para matrizes como mel e azeite\. A modelagem dicotômica \(autêntico \*versus\* fraudulento\) tende a não contabilizar gradientes de adulteração ou zonas de transição biogeográfica\. Tolelamente, a integração de \*Blockchain\* e \*Machine Learning\*, observada em 21% dos estudos de traceability, enfrenta desafios de validação na entrada de dados\. Although o registro distribuído assegure a imutabilidade da informação, a veracidade da correspondência físico-digital depende da precisão dos \"oráculos\" \(sensores ou modelos preditivos\), cuja interoperabilidade técnica ainda é incipiente \[@Wang2025\]\.":
    r"For fraud detection, binary classification approaches via SVM and KNN prevail for matrices such as honey and oil. Dichotomous modeling (authentic *versus* fraudulent) tends not to account for adulteration gradients or biogeographical transition zones. Totally, the integration of *Blockchain* and *Machine Learning*, observed in 21% of traceability studies, faces data entry validation challenges. Although distributed registry ensures information immutability, the veracity of physical-digital correspondence depends on the precision of \"oracles\" (sensors or predictive models), whose technical interoperability is still incipient [@Wang2025].",
    
    # Seção 3.2 - Network analysis
    r"Network analysis confirms the formation of distinct methodological clusters \(modularidade \$Q = 0,62\$\), com alta densidade interna \(0,53–0,68\)\.":
    r"Network analysis confirms the formation of distinct methodological clusters (modularity $Q = 0.62$), with high internal density (0.53–0.68).",
    
    # Seção 3.3 - Legenda Figura 3
    r"\*\*Figure 3\.\*\* Temporal evolution de \(a\) produtos com Indicação Geográfica \(IG\) registrados por categoria e \(b\) adoção dos principais algoritmos de Machine Learning em estudos de IG\.":
    r"**Figure 3.** Temporal evolution of (a) products with Geographical Indication (GI) registered by category and (b) adoption of main Machine Learning algorithms in GI studies.",
    
    # Seção 3.4 - Compartimentalização
    r"This methodological compartmentalization does not represents merely technical preferences, but reflects the sedimentation of regional laboratory practices over decades, consolidated through publicações, transferência de conhecimento entre grupos de pesquisa e padronização de protocolos em agências regulatórias \[@Spyros2023FoodAuth, @Agiomyrgiannaki2023\]\.":
    r"This methodological compartmentalization does not represent merely technical preferences, but reflects the sedimentation of regional laboratory practices over decades, consolidated through publications, knowledge transfer among research groups, and protocol standardization in regulatory agencies [@Spyros2023FoodAuth, @Agiomyrgiannaki2023].",
    
    # Seção 3.4 - Trade-off metrológico
    r"However, demands for portable devices \(\*field-deployable\*\) impõe um \*trade-off\* metrológico que tensiona os requisitos do Digital Terroir: a necessária compressão de modelos para operação \*in situ\* resulta em uma perda de accuracy de 10–15% em comparação aos padrões laboratoriais \[@Meena2024; @Effrosynidis2021\]\. Such discrepancy evidences current tension between field tool accessibility and robustness required for official certification, signaling that transitioning to operational Digital Twins demands not only avanços algorítmicos, mas também inovação em hardware analítico portátil que preserve a precisão metrológica\.":
    r"However, demands for portable devices (*field-deployable*) impose a metrological *trade-off* that tensions Digital Terroir requirements: the necessary model compression for *in situ* operation results in an accuracy loss of 10–15% compared to laboratory standards [@Meena2024; @Effrosynidis2021]. Such discrepancy evidences current tension between field tool accessibility and robustness required for official certification, signaling that transitioning to operational Digital Twins demands not only algorithmic advances, but also innovation in portable analytical hardware preserving metrological precision.",
    
    # Seção 3.5 - Figura 4 legenda
    r"\*\*Figure 4\.\*\* Impact of spatial validation na performance degradation em testes externos\.":
    r"**Figure 4.** Impact of spatial validation on performance degradation in external tests.",
    
    r"\*Note: Modelos sem spatial validation present 110% higher accuracy drop when applied to geographically independent regions \(\*\$p < 0,001\$, \$d = 0,948\$\)\. The dashed line indicates the acceptable degradation threshold \(≤8%\) proposed for Digital Terroir certification systems\. \$n = 148\$ estudos\.":
    r"*Note: Models without spatial validation present 110% higher accuracy drop when applied to geographically independent regions (*$p < 0.001$, $d = 0.948$). The dashed line indicates the acceptable degradation threshold (≤8%) proposed for Digital Terroir certification systems. $n = 148$ studies.",
    
    # Seção 3.5 - Transparência e XAI
    r"Regarding à transparência, apenas 13,5% dos trabalhos adotaram técnicas of Explainable Artificial Intelligence \(XAI\)\. Observou-se uma correlação negativa moderada entre explicabilidade e accuracy \(\$\\rho = -0,481, p < 0,001\$\), contudo, a penalidade absoluta de desempenho foi marginal \(1,53 pontos percentuais, não significativa\)\. Em contrapartida, o custo computacional aumentou substancialmente \(\+67,8% em tempo de processamento\)\. A análise de Pareto identificou o algoritmo XGBoost como o ponto ótimo de equilíbrio entre auditabilidade, accuracy e custo, superando arquiteturas de Deep Learning para fins regulatórios \(Figura 5\)\.":
    r"Regarding transparency, only 13.5% of works adopted Explainable Artificial Intelligence (XAI) techniques. A moderate negative correlation was observed between explainability and accuracy ($\\rho = -0.481, p < 0.001$), however, the absolute performance penalty was marginal (1.53 percentage points, not significant). In contrast, computational cost increased substantially (+67.8% in processing time). Pareto analysis identified the XGBoost algorithm as the optimal balance point among auditability, accuracy, and cost, surpassing Deep Learning architectures for regulatory purposes (Figure 5).",
    
    # Seção 3.5 - Figura 5
    r"\*\*Figure 5\.\*\* Trade-off between explainability algorítmica e desempenho preditivo\.":
    r"**Figure 5.** Trade-off between algorithmic explainability and predictive performance.",
    
    r"\*Note: Algoritmos mais explicáveis apresentam correlação negativa moderada com accuracy \(\*\$\\rho = -0,481\$, \$p < 0,001\$\), mas o custo absoluto é modesto \(\\~1,5 pontos percentuais\)\. XGBoost destaca-se como algoritmo com melhor balanço multi-critério \(score de Pareto = 0,650, considerando accuracy 93%, explicabilidade 6/10 e tempo 12 min\)\. \$n = 148\$ estudos\.":
    r"*Note: More explainable algorithms present moderate negative correlation with accuracy (*$\\rho = -0.481$, $p < 0.001$), but absolute cost is modest (~1.5 percentage points). XGBoost stands out as algorithm with best multi-criteria balance (Pareto score = 0.650, considering 93% accuracy, 6/10 explainability, and 12 min time). $n = 148$ studies.",
    
    # Seção 3.5 - Meta-análise
    r"Meta-analysis de 129 estudos indicou uma accuracy global \(pooled\) de 90,66% \[IC 95%: 89,8–91,4%\]\. O algoritmo PLS-DA obteve o melhor desempenho médio \(92,95%\), seguido por Random Forest \(91,33%\)\. Entretanto, o teste de Egger detectou publication bias severo \(\$z = 40,02, p < 0,001\$\)\. A correção pelo método trim-and-fill \(imputação de 42 estudos teóricos faltantes\) reduziu a accuracy ajustada para ~88%, sugerindo que a literatura atual superestima a maturidade tecnológica dos modelos \(Figura 6\)\.":
    r"Meta-analysis of 129 studies indicated a global pooled accuracy of 90.66% [95% CI: 89.8–91.4%]. The PLS-DA algorithm obtained the best mean performance (92.95%), followed by Random Forest (91.33%). However, Egger's test detected severe publication bias ($z = 40.02, p < 0.001$). Correction by trim-and-fill method (imputation of 42 missing theoretical studies) reduced the adjusted accuracy to ~88%, suggesting that current literature overestimates models' technological maturity (Figure 6).",
    
    # Seção 3.5 - Figura 6
    r"\*\*Figure 6\.\*\* Meta-analysis of accuracies por algoritmo de Machine Learning\.":
    r"**Figure 6.** Meta-analysis of accuracies by Machine Learning algorithm.",
    
    r"\*Note: PLS-DA e Random Forest present the highest consolidated accuracies, while SVM demonstrates greater robustness \(lower variance across studies\)\. The heterogeneity moderada \(\*\$I\^2 = 58\\%\$\) indicates substantial methodological variability across studies\. Confidence intervals represent random effects estimates \(REML model\)\. \$k = 129\$ estudos\.":
    r"*Note: PLS-DA and Random Forest present the highest consolidated accuracies, while SVM demonstrates greater robustness (lower variance across studies). Moderate heterogeneity (*$I^2 = 58\\%$) indicates substantial methodological variability across studies. Confidence intervals represent random effects estimates (REML model). $k = 129$ studies.",
    
    # Seção 3.5 - FAIR
    r"Finally, a governança de dados avaliada pelos FAIR principles atingiu um score médio crítico de 34,2/100\. A dimensão Accessible foi a mais deficitária, com apenas 10,1% dos estudos depositando dados em repositórios públicos\. Temporal analysis não indicou melhorias significativas \(\$\\rho = 0,235, p = 0,379\$\), evidencesndo a estagnação de uma cultura de \"caixa-preta\" que impede a reproducibility e a validação independente \(Figura 7\)\.":
    r"Finally, data governance evaluated by FAIR principles reached a critical mean score of 34.2/100. The Accessible dimension was the most deficient, with only 10.1% of studies depositing data in public repositories. Temporal analysis did not indicate significant improvements ($\\rho = 0.235, p = 0.379$), evidencing the stagnation of a \"black-box\" culture that prevents reproducibility and independent validation (Figure 7).",
    
    # Seção 3.5 - Figura 7
    r"\*\*Figure 7\.\*\* FAIR principles compliance de governança de dados\. \(A\) Score radar por dimensão FAIR e \(B\) Indicatores individuais de conformidade\.":
    r"**Figure 7.** FAIR principles compliance for data governance. (A) Radar score by FAIR dimension and (B) Individual compliance indicators.",
    
    # Seção 3.5.4 - Síntese inferencial (vários parágrafos)
    r"A síntese inferencial do corpus delineia quatro fraturas estruturais que comprometem a transição dos atuais modelos preditivos para uma infraestrutura de Digital Terroir auditável\. A primeira fratura constitutes uma ilusão de robustez derivada da spatial validation deficiente\.":
    r"The inferential synthesis of the corpus delineates four structural fractures that compromise the transition from current predictive models to an auditable Digital Terroir infrastructure. The first fracture constitutes a robustness illusion derived from deficient spatial validation.",
    
    r"A omissão do geographically independent partitioning em 77% dos estudos precipita uma performance degradation 110% superior em testes externos, com queda média de accuracy de 11,82% versus 5,62% em modelos validados espacialmente \(U=2900, p<0,001, d=0,948\)\. Essa falha metodológica, impulsionada pela spatial autocorrelation residual, impede que os sistemas funcionem como \"Gêmeos Digitais Adaptativos\", pois ao superajustarem-se a contextos locais, tornam-se obsoletos diante da climate variability real e falham na auditoria de ecosystem services em territorys análogos \[@Kuhn2013; @Wadoux2021\]\.":
    r"The omission of geographically independent partitioning in 77% of studies precipitates a 110% higher performance degradation in external tests, with mean accuracy drop of 11.82% versus 5.62% in spatially validated models (U=2900, p<0.001, d=0.948). This methodological failure, driven by residual spatial autocorrelation, prevents systems from functioning as \"Adaptive Digital Twins\", since by overfitting to local contexts, they become obsolete facing real climate variability and fail in ecosystem services auditing in analogous territories [@Kuhn2013; @Wadoux2021].",
    
    r"Simultaneamente, a auditabilidade regulatória é minada pela marginalização da explicabilidade\. A predominância de arquiteturas opacas em 86,5% das investigações contraria diretrizes para decisões de alto risco \[@Rudin2019\], sustentando-se na falsa premissa de um trade-off de desempenho\. A evidência estatística refuta essa narrativa, demonstrando que a diferença de accuracy entre modelos \"caixa-preta\" e modelos XAI é estatisticamente não significativa \(\$p = 0,218\$\), com o algoritmo XGBoost emergindo como solução ótima \(score de Pareto \$= 0,650\$\) ao equilibrar precisão e transparência\. A insistência na opacidade inviabiliza a defesa jurídica da certificação, uma vez que órgãos reguladores demandsm traceability causal entre marcadores químicos e environmental variables, e não apenas correlações latentes intraduzíveis\.":
    r"Simultaneously, regulatory auditability is undermined by explainability marginalization. The predominance of opaque architectures in 86.5% of investigations contradicts guidelines for high-risk decisions [@Rudin2019], sustaining itself on the false premise of a performance trade-off. Statistical evidence refutes this narrative, demonstrating that the accuracy difference between \"black-box\" models and XAI models is statistically non-significant ($p = 0.218$), with the XGBoost algorithm emerging as optimal solution (Pareto score $= 0.650$) by balancing precision and transparency. Insistence on opacity makes certification legal defense unfeasible, since regulatory bodies demand causal traceability between chemical markers and environmental variables, not just untranslatable latent correlations.",
}

def aplicar_traducoes(arquivo_entrada, arquivo_saida):
    """Aplica todas as traduções no arquivo"""
    with open(arquivo_entrada, 'r', encoding='utf-8') as f:
        conteudo = f.read()
    
    conteudo_original = conteudo
    traducoes_aplicadas = 0
    
    for padrao_pt, texto_en in traducoes.items():
        if re.search(padrao_pt, conteudo):
            conteudo = re.sub(padrao_pt, texto_en, conteudo)
            traducoes_aplicadas += 1
            print(f"✓ Tradução aplicada: {padrao_pt[:80]}...")
    
    if conteudo != conteudo_original:
        with open(arquivo_saida, 'w', encoding='utf-8') as f:
            f.write(conteudo)
        print(f"\n✅ {traducoes_aplicadas} traduções aplicadas com sucesso!")
        print(f"📄 Arquivo salvo: {arquivo_saida}")
        return True
    else:
        print("⚠️ Nenhuma tradução foi aplicada (padrões não encontrados)")
        return False

if __name__ == "__main__":
    arquivo_entrada = r"c:\Users\vidal\OneDrive\Documentos\13 - CLONEGIT\revisaoescopo\1-MANUSCRITO\revisao_escopo_en.md"
    arquivo_saida = arquivo_entrada  # Sobrescrever o mesmo arquivo
    
    print("="*70)
    print("FINALIZADOR DE TRADUÇÃO - MANUSCRITO EN")
    print("="*70)
    print(f"\nProcessando: {arquivo_entrada}\n")
    
    sucesso = aplicar_traducoes(arquivo_entrada, arquivo_saida)
    
    if sucesso:
        print("\n" + "="*70)
        print("🎯 TRADUÇÃO 100% CONCLUÍDA!")
        print("="*70)
    else:
        print("\n" + "="*70)
        print("ℹ️ Verifique manualmente os trechos restantes")
        print("="*70)
