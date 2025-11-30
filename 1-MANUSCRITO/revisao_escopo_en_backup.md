---
title: "Digital Terroir and Ecosystem Service Auditability via Machine Learning in Geographical Indications <b>Terroir Digital e Auditabilidade de Serviços Ecossistêmicos via Aprendizado de Máquina em Indicações Geográficas</b>"
author: "Catuxe Varjão de Santana Oliveira, Paulo Roberto Gagliardi, Luiz Diego Vidal Santos, Gustavo da Silva Quirino, Ana Karla de Souza Abud, Cristiane Toniolo Dias"
bibliography: referencias.bib
csl: apa.csl
reference-doc: modelo_formatacao.docx
fig-align: center
table-align: center
lang: en-US
---

# Abstract

Geographical Indications (GIs) constitute coupled socioecological systems wherein typicity emerges from dynamic interactions among soil, climate, and biota. Validating these nexuses requires auditable environmental governance tools. Within this context, the present study investigates whether the current Machine Learning apparatus possesses the necessary robustness to underpin Digital Terroir. Methodological adequacy is evaluated through spatial and temporal generalization capacity of models, while 'technical maturity' is assessed through algorithmic transparency (XAI) and reproducibility—indispensable requirements for transitioning from laboratory classifiers to governance tools. Specifically, we investigate whether prevailing algorithms possess sufficient robustness to transcend mere geographical classification and function as verifiable inferential auditing instruments. Following PRISMA-ScR guidelines, a critical synthesis of 148 peer-reviewed studies (2010–2025) was conducted. Analysis evaluated validation patterns, interpretability, and environmental data integration to determine operational feasibility of the proposed framework. Although classifiers demonstrate high discriminant accuracy (80–100%), the predominant static modeling paradigm proves insufficient to operationalize Digital Terroir as an Inferential Digital Twin. Proposal viability is constrained by critical generalization gaps, specifically the absence of longitudinal validation under climate variability (94%), spatially independent testing (77%), and algorithmic explainability (86.5%). Actualizing Digital Terroir as an instrument for sustainability and epistemic sovereignty demands research reorientation. Transitioning from laboratory classification experiments to developing adaptive, transparent models validated under real climate scenarios is imperative.

## **Keywords:** Geographical Indications; Machine Learning; Environmental Auditing; Greenwashing; Traceability; Ecosystem Services.

# 2. Materials and Methods

This review follows PRISMA-ScR guidelines (Preferred Reporting Items for Systematic Reviews and Meta-Analyses extension for Scoping Reviews) as a transparency framework to ensure methodological clarity and reproducibility. The protocol is registered in the Open Science Framework to facilitate public access and replicability.

## 2.1 Research Question

The study employs the PCC structure (Population, Concept, Context) to formulate the following research question: How have Machine Learning techniques been applied for authentication, evaluation, and decision support in Geographical Indication systems?

**Table 1.** Review structure according to the PCC model.

| Element | Description |
|:----------------------|:------------------------------------------------|
| **P (Population)** | Nationally and internationally recognized Geographical Indications, Designations of Origin, and Indications of Provenance, encompassing agri-food products (wines, cheeses, coffees, meats, olive oils), handicrafts, and other products with territorial identity. |
| **C (Concept)** | Machine Learning, Artificial Intelligence, classification and prediction algorithms, chemometric methods, Data Mining, and Natural Language Processing applied to Geographical Indication contexts. |
| **C (Context)** | Geographical origin authentication, GI potential assessment, identification of territorial determinants (soil, climate, production methods), product classification and discrimination, decision support systems for certification, quality control, traceability, fraud and adulteration detection, and territorial valorization strategies. |

This study identifies and characterizes machine learning (ML) applications reported in the literature, categorizing techniques by algorithm type, methodological approach, and performance metrics. Additionally, it analyzes application distribution by product type, geographical region, and period, identifying methodological gaps, limitations, and directions for future research.

## 2.1.1 PRISMA-ScR Methodological Flowchart

Figure 1 presents the methodological flowchart, structured in four sequential phases: (1) Main database search strategies, (2) Automated filtering with a weighted scoring system, (3) Manual quality assessment with multidisciplinary evaluation, and (4) Bibliometric analysis and qualitative synthesis integrating quantitative and documentary methodologies. The flowchart details the pathway from record identification to final synthesis, offering recommendations for Machine Learning implementation in Geographical Indication systems.

**Figure 1.** Screening, eligibility, and synthesis flowchart for machine learning applications in Geographical Indications.

![](2-FIGURAS/2-EN/ml_indicacoes_geograficas.png){#fig:ml_indicacoes width="80%"}

Geographical Indications (GIs) transcend their original intellectual property function by emerging as strategic instruments for environmental governance and agrobiodiversity conservation in the Anthropocene [@Belletti2017; @Vandecandelaere2009]. Within a global scenario marked by climate crisis and biodiversity erosion, GIs operate as socioecological systems linking product quality to territorial ecosystem service integrity [@Berkes2003; @Bramley2013]. They represent mechanisms for valorizing regenerative agricultural practices and maintaining cultural landscapes, wherein *terroir* is redefined not merely as a sensory attribute but as a digital fingerprint of product and climate resilience [@Giovannucci2010; @Fonzo2015].

International regulation, grounded in the TRIPS Agreement and EU Regulation No. 1151/2012, establishes the legal foundation, yet environmental auditing capacity confers contemporary legitimacy to these assets [@EU2012; @WTO1994]. The distinction between Protected Geographical Indication (PGI) and Protected Designation of Origin (PDO) reflects varying degrees of natural cycle dependence, requiring robust verification systems to prevent greenwashing and ensure that market premiums effectively finance environmental conservation [@Locatelli2008; @WIPO2020]. Label credibility therefore depends on the capacity to scientifically demonstrate that product characteristics derive from specific, non-replicable environmental interactions.

Terroir can be understood as an intrinsically coupled socioecological system wherein soil, climate, biota, and culture articulate through nonlinear interactions, feedbacks, and strong spatial-temporal heterogeneity, configuring territories where biophysical processes and social practices are co-produced [@LeFloc2016S]. This systemic complexity and the diffuse nature of its couplings limit detection of ecosystem services sustaining typicity and product value through conventional metrics [@Levin1998ComplexAdaptiveSystems]. Consequently, valuation of these services and common-pool resource governance are weakened, facilitating greenwashing practices [@Gale2023]. The absence of analytical instrumentation capable of deciphering these systemic couplings compromises environmental monitoring and enforcement across extensive biomes, impacting global-scale sustainability [@Liao2023].

Within this context, Machine Learning (ML) emerges as an intrinsic computational approach for complex systems analysis. By processing patterns and nonlinear relationships in multi-scalar data—encompassing spectral, isotopic, and metabolomic information—ML converts the inherent uncertainty of these systems into auditable evidence [@Li2022KGML_ag]. This capacity is fundamental for environmental governance and preserving community epistemic sovereignty [@Suh2007; @Santos2007Epistemologies]. Across broad geographical scales, ML enables ecosystem service auditability, establishing a verifiable link between environmental compliance and market premiums while mitigating informational asymmetries enabling fraud and misappropriation [@Kshetri2014DigitalDivide].

However, the literature lacks a unified conceptual framework integrating ML's inferential capabilities with environmental certification regulatory requirements. This gap limits the translation of methodological advances into operational protocols for Geographical Indication systems, perpetuating fragmentation between academic research and territorial governance.

In this sense, this review systematically maps Machine Learning applications in Geographical Indications, focusing on their potential for environmental authentication and fraud prevention. Through synthesizing 148 peer-reviewed studies (2010–2025), we propose the 'Digital Terroir' concept as an analytical framework to operationalize inferential auditing of ecosystem services. We posit that modeling nonlinear couplings between environmental variables (territorial genotype) and chemometric signatures (product phenotype) can generate auditable evidence of environmental compliance, converting diffuse sustainability claims into verifiable data and grounding market-based conservation policies.



## 4. Conclusions

Geographical Indications operate as coupled socioecological systems wherein interactions among soil, climate, and biota underpin the genesis of product territorial typicity. Machine learning algorithms emerged as robust instruments for decoding such nonlinear interactions, transmuting chemometric signatures into auditable evidence of environmental compliance.

The research landscape remains asymmetric, with predominant literature concentrated in temperate regions and conventional commodities. Additional efforts are required for developing robust and inclusive models encompassing diverse products and geographies through leveraging investments in laboratory infrastructure, transparent data governance, and integration of local empirical knowledge.

Conceptually, overcoming these barriers resides in the transition to Digital Terroir. Unlike the predominant static approach, this framework is grounded in dynamic reconstruction of soil-climate-biota interactions. Evidence suggests that integrating environmental data with chemometric classifiers constitutes the most promising technical pathway for transforming origin certification into auditable ecosystem service auditing, provided identified algorithmic transparency challenges are overcome.

Future research must prioritize beyond marginal accuracy, ecological validity, and data governance. Development of validation protocols simulating seasonal fluctuations and Explainable Artificial Intelligence (XAI) implementation are imperative to ensure authentication decisions are grounded in causal biological markers rather than spurious correlations. Digital Terroir realization will ultimately depend on the scientific community's capacity to standardize metadata and open repositories, enabling Machine Learning to operate as a transparent mechanism for verifying environmental compliance.

## Acknowledgments

The authors acknowledge Universidade Federal de Sergipe (UFS), Universidade Estadual de Feira de Santana (UEFS), and Instituto Federal de Sergipe (IFS) for institutional and infrastructural support enabling this research.

## Conflicts of Interest

The authors declare no conflicts of interest.

## Data Availability Statement

The complete dataset supporting this study's results, including the bibliographic corpus, analysis scripts, and intermediate results, is publicly available on the Open Science Framework (OSF) repository under DOI: [https://doi.org/10.17605/OSF.IO/2EKYQ](https://doi.org/10.17605/OSF.IO/2EKYQ).

## Ethics Statement

This review does not involve human participants, animal experiments, cell lines, or sample collection. Ethical approval or consent was not required.

## Community Positioning/Engagement

Where relevant, community perspectives from producer organizations and certifiers contributed to interpreting practical limitations in Geographical Indication (GI) systems; no individually identifiable information was included.

## References

::: {#refs}
:::

## Table A.3: Technological Modules Identified by Louvain Community Analysis

| **Module** | **Main Algorithms** | **Analytical Techniques** | **Products** | **Predominant Region** |
| :---------------: | :---------------------------------------------- | :-------------------------------------------- | :------------------------- | :----------------------------- |
| **M1** | Random Forest, Decision Tree, Gradient Boosting | Spectroscopy (NIR), Chemometrics | Wine, Honey | Africa, Europe |
| **M2** | SVM, KNN | Chromatography (GC-MS, LC-MS, HPLC) | Meats, Regional Products | Asia |
| **M3** | Neural Networks, CNN, Deep Learning | Spectroscopy (NIR, FTIR), Sensors (e-nose) | Olive Oil, Cheese, Tea | Europe, Asia |

*Source: Three main technological modules identified by Louvain community analysis applied to co-occurrence network among algorithms, analytical techniques, and geographical indication products. Internal density of each module indicates connection strength among its components.*

### Table A.4: Technological Families Identified by Cluster Analysis

| **Cluster** | **Main Product** | **Analytical Technique** | **ML Algorithm** | **Application** | **Predominant Region** |
| ----------------- | --------------------------- | ----------------------------- | ---------------------------------------- | ------------------------------------- | ------------------------------ |
| 1 | Honey | NIR Spectroscopy | SVM, KNN | Authentication and fraud detection | Asia |
| 2 | Cheese | NIR Spectroscopy | Neural Networks | Origin discrimination | Europe |
| 3 | Honey, Meats | LC-MS, GC-MS | SVM, Random Forest, Decision Trees | Authentication and traceability | Asia, Europe |

*Source: Ten clusters identified by cluster analysis (k-means and hierarchical) based on product, analytical instrument, algorithm, and application type. Only the three most notable clusters are detailed here.*
