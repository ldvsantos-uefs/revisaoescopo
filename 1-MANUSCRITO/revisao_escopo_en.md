---
title: "Digital Terroir and Ecosystem Governance: A Critical Review of Machine Learning for the Auditability of Geographical Indications"
author: "Catuxe Varjão de Santana Oliveira, Paulo Roberto Gagliardi, Luiz Diego Vidal Santos, Gustavo da Silva Quirino, Ana Karla de Souza Abud, Cristiane Toniolo Dias"
bibliography: referencias.bib   
csl: harvard.csl
reference-doc: modelo_formatacao_new.docx
fig-align: center
table-align: center
lang: en-US
---


# Abstract

Geographical Indications (GIs) act simultaneously as intellectual property assets and tools for agrobiodiversity conservation, linking product quality to the territory's ecosystem services. This review provides a critical, integrative synthesis of Machine Learning (ML) applications in GI systems (2010–2025), focusing on how analytical signatures (spectral, elemental, isotopic) support environmental auditing, fraud detection, and the prevention of greenwashing. Across 148 peer‑reviewed studies, supervised classifiers dominate: Random Forest and Support Vector Machines are prevalent in spectroscopy and chromatography for wines, meats, oils, and teas; Deep Learning emerges for hyperspectral data; and PLS‑DA remains central for chemometrics. Typical accuracies range from 80% to 100% in laboratory settings, yet generalization is often overestimated: only 23% of studies perform spatially independent validation and fewer include longitudinal tests, with performance drops of 2%–15% under distribution shifts. To be incorporated into environmental certification, ML models must demonstrate rigorous external validation, provide interpretability capable of identifying soil health fingerprints and climate resilience markers, and operate within transparent data governance. We synthesize methodological patterns into technological families and outline guidelines for ML to strengthen the credibility of GIs as sustainability instruments, preventing statistical optimism from eroding consumer trust and the asset's ecological value.

**Keywords:** Geographical Indications; Machine Learning; Environmental Auditing; Greenwashing; Traceability; Ecosystem Services.

# 1. Introduction

Geographical Indications (GIs) transcend their original function as intellectual property to emerge as strategic instruments for environmental governance and agrobiodiversity conservation in the Anthropocene [@Belletti2017; @Vandecandelaere2009]. In a global scenario marked by the climate crisis and the erosion of biological diversity, GIs operate as social-ecological systems that link product quality to the integrity of the territory's ecosystem services [@Berkes2003; @Bramley2013]. More than guarantees of origin, they represent mechanisms for valuing regenerative agricultural practices and maintaining cultural landscapes, where *terroir* is redefined not just as a sensory attribute, but as a fingerprint of soil health and climate resilience [@Giovannucci2010; @Fonzo2015].

The international regulation, grounded in the TRIPS Agreement and Regulation (EU) No 1151/2012, establishes the legal basis, but it is the capacity for environmental auditing that confers contemporary legitimacy to these assets [@EU2012; @WTO1994]. The distinction between Protected Geographical Indication (PGI) and Protected Designation of Origin (PDO) reflects different degrees of dependence on natural cycles, requiring robust verification systems to avoid *greenwashing* and ensure that the market premium effectively funds environmental conservation [@Locatelli2008; @WIPO2020]. The credibility of these seals depends, therefore, on the ability to scientifically prove that product characteristics derive from specific and non-replicable environmental interactions.

In this context, Machine Learning (ML) emerges as a disruptive technology for environmental auditing. By processing high-dimensional spectral, isotopic, and metabolomic data, ML algorithms can decode "soil health fingerprints" and "climate resilience markers" invisible to traditional methods [@Gbashi2024FoodIntegrityAI; @Rocha2020NonLinear]. Unlike subjective sensory analysis, ML offers a quantitative approach to validate "terroir integrity," transforming chemical complexity into auditable evidence of environmental compliance [@Qamar2023DeepLearning; @Ramos2025]. This capability is critical for auditing ecosystem services, allowing the distinction between products that genuinely conserve biodiversity and those that merely exploit regional reputation.

The application of ML in GIs, therefore, is not just a technical innovation, but a tool for epistemic sovereignty and environmental justice. It allows local communities to convert their tacit knowledge and management practices into verifiable data, protecting their genetic and cultural resources against misappropriation [@Suh2007; @Azevedo2011]. However, current literature lacks a synthesis connecting these sensing technologies to the urgent demands of environmental monitoring.

##########aqui###########
To operationalize this connection between data and territory, we propose the concept of 'Digital Terroir'. We define Digital Terroir not merely as the digitalization of geographical data, but as the computational reconstruction of the soil-climate-biota interactions that confer typicity. Unlike static soil maps, Digital Terroir is dynamic: it uses Machine Learning to continuously correlate the chemometric fingerprint of the final product (phenotype) with the environmental variables of the territory (genotype). This creates an auditable link between the product and its ecosystem services, rendering the 'taste of place' mathematically verifiable.

This review systematically maps Machine Learning applications in Geographical Indications, focusing on their potential for environmental authentication and fraud prevention. We hypothesize that ML techniques, when integrated with environmental data, function as auditing mechanisms for ecosystem services, offering a robust scientific basis for market-based conservation policies and for preventing *greenwashing* in global value chains.

# 2. Materials and Methods

This review follows PRISMA-ScR guidance (*Preferred Reporting Items for Systematic Reviews and Meta-Analyses extension for Scoping Reviews*) as a transparency framework to ensure methodological clarity and reproducibility. The protocol is registered on the Open Science Framework to facilitate public access and replicability.

## 2.1 Research Question

The study employs the PCC framework (*Population, Concept, Context*) to formulate the research question: *How have Machine Learning techniques been applied for authentication, evaluation, and decision support in Geographical Indications systems?*

**Table 1.** Structure of the review according to the PCC framework.

| Element                  | Description                                                                                                                                                                                                                                                                                                                                                                                     |
| :------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **P (Population)** | Geographical Indications, Denominations of Origin, and Indications of Provenance recognized nationally and internationally, encompassing agro-food products (wines, cheeses, coffees, meats, olive oils), crafts, and other products with territorial identity.                                                                                                                        |
| **C (Concept)**    | Machine Learning, Artificial Intelligence, classification and prediction algorithms, chemometric methods, Data Mining, and Natural Language Processing applied to Geographical Indications contexts.                                                                                                                                             |
| **C (Context)**    | Geographical origin authentication, GI potential assessment, identification of territorial determinants (soil, climate, production methods), product classification and discrimination, decision support systems for certification, quality control, traceability, fraud detection and adulterations, and territorial valorization strategies. |

This study identifies and characterizes ML applications reported in the literature, categorizing techniques by algorithm type, methodological approach, and performance metrics. Furthermore, it analyzes the distribution of applications by product type, geographical region, and time period, identifying methodological gaps, limitations, and directions for future research.

## 2.1.1 PRISMA-ScR Methodological Flowchart

Figure 1 presents the methodological flowchart, structured in four sequential phases: (1) Main database search strategies, (2) Automated filtering with a weighted scoring system, (3) Manual quality assessment with multidisciplinary evaluation, and (4) Bibliometric analysis and qualitative synthesis integrating quantitative and documentary methodologies. The flowchart details the path from record identification to final synthesis, offering recommendations for Machine Learning implementation in Geographical Indications systems.

**Figure 1.** Flowchart of screening, eligibility, and synthesis for ML applications in Geographical Indications.

![Flowchart of ML-GI review process](2-FIGURAS/2-EN/ml_indicacoes_geograficas.png){#fig:ml_indicacoes width="80%"}

## 2.3 Search Strategy and Study Extraction

Searches targeted Scopus (Elsevier) and Web of Science (Clarivate Analytics), intersecting three main thematic domains: machine learning and artificial intelligence techniques; geographical certification systems; and Geographical Indications/Denominations of Origin.

Descriptors employed controlled English terminology and Boolean operators (AND, OR, NOT), covering publications from 2010 to 2025 to capture the state of the art. The search strategy followed this logic:

*("machine learning" OR "artificial intelligence" OR "deep learning" OR "supervised learning" OR "unsupervised learning" OR "ensemble methods") AND ("geographical indications" OR "denominations of origin" OR "appellations of origin" OR "protected designations of origin") AND ("authentication" OR "traceability" OR "quality control" OR "fraud detection" OR "geospatial analysis")*.

Inclusion criteria comprised peer-reviewed articles in English, Portuguese, or Spanish presenting ML applications in GI contexts, origin authentication, or territorial quality control. Primary descriptors were required in the title, abstract, or keywords. Non-peer-reviewed works, studies lacking practical ML application, and those focused exclusively on non-territorial aspects were excluded.

############ aqui###########
While the initial search was broad, the qualitative synthesis prioritized studies that established explicit links between analytical markers and environmental variables (e.g., soil composition, rainfall patterns, altitude), filtering out strictly industrial processing studies. This ensured the review addressed the auditability of ecosystem services and the validity of the terroir concept, rather than solely manufacturing quality control.

Data extraction utilized a standardized form to record bibliographic metadata (author, year, title), geographical characteristics (country of origin, region, GI type), product details (category, specific denomination), methodological approach (ML algorithms, analytical/instrumental techniques, sample size), and performance metrics (accuracy, sensitivity, specificity, RMSE).

## 2.4 First Phase: Automated Thematic Relevance Filtering System

### 2.4.1 Weighted Scoring Algorithm

Complementing manual screening, an automated filtering system assigns thematic relevance scores based on descriptor presence and location in the title, abstract, and keywords. Implemented in Python (NLTK, spaCy), the algorithm applies a hierarchical weighting scheme to each identified term. The scoring system adheres to Analytic Hierarchy Process (AHP) principles. Equation (1) organizes descriptors into five categories with differentiated weights [@SAATY1991].


$$
S_i = \sum_{j=1}^{n} w_j \cdot l_i \cdot f_{ij}
$$

where:

- $S_i$ = total score of article $i$
- $w_j$ = weight associated with term $j$ (categorized in 5 levels: 5, 3, 2, 1, or -5/-3/-2 points)
- $l_i$ = location multiplier (1.5 for title, 1.2 for keywords, 1.0 for abstract)
- $f_{ij}$ = frequency of occurrence of term $j$ in article $i$
- $n$ = total number of terms evaluated

Priority terms (5 points) represent the core conceptual review (e.g., *geographical indications, traceability, authentication*). High relevance terms (3 points) capture central methodological concepts (e.g., *machine learning, deep learning, neural networks*). Medium relevance terms (2 points) cover complementary themes (e.g., *chemometrics, data mining*), while Context terms (1 point) indicate potential environments (e.g., *regional products, certification*). Exclusion terms receive negative weights to penalize out-of-scope records, particularly in *medical/clinical* (−5), *urban planning* (−3), and *finance* (−2) domains [@MUNN2018; @tricco2018].

### 2.4.2 Algorithm Implementation and Validation

For each record, the algorithm scans the title, abstract, and keywords, applies the category weights, and multiplies each occurrence by the location factor. The final score sums these products across all identified terms.

The empirical score distribution defined the minimum inclusion threshold, identifying the inflection point in the cumulative curve (Pareto/elbow criterion) and adjusting it via manual validation with stratified sampling. The final value represents the optimal compromise between sensitivity and specificity, stabilizing inter-rater concordance in borderline cases.

### 2.4.3 Participatory Validation and Algorithm Refinement

To ensure scientific validity, a validation protocol involving three independent reviewers specializing in machine learning and GI systems was implemented. The protocol included a systematic manual review of 272 studies to verify adherence to inclusion criteria. An inter-rater concordance test verified classification consistency [@Tricco2018].

The process involved qualitative investigation of borderline cases and iterative refinement of eligibility criteria. Validation yielded a 90.2% concordance rate between the automated system and manual evaluation, indicating high algorithmic effectiveness in thematic screening.

### 2.4.4 Coverage Verification and Automated Categorization

An automated system verified bibliographic coverage, ensuring completeness and consistency between textual citations and bibliographic files.

The consolidated corpus underwent automated categorization using Natural Language Processing (NLP). A computational pipeline extracted, tokenized, and vectorized reference metadata and abstracts, using supervised models and semantic rules for pattern recognition [@Young2019; @Casey2021]. References were classified into predefined methodological categories, including machine learning techniques and GI systems.

To quantify coverage and study adequacy, citation coverage metrics and corpus bibliographic usage rates were applied [@tranfield2003; @webster2002]. These metrics allow quantitative evaluation of reference base utilization, ensuring selected studies adequately reflect the review's thematic scope.

## 2.5 Second Phase: Manual Methodological Quality Assessment

In the second phase, three independent reviewers assessed the methodological quality of selected studies, ensuring multidisciplinary analysis and reducing interpretive bias. The MMAT scale [@pluye2009; @hong2018] was adapted for interdisciplinary studies involving ML and GI systems, structuring eight indicators on a 3-point Likert scale. Indicators included methodological rigor, algorithm validation, ethical protocol adherence, reproducibility, quantitative-qualitative integration, impact on GI systems, documentation completeness, and method generalizability (Table 2).

Each indicator received a score from 0 to 2: zero for unmet criteria or substantial deficiencies; one for partial fulfillment with limitations; and two for complete fulfillment with clear evidence. A 3-point scale was selected because dichotomous evaluations fail to capture interdisciplinary complexity, while larger scales generate inter-rater inconsistency [@Likert3vs5_2025].


**Table 2.** Indicators of methodological quality for ML-GI studies.

| Code | Indicator                                                                     | Domain                |
| ------- | ----------------------------------------------------------------------------- | ----------------------- |
| RIG     | Methodological rigor in territorial data collection and processing           | Territorial Quality   |
| VAL     | Technical validation of algorithms with appropriate metrics                 | Computational Quality |
| ETI     | Adherence to ethical protocols for research with producer communities      | Ethical Quality        |
| REP     | Reproducibility of computational experiments                             | Technical Quality      |
| INT     | Effective integration between quantitative and qualitative territorial methods | Methodological Quality |
| IMP     | Impact and applicability of results for GI systems                   | Social Quality        |
| DOC     | Complete documentation of algorithms and certification procedures      | Documentary Quality    |
| GEN     | Generalizability and transferability of proposed methods                 | Scientific Quality   |

### 2.5.1 Consensus Procedures and Inter-Rater Validation

The manual assessment included a consensus protocol. Initially, reviewers independently assessed a pilot sample of 30 studies (~11% of the corpus) to calibrate criteria. For the full corpus, discordance cases (difference ≥ 2 points) underwent blind reassessment and discussion to reach consensus. The intraclass correlation coefficient (ICC) was calculated according to @shrout1979, obtaining a value of 0.87 (95% CI: 0.84–0.91), indicating good concordance.

### 2.5.2 Specific Criteria for Interdisciplinary Studies

Given the interdisciplinary nature of the studies, quality criteria examined the coherence of quantitative-qualitative integration, validation across multiple geographical contexts, algorithmic transparency, ethical adherence, and practical applicability for certification.

This phase resulted in the selection of 25 studies with adequate methodological quality (score ≥ 20 points) from the initial 272 articles. These formed the basis for subsequent analyses. The distribution included 1 excellence article (≥40 pts), 2 high relevance (≥30 pts), and 22 adequate (≥20 pts).

## 2.6 Third Phase: Bibliometric Analysis

Lotka's Law [@lotka1926] analyzed scientific productivity, describing the non-linear distribution of author productivity to identify concentration or dispersion patterns. Bibliographic coupling and co-citation analyses were not performed due to missing cited reference fields in the available bibliographic files.

## 2.7 Fourth Phase: Qualitative Synthesis and Integration with Documentary Analysis

The fourth phase systematically integrated findings with documentary analysis of regulatory frameworks to ground methodological recommendations.

The final synthesis combined thematic qualitative analysis with selection based on the Pareto principle (80/20), prioritizing the top 20% of articles by combined score (40% methodological quality, 35% thematic relevance, 25% bibliometric impact).

The final combined score was calculated using Equation (2):

$$
P_{final} = (0.40 \cdot Q_{met}) + (0.35 \cdot Q_{tem}) + (0.25 \cdot Q_{biblio})
$$

Where:

- $P_{final}$ = final selection score
- $Q_{met}$ = normalized methodological quality (0-1)
- $Q_{tem}$ = normalized thematic relevance (0-1)
- $Q_{biblio}$ = normalized bibliometric impact (0-1)

## 2.8 Statistical Analyses

Statistical analyses in R [@RCoreTeam2024] using RStudio [@RStudioTeam2023] systematically characterized the corpus and identified emerging patterns. Multiple Correspondence Analysis (MCA) investigated associations between categorical variables (algorithms, products, regions, analytical techniques), following @Le2008 and @Greenacre2017, using `FactoMineR` to extract main dimensions. Subsequently, Cluster Analysis (k-means and hierarchical) using `FactoMineR` and `factoextra` identified recurring product-instrument-algorithm groupings, synthesizing the "technological families" discussed in Section 3.8.

Network analysis mapped co-occurrences between algorithms, products, and regions [@Csardi2006; @Schoch2020]. Using `igraph` and `ggraph`, an undirected graph was constructed, calculating centrality metrics (degree, eigenvector, betweenness), and community detection was performed with the Louvain algorithm [@Blondel2008] to identify thematic modules (Section 3.9).

Time series and Spearman's correlation test [@Spearman1904] analyzed the temporal evolution of publications (2010–2025) to detect trends in study volume and algorithm adoption. Visualizations generated with `ggplot2` used LOESS smoothing [@Cleveland1979] to illustrate growth dynamics.

Finally, global predictive models evaluated whether bibliometric and methodological variables could anticipate study scores. Regression models (OLS, Ridge, Lasso, Random Forest) and classification models (Logistic Regression, Random Forest) were estimated using `caret` and `randomForest` with stratified k-fold cross-validation. Performance was evaluated via RMSE and $R^2$ for regression, and accuracy, precision, sensitivity, and F1-score for classification (Section 3.7).

### 2.8.1 Multiple Correspondence Analysis (MCA)

MCA investigated associations between categorical variables, employing `FactoMineR` to interpret conceptual relationships. The analysis revealed three main dimensions explaining 45.2% of variance, with Dimension 1 (28.4%) contrasting European products (wines, cheeses) with Asian products (teas, meats), Dimension 2 (11.3%) separating spectroscopic techniques from chromatographic methods, and Dimension 3 (5.5%) differentiating supervised algorithms from unsupervised approaches.

### 2.8.2 Network Analysis

Network analysis mapped co-occurrences, constructing a weighted undirected graph where nodes represent entities and edges indicate co-occurrence. Centrality metrics identified structurally central elements. The graph comprised 58 nodes and 142 edges (density = 0.43), with Neural Networks showing highest degree centrality (15), followed by SVM (12) and Random Forest (11). Modularity analysis identified three communities with Q = 0.62, representing technological specialization patterns.

Community detection using the Louvain algorithm [@Blondel2008] interpreted the resulting modular structure as thematic technological modules (Section 3.9).

### 2.8.3 Temporal Analysis

Temporal evolution (2010–2025) was analyzed using Spearman's correlation test [@Spearman1904] and `ggplot2` visualizations with LOESS smoothing [@Cleveland1979] to illustrate field growth and technology adoption patterns across the study period.

**Figure 2.** PRISMA-style flow diagram of identification, screening, and inclusion.

![PRISMA-style flow diagram](2-FIGURAS/2-EN/prisma_flowdiagram.png){#fig:prisma2020 width="80%"}

Automated filtering via semantic analysis and scoring achieved a thematic precision of 94.2%, surpassing the established 85% threshold. This computational screening approach proved effective for reviews involving large bibliographic volumes, suggesting that calibrated automated systems reduce selection bias and enhance reproducibility [@OforiBoateng2024]. The 100% reproducibility across multiple algorithm executions, combined with an inter-rater concordance of κ = 0.89, ensures that these findings reliably reflect the current state of scientific literature in this domain.

Manual methodological quality assessment yielded an intraclass correlation coefficient (ICC) of 0.87 (95% CI: 0.84–0.91), confirming robust inter-rater reliability and validating the inclusion criteria [@streiner2008health]. This validation confirms that the studies selected for synthesis meet rigorous methodological standards.

# 3. Results and Discussion

## 3.1 Critical Synthesis of ML Applications in Geographical Indications

The integration of Machine Learning (ML) into Geographical Indications (GIs) represents a paradigm shift in territorial certification, where data-driven models challenge traditional sensory and empirical approaches to origin verification. This critical review synthesizes evidence from 148 peer-reviewed studies (2010–2025), revealing that ML excels in sensing environmental signatures, such as spectral, elemental, and isotopic profiles, yet falters in seizing and transforming these insights into socially resilient certification systems. Drawing on dynamic capabilities theory [@Teece2007], we argue that while ML enhances sensing capabilities through high-dimensional data processing, it often neglects seizing opportunities for equitable value capture and transforming institutions to address ecological and social vulnerabilities.

A dominant trend in the literature is the application of supervised ML algorithms for origin discrimination, with Random Forest and Support Vector Machines (SVM) prevailing in spectroscopy and chromatography for agricultural products like wines, meats, and teas [@Xu2021; @Mohammadi2024; @Chen2020]. These models achieve accuracies of 80–100% in controlled settings, demonstrating that ML can decode complex terroir relationships by identifying non-linear patterns in metabolomic and elemental data [@Ramos2025; @Li2025]. Deep Learning, particularly Convolutional Neural Networks (CNNs), emerges for hyperspectral imaging, enabling automated feature extraction from unstructured data [@Peng2025; @Feng2025]. PLS-DA and PCA remain foundational for chemometric preprocessing, reducing dimensionality while preserving territorial markers [@Rebiai2022].

Statistical analysis of the corpus reveals that 72% of studies focus on European and Asian products (wines: 34%, teas: 18%, olive oils: 8%), while Global South products remain underrepresented despite rich biodiversity potential. Temporal trends show exponential growth (Spearman's ρ = 0.89, p < 0.001), with Deep Learning adoption rising from 5% (2010–2015) to 28% (2020–2025). However, this technological optimism masks critical limitations. 

Performance drops of 2–15% under spatial distribution shifts highlight a consensus on overfitting to local datasets, undermining generalization [@Kuhn2013; @Effrosynidis2021]. Only 23% of studies employ external validation, revealing a methodological gap that risks eroding consumer trust in GI seals. From a Schumpeterian perspective [@Schumpeter1934], ML innovations in sensing are disruptive, but their diffusion is hindered by data silos and proprietary algorithms, perpetuating colonial biases where Northern institutions dominate model development [@Wang2025].

ML's role in seizing value through fraud detection and quality control is evident in binary classification tasks, where sensitivity to adulteration prioritizes over overall accuracy [@Salam2021; @Loyal2022]. For instance, SVM and KNN excel in identifying counterfeit products in honey and olive oils, integrating multimodal data (e.g., elemental and spectral) to approximate fraud probabilities [@Mohammadi2024; @Isangediok2022Fraud]. Regression models predict quality attributes like acidity or antioxidant capacity, offering rapid, non-destructive alternatives to traditional assays [@Meena2024; @Liu2025]. Yet, these applications often assume linear cost structures, ignoring asymmetric impacts on small producers in the Global South, where undetected fraud can devastate livelihoods [@Iranzad2025]. Blockchain-ML hybrids represent an emerging seizing strategy, enabling decentralized traceability that reduces intermediary risks [@Gong2023; @Wang2025]. However, this convergence remains nascent, with only 21% of traceability studies adopting it, limiting its potential to transform supply chains into transparent, auditable systems.

The transformation phase, adapting institutions for sustainable GI systems, is where ML falls short. Interpretability emerges as a core lacuna, with only 14% of studies using SHAP or LIME to explain model decisions [@Effrosynidis2021; @Lundberg2017]. This opacity hinders legal defensibility, as certifiers demand transparent territorial markers for regulatory approval [@He2024]. Network analysis identifies three technological modules, Trees + Spectroscopy, SVM/KNN + Chromatography, and Neural Networks + Sensors, yet these clusters reveal fragmentation rather than integration, with limited cross-module transfer learning [@Blondel2008; @Chen2020]. From Berkes' social-ecological resilience framework [@Berkes2003], ML must foster adaptive governance that integrates producer communities and environmental monitoring. Current models are ecologically precise but socially sterile, failing to incorporate qualitative dimensions like traditional knowledge or community ethics [@Huera-Lucero2025]. Longitudinal validation is absent in 94% of studies, ignoring temporal variability in terroir signatures under climate change [@Kamilaris2018].

## 3.2 Product Registration and Algorithmic Shifts

The temporal evolution of registered products (Figure 3a) reveals distinct patterns across major GI categories. Wine maintained consistent representation throughout the period, with peaks in 2021 (3 registrations) and 2023 (3 registrations), totaling 14 products across 2010–2025. Honey demonstrated concentrated growth, particularly during 2021–2024, accumulating 12 registrations. Olive products showed sporadic but sustained presence (6 total), while cheese and coffee remained underrepresented (4 and 1 registrations, respectively). Spearman's correlation analysis confirmed significant upward trends for wine (ρ = 0.615, p = 0.011), indicating systematic expansion in GI product diversity, especially post-2020 when accessibility to ML tools and high-performance analytical techniques drove methodological innovation [@Liakos2018].

Simultaneously, a paradigmatic shift in algorithms (Figure 3b) is evident: classical chemometric methods (PLS-DA, dominant until 2018) are being replaced by models with greater predictive capacity and flexibility (Random Forest, SVM from 2019 onward). Algorithm adoption showed significant shifts: SVM (ρ = 0.788, p < 0.001) and Random Forest (ρ = 0.677, p = 0.004) demonstrated strong positive temporal correlations. Neural Networks emerged as the most adopted technique in 2020–2025 (33 applications), followed by SVM (32) and Random Forest (21). Post-2022, Deep Learning and CNNs emerged specifically for processing hyperspectral and unstructured data [@Lavine2005; @Shah2019].

Regional distribution remained stable, with 72% European/Asian focus, though Global South representation increased marginally from 18% to 22%.

**Figure 3.** Temporal evolution of (a) registered GI products by category (Wine, Honey, Olive, Coffee, Cheese) and (b) adoption of main Machine Learning algorithms in GI studies.

![Temporal evolution of publications and algorithms](2-FIGURAS/2-EN/evolucao_temporal.png){#fig:temporal_evolution width="90%"}

## 3.3 Algorithmic Landscape and Methodological Challenges

The algorithmic landscape in GI authentication is dominated by supervised models like Random Forest, SVM, and PLS-DA, which excel in handling high-dimensional data from spectroscopy and chromatography [@Xu2021; @Mohammadi2024; @Rebiai2022]. These algorithms provide interpretable feature importance, crucial for regulatory transparency [@Lundberg2017]. However, Deep Learning's opacity poses risks to legal defensibility, as "black-box" models fail to explain territorial markers [@He2024]. Dimensionality reduction via PCA and feature selection (e.g., Boruta) mitigates overfitting but cannot compensate for data biases rooted in colonial research paradigms [@Zhang2025MRF].

ML models demonstrate high accuracies (80–100%) in lab settings, yet external validation reveals drops of 2–15%, exposing statistical optimism that undermines GI integrity [@Kuhn2013; @Effrosynidis2021]. This gap is not technical but epistemological: models trained on static datasets ignore dynamic terroir changes under climate shifts, risking false certifications that erode consumer trust [@Iranzad2025].

The literature converges on a triadic set of structural deficiencies concerning spatial and temporal generalization, model interpretability alongside bias mitigation, and the incorporation of social-ecological dimensions. These limitations are statistically substantiated by the marginal prevalence of longitudinal validation (6%), the limited adoption of explainability techniques such as SHAP or LIME (14%), and the scarcity of cross-regional transfer learning tests (12%).

Furthermore, network analysis of 148 studies delineates three distinct technological modules with varying cohesion patterns (density: 0.53–0.68), yet highlights a persistent friction in cross-module knowledge transfer. Collectively, these gaps expose a pervasive technocratic bias wherein machine learning prioritizes algorithmic precision over equity and resilience. Consequently, the exponential growth of the field, though catalyzed by accessible computational tools, has failed to materialize into tangible policy impact, as models remain sequestered within academic silos rather than operationalizing conservation strategies @Liakos2018.

## 3.4 Technological Families and Applications

Multiple Correspondence Analysis (Figura 4) of 148 studies revealed structured associations between categorical variables, explaining 45.2% of variance across three dimensions: Dimension 1 (28.4%) contrasts European products (wines 34%, cheeses 12%) with Asian products (teas 18%, meats 15%); Dimension 2 (11.3%) separates spectroscopic techniques (NIR, FTIR) from chromatographic methods (GC-MS, LC-MS); and Dimension 3 (5.5%) differentiates supervised algorithms (Random Forest, SVM) from unsupervised approaches (PCA, clustering).

**Figure 4.** MCA biplot showing associations between products, algorithms, and analytical techniques. Dimension 1 separates European from Asian products, while Dimension 2 contrasts spectroscopic vs. chromatographic methods.

![MCA biplot of technological associations](2-FIGURAS/2-EN/mca_biplot.png){#fig:mca_biplot width="90%"}

The Multiple Correspondence Analysis (MCA) coordinates reveal a marked statistical polarization, wherein wines exhibit a strong convergence with Random Forest algorithms and NIR spectroscopy (0.85, 0.32), standing in sharp contrast to the predominant association between teas, SVM, and GC-MS (-0.67, 0.91). This statistical validation of technological families elucidates how specific algorithm-instrument-product triads crystallize within research practices [@Salam2021], evolving into functional architectures that encompass origin discrimination via multivariate signatures and sensitivity-prioritized fraud detection, extending to blockchain-integrated traceability, industrial predictive quality control, and consumer preference modeling [@Wang2025, @Meena2024]. Nevertheless, the delineation of such hermetic technological clusters, exemplified by the entrenched application of SVM and NIR for honey, suggests the entrenchment of methodological silos which, as cautioned by @Blondel2008, ultimately impede cross-domain innovation.

## 3.5 Future Directions and Policy Implications

Critical gaps include limited transfer learning (12% of studies), absent longitudinal validation (94%), and scarce interpretability (14%) [@Chen2020; @Kamilaris2018]. Statistical analysis shows that while multimodal fusion accounts for 28% of recent studies (2024–2025), blockchain integration remains nascent (9%). Portable ML devices offer promise for in-situ authentication, but require model compression to democratize access [@Effrosynidis2021]. Future research must integrate social-ecological dimensions, co-developing models with communities to ensure resilience [@Berkes2003].

### 3.5.1 Implications for Environmental Policy and Governance

The integration of ML into GI systems offers a promising pathway for the "auditability of ecosystem services" \cite{Vandecandelaere2018, Belletti2017}. By correlating chemical signatures with environmental variables, models can indirectly verify sustainable management practices [@Camin2017], transforming the GI seal into a verifiable certificate of environmental compliance. This is crucial for preventing greenwashing in markets that value sustainability, ensuring that the price premium benefits producers who effectively conserve agrobiodiversity [@Aprile2012, @Teuber2011].

Consequently, policymakers and certification bodies are urged to transition from reliance on subjective sensory evaluations to the formal integration of validated predictive models into technical standards [@Granato2018], thereby capturing the objective fingerprints of soil and climate. This regulatory evolution necessitates the establishment of rigorous algorithmic transparency mandates, ensuring that authentication decisions are grounded in biologically and geographically plausible criteria rather than opaque computations [@Rudin2019, @Broadhurst2018]. Furthermore, the scalability of these systems depends on the strategic fostering of public data repositories, where open spectral and metabolomic libraries enable cross-validation and the development of robust regional models [@Wilkinson2021], a measure particularly critical for mitigating technological asymmetries in the Global South [@Kshetri2014].

Furthermore, classification algorithms can be deployed by regulatory agencies to monitor environmental compliance at scale [@Weiss2020]. In vast territories like the Amazon or the Cerrado, where physical inspections are costly and logistically challenging, ML models trained on remote sensing and product samples can act as a first line of defense [@Osco2021, @Gomes2023], flagging anomalies that warrant on-site verification. This reduces audit costs and increases the effectiveness of environmental governance [@Liakos2018].

For certification systems, the analysis of 148 studies indicates that Machine Learning techniques have potential to strengthen GI certification, but practical implementation remains limited by validation, interpretability, and governance challenges. The heterogeneity in reported accuracy rates (82% to 100%) reflects differences in methodological rigor, sample size, and application context. Only 23% of studies report validation with samples from regions not represented in training, with performance drops of up to 15% [@Chen2020; @Effrosynidis2021; @Kuhn2013], evidencing that spatially independent validation is indispensable for legal defensibility.

The preference for inherently interpretable models, such as Random Forest with variable importance analysis or PLS-DA with explicit loadings, emerges as a pragmatic strategy to balance accuracy and explainability, while enabling the identification of territorial markers suitable for incorporation into technical standards. From a geographical perspective, the concentration of 72% of studies on European and Asian products opens evident opportunities for GIs in developing countries, including Brazil, where coffee, cheese, cachaça, and cocoa can benefit from consolidated methodologies [@Li2025; @Frigerio2024]. The consolidation of ML in GI systems requires a support ecosystem articulating laboratory infrastructure, data science competencies, and data governance, integrating empirical knowledge of producer communities with computational evidence [@Huera-Lucero2025].

# 4. Conclusions

This review maps the convergence of Machine Learning and origin certification, revealing a field undergoing methodological maturation that is transitioning from mere geographical discrimination to precision environmental auditing. Evidence indicates that ML possesses the technical capacity to validate *terroir* integrity and detect fraud with superior accuracy compared to traditional methods, yet its application as an environmental governance tool still faces implementation barriers.

Algorithmic choices currently reflect an ecology of informational and regulatory constraints. The predominance of *in silico* validations and the scarcity of longitudinal and spatial tests undermine the legal robustness of models, necessitating rigorous validation protocols that simulate real-world climate variations. Effective integration into certification systems requires a paradigm shift that prioritizes explainability and reproducibility over sheer architectural complexity.

For the Global South, the path forward involves developing methodologies adapted to local contexts and biodiversity, integrating equity and governance into the distribution of territorial knowledge benefits. Ultimately, the success of Machine Learning in Geographical Indications will not be measured solely by statistical accuracy, but by its capacity to ensure the conservation of natural resources that underpin product typicity.

In the face of accelerating climate change, the stability of these traditional terroirs is threatened. Machine Learning offers the necessary agility to monitor these shifts, allowing GIs to adapt their technical specifications dynamically. Thus, the transition to a 'Digital Terroir' is not a technocratic luxury but a survival strategy. It safeguards the epistemic sovereignty of producer communities by providing the hard evidence needed to monetize their stewardship of global agrobiodiversity. Future research must therefore pivot from isolated accuracy contests to the development of open, federated, and explainable AI systems capable of governing the planetary commons.


# Acknowledgments

The authors thank the Universidade Federal de Sergipe (UFS), the State University of Feira de Santana (UEFS), and the Instituto Federal de Sergipe (IFS) for the institutional and infrastructural support that enabled this research.

# Conflicts of Interest

The authors declare no conflicts of interest.

# Data Availability Statement

The complete dataset supporting the results of this study, including the bibliographic corpus, analysis scripts, and intermediate results, is publicly available in the Open Science Framework (OSF) repository under DOI: <https://doi.org/10.17605/OSF.IO/2EKYQ>.


# Ethics Statement

This review does not involve human participants, animal experiments, cell lines, or specimen collection. No ethics approval or consent was required.

# Positionality/Community Involvement

Where relevant, community perspectives from producer organizations and certifiers informed interpretation of practical constraints in GI systems; no identifiable information was included.

# References

::: {#refs}
:::
