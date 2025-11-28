---
title: "Digital Terroir A Critical Review of Machine Learning for Environmental Governance in Geographical Indications"
author: "Catuxe Varjão de Santana Oliveira, Paulo Roberto Gagliardi, Luiz Diego Vidal Santos, Gustavo da Silva Quirino, Ana Karla de Souza Abud, Cristiane Toniolo Dias"
bibliography: referencias.bib
csl: apa.csl
reference-doc: modelo_formatacao.docx
fig-align: center
table-align: center
lang: en-US
---
# Abstract

Geographical Indications (GIs) operate as coupled socioecological systems, wherein product typicity emerges from complex interactions among soil, climate, and biota. Auditing these systems demands robust analytical methods capable of validating ecosystem services and preventing fraud. This scoping review analyzes how Machine Learning (ML) algorithms process analytical signatures (spectral, elemental, and isotopic) to support environmental auditing, fraud detection, and greenwashing prevention, proposing the Digital Terroir concept as a governance mechanism. Following PRISMA-ScR guidelines, a systematic search was conducted for peer-reviewed studies published between 2010 and 2025. A total of 148 articles applying ML to GI authentication were included. Although algorithms demonstrate high discriminant accuracy (80–100%), the predominance of static model applications renders Digital Terroir operationalization unfeasible. The Inferential Digital Twin function is compromised by the critical absence of longitudinal validation under climate variability (94%), spatially independent testing (77%), and algorithmic explainability (86%), limiting regulatory applicability. ML must evolve from a classification tool to a verifiable socioecological auditing mechanism. The review concludes with recommendations for implementing rigorous external validation protocols, open-access spectral repositories, and participatory structures, aiming to strengthen GI credibility as instruments for agrobiodiversity conservation and climate mitigation.

**Keywords:** Geographical Indications; Machine Learning; Environmental Auditing; Greenwashing; Traceability; Ecosystem Services.
---------------------------------------------------------------------------------------------------------------------------------------------------

# 1. Introduction

Geographical Indications (GIs) transcend their original intellectual property function by emerging as strategic instruments for environmental governance and agrobiodiversity conservation in the Anthropocene [@Belletti2017; @Vandecandelaere2009]. Within a global context marked by climate crisis and biodiversity erosion, GIs operate as socioecological systems linking product quality to the integrity of territorial ecosystem services [@Berkes2003; @Bramley2013]. They represent mechanisms for valorizing regenerative agricultural practices and maintaining cultural landscapes, where *terroir* is redefined not merely as a sensory attribute but as a digital fingerprint of product and climate resilience [@Giovannucci2010; @Fonzo2015].

International regulation, grounded in the TRIPS Agreement and EU Regulation No. 1151/2012, establishes the legal foundation, yet environmental auditing capacity confers contemporary legitimacy to these assets [@EU2012; @WTO1994]. The distinction between Protected Geographical Indication (PGI) and Protected Designation of Origin (PDO) reflects varying degrees of natural cycle dependence, requiring robust verification systems to prevent greenwashing and ensure that market premiums effectively finance environmental conservation [@Locatelli2008; @WIPO2020]. The credibility of these labels therefore depends on the capacity to scientifically demonstrate that product characteristics derive from specific, non-replicable environmental interactions.

Terroir can be understood as an intrinsically coupled socioecological system wherein soil, climate, biota, and culture articulate through nonlinear interactions, feedbacks, and strong spatial-temporal heterogeneity, configuring territories where biophysical processes and social practices are co-produced [@LeFloc2016S]. This systemic complexity and the diffuse nature of its couplings constrain the detection of ecosystem services sustaining product typicity and value through conventional metrics [@Levin1998ComplexAdaptiveSystems]. Consequently, the valuation of these services and common-pool resource governance are weakened, facilitating greenwashing practices [@Gale2023]. The absence of analytical instrumentation capable of deciphering these systemic couplings compromises environmental monitoring and enforcement across extensive biomes, impacting global-scale sustainability [@Liao2023].

Against this background, Machine Learning (ML) emerges as an intrinsic computational approach for complex systems analysis. By processing patterns and nonlinear relationships in multi-scalar data—encompassing spectral, isotopic, and metabolomic information—ML converts the inherent uncertainty of these systems into auditable evidence [@Li2022KGML_ag]. This capacity is fundamental for environmental governance and preserving community epistemic sovereignty [@Suh2007; @Santos2007Epistemologies]. Across broad geographical scales, ML enables ecosystem service auditability, establishing a verifiable link between environmental compliance and market premiums while mitigating informational asymmetries that enable fraud and misappropriation [@Kshetri2014DigitalDivide].

However, the literature lacks a unified conceptual framework integrating ML's inferential capabilities with environmental certification regulatory requirements. This gap limits the translation of methodological advances into operational protocols for Geographical Indication systems, perpetuating fragmentation between academic research and territorial governance.

Accordingly, this review systematically maps Machine Learning applications in Geographical Indications, focusing on their potential for environmental authentication and fraud prevention. Through synthesizing 148 peer-reviewed studies (2010–2025), we propose the Digital Terroir concept as an analytical framework to operationalize inferential auditing of ecosystem services. We posit that modeling nonlinear couplings between environmental variables (territorial genotype) and chemometric signatures (product phenotype) can generate auditable evidence of environmental compliance, converting diffuse sustainability claims into verifiable data and grounding market-based conservation policies.



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
