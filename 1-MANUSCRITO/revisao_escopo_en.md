---
title: "Digital Terroir e Auditabilidade de Serviços Ecossistêmicos via Machine Learning em Geographical Indications <b>Digital Terroir and Ecosystem Service Auditability via Machine Learning in Geographical Indications</b>"
author: "Catuxe Varjão de Santana Oliveira, Paulo Roberto Gagliardi, Luiz Diego Vidal Santos, Gustavo da Silva Quirino, Ana Karla de Souza Abud, Cristiane Toniolo Dias"
bibliography: referencias.bib
csl: apa.csl
reference-doc: modelo_formatacao.docx
fig-align: center
table-align: center
lang: en-US
---

# Abstract

Geographical Indications (GIs) constitute coupled socioecological systems, wherein typicity emerges from dynamic interactions among soil, climate, and biota. Validating these nexuses demands auditable environmental governance tools. Within this context, the present study investigates whether current Machine Learning apparatus possesses the necessary robustness to underpin Digital Terroir. Methodological adequacy is evaluated by models' spatial and temporal generalization capacity, and 'technical maturity' by the degree of algorithmic transparency (XAI) and reproducibility, indispensable requirements for transitioning from laboratory classifiers to governance tools. Specifically, it investigates whether prevailing algorithms possess the necessary robustness to transcend mere geographical classification and act as verifiable inferential auditing instruments. In accordance with PRISMA-ScR guidelines, a critical synthesis of 148 peer-reviewed studies (2010–2025) was conducted. Analysis evaluated validation patterns, interpretability, and environmental data integration to determine the operational viability of the proposed framework. Although classifiers demonstrate high discriminant accuracy (80–100%), the prevailing static modeling paradigm proves insufficient to operationalize Digital Terroir as an Inferential Digital Twin. The proposal's viability is constrained by critical generalization gaps, specifically the absence of longitudinal validation under climate variability (94%), spatially independent tests (77%), and algorithmic explainability (86.5%). Actualizing Digital Terroir as sustainability instrument and epistemic sovereignty demands research reorientation. Transitioning from laboratory classification experiments to developing adaptive, transparent models validated under real climate scenarios is imperative.

## **Keywords:** Geographical Indications; Machine Learning; Auditoria Ambiental; Greenwashing; Rastreabilidade; Serviços Ecossistêmicos.

# 1. Introduction

Geographical Indications (GIs) transcend their original intellectual property function by emerging as strategic instruments for environmental governance and agrobiodiversity conservation in the Anthropocene [@Belletti2017; @Vandecandelaere2009]. In a global scenario marked by climate crisis and biodiversity erosion, GIs operate as socioecological systems linking product quality to territory ecosystem services integrity [@Berkes2003; @Bramley2013]. They represent mechanisms to value regenerative agricultural practices and maintain cultural landscapes, where *terroir* is redefined not merely as a sensory attribute, but as a fingerprint of the product and climate resilience [@Giovannucci2010; @Fonzo2015].

International regulation, grounded in the TRIPS Agreement and Regulation (EU) No 1151/2012, establishes the legal basis, but it is environmental auditing capacity that confers contemporary legitimacy to these assets [@EU2012; @WTO1994]. The distinction between Protected Geographical Indication (PGI) and Protected Designation of Origin (PDO) reflects different degrees of dependence on natural cycles, requiring robust verification systems to avoid greenwashing and ensure that market premium effectively finances environmental conservation [@Locatelli2008; @WIPO2020]. These seals' credibility therefore depends on the capacity to scientifically prove that product characteristics derive from specific, non-replicable environmental interactions.

Terroir can be understood as an intrinsically coupled socioecological system, wherein soil, climate, biota, and culture articulate through non-linear interactions, feedbacks, and strong spatial-temporal heterogeneity, configuring a territory where biophysical processes and social practices are co-produced [@LeFloc2016S]. This systemic complexity and the diffuse nature of its couplings limit conventional metrics' detection of ecosystem services sustaining typicity and product value [@Levin1998ComplexAdaptiveSystems]. Consequently, valuation of these services and commons governance are weakened, facilitating greenwashing practices [@Gale2023]. The absence of analytical instrumentation capable of deciphering these systemic couplings compromises environmental monitoring and enforcement in extensive biomes, impacting sustainability on a global scale [@Liao2023].

Within this context, Machine Learning (ML) proves an intrinsic computational approach for complex systems analysis. By processing non-linear patterns and relationships in multiscalar data, including spectral, isotopic, and metabolomic information, ML converts these systems' intrinsic uncertainty into auditable evidence [@Li2022KGML_ag]. This capacity is fundamental for environmental governance and preserving communities' epistemic sovereignty [@Suh2007; @Santos2007Epistemologies]. At broad geographical scales, ML enables ecosystem services auditability, establishing a verifiable link between environmental compliance and market premium, and mitigating informational asymmetries that facilitate fraud and misappropriation [@Kshetri2014DigitalDivide].

However, the literature lacks a unified conceptual framework that integrates ML's inferential capabilities with environmental certification regulatory requirements. This gap limits translating methodological advances into operational protocols for Geographical Indication systems, perpetuating fragmentation between academic research and territorial governance.

In this sense, this review systematically maps Machine Learning applications in Geographical Indications, focusing on their potential for environmental authentication and fraud prevention. From synthesizing 148 peer-reviewed studies (2010–2025), the concept of 'Digital Terroir' is proposed as an analytical framework to operationalize ecosystem services inferential auditing. It is postulated that modeling non-linear couplings between environmental variables (territorial genotype) and chemometric signatures (product phenotype) can generate auditable environmental compliance evidence, converting diffuse sustainability claims into verifiable data and grounding market-based conservation policies.

# 2. Materials and Methods

This review follows PRISMA-ScR guidelines (Preferred Reporting Items for Systematic Reviews and Meta-Analyses extension for Scoping Reviews) as a transparency framework to ensure methodological clarity and reproducibility. The protocol is registered in the Open Science Framework to facilitate public access and replicability.

## 2.1 Research Question

The study employs a PCC structure (Population, Concept, Context) to formulate the following research question: How have Machine Learning techniques been applied for authentication, evaluation, and decision support in Geographical Indication systems?

**Table 1.** Review structure according to the PCC model.

| Element | Description |
|:----------------------|:------------------------------------------------|
| **P (Population)** | Geographical Indications, Designations of Origin, and Indications of Provenance recognized nationally and internationally, encompassing agri-food products (wines, cheeses, coffees, meats, olive oils), handicrafts, and other products with territorial identity. |
| **C (Concept)** | Machine Learning, Artificial Intelligence, classification and prediction algorithms, chemometric methods, Data Mining, and Natural Language Processing applied to Geographical Indication contexts. |
| **C (Context)** | Geographical origin authentication, GI potential assessment, identification of territorial determinants (soil, climate, production methods), product classification and discrimination, decision support systems for certification, quality control, traceability, fraud and adulteration detection, and territorial valorization strategies. |

This study identifies and characterizes Machine Learning (ML) applications reported in the literature, categorizing techniques by algorithm type, methodological approach, and performance metrics. Additionally, it analyzes application distribution by product type, geographical region, and time period, identifying methodological gaps, limitations, and directions for future research.

## 2.1.1 PRISMA-ScR Methodological Flowchart

Figure 1 presents the methodological flowchart, structured in four sequential phases: (1) Primary database search strategies, (2) Automated filtering with a weighted scoring system, (3) Manual quality assessment with multidisciplinary evaluation, and (4) Bibliometric analysis and qualitative synthesis integrating quantitative and documentary methodologies. The flowchart details the pathway from record identification to final synthesis, offering recommendations for Machine Learning implementation in Geographical Indication systems.

**Figure 1.** Screening flowchart, eligibility, and synthesis for Machine Learning applications in Geographical Indications.

![](2-FIGURAS/2-EN/ml_indicacoes_geograficas.png){#fig:ml_indicacoes width="80%"}

## 2.2 Search Strategy and Study Extraction

Searches were directed to Scopus (Elsevier) and Web of Science (Clarivate Analytics), crossing three main thematic domains: machine learning and artificial intelligence techniques; geographical certification systems; and Geographical Indications/Designations of Origin.

Descriptors employed controlled English terminology and Boolean operators (AND, OR, NOT), covering publications from 2010 to 2025 to capture the state of the art. The search strategy followed this logic:

*(“machine learning” OR “artificial intelligence” OR “deep learning” OR “supervised learning” OR “unsupervised learning” OR “ensemble methods”) AND (“geographical indications” OR “designations of origin” OR “protected designations of origin”) AND (“authentication” OR “traceability” OR “quality control” OR “fraud detection” OR “geospatial analysis”)* .

Inclusion criteria comprised peer-reviewed articles in English, Portuguese, or Spanish presenting machine learning applications in GI (Geographical Indication) contexts, origin authentication, or territorial quality control. Primary descriptors were mandatory in title, abstract, or keywords. Non-peer-reviewed works, studies without practical machine learning application, and those focused exclusively on non-territorial aspects were excluded.

Although the initial search was broad, qualitative synthesis prioritized studies establishing explicit links between analytical markers and environmental variables (e.g., soil composition, precipitation patterns, altitude), filtering studies strictly focused on industrial processing. This ensured the review addressed ecosystem services auditability and terroir concept validity, rather than focusing exclusively on production quality control.

Data extraction used a standardized form to record bibliographic metadata (author, year, title), geographical characteristics (country of origin, region, GI type), product details (category, specific denomination), methodological approach (machine learning algorithms, analytical/instrumental techniques, sample size), and performance metrics (accuracy, sensitivity, specificity, RMSE).

## 2.3 First Phase: Automated Filtering System by Thematic Relevance

### 2.3.1 Weighted Scoring Algorithm

Complementing manual screening, an automated filtering system assigns thematic relevance scores based on descriptor presence and location in title, abstract, and keywords. Implemented in Python (NLTK, spaCy), the algorithm applies a hierarchical weighting scheme to each identified term. The scoring system follows Analytic Hierarchy Process (AHP) principles. Equation (1) organizes descriptors into five categories with differentiated weights [@SAATY1991].

$$
S_i = \sum_{j=1}^{n} w_j \cdot l_i \cdot f_{ij}
$$

onde:

-   $S_i$ = pontuação total do artigo $i$
-   $w_j$ = peso associado ao termo $j$ (categorizado em 5 níveis: 5, 3, 2, 1 ou -5/-3/-2 pontos)
-   $l_i$ = multiplicador de localização (1,5 para título, 1,2 para palavras-chave, 1,0 para resumo)
-   $f_{ij}$ = frequência de ocorrência do termo $j$ no artigo $i$
-   $n$ = número total de termos avaliados

Priority terms (5 points) represent the central conceptual review (e.g., *geographical indications, traceability, authentication*). High-relevance terms (3 points) encompass core methodological concepts (e.g., *machine learning, deep learning, neural networks*). Medium-relevance terms (2 points) cover complementary themes (e.g., *chemometrics, data mining*), while context terms (1 point) indicate potential environments (e.g., *regional products, certification*). Exclusion terms receive negative weights to penalize out-of-scope records, particularly in *medical/clinical* (−5), *urban planning* (−3), and *financial* (−2) domains [@MUNN2018; @tricco2018].

### 2.3.2 Algorithm Implementation and Validation

For each record, the algorithm examines title, abstract, and keywords, applies category weights, and multiplies each occurrence by the location factor. The final score sums these products for all identified terms.

Empirical score distribution defined the minimum inclusion threshold, identifying the inflection point in the cumulative curve (Pareto/elbow criterion) and adjusting it through manual validation with stratified sampling. The final value represents the ideal balance between sensitivity and specificity, stabilizing inter-rater agreement in borderline cases.

### 2.3.3 Participatory Validation and Algorithm Refinement

To ensure scientific validity, a validation protocol involving three independent reviewers specialized in machine learning and GI systems was implemented. The protocol included systematic manual review of 272 studies to verify inclusion criteria adherence. An inter-rater agreement test verified classification consistency [@Tricco2018].

The process involved qualitative investigation of borderline cases and iterative refinement of eligibility criteria. Validation resulted in a 90.2% agreement rate between the automated system and manual evaluation, indicating high algorithmic efficacy in thematic screening.

### 2.3.4 Coverage Verification and Automated Categorization

An automated system verified bibliographic coverage, ensuring integrity and consistency between textual citations and bibliographic files.

The consolidated corpus was subjected to automated categorization using Natural Language Processing (NLP). A computational pipeline extracted, tokenized, and vectorized reference metadata and abstracts, using supervised models and semantic rules for pattern recognition [@Young2019; @Casey2021]. References were classified into predefined methodological categories, including machine learning techniques and geographical information systems.

To quantify studies' coverage and adequacy, metrics were applied de cobertura de citações e taxas de utilização bibliográfica do corpus [@tranfield2003; @webster2002]. These metrics enable quantitative evaluation da utilização da base de referências, ensuring selected studies adequately reflect the review's thematic scope.

## 2.4 Second Phase: Manual Methodological Quality Assessment

In the second phase, three independent reviewers assessed selected studies' methodological quality, ensuring multidisciplinary analysis and reducing interpretive bias. The MMAT scale [@pluye2009; @hong2018] was adapted for interdisciplinary studies involving machine learning and GI systems, structuring eight indicators on a 3-point Likert scale. Indicators included methodological rigor, algorithm validation, ethical protocol adherence, reproducibility, quantitative-qualitative integration, GI systems impact, documentation completeness, and method generalization (Table 2).

Each indicator received a score from 0 to 2: zero for unmet criteria or substantial deficiencies; one for partial compliance with limitations; and two for complete compliance with clear evidence. A 3-point scale was selected because dichotomous assessments cannot capture interdisciplinary complexity, while larger scales generate inter-rater inconsistency [@Likert3vs5_2025].

**Table 2.** Methodological quality indicators for ML-GI studies.

| Code | Indicator | Domain |
|-------------------|----------------------------------|-------------------|
| RIG | Methodological rigor in territorial data collection and processing | Territorial Quality |
| VAL | Technical validation of algorithms with appropriate metrics | Computational Quality |
| ETI | Adherence to ethical protocols for research with producer communities | Ethical Quality |
| REP | Reproducibility of computational experiments | Technical Quality |
| INT | Effective integration between quantitative and qualitative territorial methods | Methodological Quality |
| IMP | Impact and applicability of results for GI systems | Social Quality |
| DOC | Complete documentation of algorithms and certification procedures | Documentary Quality |
| GEN | Generalization and transferability of proposed methods | Scientific Quality |

### 2.4.1 Consensus Procedures and Inter-Rater Validation

Manual assessment included a consensus protocol. Initially, reviewers independently evaluated a pilot sample of 30 studies (approximately 11% of corpus) to calibrate criteria. For the complete corpus, discordance cases (difference ≥ 2 points) were subjected to blinded reassessment and discussion to reach consensus. Intraclass correlation coefficient (ICC) was calculated according to @shrout1979, obtaining a value of 0.87 (95% CI: 0.84–0.91), indicating good agreement.

### 2.4.2 Specific Criteria for Interdisciplinary Studies

Given the interdisciplinary nature of studies, quality criteria examined quantitative-qualitative integration coherence, validation in multiple geographical contexts, algorithmic transparency, ethical adherence, and practical applicability for certification.

This phase resulted in selecting 25 studies with adequate methodological quality (score ≥ 20 points) from 272 initial articles. These constituted the basis for subsequent analyses. Distribution included 1 article of excellence (≥40 points), 2 of high relevance (≥30 points), and 22 adequate (≥20 points).

## 2.5 Third Phase: Bibliometric Analysis

Lotka's Law [@lotka1926] analyzed scientific productivity, describing non-linear author productivity distribution to identify concentration or dispersion patterns. Bibliographic coupling and co-citation analyses were not performed due to absence of cited reference fields in available bibliographic files.

## 2.6 Fourth Phase: Qualitative Synthesis and Integration with Documentary Analysis

The fourth phase systematically integrated findings with documentary analysis of regulatory frameworks to ground methodological recommendations.

Final synthesis combined qualitative thematic analysis with Pareto principle-based selection (80/20), prioritizing the top 20% articles by combined score (40% methodological quality, 35% thematic relevance, 25% bibliometric impact).

A pontuação combinada final foi calculada usando a Equação (2):

$$
P_{final} = (0,40 \cdot Q_{met}) + (0,35 \cdot Q_{tem}) + (0,25 \cdot Q_{biblio})
$$

Onde:

-   $P_{final}$ = pontuação final de seleção
-   $Q_{met}$ = qualidade metodológica normalizada (0-1)
-   $Q_{tem}$ = relevância temática normalizada (0-1)
-   $Q_{biblio}$ = impacto bibliométrico normalizado (0-1)

## 2.7 Statistical Analyses

The corpus of 148 studies underwent two classes of statistical analyses: descriptive and exploratory analyses to characterize structural patterns in the literature, and inferential analyses to empirically quantify methodologically identified gaps qualitatively.

### 2.7.1 Descriptive and Exploratory Corpus Analyses

Multiple Correspondence Analysis (MCA) [@Le2008; @Greenacre2017] was employed to investigate associations among categorical variables (algorithms, products, regions, analytical techniques) through contingency table decomposition. Implemented with the `FactoMineR` package, MCA enables extracting latent dimensions explaining variance in category associations. Complementarily, Cluster Analysis (k-means and hierarchical) was applied with the `factoextra` package to identify recurring groupings among product-instrument-algorithm combinations.

Network analysis [@Csardi2006; @Schoch2020] was employed to map co-occurrences through construction of a weighted undirected graph using the `igraph` and `ggraph` packages, where nodes represent entities (algorithms, products, regions) and edges indicate co-occurrence in studies. Centrality metrics (degree, eigenvector, betweenness) were calculated to identify structurally central elements in the research field. Community detection was performed via the Louvain algorithm [@Blondel2008] to identify technological modules and specialization patterns by product-instrument-algorithm. Time series (2010–2025) employed Spearman correlation [@Spearman1904] to detect trends in publication volume and algorithmic adoption.

### 2.7.2 Inferential Analyses for Operational Criteria Validation

To empirically quantify methodological gaps and substantiate Digital Terroir operational criteria, four complementary inferential analyses were conducted. Seeking to analyze spatial validation impact on predictive performance, models with geographically independent partitioning ($n = 70$) were compared versus conventional random ($n = 78$), calculating percentage performance degradation between internal validation and external tests. Differences were evaluated by Mann-Whitney U [@Mann1947], with effect size quantified by Cohen's $d$ [@Cohen1988]: small ($d = 0.2$), medium ($d = 0.5$), or large ($d = 0.8$) according to @Sawilowsky2009. Logistic regression [@Hosmer2013] estimated the odds ratio of high performance ($\text{accuracy} \geq 85\%$) as a function of spatial validation, controlling for algorithm and product, following @Kuhn2013.

To investigate the trade-off between explainability and algorithmic performance, the relationship between algorithmic explainability (ordinal scale 0–10 based on @Rudin2019) and accuracy was analyzed through Spearman correlation [@Spearman1904]. Differences in accuracy between models with XAI ($n = 20$) and without XAI ($n = 128$) were evaluated by Student's $t$-test [@Student1908], verifying normality via Shapiro-Wilk [@Shapiro1965]. Computational overhead was compared by Mann-Whitney. Pareto analysis [@Pareto1896; @Deb2001] identified optimal algorithms under weighted utility function: $U = 0.4 \times \text{accuracy} + 0.4 \times \text{explainability} + 0.2 \times (1 - \text{normalized time})$.

Aiming to evaluate accuracy reported in studies and detect potential publication bias, random-effects meta-analysis was conducted [@Borenstein2009] with the `metafor` package [@Viechtbauer2010], transforming accuracies via logit to stabilize variances [@Barendregt2013]: $\text{logit}(p) = \ln[p/(1-p)]$. Pooled accuracy was estimated by REML model [@DerSimonian1986] with 95% CI. Heterogeneity was quantified by the $I^2$ statistic [@Higgins2003]: low ($< 25\%$), moderate ($25\%$–$75\%$), or high ($> 75\%$). Cochran's Q test [@Cochran1954] evaluated heterogeneity significance ($\alpha = 0.05$). Meta-regression [@Thompson2002] investigated effects of publication year and sample size. Publication bias was detected by Egger's test [@Egger1997] and trim-and-fill method [@Duval2000]. Stratified forest plots were generated following @Balduzzi2019.

Finally, to evaluate compliance with open data governance principles, FAIR compliance was quantified through standardized score (0–100 points) based on 12 binary indicators from @Wilkinson2016: DOI (F1), rich metadata (F2), public repository (A1), access protocol (A2), license (R1.1), source code (R1.2), interoperable format (I1), controlled vocabulary (I2), provenance (R1.3), community standard (I3), accessible API (A1.1), and versioning (R1.2). Each indicator contributed $100/12 \approx 8.33$ points. Scores were aggregated in the four FAIR dimensions by arithmetic mean. Temporal analysis employed Spearman correlation [@Spearman1904]. Comparisons between studies with/without blockchain used Mann-Whitney. Multidimensional radar charts visualized FAIR profiles with European Commission benchmark (75/100) [@EC2018].

All analyses were implemented in R [@RCoreTeam2024] using the `ggplot2` package for visualizations [@Wickham2016], `metafor` for meta-analysis [@Viechtbauer2010], `effsize` for effect size calculation [@Torchiano2020], and customized routines for FAIR compliance. $\alpha = 0.05$ was employed as significance level, applying Bonferroni correction [@Bonferroni1936] when pertinent for multiple comparisons. Code and processed data were deposited in the OSF repository (DOI: 10.17605/OSF.IO/2EKYQ) to ensure reproducibility [@Nosek2015].

## 2.8 Digital Terroir as Inferential Auditing System

From the systematic analysis of the bibliographic corpus, it was identified that ML applications in GIs lack a conceptual framework integrating computational capabilities with regulatory environmental auditing requirements. To fill this gap, the concept of **Digital Terroir** is proposed as an inferential auditing system empirically derived from the review.

### 2.8.1 Analytical Framework Application

Finally, the Digital Terroir framework was employed in this review as an analytical lens to evaluate studies' methodological maturity. Each publication was examined for compliance with operational criteria, allowing identification of the proportion of studies with adequate spatial and temporal validation, adoption of XAI methods for interpretability, data and protocol availability in open repositories, and implementation of continuous auditing systems (Figure 2). This approach enabled quantifying gaps between the current state of literature and requirements for digital terroir operationalization, grounding methodological recommendations presented in conclusions.

**Figure 2.** Study flow diagram.

![](2-FIGURAS/2-EN/prisma_flowdiagram.png){#fig:prisma2020 width="80%"}

Automated filtering through semantic analysis and scoring achieved thematic precision of 94.2%, exceeding the established threshold of 85%. This computational screening approach proved effective for reviews involving large bibliographic volumes, suggesting that calibrated automated systems reduce selection bias and increase reproducibility [@OforiBoateng2024]. The 100% reproducibility in multiple algorithm executions, combined with inter-rater agreement of κ = 0.89, ensures that these results reliably reflect the current state of scientific literature in this area.

Manual methodological quality assessment resulted in an intraclass correlation coefficient (ICC) of 0.87 (95% CI: 0.84–0.91), confirming robust inter-rater reliability and validating inclusion criteria [@streiner2008health]. This validation confirms that studies selected for synthesis meet rigorous methodological standards.

# 3. Results and Discussion

## 3.1 Digital Terroir: Constitutive and Operational Definitions

We adopt in this study the constitutive definition of Digital Terroir as the dynamic and continuous computational reconstruction of systemic interactions among soil, climate, biota, and human practices (the territorial genotype) and the final chemometric expression of the product (the phenotype), operating as an inferential Digital Twin [@Pylianidis2021; @Hensel2021]. Unlike traditional static cartography, which provides point representation of physical space, Digital Terroir correlates, in near real-time, environmental variables with high-dimensionality analytical signatures, converting ecological uncertainty into auditable evidence of authenticity and environmental compliance [@Guerena2024; @Nasirahmadi2022].

This formulation dialogues with the Digital Twins framework applied to agroecosystems [@Pylianidis2021] and with the understanding of terroir as socioecological coupling [@Bramley2013; @LeFloc2016S], integrating computational inference with territorial foundations. The concept establishes an auditable link between product and ecosystem services [@Vandecandelaare2018; @Belletti2017GeographicalIndications], transforming place identity into a testable and mathematically verifiable hypothesis.

For technical operational recognition as Digital Terroir, a computational system must meet structured operational criteria, derived from methodological gaps identified in the review. Validation robustness constitutes primary requirement, demanding consistent performance through spatially independent validation with geographical partitioning [@Kuhn2013], longitudinal time series representative of climate variability interannual and transfer tests across comparable harvests, batches, and regions. Algorithmic transparency demands implementation of methods of Explainable Artificial Intelligence (XAI) [@Lundberg2017; @Rudin2019] capable of identifying territorial markers with physicochemical plausibility, tracing authentication decisions to causal environmental variables, and rejecting spurious correlations without ecological foundation.

Open data governance must operate under FAIR standards [@Wilkinson2021], ensuring standardized metadata allowing independent cross-validation, publicly accessible spectral and metabolomic repositories, and documented and replicable sampling protocols. Finally, regulatory auditability presupposes incorporation of verification mechanisms, including audit trails documenting inference history, immutable certification registry through technologies such as blockchain when pertinent [@Kshetri2014], and previously defined and continuously monitored performance degradation limits.

## 3.2 Overview of Machine Learning Applications in Geographical Indications

Analysis of 148 peer-reviewed studies (2010–2025) evaluates to what extent the current state of the art in Machine Learning applied to Geographical Indications meets validation, transparency, data governance, and auditability criteria proposed in Digital Terroir. Data demonstrated that supervised learning algorithms constituted the predominant approach for origin authentication in Geographical Indication systems. Random Forest and Support Vector Machines presented consolidated application in spectroscopy and chromatography for wines, meats, and teas, achieving accuracies of 80–100% in controlled environments [@Xu2021; @Mohammadi2024].

This predominance of supervised architectures over unsupervised methods reflects labeled dataset availability and pressure for quantifiable accuracy metrics, as documented by @Liakos2018 in analysis on Machine Learning trends in precision agriculture. Convolutional Neural Networks consolidated specifically for hyperspectral data processing, while PLS-DA maintained relevance in chemometric preprocessing [@Peng2025; @Feng2025; @Rebiai2022], establishing an instrumental paradigm favoring high-value products (wines, oils) to the detriment of complex food matrices.

The analyzed studies' geographical distribution evidences an imbalance in sampling representativeness, with 72% of corpus concentrated on European and Asian products, predominantly wines (34%), teas (18%), and oils (8%). Such concentration indicates that digital authentication infrastructure advances primarily in consolidated GI systems, while Global South regions present lower publication volumes, reflecting disparities in access to analytical characterization technologies [@Belletti2017GeographicalIndications].

Temporal analysis indicates positive correlation between academic production and algorithmic complexity (Spearman's $\rho = 0.89$; $p < 0.001$), observing a Deep Learning adoption increase from 5% (2010–2015) to 28% (2020–2025). However, these models' validation presents structural limitations: longitudinal testing absence in 94% of works suggests that algorithms are calibrated for specific seasonal conditions. This characteristic restricts model generalization facing interannual climate variability, a limiting factor for implementing continuous environmental audits [@Iranzad2025].

Regarding spatial robustness, only 23% of studies applied geographically independent validation, registering accuracy decreases between 2% and 15% when models are exposed to new datasets [@Effrosynidis2021]. These results corroborate the overfitting hypothesis to local contexts, as discussed by @Kuhn2013. Additionally, the low implementation rate of explainability metrics (XAI), present in 14% of research, hinders adequacy to regulatory auditability requirements, since \"black-box\" models do not offer the decision traceability required by certification bodies [@Lundberg2017].

For fraud detection, binary classification approaches via SVM and KNN prevail for matrices such as honey and oil. Dichotomous modeling (authentic *versus* fraudulent) tends not to account for adulteration gradients or biogeographical transition zones. Totally, the integration of *Blockchain* and *Machine Learning*, observed in 21% of traceability studies, faces data entry validation challenges. Although distributed registry ensures information immutability, the veracity of physical-digital correspondence depends on the precision of \"oracles\" (sensors or predictive models), whose technical interoperability is still incipient [@Wang2025].

Network analysis confirms the formation of distinct methodological clusters (modularity $Q = 0.62$), with high internal density (0.53–0.68). The correlation between specific algorithms and instrumental techniques (such as Neural Networks associated with spectral data) suggests a compartmentalization of technical development. This modular structure indicates that parameter transfer between different product classes and analytical instruments remains limited, hindering universal protocol standardization for digital origin certification.

## 3.3 Temporal Evolution of Products and Algorithms

Temporal analysis of registered products presented distinct patterns among GI categories. Wines maintained constant representation with 14 products (2010–2025), presenting peaks in 2021 and 2023 (3 records each). Honey demonstrated concentrated growth in 2021–2024 (12 records), while olive-based products presented sporadic distribution (6 in total). Cheese and coffee remained under-represented (4 and 1 records, respectively). Spearman correlation confirmed ascending trend for wines (ρ = 0.615, p = 0.011), indicating systematic expansion after 2020 [@Liakos2018]. This consolidation of wines as dominant category reflects both the maturity of European GI systems and spectral data availability, contrasting with fragmentation observed in rising categories such as coffee, where the heterogeneity of processing methods hinders creating universal chemical signatures.

Algorithmic adoption presented measurable transition. PLS-DA, dominant until 2018, was progressively replaced by Random Forest and SVM from 2019, accompanying the availability of open-source ML libraries (scikit-learn, caret) and increased computational capacity [@Lavine2005]. Temporal correlation analysis demonstrated significant changes for SVM (ρ = 0.788, p < 0.001) and Random Forest (ρ = 0.677, p = 0.004).

Neural Networks constituted the most adopted technique in 2020–2025 (33 applications), followed by SVM (32) and Random Forest (21). Deep Learning and CNNs disseminated after 2022 specifically for hyperspectral data processing [@Shah2019], although their interpretative opacity limits adoption in regulatory contexts. Regional distribution maintained stability, with 72% of studies concentrated in Europe and Asia. Global South representation increased marginally from 18% to 22% in the analyzed period, suggesting persistent barriers related to laboratory infrastructure and access to scientific funding.

**Figure 3.** Temporal evolution of (a) products with Geographical Indication (GI) registered by category and (b) adoption of main Machine Learning algorithms in GI studies.
![](2-FIGURAS/2-EN/evolucao_temporal.png){#fig:temporal_evolution width="90%"}

## 3.4 Technological Families and Applications

Methodological approaches compartmentalization configured itself as critical obstacle to operationalizing Digital Terroir as adaptive and transferable system. While the proposed framework demands models capable of spatial and temporal generalization through different products and regions, the analysis revealed the formation of rigid "technological silos" limiting interoperability between instrumental techniques and algorithms.

Multiple Correspondence Analysis (MCA) explained 45.2% of total inertia in three dimensions, revealing a polarized latent structure that frontally contradicts the Digital Terroir transferability principle. Dimension 1 (28.4%) established a clear biogeographical contrast: European products (wines, cheeses) opposed Asian products (teas, meats). Subsequent dimensions segregated the instrumental matrix (Dimension 2: Spectroscopy *vs.* Chromatography) and algorithmic approach (Dimension 3: Supervised *vs.* Unsupervised). This spatial configuration suggests the consolidation of distinct regional paradigms, where European laboratories standardized NIR spectroscopy use for wines, while Asian institutions privileged high-resolution chromatography for teas.

This methodological compartmentalization does not represent merely technical preferences, but reflects the sedimentation of regional laboratory practices over decades, consolidated through publications, knowledge transfer among research groups, and protocol standardization in regulatory agencies [@Spyros2023FoodAuth, @Agiomyrgiannaki2023]. Such structural rigidity compromises Digital Terroir vision as universally applicable infrastructure, requiring multimodal protocols transcending regional specializations.

Vector coordinates confirm the existence of stable "technological triads". Strong convergence is observed between Wines, Random Forest, and NIR (0.85; 0.32), in opposition to the cluster formed by Teas, SVM, and GC-MS (-0.67; 0.91). The rigidity of these groupings indicates compartmentalization methodological compartmentalization restricting interdisciplinary innovation [@Blondel2008]. These silos' formation prevents algorithmic advances obtained in one instrumental triad from being transferred to others, limiting generalization of authentication architectures [@Salam2021; @Wang2025], fundamental requirement for a truly interoperable Digital Terroir across different food matrices and geographical contexts.

In recent scenario, multimodal data fusion (28%) and blockchain integration (9%) emerge as technological expansion frontiers that, in theory, meet the proposed framework's auditability criteria. However, demands for portable devices (*field-deployable*) impose a metrological *trade-off* that tensions Digital Terroir requirements: the necessary model compression for *in situ* operation results in an accuracy loss of 10–15% compared to laboratory standards [@Meena2024; @Effrosynidis2021]. Such discrepancy evidences current tension between field tool accessibility and robustness required for official certification, signaling that transitioning to operational Digital Twins demands not only algorithmic advances, but also innovation in portable analytical hardware preserving metrological precision.

## 3.5 Quantitative Evidence and Meta-Analyses

Methodological robustness evaluation revealed that 77% of studies did not implement geographically independent partitioning. To measure this omission's impact, model performance with rigorous spatial validation was compared versus random. According to Figure 4, spatial validation absence resulted in a mean accuracy drop of 11.82% in external tests, compared to 5.62% in spatially validated models. This discrepancy (110% relative degradation) was statistically significant ($U = 2900, p < 0.001, d = 0.948$), corroborating the spatial overfitting hypothesis described by @Kuhn2013, where autocorrelation inflates internal metrics and compromises certification utility.

**Figure 4.** Impact of spatial validation on performance degradation in external tests. 
![](2-FIGURAS/2-EN/validacao_espacial.png){#fig:validacao_espacial width="85%"} *Note: Models without spatial validation present 110% higher accuracy drop when applied to geographically independent regions (*$p < 0.001$, $d = 0.948$). The dashed line indicates the acceptable degradation threshold (≤8%) proposed for Digital Terroir certification systems. $n = 148$ studies.

Regarding transparency, only 13.5% of works adopted Explainable Artificial Intelligence (XAI) techniques. A moderate negative correlation was observed between explainability and accuracy ($\rho = -0.481, p < 0.001$), however, the absolute performance penalty was marginal (1.53 percentage points, not significant). In contrast, computational cost increased substantially (+67.8% in processing time). Pareto analysis identified the XGBoost algorithm as the optimal balance point among auditability, accuracy, and cost, surpassing Deep Learning architectures for regulatory purposes (Figure 5).

**Figure 5.** Trade-off between algorithmic explainability and predictive performance.

![](2-FIGURAS/2-EN/tradeoff_explicabilidade.png){#fig:tradeoff_xai width="85%"} *Note: More explainable algorithms present moderate negative correlation with accuracy (*$\rho = -0.481$, $p < 0.001$), but absolute cost is modest (~1.5 percentage points). XGBoost stands out as algorithm with best multi-criteria balance (Pareto score = 0.650, considering 93% accuracy, 6/10 explainability, and 12 min time). $n = 148$ studies.

Meta-analysis of 129 studies indicated a global pooled accuracy of 90.66% [95% CI: 89.8–91.4%]. The PLS-DA algorithm obtained the best mean performance (92.95%), followed by Random Forest (91.33%). However, Egger's test detected severe publication bias ($z = 40.02, p < 0.001$). Correction by trim-and-fill method (imputation of 42 missing theoretical studies) reduced the adjusted accuracy to ~88%, suggesting that current literature overestimates models' technological maturity (Figure 6).

**Figure 6.** Meta-analysis of accuracies by Machine Learning algorithm.

![](2-FIGURAS/2-EN/meta_analise_algoritmos.png){#fig:meta_algoritmo width="90%"} *Note: PLS-DA and Random Forest present the highest consolidated accuracies, while SVM demonstrates greater robustness (lower variance across studies). Moderate heterogeneity (*$I^2 = 58\%$) indicates substantial methodological variability across studies. Confidence intervals represent random effects estimates (REML model). $k = 129$ studies.

Finally, data governance evaluated by FAIR principles reached a critical mean score of 34.2/100. The Accessible dimension was the most deficient, with only 10.1% of studies depositing data in public repositories. Temporal analysis did not indicate significant improvements ($\rho = 0.235, p = 0.379$), evidencing the stagnation of a \"black-box\" culture that prevents reproducibility and independent validation (Figure 7).

**Figure 7.** FAIR principles compliance for data governance. (A) Radar score by FAIR dimension and (B) Individual compliance indicators.

![](2-FIGURAS/2-EN/fair_radar.png){#fig:fair_radar width="45%"} ![](2-FIGURAS/2-EN/fair_indicadores.png){#fig:fair_indicadores width="45%"}


## 3.5.4 Inferential Synthesis and Operational Implications

The inferential synthesis of the corpus delineates four structural fractures that compromise the transition from current predictive models to an auditable Digital Terroir infrastructure. The first fracture constitutes a robustness illusion derived from deficient spatial validation. The omission of geographically independent partitioning in 77% of studies precipitates a 110% higher performance degradation in external tests, with mean accuracy drop of 11.82% versus 5.62% in spatially validated models (U=2900, p<0.001, d=0.948). This methodological failure, driven by residual spatial autocorrelation, prevents systems from functioning as \"Adaptive Digital Twins\", since by overfitting to local contexts, they become obsolete facing real climate variability and fail in ecosystem services auditing in analogous territories [@Kuhn2013; @Wadoux2021].

Simultaneously, regulatory auditability is undermined by explainability marginalization. The predominance of opaque architectures in 86.5% of investigations contradicts guidelines for high-risk decisions [@Rudin2019], sustaining itself on the false premise of a performance trade-off. Statistical evidence refutes this narrative, demonstrating that the accuracy difference between \"black-box\" models and XAI models is statistically non-significant ($p = 0.218$), with the XGBoost algorithm emerging as optimal solution (Pareto score $= 0.650$) by balancing precision and transparency. Insistence on opacity makes certification legal defense unfeasible, since regulatory bodies demand causal traceability between chemical markers and environmental variables, not just untranslatable latent correlations.

Additionally, publication bias distorts technological maturity assessment. Correction via trim-and-fill method, with imputation of 42 missing studies ($z = 40.02$), reduced pooled accuracy from ~91% to ~88%, revealing that literature systematically overestimates models' discriminant capacity. This metric inflation, combined with moderate methodological heterogeneity ($I^2 = 58\%$), compromises risk calibration and aligns with the reproducibility crisis diagnosed by @Kapoor2023, where data leakage masks tools' actual efficacy. Finally, data governance erosion perpetuates fundamental epistemic asymmetries. With a critical FAIR score of 34.2/100 and temporal stagnation in data openness ($\rho = 0.235$, $p = 0.379$), the field fails to ensure independent verification. In this scenario, Blockchain technology, present in 21% of the sample, acts merely as superficial legitimizer; without open repositories and audit trails for physical sensors (Accessible dimension at only 14.5%), immutable registry does not resolve the "Oracle Paradox", forcing Global South producers to depend on costly external validations and undermining sovereignty over their digital assets.

To remedy such deficits and operationalize Digital Terroir, mandatory adoption of Compliance Thresholds is proposed, requiring post-spatial validation accuracy $\ge 85\%$ and maximum external degradation $\le 8\%$ [@vanEtten2023DataDrivenCrop], simultaneously conditioned on mandatory XAI explainability for critical territorial markers and FAIR compliance $\ge 60/100$ with deposition in interoperable repositories [@Wilkinson2016FAIR]. Adherence to these parameters constitutes a sine qua non condition to transmute Machine Learning from laboratory classification tool into socioecological auditing infrastructure, reducing certification costs by up to 40% through federated data and ensuring ecosystem services auditability [@An2024EnvML_ChatGPT; @WorldBank2014AgData].


## 3.6 Barriers to Auditability and the Failure of Static Digital Terroir

The prevailing algorithmic sophistication does not translate into robustness for environmental governance. The stationarity assumption implicit in dominant methodology constitutes the fundamental ontological limitation. High laboratory accuracy (80–100%) reflects models' capacity to memorize chemical signatures from specific harvests rather than apprehending terroir causality. Longitudinal validation absence in 94% of studies and spatially independent testing in 77% indicates low external model robustness [@Moran2020]. This methodological omission prevents capturing phenotypic plasticity, wherein plant chemical expression naturally varies under environmental fluctuations, compromising terroir causality [@GeneEnvironment2022]. According to @Kuhn2013, such failure invalidates continuous auditing, as algorithms fail to operate as Inferential Digital Twins under climate dynamics. In this sense, dynamic Digital Terroir is presented as solution, reconstructing systemic couplings among soil, climate, and biota.


Regarding temporal obsolescence, models calibrated on "ideal time windows" become blind to chemical drifts induced by extreme climatic events, which can alter secondary metabolite composition by more than 20% between production cycles [@Iranzad2025; @Urvieta2021]. By ignoring non-linearity and dynamic couplings among climate, soil, and biota, current systems degrade into static classifiers, unfit to operate as Inferential Digital Twins under climate change scenarios [@Celette2016WaterStress; @Kuhn2013]. This epistemic fragility is exacerbated by computational opacity. Low adherence to Explainable Artificial Intelligence (XAI) protocols in 86.5% of cases generates legally indefensible "black boxes", as regulatory auditing demands traceable causal nexuses, not blind correlations [@Xu2021; @He2024].

From a governance perspective, FAIR principles non-compliance (mean score of 34.2/100) perpetuates data colonialism. Without open repository federalization, Global South producers remain hostage to costly exogenous validations, undermining Epistemic Sovereignty over their biocultural assets [@Wilkinson2016FAIR]. Digital Terroir operationalization resides not in accuracy increment but in data governance restructuring to transmute Geographical Indications from static seals into dynamic ecosystem services certificates. @Rodriguez2023 points out that this transformation demands model calibration via remote sensing and strategic sampling in agricultural frontiers such as the Amazon. Such approach constitutes the only scalable pathway for computational surveillance, correlating chemical signatures with conservationist practices. According to @Osco2021, this approach enables shielding the market against greenwashing and ensures effective agrobiodiversity remuneration, promoting epistemic sovereignty in the Global South.



## 4. Conclusions

This research consolidates understanding of Geographical Indications as coupled socioecological systems, whose typicity emerges from non-linear interactions between edaphoclimatic variables and cultural practices. Critical analysis confirms that, although Machine Learning's inferential architecture holds technical capacity to convert chemometric signatures into environmental compliance evidence, the current state of the art lacks operational maturity necessary to sustain a full Inferential Digital Twin. Such limitation is aggravated by methodological concentration on consolidated chains in temperate regions, which not only reproduces epistemic asymmetries but severely restricts technological transfer to complex matrices of Global South agrobiodiversity.

Continuous computational certification is currently undermined by critical structural deficits, notably the absence of independent spatial validation and neglect of longitudinal testing under interannual climate variability. Overcoming this scenario and consequently operationalizing Digital Terroir as adaptive monitoring analytical layer therefore impose establishing strict regulatory robustness thresholds, defined by post-spatial validation accuracy and maximum performance degradation in external tests.

Algorithmic explainability (XAI) must constitute an environmental due diligence criterion, converting latent variables into traceable chemical-ecological justifications, while adherence to FAIR principles is necessary to enable third-party auditing. Such operational thresholds transform performance metrics into regulatory legitimacy safeguards.

Actualizing epistemic sovereignty demands a paradigmatic reorientation that replaces incremental competition for internal precision metrics with constructing transparent computational governance based on open repositories. This structural change enables the transition to Digital Terroir, which transcends mere instrumental advancement to constitute an ontological redefinition of certification: by computationally reconstructing dynamic couplings between territorial genotype and product phenotype, the framework converts climate uncertainty into auditable ecosystem services evidence, shielding Geographical Indications against greenwashing.

## Acknowledgments

Os autores agradecem à Universidade Federal de Sergipe (UFS), à Universidade Estadual de Feira de Santana (UEFS) e ao Instituto Federal de Sergipe (IFS) pelo apoio institucional e infraestrutural que possibilitou esta pesquisa.

## Conflicts of Interest

Os autores declaram não haver conflitos de interesse.

## Data Availability Statement

O conjunto de dados completo que apoia os resultados deste estudo, incluindo o corpus bibliográfico, os scripts de análise e os resultados intermediários, está disponível publicamente no repositório Open Science Framework (OSF) sob DOI: <https://doi.org/10.17605/OSF.IO/2EKYQ>.

## Ethics Statement

Esta revisão não envolve participantes humanos, experimentos com animais, linhagens celulares ou coleta de amostras. Não foi necessária aprovação ética nem consentimento.

## Community Positioning/Engagement

Quando relevante, as perspectivas da comunidade, provenientes de organizações de produtores e certificadoras, contribuíram para a interpretação das limitações práticas nos sistemas de Indicação Geográfica (IG); nenhuma informação que permitisse a identificação do indivíduo foi incluída.

## References

::: {#refs}
:::

## Tabela A.3: Technological Modules Identified pela Análise de Comunidade Louvain

| **Module** | **Main Algorithms** | **Analytical Techniques** | **Products** | **Predominant Region** |
|:-------------:|:--------------|:--------------|:--------------|:--------------|
| **M1** | Random Forest, Decision Tree, Gradient Boosting | Espectroscopia (NIR), Quimiometria | Vinho, Mel | África, Europa |
| **M2** | SVM, KNN | Cromatografia (GC-MS, LC-MS, HPLC) | Carnes, Products Regionais | Ásia |
| **M3** | Neural Networks, CNN, Deep Learning | Espectroscopia (NIR, FTIR), Sensores (e-nose) | Azeite, Queijo, Chá | Europa, Ásia |

*Source: Três principais módulos tecnológicos identificados pela análise de comunidade Louvain aplicada à rede de coocorrência entre algoritmos, técnicas analíticas e produtos com indicatesção geográfica. A densidade interna de cada módulo indicates a força das conexões entre seus componentes.*

### Tabela A.4: Technological Families Identified pela Análise de Cluster

| **Cluster** | **Main Product** | **Analytical Technique** | **ML Algorithm** | **Application** | **Predominant Region** |
|------------|------------|------------|------------|------------|------------|
| 1 | Mel | Espectroscopia NIR | SVM, KNN | Autenticação e detecção de fraude | Ásia |
| 2 | Queijo | Espectroscopia NIR | Redes Neurais | Discriminação de origem | Europa |
| 3 | Mel, Carnes | LC-MS, GC-MS | SVM, Random Forest, Árvores de Decisão | Autenticação e traceability | Ásia, Europa |

*Source: Dez clusters identificados pela análise de cluster (k-means e hierárquica) baseada em produto, instrumento analítico, algoritmo e tipo de aplicação. Apenas os três clusters mais notáveis são detalhados aqui.*