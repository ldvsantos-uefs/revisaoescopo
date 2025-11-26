---
title: "Aprendizado de Máquina em Indicações Geográficas: Uma Revisão Crítica Integrativa sobre Autenticação e Certificação"
author: "Catuxe Varjão de Santana Oliveira, Paulo Roberto Gagliardi, Luiz Diego Vidal Santos, Gustavo da Silva Quirino, Ana Karla de Souza Abud, Cristiane Toniolo Dias"
bibliography: referencias.bib
csl: apa.csl
reference-doc: modelo_formatacao.docx
fig-align: center
table-align: center
lang: pt-BR
---

# Resumo

Indicações Geográficas (IGs) atuam simultaneamente como ativos de propriedade intelectual e ferramentas de conservação da agrobiodiversidade, vinculando a qualidade do produto aos serviços ecossistêmicos do território. Esta revisão fornece uma síntese crítica integrativa das aplicações de Aprendizado de Máquina (ML) em sistemas de IG (2010–2025), com foco em como assinaturas analíticas (espectrais, elementares, isotópicas) sustentam a auditoria ambiental, a detecção de fraudes e a prevenção de *greenwashing*. Em 148 estudos revisados por pares, classificadores supervisionados dominam: Random Forest e Support Vector Machines são prevalentes em espectroscopia e cromatografia para vinhos, carnes, óleos e chás; Deep Learning emerge para dados hiperespectrais; e PLS‑DA permanece central em quimiometria. Acurácias típicas variam de 80% a 100% em ambientes laboratoriais, porém a generalização é frequentemente superestimada: apenas 23% dos estudos executam validação espacialmente independente e menos ainda incluem testes longitudinais, com quedas de desempenho de 2%–15% sob deslocamentos de distribuição. Para incorporação em certificação ambiental, os modelos devem demonstrar validação externa rigorosa, oferecer interpretabilidade capaz de identificar marcadores de saúde do solo e resiliência climática, e operar sob governança de dados transparente. Sintetizamos padrões metodológicos em famílias tecnológicas e delineamos orientações para que o ML fortaleça a credibilidade das IGs como instrumentos de sustentabilidade, evitando que o otimismo estatístico corroa a confiança do consumidor e o valor ecológico do ativo.

**Palavras‑chave:** Indicações Geográficas; Aprendizado de Máquina; Auditoria Ambiental; Greenwashing; Rastreabilidade; Serviços Ecossistêmicos.
---


# 1. Introdução

As Indicações Geográficas (IGs) transcendem sua função original de propriedade intelectual para emergir como instrumentos estratégicos de governança ambiental e conservação da agrobiodiversidade no Antropoceno [@Belletti2017; @Vandecandelaere2009]. Em um cenário global marcado pela crise climática e pela erosão da diversidade biológica, as IGs operam como sistemas socioecológicos que vinculam a qualidade do produto à integridade dos serviços ecossistêmicos do território [@Berkes2003; @Bramley2013]. Mais do que garantias de origem, elas representam mecanismos de valorização de práticas agrícolas regenerativas e de manutenção de paisagens culturais, em que o terroir é redefinido não apenas como atributo sensorial, mas como uma impressão digital da saúde do solo e da resiliência climática [@Giovannucci2010; @Fonzo2015].

A regulação internacional, ancorada no Acordo TRIPS e no Regulamento (UE) nº 1151/2012, estabelece a base legal, mas é a capacidade de auditoria ambiental que confere legitimidade contemporânea a esses ativos [@EU2012; @WTO1994]. A distinção entre Indicação Geográfica Protegida (IGP) e Denominação de Origem Protegida (DOP) reflete diferentes graus de dependência de ciclos naturais, exigindo sistemas de verificação robustos para evitar greenwashing e assegurar que o prêmio de mercado financie efetivamente a conservação ambiental [@Locatelli2008; @WIPO2020]. A credibilidade desses selos depende, portanto, da capacidade de provar cientificamente que as características do produto derivam de interações ambientais específicas e não replicáveis.

Nesse contexto, o Aprendizado de Máquina (ML) emerge como tecnologia disruptiva para auditoria ambiental. Ao processar dados espectrais, isotópicos e metabolômicos de alta dimensão, algoritmos de ML podem decodificar “assinaturas de saúde do solo” e “marcadores de resiliência climática” invisíveis a métodos tradicionais [@Gbashi2024FoodIntegrityAI; @Rocha2020NonLinear]. Diferentemente da análise sensorial subjetiva, o ML oferece abordagem quantitativa para validar a “integridade do terroir”, transformando a complexidade química em evidência auditável de conformidade ambiental [@Qamar2023DeepLearning; @Ramos2025]. Essa capacidade é crítica para auditar serviços ecossistêmicos, permitindo distinguir produtos que genuinamente conservam a biodiversidade daqueles que apenas exploram reputações regionais.

A aplicação de ML em IGs não é apenas inovação técnica, mas ferramenta de soberania epistêmica e justiça ambiental. Permite que comunidades locais convertam conhecimento tácito e práticas de manejo em dados verificáveis, protegendo recursos genéticos e culturais contra apropriação indevida [@Suh2007; @Azevedo2011]. Contudo, a literatura carece de síntese que conecte essas tecnologias de sensoriamento às demandas urgentes de monitoramento ambiental.

Esta revisão mapeia sistematicamente aplicações de Machine Learning em Indicações Geográficas, focando seu potencial para autenticação ambiental e prevenção de fraudes. Hipotetizamos que técnicas de ML, quando integradas a dados ambientais, funcionam como mecanismos de auditoria de serviços ecossistêmicos, oferecendo base científica robusta para políticas de conservação orientadas pelo mercado e para a prevenção do greenwashing em cadeias globais de valor.

# 2. Materiais e Métodos

Esta revisão segue as diretrizes PRISMA-ScR (*Preferred Reporting Items for Systematic Reviews and Meta-Analyses extension for Scoping Reviews*) como estrutura de transparência para garantir clareza metodológica e reprodutibilidade. O protocolo está registrado no Open Science Framework para facilitar acesso público e replicabilidade.

## 2.1 Questão de Pesquisa

O estudo emprega o modelo PCC (População, Conceito, Contexto) para formular a questão de pesquisa: Como as técnicas de Machine Learning têm sido aplicadas para autenticação, avaliação e apoio à decisão em sistemas de Indicações Geográficas?

**Tabela 1.** Estrutura da revisão segundo o modelo PCC.

| Elemento | Descrição |
| :-- | :-- |
| **P (População)** | Indicações Geográficas, Denominações de Origem e Indicações de Procedência reconhecidas nacional e internacionalmente, abrangendo produtos agroalimentares (vinhos, queijos, cafés, carnes, azeites), artesanato e outros produtos com identidade territorial. |
| **C (Conceito)** | Machine Learning, Inteligência Artificial, algoritmos de classificação e predição, métodos quimiométricos, Mineração de Dados e Processamento de Linguagem Natural aplicados a contextos de Indicações Geográficas. |
| **C (Contexto)** | Autenticação de origem geográfica, avaliação de potencial de IG, identificação de determinantes territoriais (solo, clima, métodos de produção), classificação e discriminação de produtos, sistemas de apoio à decisão para certificação, controle de qualidade, rastreabilidade, detecção de fraudes e adulterações, e estratégias de valorização territorial. |

Este estudo identifica e caracteriza aplicações de ML relatadas na literatura, categorizando técnicas por tipo de algoritmo, abordagem metodológica e métricas de desempenho. Adicionalmente, analisa a distribuição de aplicações por tipo de produto, região geográfica e período, identificando lacunas, limitações e direções para pesquisas futuras.

## 2.1.1 Fluxograma Metodológico PRISMA-ScR

A Figura 1 apresenta o fluxograma metodológico, estruturado em quatro fases sequenciais: (1) Estratégias de busca nas principais bases; (2) Filtragem automatizada com sistema de pontuação ponderada; (3) Avaliação manual de qualidade com revisão multidisciplinar; e (4) Análise bibliométrica e síntese qualitativa integrando metodologias quantitativas e documentais. O fluxograma detalha o percurso da identificação à síntese, oferecendo recomendações para implementação de ML em sistemas de IG.

**Figura 1.** Fluxograma de triagem, elegibilidade e síntese de aplicações de ML em IGs.

![Fluxograma do processo de revisão ML‑IG](2-FIGURAS/2-EN/ml_indicacoes_geograficas.png){#fig:ml_indicacoes width="80%"}

## 2.3 Estratégia de Busca e Extração de Estudos

As buscas abrangeram Scopus (Elsevier) e Web of Science (Clarivate), cruzando três domínios: técnicas de ML/IA; sistemas de certificação geográfica; e IGs/Denominações de Origem.

Descritores empregaram terminologia controlada em inglês e operadores booleanos (AND, OR, NOT), cobrindo 2010–2025:

*("machine learning" OR "artificial intelligence" OR "deep learning" OR "supervised learning" OR "unsupervised learning" OR "ensemble methods") AND ("geographical indications" OR "denominations of origin" OR "appellations of origin" OR "protected designations of origin") AND ("authentication" OR "traceability" OR "quality control" OR "fraud detection" OR "geospatial analysis")*.

Critérios de inclusão: artigos revisados por pares em inglês, português ou espanhol com aplicações de ML em contextos de IG, autenticação de origem ou controle de qualidade territorial. Descritores primários no título, resumo ou palavras‑chave. Exclusões: não revisados por pares, estudos sem aplicação prática de ML ou sem dimensão territorial.

A extração usou formulário padronizado para registrar metadados (autor, ano, título), características geográficas (país, região, tipo de IG), detalhes do produto (categoria, denominação), abordagem metodológica (algoritmos, técnicas instrumentais, tamanho amostral) e métricas (acurácia, sensibilidade, especificidade, RMSE).

## 2.4 Primeira Fase: Sistema Automatizado de Filtragem de Relevância Temática

### 2.4.1 Algoritmo de Pontuação Ponderada

Para complementar a triagem manual, um sistema automatizado atribui pontuações de relevância com base na presença e localização de descritores no título, resumo e palavras‑chave. Implementado em Python (NLTK, spaCy), o algoritmo aplica ponderação hierárquica e adere aos princípios do AHP (Equação 1), organizando descritores em cinco categorias com pesos diferenciados [@SAATY1991].

$$
S_i = \sum_{j=1}^{n} w_j \cdot l_i \cdot f_{ij}
$$

onde: $S_i$ é a pontuação do artigo $i$; $w_j$ é o peso do termo $j$ (5, 3, 2, 1 ou −5/−3/−2); $l_i$ é o fator de localização (1,5 para título, 1,2 para palavras‑chave, 1,0 para resumo); $f_{ij}$ é a frequência do termo $j$; e $n$ o número total de termos.

Termos prioritários (5) representam o núcleo conceitual (ex.: geographical indications, traceability, authentication). Alta relevância (3) cobre conceitos metodológicos (ex.: machine learning, deep learning, neural networks). Média relevância (2) contempla temas complementares (ex.: chemometrics, data mining). Termos de contexto (1) indicam ambientes potenciais (ex.: regional products, certification). Termos de exclusão recebem pesos negativos (médico/clínico −5; urbanismo −3; finanças −2) [@MUNN2018; @tricco2018].

### 2.4.2 Implementação e Validação

Para cada registro, o algoritmo varre os campos, aplica pesos e multiplica por fatores de localização. O limiar mínimo de inclusão foi definido pela inflexão da curva cumulativa (Pareto/cotovelo), ajustado por validação manual com amostragem estratificada.

### 2.4.3 Validação Participativa e Refinamento

Três revisores independentes (ML e IG) avaliaram sistematicamente 272 estudos. O protocolo incluiu reavaliação cega e discussão de casos limítrofes. A concordância entre o sistema automatizado e a revisão manual atingiu 90,2%.

### 2.4.4 Cobertura Bibliográfica e Categorização Automatizada

Um verificador automatizado assegurou a consistência entre citações no texto e arquivos bibliográficos. O corpus foi categorizado via PLN, combinando modelos supervisionados e regras semânticas [@Young2019; @Casey2021]. Métricas de cobertura e uso bibliográfico avaliaram a adequação temática [@tranfield2003; @webster2002].

## 2.5 Segunda Fase: Avaliação Manual de Qualidade

Três revisores avaliaram qualidade metodológica, reduzindo viés interpretativo. A escala MMAT [@pluye2009; @hong2018] foi adaptada para estudos interdisciplinares ML‑IG, com oito indicadores em escala Likert de 3 pontos (Tabela 2): rigor, validação, ética, reprodutibilidade, integração quanti‑quali, impacto, documentação e generalização.

Cada indicador recebeu 0 (não atende), 1 (parcial) ou 2 (atende plenamente). A escala de 3 pontos equilibra granularidade e consistência interavaliadores [@Likert3vs5_2025].

**Tabela 2.** Indicadores de qualidade para estudos ML‑IG.

| Código | Indicador | Domínio |
| -- | -- | -- |
| RIG | Rigor metodológico na coleta e processamento de dados territoriais | Qualidade Territorial |
| VAL | Validação técnica com métricas apropriadas | Qualidade Computacional |
| ETI | Adesão a protocolos éticos com comunidades produtoras | Qualidade Ética |
| REP | Reprodutibilidade de experimentos computacionais | Qualidade Técnica |
| INT | Integração entre métodos territoriais quantitativos e qualitativos | Qualidade Metodológica |
| IMP | Impacto e aplicabilidade para sistemas de IG | Qualidade Social |
| DOC | Documentação completa de algoritmos e procedimentos | Qualidade Documental |
| GEN | Generalização e transferibilidade dos métodos | Qualidade Científica |

### 2.5.1 Procedimentos de Consenso e Validação Interavaliadores

Uma amostra piloto (n≈30; ~11%) calibraram critérios. No corpus completo, discordâncias (≥2 pontos) passaram por reavaliação cega e consenso. O ICC foi 0,87 (IC95%: 0,84–0,91) [@shrout1979].

### 2.5.2 Critérios para Estudos Interdisciplinares

Os critérios avaliaram coerência da integração quanti‑quali, validação multirregional, transparência algorítmica, adesão ética e aplicabilidade para certificação. Selecionaram‑se 25 estudos com qualidade adequada (≥20 pontos) dentre 272: 1 excelência (≥40), 2 alta relevância (≥30) e 22 adequados (≥20).

## 2.6 Terceira Fase: Análise Bibliométrica

A Lei de Lotka [@lotka1926] descreveu a produtividade científica, identificando padrões de concentração/disp ersão. Acoplamento bibliográfico e cocitação não foram realizados por ausência de campos de referências citadas.

## 2.7 Quarta Fase: Síntese Qualitativa e Análise Documental

A síntese final combinou análise temática e o princípio de Pareto (80/20), priorizando os 20% de maior pontuação (40% qualidade, 35% relevância, 25% impacto bibliométrico). A pontuação final foi:

$$
P_{final} = (0{,}40\,Q_{met}) + (0{,}35\,Q_{tem}) + (0{,}25\,Q_{biblio})
$$

## 2.8 Análises Estatísticas

As análises em R [@RCoreTeam2024] via RStudio [@RStudioTeam2023] caracterizaram o corpus e identificaram padrões. A MCA investigou associações entre variáveis categóricas (algoritmos, produtos, regiões, técnicas), seguindo @Le2008; @Greenacre2017, com `FactoMineR`. Em seguida, análises de cluster (k‑means e hierárquica) com `FactoMineR` e `factoextra` identificaram agrupamentos produto‑instrumento‑algoritmo, sintetizando “famílias tecnológicas” (Seção 3.4).

Redes de coocorrência mapearam algoritmos, produtos e regiões [@Csardi2006; @Schoch2020]. Com `igraph` e `ggraph`, construiu‑se grafo não direcionado, calculando centralidades (grau, autovetor, intermediação). Comunidades foram detectadas via Louvain [@Blondel2008] (Seção 3.4).

A evolução temporal (2010–2025) foi analisada com correlação de Spearman [@Spearman1904] e visualizações `ggplot2` com LOESS [@Cleveland1979]. Modelos preditivos globais testaram se variáveis bibliométricas/metodológicas antecipam pontuações (OLS, Ridge, Lasso, Random Forest; classificação por Regressão Logística, Random Forest) com `caret` e `randomForest`. Métricas: RMSE e $R^2$ para regressão; acurácia, precisão, sensibilidade e F1‑score para classificação (Seção 3.3).

### 2.8.1 Análise de Correspondência Múltipla (MCA)

A MCA revelou três dimensões explicando 45,2% da variância: Dimensão 1 (28,4%) contrasta produtos europeus (vinhos, queijos) com asiáticos (chás, carnes); Dimensão 2 (11,3%) separa espectroscopia de cromatografia; Dimensão 3 (5,5%) diferencia algoritmos supervisionados de não supervisionados.

### 2.8.2 Análise de Rede

O grafo contou 58 nós e 142 arestas (densidade = 0,43); Redes Neurais tiveram maior grau (15), seguidas por SVM (12) e Random Forest (11). A modularidade (Q = 0,62) indicou três comunidades (Seção 3.4).

### 2.8.3 Análise Temporal

Correlação de Spearman e LOESS ilustraram crescimento do campo e adoção tecnológica.

**Figura 2.** Diagrama PRISMA de identificação, triagem e inclusão.

![Diagrama PRISMA](2-FIGURAS/2-EN/prisma_flowdiagram.png){#fig:prisma2020 width="80%"}

A triagem automatizada atingiu precisão temática de 94,2%, superando o limiar de 85%. A reprodutibilidade de 100% entre execuções, com κ = 0,89, indica que os achados refletem fielmente o estado da arte [@OforiBoateng2024]. A avaliação manual obteve ICC = 0,87 (IC95%: 0,84–0,91), confirmando robusta confiabilidade interavaliadores [@streiner2008health].

# 3. Resultados e Discussão

## 3.1 Síntese crítica das aplicações de ML em IGs

A integração de ML às IGs representa mudança de paradigma na certificação territorial. A partir de 148 estudos (2010–2025), ML se destaca em captar assinaturas ambientais (espectrais, elementares, isotópicas), mas falha em transformá‑las em sistemas de certificação socialmente resilientes. Com base na teoria de capacidades dinâmicas [@Teece2007], argumentamos que ML amplia a capacidade de “detectar” com dados de alta dimensão, porém negligencia “aproveitar” valor de forma equitativa e “transformar” instituições para enfrentar vulnerabilidades ecológicas e sociais.

Supervisionados dominam a discriminação de origem, com Random Forest e SVM prevalecendo em espectroscopia e cromatografia (vinhos, carnes, chás) [@Xu2021; @Mohammadi2024; @Chen2020], atingindo 80%–100% em ambientes controlados [@Ramos2025; @Li2025]. CNNs emergem para hiperespectral [@Peng2025; @Feng2025]. PLS‑DA e PCA permanecem basais na quimiometria [@Rebiai2022].

Há concentração de 72% em produtos europeus/asiáticos (vinhos 34%, chás 18%, azeites 8%), com sub‑representação do Sul Global. O crescimento temporal é exponencial (ρ = 0,89, p < 0,001), com Deep Learning de 5% (2010–2015) para 28% (2020–2025). Entretanto, quedas de 2%–15% sob deslocamentos espaciais evidenciam sobreajuste e frágil generalização [@Kuhn2013; @Effrosynidis2021]. Apenas 23% executam validação externa. Sob uma leitura schumpeteriana [@Schumpeter1934], inovações de “detecção” são disruptivas, mas a difusão é travada por silos de dados e algoritmos proprietários, reforçando assimetrias Norte‑Sul [@Wang2025].

Na “captura de valor”, SVM e KNN destacam‑se em detecção de fraude em mel e azeites [@Mohammadi2024; @Isangediok2022Fraud]; regressão prediz acidez e antioxidantes [@Meena2024; @Liu2025]. Porém, impactos assimétricos sobre pequenos produtores são subestimados [@Iranzad2025]. Híbridos Blockchain‑ML avançam a rastreabilidade descentralizada [@Gong2023; @Wang2025], ainda incipientes (21%).

Na “transformação”, persiste déficit de interpretabilidade (14% usam SHAP/LIME) [@Effrosynidis2021; @Lundberg2017], o que dificulta defensibilidade legal [@He2024]. Três módulos tecnológicos foram identificados — Árvores + Espectroscopia; SVM/KNN + Cromatografia; Redes Neurais + Sensores — mas revelam fragmentação e baixa transferência cruzada [@Blondel2008; @Chen2020]. À luz de Berkes [@Berkes2003], ML deve fomentar governança adaptativa, integrando comunidades e monitoramento ambiental. Modelos são ecologicamente precisos, porém socialmente estéreis [@Huera-Lucero2025]. Validação longitudinal é rara (6%), ignorando variabilidade temporal sob mudanças climáticas [@Kamilaris2018].

## 3.2 Evolução temporal: registro de produtos e mudanças algorítmicas

A evolução temporal de produtos registrados (Figura 3a) mostra padrões distintos: vinhos mantêm representação consistente (picos em 2021 e 2023; total 14), mel cresce entre 2021–2024 (12), azeite é esporádico porém constante (6), queijo e café são sub‑representados (4 e 1). Spearman confirmou tendência ascendente para vinhos (ρ = 0,615; p = 0,011), refletindo expansão pós‑2020 com maior acesso a ferramentas de ML e instrumentação analítica [@Liakos2018].

Nos algoritmos (Figura 3b), PLS‑DA (dominante até 2018) cede espaço a Random Forest e SVM (a partir de 2019). Adoção com forte correlação temporal: SVM (ρ = 0,788; p < 0,001) e Random Forest (ρ = 0,677; p = 0,004). Em 2020–2025, Redes Neurais lideram (33), seguidas por SVM (32) e Random Forest (21). Pós‑2022, DL/CNNs avançam para dados hiperespectrais e não estruturados [@Lavine2005; @Shah2019].

Distribuição regional permanece estável (72% Europa/Ásia), com leve avanço do Sul Global (18% → 22%).

**Figura 3.** Evolução temporal de (a) produtos IG registrados por categoria (Vinho, Mel, Azeite, Café, Queijo) e (b) adoção dos principais algoritmos de ML em estudos de IG.

![Evolução temporal de publicações e algoritmos](2-FIGURAS/2-EN/evolucao_temporal.png){#fig:temporal_evolution width="90%"}

## 3.3 Paisagem algorítmica e desafios metodológicos

Random Forest, SVM e PLS‑DA dominam dados de alta dimensão (espectroscopia/cromatografia) [@Xu2021; @Mohammadi2024; @Rebiai2022], oferecendo importância de variáveis interpretável [@Lundberg2017]. A opacidade de DL ameaça a defensibilidade legal [@He2024]. PCA e seleção de atributos (Boruta) mitigam sobreajuste, mas não corrigem vieses de dados e paradigmas coloniais [@Zhang2025MRF]. Em laboratório, acurácias de 80%–100%; em validação externa, quedas de 2%–15% [@Kuhn2013; @Effrosynidis2021]. A lacuna é epistemológica: modelos estáticos ignoram terroir dinâmico sob clima [@Iranzad2025].

Três lacunas estruturais: generalização espacial/temporal, interpretabilidade + mitigação de vieses, integração socioecológica. Dados: 6% longitudinal, 14% explicabilidade, 12% transferência entre regiões. Redes revelam três módulos (densidade 0,53–0,68) com baixa transferência. O crescimento do campo não se converte em impacto regulatório por confinamento acadêmico @Liakos2018.

## 3.4 Famílias tecnológicas e aplicações

A MCA (Figura 4) explica 45,2% da variância em três dimensões (Europa vs. Ásia; espectroscopia vs. cromatografia; supervisionado vs. não supervisionado).

**Figura 4.** Biplot da MCA: produtos, algoritmos e técnicas. Dimensão 1 separa produtos europeus de asiáticos; Dimensão 2 contrasta métodos espectroscópicos e cromatográficos.

![Biplot MCA de associações tecnológicas](2-FIGURAS/2-EN/mca_biplot.png){#fig:mca_biplot width="90%"}

Vinhos convergem com Random Forest e NIR (0,85; 0,32), enquanto chás se associam a SVM e GC‑MS (‑0,67; 0,91). Tais famílias tecnológicas sustentam arquiteturas funcionais para: (i) discriminação de origem; (ii) detecção de fraude com prioridade à sensibilidade; (iii) rastreabilidade com blockchain; (iv) controle preditivo de qualidade; e (v) modelagem de preferência do consumidor [@Salam2021; @Wang2025; @Meena2024]. Contudo, o enrijecimento de silos (ex.: SVM + NIR em mel) limita inovação cruzada [@Blondel2008].

## 3.5 Direções futuras e implicações de política

Lacunas críticas: *transfer learning* (12%), validação longitudinal (94% ausente) e interpretabilidade (14%) [@Chen2020; @Kamilaris2018]. Fusão multimodal cresce (28% em 2024–2025), enquanto blockchain ainda é incipiente (9%). Dispositivos portáteis pedem compressão de modelos [@Effrosynidis2021]. Pesquisas futuras devem integrar dimensões socioecológicas e co‑desenvolver modelos com comunidades [@Berkes2003].

### 3.5.1 Implicações para política e governança ambiental

ML pode viabilizar “auditabilidade de serviços ecossistêmicos” \cite{Vandecandelaere2018, Belletti2017}. Ao correlacionar assinaturas químicas com variáveis ambientais, verifica práticas sustentáveis [@Camin2017], tornando o selo IG um certificado verificável de conformidade — essencial contra greenwashing [@Aprile2012, @Teuber2011].

Propõe‑se migrar de avaliações sensoriais subjetivas para a integração formal de modelos preditivos validados em normas técnicas [@Granato2018], com mandatos de transparência algorítmica que assegurem critérios biologicamente e geograficamente plausíveis [@Rudin2019, @Broadhurst2018]. A escalabilidade requer repositórios públicos (bibliotecas espectrais/metabolômicas) para validação cruzada e modelos regionais robustos [@Coelho2023], sobretudo no Sul Global [@Kshetri2014].

Agências podem usar algoritmos para monitorar conformidade ambiental em larga escala [@Weiss2020]. Em Amazônia e Cerrado, modelos treinados com sensoriamento remoto e amostras de produtos funcionam como triagem inicial [@Osco2021, @Gomes2023], sinalizando anomalias para inspeção in loco e reduzindo custos [@Liakos2018].

Para certificação, apenas 23% validam com amostras de regiões fora do treinamento; quedas de até 15% [@Chen2020; @Effrosynidis2021; @Kuhn2013] exigem validação espacialmente independente. Modelos inerentemente interpretáveis (Random Forest com importância de variáveis; PLS‑DA com loadings) equilibram acurácia e explicabilidade, viabilizando marcadores territoriais em normas. O foco em Europa/Ásia (72%) abre oportunidades no Brasil (café, queijo, cachaça, cacau) [@Li2025; @Frigerio2024]. A consolidação requer infraestrutura laboratorial, competências em ciência de dados e governança, integrando conhecimento das comunidades com evidência computacional [@Huera-Lucero2025].

# 4. Conclusões

O campo transita da discriminação geográfica para a auditoria ambiental de precisão. ML valida a integridade do terroir e detecta fraudes com alta acurácia, mas ainda enfrenta barreiras de validação, interpretabilidade e governança.

As escolhas algorítmicas refletem restrições informacionais/regulatórias. Predominam validações in silico; faltam testes longitudinais e espaciais, fragilizando a robustez legal. É necessária mudança de paradigma priorizando explicabilidade e reprodutibilidade.

No Sul Global, metodologias devem ser adaptadas aos contextos e à biodiversidade, com equidade e governança na distribuição de benefícios do conhecimento territorial. O sucesso será medido não apenas pela acurácia, mas pela capacidade de fortalecer a soberania epistêmica e conservar os recursos naturais que sustentam a tipicidade.

# Agradecimentos

Agradecemos à Universidade Federal de Sergipe (UFS), à Universidade Estadual de Feira de Santana (UEFS) e ao Instituto Federal de Sergipe (IFS) pelo apoio institucional e infraestrutural.

# Conflitos de Interesse

Os autores declaram não haver conflitos de interesse.

# Declaração de Disponibilidade de Dados

O conjunto de dados completo, incluindo corpus bibliográfico, scripts e resultados intermediários, está disponível no OSF em: <https://doi.org/10.17605/OSF.IO/2EKYQ>.

# Declaração de Ética

Esta revisão não envolve participantes humanos, experimentos com animais, linhas celulares ou coleta de espécimes. Não houve necessidade de aprovação ética.

# Posicionalidade/Envolvimento Comunitário

Quando pertinente, perspectivas de organizações de produtores e certificadores informaram a interpretação de restrições práticas; nenhuma informação identificável foi incluída.

# Referências

::: {#refs}
:::

### Tabela A.3: Módulos Tecnológicos Identificados pela Análise de Comunidade Louvain

| **Módulo** | **Algoritmos Principais**                 | **Técnicas Analíticas**               | **Produtos**         | **Região Predominante** |
| :---------------: | :---------------------------------------------- | :-------------------------------------------- | :------------------------- | :----------------------------- |
|   **M1**   | Random Forest, Decision Tree, Gradient Boosting | Espectroscopia (NIR), Quimiometria            | Vinho, Mel                 | África, Europa                |
|   **M2**   | SVM, KNN                                        | Cromatografia (GC-MS, LC-MS, HPLC)            | Carnes, Produtos Regionais | Ásia                          |
|   **M3**   | Neural Networks, CNN, Deep Learning             | Espectroscopia (NIR, FTIR), Sensores (e-nose) | Azeite, Queijo, Chá       | Europa, Ásia                  |

*Fonte: Três principais módulos tecnológicos identificados pela análise de comunidade Louvain aplicada à rede de coocorrência entre algoritmos, técnicas analíticas e produtos com indicação geográfica. A densidade interna de cada módulo indica a força das conexões entre seus componentes.*

### Tabela A.4: Famílias Tecnológicas Identificadas pela Análise de Cluster

| **Cluster** | **Produto Principal** | **Técnica Analítica** | **Algoritmo ML** | **Aplicação** | **Região Predominante** |
|-------------|-----------------------|-----------------------|------------------|---------------|--------------------------|
| 1 | Mel | Espectroscopia NIR | SVM, KNN | Autenticação e detecção de fraude | Ásia |
| 2 | Queijo | Espectroscopia NIR | Redes Neurais | Discriminação de origem | Europa |
| 3 | Mel, Carnes | LC-MS, GC-MS | SVM, Random Forest, Árvores de Decisão | Autenticação e rastreabilidade | Ásia, Europa |

*Fonte: Dez clusters identificados pela análise de cluster (k-means e hierárquica) baseada em produto, instrumento analítico, algoritmo e tipo de aplicação. Apenas os três clusters mais notáveis são detalhados aqui.*
