---
title: "Machine Learning para Indicações Geográficas: Uma Revisão de Escopo sobre Autenticação, Certificação e Ecossistemas de Dados Abertos"
author: "Catuxe Varjão de Santana Oliveira, Paulo Roberto Gagliardi, Luiz Diego Vidal Santos, Gustavo da Silva Quirino, Ana Karla de Souza Abud, Cristiane Toniolo Dias"
bibliography: referencias.bib
csl: apa.csl
reference-doc: modelo_formatacao.docx
fig-align: center
table-align: center
lang: pt-BR
---

# Resumo

As Indicações Geográficas (IGs) ancoram a qualidade do produto ao território, necessitando de mecanismos robustos de autenticação. Embora o Machine Learning (ML) ofereça ferramentas poderosas para verificação de origem, o campo carece de uma síntese sistemática de suas aplicações. Esta revisão de escopo mapeia a utilização de ML em IGs, caracterizando algoritmos, matrizes e rigor metodológico em 148 estudos revisados por pares (2010–2025) recuperados da Scopus e Web of Science. A metodologia integrou filtragem semântica automatizada (precisão de 94,2%), avaliação manual de qualidade (ICC = 0,87) e análise estatística multivariada. Os resultados revelam um aumento de 400% na produção de pesquisa desde 2018, agrupando-se em três módulos tecnológicos: Random Forest acoplado à espectroscopia (vinhos), SVM com cromatografia (carnes) e Deep Learning com arranjos de sensores (chás). Apesar das acurácias relatadas de 80–100%, a generalização permanece um gargalo crítico. Apenas 23% dos estudos empregaram validação espacialmente independente, revelando quedas de desempenho de 2–15% e viés de otimismo estatístico generalizado. Concluímos que, embora o ML discrimine efetivamente a origem, a adoção regulatória exige protocolos de validação longitudinal, maior explicabilidade do modelo e governança equitativa para garantir uma integração confiável nas estruturas de certificação.

**Palavras-chave:** Indicações Geográficas; Machine Learning; Inteligência Artificial; Rastreabilidade de Alimentos; Produtos Agroecológicos; Propriedade Intelectual; Justiça Territorial; Revisão de Escopo.

# 1. Introdução

As Indicações Geográficas (IGs) protegem territórios e produtos na economia do conhecimento, concedendo direitos exclusivos sobre bens cuja qualidade, reputação e características decorrem de sua origem geográfica [@Locatelli2008; @WIPO2018]. Fundamentadas na Convenção de Berna [@berna1886] e no Acordo TRIPS [@trips1994], as IGs vinculam territórios produtivos e comunidades locais a nichos de mercado, acoplando a proteção de direitos à preservação do conhecimento tradicional [@Suh2007]. Além de sua função legal, as IGs representam ativos intangíveis estratégicos sob a teoria da Visão Baseada em Recursos (Resource-Based View). Elas atuam como recursos raros, valiosos, inimitáveis e insubstituíveis que sustentam a vantagem competitiva territorial sustentável [@Barney1991]. A apropriação de valor por meio de IGs estende-se além da lucratividade imediata; ela ancora a captura de valor futuro ao alavancar mercados diferenciados e a disposição do consumidor em pagar prêmios por produtos de origem certificada [@Loureiro2002; @VazquezFontes2010].

No Brasil, a Lei da Propriedade Industrial (Lei nº 9.279/1996) regula as IGs, estabelecendo duas categorias de reconhecimento com implicações legais e econômicas distintas: Indicação de Procedência (IP) e Denominação de Origem (DO) [@Brasil1996]. Uma IP refere-se a um nome geográfico renomado pela produção ou fabricação de um produto específico, servindo como um mecanismo de sinalização de origem. Por outro lado, uma DO designa produtos cujas qualidades resultam exclusiva ou essencialmente do meio geográfico, incluindo fatores naturais e humanos. Esta categoria oferece proteção robusta ao vincular diretamente a qualidade ao *terroir* [@MAPA2020].

O Instituto Nacional da Propriedade Industrial (INPI) gerencia o controle de registros, apoiado pelo Ministério da Agricultura, Pecuária e Abastecimento, que implementa políticas para fomento e certificação de produtos agrícolas com identidade territorial [@MAPA2020]. Este marco regulatório alinha-se com a Lei de Inovação (nº 10.973/2004) e o Novo Marco Legal de Ciência, Tecnologia e Inovação (nº 13.243/2016), reconhecendo as IGs como ativos de propriedade intelectual elegíveis para proteção estratégica, valoração e comercialização [@Brasil2004; @Brasil2016].

Produtos artesanais e agroalimentares brasileiros com potencial de IG representam manifestações culturais significativas e oportunidades estratégicas para captura de valor territorial. Pesquisas vinculam as características únicas de produtos regionais ,  como a cerâmica artesanal do Baixo São Francisco ou vinhos especializados ,  a atributos geográficos específicos, incluindo condições edafoclimáticas (solo, clima, altitude) e métodos de produção distintos [@Bureau2018; @Azevedo2011; @Santos2018; @Fonzo2015; @SantosJC2019]. A caracterização territorial, exigida para o reconhecimento de DO sob o Artigo 178 da Lei nº 9.279/1996 [@Brasil1996], exige análises técnicas rigorosas para validar cientificamente a relação entre qualidade e fatores geográficos [@GoncalvesMaduro2020]. Esse requisito levanta uma questão central: como os sistemas de certificação podem validar rigorosa e objetivamente o vínculo entre origem geográfica e qualidade do produto?

As tecnologias de Machine Learning (ML) abordam essa lacuna transformando dados analíticos complexos em conhecimento certificável sobre autenticidade e origem. Diferentemente da análise sensorial tradicional, que depende de expertise humana tácita e sofre de subjetividade e limites de escalabilidade, os algoritmos de ML operam via lógica indutiva ou abdutiva. Eles processam automaticamente dados multidimensionais, identificando padrões não lineares e relações latentes frequentemente perdidas pelas estatísticas clássicas de teste de hipóteses. A capacidade de construir modelos com formas funcionais flexíveis revela estruturas de dados não especificadas pela teoria, fornecendo robustez matemática à certificação territorial [@Ramos2025; @Chen2020].

No contexto de IG, o Machine Learning apoia a autenticação de origem, detecção de fraudes, controle de qualidade preditivo e rastreabilidade total. Ele opera sobre assinaturas químicas, isotópicas, espectrais e geoespaciais que capturam a relação produto-território [@longo2021; @acquarelli2021; @rodrigues2022; @rana2023]. A integração de dados instrumentais de alta dimensão com modelos supervisionados permite a discriminação de origem, identificação de adulteração e estimativa de atributos sensoriais/físico-químicos com precisão atendendo aos padrões de certificação [@Jiang2025; @Peng2025; @Santoma2025; @Li2025; @Wang2025].

A seleção de variáveis e a escolha do algoritmo ,  particularmente Random Forest, SVM, PLS-DA, PCA e métodos de seleção como Boruta e RFE ,  transcendem decisões técnicas para se tornarem componentes da arquitetura regulatória. Eles definem quais marcadores territoriais se qualificam como evidência de autenticidade [@Salam2021; @Malik2023; @Iranzad2025; @Effrosynidis2021; @Loyal2022; @Chen2020; @Rebiai2022].

Apesar do interesse acadêmico e tecnológico atual, nenhuma revisão de escopo sintetiza sistematicamente as evidências científicas disponíveis, identifica as técnicas empregadas, avalia o desempenho em produtos e contextos geográficos ou indica direções futuras de pesquisa. Essa limitação dificulta o desenvolvimento metodológico e a transferência de conhecimento para sistemas de certificação e controle de IGs.

Esta revisão de escopo mapeia sistematicamente as aplicações de Machine Learning em Indicações Geográficas, usando a estrutura PCC (*População, Conceito, Contexto*) para sintetizar evidências científicas sobre a integração de ML com aspectos territoriais. Hipotetizamos que as técnicas de Machine Learning apoiam processos de autenticação, avaliação e tomada de decisão em IGs, revelando padrões metodológicos que consolidam o conhecimento para o desenvolvimento de modelos computacionais em certificação geográfica.

# 2. Materiais e Métodos

Esta revisão de escopo segue as diretrizes PRISMA-ScR (*Preferred Reporting Items for Systematic Reviews and Meta-Analyses extension for Scoping Reviews*) para garantir transparência metodológica e reprodutibilidade. O protocolo está registrado no Open Science Framework para facilitar o acesso público e a replicabilidade.

## 2.1 Questão de Pesquisa

O estudo emprega a estrutura PCC (*População, Conceito, Contexto*) para formular a questão de pesquisa: *Como as técnicas de Machine Learning têm sido aplicadas para autenticação, avaliação e apoio à decisão em sistemas de Indicações Geográficas?*

**Tabela 1.** Estrutura da revisão de escopo de acordo com a estrutura PCC.

| Elemento                  | Descrição                                                                                                                                                                                                                                                                                                                                                                                     |
| :------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **P (População)** | Indicações Geográficas, Denominações de Origem e Indicações de Procedência reconhecidas nacional e internacionalmente, abrangendo produtos agroalimentares (vinhos, queijos, cafés, carnes, azeites), artesanato e outros produtos com identidade territorial.                                                                                                                        |
| **C (Conceito)**    | Machine Learning, Inteligência Artificial, algoritmos de classificação e predição, métodos quimiométricos, Mineração de Dados e Processamento de Linguagem Natural aplicados a contextos de Indicações Geográficas.                                                                                                                                             |
| **C (Contexto)**    | Autenticação de origem geográfica, avaliação de potencial de IG, identificação de determinantes territoriais (solo, clima, métodos de produção), classificação e discriminação de produtos, sistemas de apoio à decisão para certificação, controle de qualidade, rastreabilidade, detecção de fraudes e adulterações, e estratégias de valorização territorial. |

Este estudo identifica e caracteriza aplicações de ML relatadas na literatura, categorizando técnicas por tipo de algoritmo, abordagem metodológica e métricas de desempenho. Além disso, analisa a distribuição de aplicações por tipo de produto, região geográfica e período de tempo, identificando lacunas metodológicas, limitações e direções para pesquisas futuras.

## 2.1.1 Fluxograma Metodológico PRISMA-ScR

A Figura 1 apresenta o fluxograma metodológico, estruturado em quatro fases sequenciais: (1) Estratégias de busca nas principais bases de dados, (2) Filtragem automatizada com sistema de pontuação ponderada, (3) Avaliação manual de qualidade com avaliação multidisciplinar e (4) Análise bibliométrica e síntese qualitativa integrando metodologias quantitativas e documentais. O fluxograma detalha o caminho desde a identificação do registro até a síntese final, oferecendo recomendações para a implementação de Machine Learning em sistemas de Indicações Geográficas.

**Figura 1.** Fluxograma da Revisão de Escopo sobre Aplicações de Machine Learning em Indicações Geográficas.

![](2-FIGURAS/2-EN/ml_indicacoes_geograficas.png){#fig:ml_indicacoes width="80%"}

## 2.3 Estratégia de Busca e Extração de Estudos

As buscas visaram Scopus (Elsevier) e Web of Science (Clarivate Analytics), interceptando três domínios temáticos principais: técnicas de machine learning e inteligência artificial; sistemas de certificação geográfica; e Indicações Geográficas/Denominações de Origem.

Os descritores empregaram terminologia controlada em inglês e operadores booleanos (AND, OR, NOT), cobrindo publicações de 2010 a 2025 para capturar o estado da arte. A estratégia de busca seguiu esta lógica:

*("machine learning" OR "artificial intelligence" OR "deep learning" OR "supervised learning" OR "unsupervised learning" OR "ensemble methods") AND ("geographical indications" OR "denominations of origin" OR "appellations of origin" OR "protected designations of origin") AND ("authentication" OR "traceability" OR "quality control" OR "fraud detection" OR "geospatial analysis")*.

Os critérios de inclusão compreenderam artigos revisados por pares em inglês, português ou espanhol apresentando aplicações de ML em contextos de IG, autenticação de origem ou controle de qualidade territorial. Descritores primários foram exigidos no título, resumo ou palavras-chave. Trabalhos não revisados por pares, estudos sem aplicação prática de ML e aqueles focados exclusivamente em aspectos não territoriais foram excluídos.

A extração de dados utilizou um formulário padronizado para registrar metadados bibliográficos (autor, ano, título), características geográficas (país de origem, região, tipo de IG), detalhes do produto (categoria, denominação específica), abordagem metodológica (algoritmos de ML, técnicas analíticas/instrumentais, tamanho da amostra) e métricas de desempenho (acurácia, sensibilidade, especificidade, RMSE).

## 2.4 Primeira Fase: Sistema Automatizado de Filtragem de Relevância Temática

### 2.4.1 Algoritmo de Pontuação Ponderada

Complementando a triagem manual, um sistema de filtragem automatizado atribui pontuações de relevância temática com base na presença e localização de descritores no título, resumo e palavras-chave. Implementado em Python (NLTK, spaCy), o algoritmo aplica um esquema de ponderação hierárquica a cada termo identificado. O sistema de pontuação adere aos princípios do Processo de Análise Hierárquica (AHP) (Equação 1), organizando descritores em cinco categorias com pesos diferenciados [@SAATY1991].

$$
S_i = \sum_{j=1}^{n} w_j \cdot l_i \cdot f_{ij}
$$

onde:

- $S_i$ = pontuação total do artigo $i$
- $w_j$ = peso associado ao termo $j$ (categorizado em 5 níveis: 5, 3, 2, 1 ou -5/-3/-2 pontos)
- $l_i$ = multiplicador de localização (1,5 para título, 1,2 para palavras-chave, 1,0 para resumo)
- $f_{ij}$ = frequência de ocorrência do termo $j$ no artigo $i$
- $n$ = número total de termos avaliados

Termos Prioritários (5 pontos) representam o núcleo conceitual da revisão (ex: *geographical indications, traceability, authentication*). Termos de Alta Relevância (3 pontos) capturam conceitos metodológicos centrais (ex: *machine learning, deep learning, neural networks*). Termos de Média Relevância (2 pontos) cobrem temas complementares (ex: *chemometrics, data mining*), enquanto Termos de Contexto (1 ponto) indicam ambientes potenciais (ex: *regional products, certification*). Termos de Exclusão recebem pesos negativos para penalizar registros fora do escopo, particularmente nos domínios *médico/clínico* (-5), *planejamento urbano* (-3) e *finanças* (-2) [@MUNN2018; @tricco2018].

### 2.4.2 Implementação e Validação do Algoritmo

Para cada registro, o algoritmo varre o título, resumo e palavras-chave, aplica os pesos da categoria e multiplica cada ocorrência pelo fator de localização. A pontuação final soma esses produtos em todos os termos identificados.

A distribuição empírica da pontuação definiu o limite mínimo de inclusão, identificando o ponto de inflexão na curva cumulativa (critério de Pareto/cotovelo) e ajustando-o via validação manual com amostragem estratificada. O valor final representa o compromisso ideal entre sensibilidade e especificidade, estabilizando a concordância entre avaliadores em casos limítrofes.

### 2.4.3 Validação Participativa e Refinamento do Algoritmo

Para garantir a validade científica, foi implementado um protocolo de validação envolvendo três revisores independentes especializados em machine learning e sistemas de IG. O protocolo incluiu uma revisão manual sistemática de 272 estudos para verificar a aderência aos critérios de inclusão. Um teste de concordância entre avaliadores verificou a consistência da classificação [@Tricco2018].

O processo envolveu investigação qualitativa de casos limítrofes e refinamento iterativo dos critérios de elegibilidade. A validação produziu uma taxa de concordância de 90,2% entre o sistema automatizado e a avaliação manual, indicando alta eficácia algorítmica na triagem temática.

### 2.4.4 Verificação de Cobertura Bibliográfica e Categorização Automatizada

Um sistema automatizado verificou a cobertura bibliográfica, garantindo completude e consistência entre citações textuais e arquivos bibliográficos.

O corpus consolidado passou por categorização automatizada usando Processamento de Linguagem Natural (PLN). Um pipeline computacional extraiu, tokenizou e vetorizou metadados de referência e resumos, usando modelos supervisionados e regras semânticas para reconhecimento de padrões [@Young2019; @Casey2021]. As referências foram classificadas em categorias metodológicas predefinidas, incluindo técnicas de machine learning e sistemas de IG.

Para quantificar a cobertura e a adequação do estudo, foram aplicadas métricas de cobertura de citação e taxas de uso bibliográfico do corpus [@tranfield2003; @webster2002]. Essas métricas permitem a avaliação quantitativa da utilização da base de referência, garantindo que os estudos selecionados reflitam adequadamente o escopo temático da revisão.

## 2.5 Segunda Fase: Avaliação Manual da Qualidade Metodológica

Na segunda fase, três revisores independentes avaliaram a qualidade metodológica dos estudos selecionados, garantindo análise multidisciplinar e reduzindo o viés interpretativo. A escala MMAT [@pluye2009; @hong2018] foi adaptada para estudos interdisciplinares envolvendo ML e sistemas de IG, estruturando oito indicadores em uma escala Likert de 3 pontos. Os indicadores incluíram rigor metodológico, validação de algoritmo, adesão a protocolos éticos, reprodutibilidade, integração quantitativa-qualitativa, impacto nos sistemas de IG, completude da documentação e generalização do método (Tabela 2).

Cada indicador recebeu uma pontuação de 0 a 2: zero para critérios não atendidos ou deficiências substanciais; um para cumprimento parcial com limitações; e dois para cumprimento completo com evidências claras. Uma escala de 3 pontos foi selecionada porque avaliações dicotômicas falham em capturar a complexidade interdisciplinar, enquanto escalas maiores geram inconsistência entre avaliadores [@Likert3vs5_2025].

**Tabela 2.** Indicadores de qualidade metodológica para estudos ML-IG.

| Código | Indicador                                                                     | Domínio                |
| ------- | ----------------------------------------------------------------------------- | ----------------------- |
| RIG     | Rigor metodológico na coleta e processamento de dados territoriais           | Qualidade Territorial   |
| VAL     | Validação técnica de algoritmos com métricas apropriadas                 | Qualidade Computacional |
| ETI     | Adesão a protocolos éticos para pesquisa com comunidades produtoras      | Qualidade Ética        |
| REP     | Reprodutibilidade de experimentos computacionais                             | Qualidade Técnica      |
| INT     | Integração efetiva entre métodos territoriais quantitativos e qualitativos | Qualidade Metodológica |
| IMP     | Impacto e aplicabilidade dos resultados para sistemas de IG                   | Qualidade Social        |
| DOC     | Documentação completa de algoritmos e procedimentos de certificação      | Qualidade Documental    |
| GEN     | Generalização e transferibilidade dos métodos propostos                 | Qualidade Científica   |

### 2.5.1 Procedimentos de Consenso e Validação Interavaliadores

A avaliação manual incluiu um protocolo de consenso. Inicialmente, os revisores avaliaram independentemente uma amostra piloto de 30 estudos (~11% do corpus) para calibrar critérios. Para o corpus completo, casos de discordância (diferença ≥ 2 pontos) passaram por reavaliação cega e discussão para chegar a um consenso. O coeficiente de correlação intraclasse (ICC) foi calculado de acordo com @shrout1979, obtendo um valor de 0,87 (IC 95%: 0,84–0,91), indicando boa concordância.

### 2.5.2 Critérios Específicos para Estudos Interdisciplinares

Dada a natureza interdisciplinar dos estudos, os critérios de qualidade examinaram a coerência da integração quantitativa-qualitativa, validação em múltiplos contextos geográficos, transparência algorítmica, adesão ética e aplicabilidade prática para certificação.

Esta fase resultou na seleção de 25 estudos com qualidade metodológica adequada (pontuação ≥ 20 pontos) dos 272 artigos iniciais. Estes formaram a base para análises subsequentes. A distribuição incluiu 1 artigo de excelência (≥40 pts), 2 de alta relevância (≥30 pts) e 22 adequados (≥20 pts).

## 2.6 Terceira Fase: Análise Bibliométrica

A Lei de Lotka [@lotka1926] analisou a produtividade científica, descrevendo a distribuição não linear da produtividade do autor para identificar padrões de concentração ou dispersão. Análises de acoplamento bibliográfico e cocitação não foram realizadas devido à falta de campos de referência citada nos arquivos bibliográficos disponíveis.

## 2.7 Quarta Fase: Síntese Qualitativa e Integração com Análise Documental

A quarta fase integrou sistematicamente as descobertas com a análise documental de marcos regulatórios para fundamentar recomendações metodológicas.

A síntese final combinou análise qualitativa temática com seleção baseada no princípio de Pareto (80/20), priorizando os 20% melhores artigos por pontuação combinada (40% qualidade metodológica, 35% relevância temática, 25% impacto bibliométrico).

A pontuação combinada final foi calculada usando a Equação 2:

$$
P_{final} = (0.40 \cdot Q_{met}) + (0.35 \cdot Q_{tem}) + (0.25 \cdot Q_{biblio})
$$

Onde:

- $P_{final}$ = pontuação final de seleção
- $Q_{met}$ = qualidade metodológica normalizada (0-1)
- $Q_{tem}$ = relevância temática normalizada (0-1)
- $Q_{biblio}$ = impacto bibliométrico normalizado (0-1)

## 2.8 Análises Estatísticas

Análises estatísticas no R [@RCoreTeam2024] usando RStudio [@RStudioTeam2023] caracterizaram sistematicamente o corpus e identificaram padrões emergentes. A Análise de Correspondência Múltipla (MCA) investigou associações entre variáveis categóricas (algoritmos, produtos, regiões, técnicas analíticas), seguindo @Le2008 e @Greenacre2017, usando `FactoMineR` para extrair as principais dimensões. Subsequentemente, a Análise de Cluster (k-means e hierárquica) usando `FactoMineR` e `factoextra` identificou agrupamentos recorrentes de produto-instrumento-algoritmo, sintetizando as "famílias tecnológicas" discutidas na Seção 3.8.

A análise de rede mapeou coocorrências entre algoritmos, produtos e regiões [@Csardi2006; @Schoch2020]. Usando `igraph` e `ggraph`, um grafo não direcionado foi construído, calculando métricas de centralidade (grau, autovetor, intermediação), e a detecção de comunidade foi realizada com o algoritmo Louvain [@Blondel2008] para identificar módulos temáticos (Seção 3.9).

Séries temporais e o teste de correlação de Spearman [@Spearman1904] analisaram a evolução temporal das publicações (2010–2025) para detectar tendências no volume de estudos e adoção de algoritmos. Visualizações geradas com `ggplot2` usaram suavização LOESS [@Cleveland1979] para ilustrar a dinâmica de crescimento.

Finalmente, modelos preditivos globais avaliaram se variáveis bibliométricas e metodológicas poderiam antecipar pontuações de estudo. Modelos de regressão (OLS, Ridge, Lasso, Random Forest) e modelos de classificação (Regressão Logística, Random Forest) foram estimados usando `caret` e `randomForest` com validação cruzada k-fold estratificada. O desempenho foi avaliado via RMSE e $R^2$ para regressão, e acurácia, precisão, sensibilidade e F1-score para classificação (Seção 3.7).

### 2.8.1 Análise de Correspondência Múltipla (MCA)

A MCA investigou associações entre variáveis categóricas, empregando `FactoMineR` para interpretar relacionamentos conceituais.

### 2.8.2 Análise de Rede

A análise de rede mapeou coocorrências, construindo um grafo não direcionado ponderado onde nós representam entidades e arestas indicam coocorrência. Métricas de centralidade identificaram elementos estruturalmente centrais.

A detecção de comunidade usando o algoritmo Louvain [@Blondel2008] interpretou a estrutura modular resultante como módulos tecnológicos temáticos (Seção 3.9).

### 2.8.3 Análise Temporal

A evolução temporal (2010–2025) foi analisada usando o teste de correlação de Spearman [@Spearman1904] e visualizações `ggplot2` com suavização LOESS [@Cleveland1979] para ilustrar o crescimento do campo e a adoção de tecnologia.

# 3. Resultados e Discussão

## 3.1 Síntese Executiva da Revisão de Escopo

Esta revisão de escopo, estruturada de acordo com as diretrizes PRISMA-ScR (Figura 2), identificou e analisou 272 estudos (140 da Scopus, 132 da Web of Science) publicados entre 2010 e 2025. Após filtragem automatizada e avaliação manual da qualidade metodológica, 148 artigos relevantes foram selecionados. Este processo de seleção sistemática estabeleceu um corpus representativo de aplicações de Machine Learning (ML) em Indicações Geográficas (IGs). Os dados revelam um crescimento recente significativo, com 68% das publicações concentradas no período de 2021–2025. Essa tendência indica uma convergência entre certificação territorial e transformação digital, alinhando-se com padrões globais de inovação em sistemas agroalimentares [@Hu2024].

**Figura 2.** Fluxograma da Revisão de Escopo sobre Aplicações de Machine Learning em Indicações Geográficas.

![](2-FIGURAS/2-EN/prisma_flowdiagram.png){#fig:prisma2020 width="80%"}

A filtragem automatizada via análise semântica e pontuação alcançou uma precisão temática de 94,2%, superando o limite estabelecido de 85%. Essa abordagem de triagem computacional provou ser eficaz para revisões envolvendo grandes volumes bibliográficos, sugerindo que sistemas automatizados calibrados reduzem o viés de seleção e aumentam a reprodutibilidade [@OforiBoateng2024]. A reprodutibilidade de 100% em múltiplas execuções de algoritmos, combinada com uma concordância entre avaliadores de κ = 0,89, garante que essas descobertas reflitam de forma confiável o estado atual da literatura científica neste domínio.

A avaliação manual da qualidade metodológica produziu um coeficiente de correlação intraclasse (ICC) de 0,87 (IC 95%: 0,84–0,91), confirmando robusta confiabilidade entre avaliadores e validando os critérios de inclusão [@streiner2008health]. Esta validação confirma que os estudos selecionados para síntese atendem a rigorosos padrões metodológicos.

## 3.2 Análise Estrutural e Temporal do Corpus Científico

A Análise de Correspondência Múltipla (MCA) mapeou a evolução temporal das aplicações de ML em IGs, examinando as relações entre abordagens metodológicas (algoritmos, instrumentos, aplicações), produtos investigados e períodos de publicação. As duas primeiras dimensões da MCA explicaram 9,59% da inércia total (Dim1: 4,82%, Dim2: 4,77%). Esse valor é consistente com a alta dimensionalidade do corpus (148 estudos, 33 variáveis binárias categóricas) e indica uma estrutura conceitual diversificada (Figura 3).

**Figura 3.** Biplot da Análise de Correspondência Múltipla (MCA) sobre a evolução temporal das aplicações de ML para autenticação de Indicações Geográficas (2010-2025).

![](2-FIGURAS/2-EN/mca_biplot_temporal_completo.png){#fig:mca_temporal width="80%"}

*Nota: Elipses coloridas (intervalos de confiança de 95%) representam três períodos de tempo: 2010–2018 (verde, n=26), 2019–2021 (laranja, n=27) e 2022–2025 (roxo, n=95). Pontos representam estudos individuais, com formas indicando a abordagem metodológica primária: círculos para estudos focados em algoritmos, quadrados para estudos focados em instrumentos/técnicas e triângulos para estudos focados em aplicações. Rótulos de produtos (Vinho, Mel, Azeite, Café) são exibidos acima dos pontos correspondentes.*

A trajetória temporal delineia três fases distintas (Figura 3). O período de 2010 a 2018 representa uma fase de consolidação metodológica, caracterizada por produtos europeus tradicionais (principalmente vinhos) e técnicas espectroscópicas estabelecidas (NIR, FTIR) emparelhadas com algoritmos clássicos como PLS-DA e SVM [@Mohammadi2024; @Rebiai2022]. O período intermediário (2019–2021) marca uma transição, onde a democratização das ferramentas de ML e o acesso a técnicas analíticas avançadas impulsionaram a diversificação de produtos (incorporando chás asiáticos e plantas medicinais) e a adoção gradual de Random Forest e redes neurais [@Liakos2018]. A fase recente (2022–2025), compreendendo 64% do corpus, indica expansão rápida e heterogênea. Este período apresenta aumento nas aplicações de Deep Learning, metabolômica *untargeted*, abordagens multimodais e estratégias de transfer learning [@He2024; @Liu2025; @Wang20218065; @Peng2025; @Feng2025].

**Figura 4.** Análise de Rede de Coocorrência. (a) Rede completa mostrando comunidades temáticas entre algoritmos, produtos e técnicas. (b) Rede focada na coocorrência entre algoritmos de ML e produtos.

![](2-FIGURAS/2-EN/network_centrality_metrics.png){#fig:network_analysiss}

A dinâmica da produção científica (Figura 5a) mostra um crescimento exponencial superior a 400% entre 2018 e 2024, impulsionado por ferramentas de ML acessíveis e técnicas analíticas de alto desempenho [@Liakos2018]. Simultaneamente, uma mudança paradigmática nos algoritmos (Figura 5b) é evidente: métodos quimiométricos clássicos (PLS-DA, dominante até 2018) estão sendo substituídos por modelos com maior capacidade preditiva e flexibilidade (Random Forest, SVM a partir de 2019). Pós-2022, Deep Learning e CNNs emergiram, especificamente para processamento de dados hiperespectrais e não estruturados [@Lavine2005; @Shah2019].

**Figura 5.** Evolução temporal de (a) número de publicações e (b) adoção dos principais algoritmos de Machine Learning em estudos de IG.

![](2-FIGURAS/2-EN/evolucao_temporal.png){#fig:temporal_algoritmos width="80%"}

## 3.3 Domínios de Aplicação, Produtos e Distribuição Geográfica

As aplicações de ML em IGs visam predominantemente produtos agroalimentares, enfatizando bebidas alcoólicas, carnes processadas e bens agrícolas especializados (Apêndice A, Tabela A.1). Essa distribuição reflete a convergência de mercados de alto valor, incidência significativa de fraude e a disponibilidade de métodos analíticos gerando dados multivariados adequados para ML.

Vinhos com denominação de origem protegida (DOP) ,  como os do Douro, Rioja e Bordeaux ,  e chás com IG como Wuyi Rock Tea constituem o domínio de aplicação primário. Nesses estudos, a discriminação de origem baseia-se em *fingerprinting* metabolômico e análise de traços elementares, demonstrando que o perfil químico está intrinsecamente ligado às condições geográficas de produção e ao *terroir* [@Ramos2025; @Xu2021]. Carnes e produtos cárneos (ex: cordeiro regional, presunto Jinhua) formam uma segunda categoria importante, onde a discriminação de origem é baseada em assinaturas elementares e isotópicas processadas por algoritmos como Random Forest e SVM [@Chen2020].

Setores como frutas, vegetais e plantas medicinais expandem essa estrutura. Para frutas e vegetais, o ML rastreia a origem via *fingerprints* metabólicos e perfis nutricionais, testando a hipótese de que assinaturas bioquímicas refletem condições edafoclimáticas específicas [@Luan2020; @Peng2025]. Para plantas medicinais como *Panax notoginseng*, a certificação de origem também está ligada à potência farmacológica, reforçando a conexão entre geografia, composição bioativa e valor econômico [@Feng2025].

Geograficamente, instituições asiáticas, particularmente na China, dominam o cenário de pesquisa, seguidas pela Europa. O Brasil e outras economias emergentes estão menos representados. Essa assimetria reflete o recente investimento chinês em tecnologias de rastreabilidade [@Wang2025] versus a infraestrutura analítica consolidada na Europa. Para o Brasil, essa lacuna representa uma oportunidade estratégica para desenvolver aplicações de ML para proteger e valorizar IGs nacionais.

### 3.3.1 Análise Bibliométrica

A Lei de Lotka aplicada ao corpus revelou uma distribuição de produtividade do autor aproximando-se do padrão esperado ($n \approx 2$). A análise identificou 869 autores únicos: 623 (71,7%) publicaram um único artigo, 152 (17,5%) publicaram dois, enquanto um autor (Li) publicou 28. Isso sugere um campo colaborativo com muitos contribuintes esporádicos e alguns especialistas altamente produtivos, provavelmente em quimiometria ou análise instrumental.

A aplicação do princípio de Pareto (80/20) selecionou os 20% melhores artigos com base em uma pontuação combinada (Equação 6: 40% qualidade metodológica, 35% relevância temática, 25% impacto bibliométrico). A Tabela A.2 (Apêndice A) lista os dez artigos com maior pontuação.

## 3.4 O Ecossistema Algorítmico na Autenticação de IG

O ecossistema algorítmico é diverso, mas estruturado em torno de núcleos tecnológicos específicos. Em vez de fragmentação, essa variedade indica que diferentes matrizes, tamanhos de amostra e contextos regulatórios exigem soluções computacionais personalizadas. Algoritmos de classificação supervisionada dominam, com Random Forest e Support Vector Machines (SVM) respondendo por aproximadamente dois terços das aplicações. Por exemplo, @Xu2021 usaram Random Forest para discriminar a origem do vinho via perfis elementares (acurácia > 95%), enquanto @Mohammadi2024 integraram SVM com um kernel RBF para autenticar azeites usando espectroscopia NIR em um cenário de alta dimensionalidade.

Funcionalmente, esses modelos transformam vetores de características $x$ (intensidades espectrais, concentrações elementares, abundâncias de metabólitos) em decisões de origem geográfica. Em estudos de PLS-DA e SVM, essa transformação frequentemente assume uma função de decisão linear $f(x) = w^\top x + b$, onde a combinação ponderada de variáveis ($w$) cria um "hiperplano territorial" separando regiões. Formulações de alta dimensionalidade, particularmente SVM com kernels não lineares, permitem que limites de decisão capturem relacionamentos complexos entre marcadores químicos e território. Crucialmente, $w$ permanece interpretável como um vetor concentrando os pesos da evidência analítica para cada origem.

A prevalência do Random Forest decorre de sua capacidade de modelar interações não lineares, lidar com classes desbalanceadas e fornecer Medidas de Importância de Variável (VIM) para identificar marcadores territoriais com valor regulatório [@Zhang2025MRF]. Esses modelos operam como comitês de classificadores $h_m(x)$, agregados em uma decisão final $\hat{y}$ [@Cornelio2019VORACE]. @Li2025 utilizaram essa arquitetura para isolar subconjuntos de variáveis químicas que suportam transparentemente alegações de autenticidade geográfica.

Em domínios de imagem ou hiperespectrais, Deep Learning ,  especificamente Redes Neurais Convolucionais (CNNs) ,  é o padrão emergente. @Peng2025 usaram CNNs para classificar chás com IG a partir de imagens hiperespectrais, enquanto @Feng2025 aplicaram arquiteturas profundas para autenticação visual de plantas medicinais. A operação de convolução $(K * X)(i,j)$ permite que filtros extraiam padrões locais, reforçando que a autenticação depende de estruturas espaciais ou espectrais recorrentes codificando o *terroir*, não apenas valores de intensidade pontuais.

Para dados espectrais, a Análise Discriminante por Mínimos Quadrados Parciais (PLS-DA) permanece central, aparecendo em quase metade dos estudos. @Rebiai2022 demonstraram a robustez do PLS-DA contra multicolinearidade e o regime $n < p$ na discriminação de azeites. Ao contrário da PCA, que representa a variância total, o PLS-DA otimiza explicitamente a separação de classes, tornando-o ideal para autenticação de origem.

A redução de dimensionalidade é um tema transversal. A PCA é usada em mais da metade dos estudos para pré-processamento, redução de ruído e visualização. @Ramos2025 aplicaram PCA para condensar variáveis metabolômicas de vinho para modelagem Random Forest. Métodos de seleção de características como RF-RFE e Boruta são empregados em um terço dos trabalhos para identificar subconjuntos de variáveis discriminantes. @Salam2021 mostraram que o Boruta reduziu elementos traço de 80 para 15 em estudos de carne sem perda de desempenho. Essa combinação de redução/seleção e classificadores robustos é essencial para controlar o *overfitting* e definir conjuntos compactos de marcadores territoriais para protocolos oficiais.

A escolha do modelo em IGs não é meramente incremental, mas condicionada pela natureza da matriz, estrutura de dados e requisitos regulatórios. Random Forest, SVM, PLS-DA e CNNs ocupam nichos complementares. A interpretabilidade é um requisito fundamental para a validade legal. Algoritmos que fornecem importância explícita de variáveis (Random Forest, PLS-DA) oferecem uma vantagem crítica sobre modelos "caixa-preta" em contextos regulatórios, facilitando a auditoria científica e reforçando a confiança das partes interessadas [@Lundberg2017; @He2024].

## 3.5 Desempenho Preditivo dos Modelos

Modelos de Machine Learning alcançam desempenho preditivo substancial, com acurácias frequentemente entre 80% e 100%, confirmando que assinaturas geográficas são computacionalmente detectáveis. Para tarefas de regressão (ex: acidez, teor de fenol), a qualidade do ajuste é tipicamente medida por MAE e RMSE.

No entanto, o desempenho é heterogêneo e depende do rigor metodológico. Acurácias de 100% em classificação binária (ex: presunto Jinhua, chá Wuyi Rock) frequentemente refletem alta separabilidade de classes via marcadores únicos [@Chen2020; @Effrosynidis2021]. Tais resultados justificam ceticismo se não acompanhados de validação externa robusta.

Uma faixa de desempenho mais realista para problemas multiclasse (ex: múltiplas denominações de vinho) é 88%–99%. Estudos alcançando alta sensibilidade (>99,3%) frequentemente empregam validação rigorosa como k-fold repetido ou leave-one-out [@Mohammadi2024; @Meena2024]. Na detecção de fraude (54% dos estudos), o desempenho é priorizado via sensibilidade e especificidade para minimizar falsos negativos, frequentemente usando técnicas de balanceamento de classe.

Uma lacuna crítica é a generalização do modelo. Apenas 23% dos estudos empregaram validação externa com amostras de origens geográficas independentes. Quando realizada, a acurácia caiu de 2% a 15%, consistente com a degradação de desempenho em distribuições deslocadas [@Kuhn2013]. Isso sugere que muitos sistemas operam sob otimismo estatístico não controlado. Para defensibilidade legal, modelos de ML devem ser testados em amostras que desafiem sua capacidade de generalização (diferentes safras, regiões, lotes).

Essa falha de validação externa representa não apenas uma limitação metodológica, mas um risco reputacional e econômico substancial para as Indicações Geográficas. Um modelo superestimado pode levar à certificação incorreta de produtos, erodindo a confiança do consumidor no selo de origem e depreciando o valor premium associado ao *terroir* [@He2024]. Em termos econômicos, a exposição de fraudes não detectadas ou falsos positivos pode resultar em litígios, perda de mercado e desvalorização de ativos intangíveis, transformando o otimismo estatístico em uma vulnerabilidade sistêmica que ameaça a sustentabilidade das IGs como estratégia de desenvolvimento territorial.

Na modelagem preditiva global, tarefas de regressão mostraram desempenho modesto (RMSE 11,8–12,5, $R^2$ 0,11–0,14), indicando que prever um índice de qualidade sintético a partir de variáveis bibliométricas é difícil [@Hair2010; @Wang2013]. Por outro lado, tarefas de classificação (alta pontuação vs. outros) mostraram que a Regressão Logística superou o Random Forest (Acurácia 0,69 vs. 0,53), sugerindo que estudos de alta qualidade são distinguidos por padrões relativamente simples e lineares [@Rudin2019]. A Figura 6 destaca essa assimetria.

**Figura 6.** Comparação do desempenho do modelo de regressão e classificação para prever pontuação contínua e categoria de alta pontuação dos estudos.

![](2-FIGURAS/2-EN/model_metricas_comparacao.png){#fig:model_metricas width="80%"}

## 3.6 Aplicações Temáticas Identificadas

A análise temática do corpus revelou cinco arquiteturas funcionais predominantes em aplicações de Machine Learning em Indicações Geográficas, cada uma respondendo a demandas específicas de certificação, controle de qualidade e rastreabilidade. Essas arquiteturas refletem a diversidade de desafios enfrentados na autenticação de produtos com IG, bem como representam uma evolução paradigmática na própria governança da prova de origem [@Zhang2024]. Ao mover a validação territorial de um domínio de expertise tácita e subjetiva para um de evidência computacional auditável, o ML redefine o que constitui "prova de origem", transformando a certificação de um processo empírico em um sistema de verificação algorítmica que integra dados analíticos, conhecimento territorial e marcos regulatórios.

A primeira arquitetura, mais frequente no corpus analisado (79% dos estudos), visa estabelecer a procedência territorial através da análise multivariada de assinaturas analíticas. @Xu2021 fundamentam teoricamente esta aplicação na suposição de que a origem geográfica inscreve *fingerprints* químicos detectáveis, *fingerprints* metabolômicos, assinaturas elementares e perfis isotópicos, que manifestam padrões distintos entre regiões devido a interações gene × ambiente × microbiota específicas de cada *terroir*. Operacionalmente, esses estudos constroem funções de decisão $f(x)$ que particionam o espaço de características em regiões associadas a designações específicas, de modo que cada vetor $x$ de intensidades ou concentrações seja mapeado para uma origem estimada $\hat{y}$. A fronteira entre essas regiões, aprendida a partir de dados rotulados, representa, em termos matemáticos, a noção de prova de origem ao traduzir diferenças físico-químicas em classificações reprodutíveis.

Autores como @Li2025 e @Ratnasekhar2025 demonstraram que *fingerprinting* metabolômico integrado com Random Forest, análise de traços elementares via ICP-MS acoplada com SVM e caracterização isotópica de razões ¹²C/¹³C, ¹⁴N/¹⁵N, ¹H/²H e ³²S/³⁴S processadas por LDA ou PLS-DA constituem as estratégias metodológicas predominantes. @Chen2020 e @Luan2020 relataram acurácias variando de 82% a 99%, com concentração modal entre 90% e 97%, demonstrando que a discriminação de origem computacional não é apenas viável, mas atinge níveis de confiabilidade compatíveis com requisitos formais de certificação em múltiplos contextos territoriais.

A segunda arquitetura funcional, focada na identificação de produtos falsificados, adulterados ou misturados, foi documentada por @Salam2021 e @Loyal2022 como presente em 54% dos estudos, respondendo a desafios econômicos críticos em mercados de alto valor agregado. @Mohammadi2024 categorizaram práticas fraudulentas específicas identificadas como a adição de etanol industrial a bebidas alcoólicas, a mistura de produtos de designação protegida com não protegidos (conhecido como "corte" em vinhos) e a falsificação de processos tradicionais através de envelhecimento artificial versus natural em presuntos. Nesses cenários, os modelos vão além de simplesmente atribuir rótulos de origem e começam a aproximar probabilidades de fraude, a partir das quais um limite de decisão é estabelecido para classificar amostras como suspeitas. A escolha desse limite, frequentemente calibrada por curvas ROC, reflete explicitamente a assimetria de custo entre falsos negativos (fraude não detectada) e falsos positivos (produto autêntico sinalizado incorretamente), deslocando a arquitetura para regimes onde a sensibilidade máxima é priorizada, mesmo ao custo de alguma perda de especificidade.

Em estudos semelhantes, @Salam2021 e @Loyal2022 demonstraram que esta aplicação emprega predominantemente classificação binária (autêntico versus adulterado), frequentemente beneficiando-se de estratégias de balanceamento de classe, *oversampling* de amostras fraudulentas e *undersampling* de amostras autênticas para maximizar a sensibilidade à fraude, priorizando a não ocorrência de falsos negativos. @Chen2020 e @Effrosynidis2021 enfatizam que as métricas de desempenho são preferencialmente relatadas em termos de sensibilidade e especificidade, em vez de acurácia geral, refletindo a criticidade assimétrica de erros onde falhar em detectar fraude tem consequências regulatórias, econômicas e reputacionais substancialmente mais sérias do que classificar erroneamente um produto autêntico como suspeito.

Representando a terceira arquitetura funcional, @Wang2025 identificaram que 31% dos estudos abordam o estabelecimento de continuidade entre o produto final e a origem das matérias-primas, respondendo às crescentes demandas por transparência e responsabilidade em cadeias de suprimentos complexas. @Gong2023 documentaram uma tendência emergente particularmente inovadora neste domínio: a integração de Machine Learning com blockchain, observada em 21% dos estudos de rastreabilidade, onde modelos preditivos são codificados em contratos inteligentes que verificam a autenticidade do lote em cada estágio de distribuição.

Autores como @Wang2025 argumentam que essa arquitetura híbrida ,  algoritmos de ML operando em dados imutáveis de blockchain ,  permite a auditoria computacional da cadeia de suprimentos, reduzindo a fraude intermediária por meio de verificação descentralizada e à prova de violação. @Hu2024 demonstraram uma aplicação prática dessa convergência tecnológica em cadeias de suprimentos de chá chinês, onde sensores IoT capturam dados ambientais durante o processamento e transporte, o ML valida a conformidade com perfis esperados e o blockchain registra permanentemente cada verificação, criando um "passaporte digital" rastreável para o produto.

A análise de cluster (k-means e hierárquica) organizada em torno de variáveis de produto, instrumento analítico, algoritmo e tipo de aplicação revelou a existência de dez clusters bem definidos, sintetizando famílias tecnológicas recorrentes no campo. Entre eles, clusters notáveis incluem um centrado na autenticação e detecção de fraude em mel, combinando espectroscopia NIR com classificadores SVM e KNN, com forte presença de estudos asiáticos; um cluster dominado por queijos europeus, onde redes neurais e espectroscopia NIR são mobilizadas para discriminação de origem; e um conjunto de estudos integrando LC-MS e GC-MS em matrizes como mel e carnes, associados a SVM, Random Forest e métodos baseados em árvores de decisão.

Outro cluster relevante reúne aplicações usando ICP-MS em carnes e produtos cárneos, onde a análise de traços elementares é combinada com algoritmos de classificação para autenticação territorial (Figura 7). Esses agrupamentos mostram que a adoção de técnicas de ML demonstra que instrumentos e algoritmos tendem a se articular em ecossistemas coerentes, onde combinações específicas (ex: RMN + redes neurais em vinhos, FTIR + SVM em azeites) se consolidam como arquiteturas de referência para problemas específicos. Do ponto de vista metodológico, essa estrutura de cluster reforça a existência de caminhos tecnológicos preferenciais, que podem orientar decisões de design experimental em futuras aplicações de ML em Indicações Geográficas [@Qi2021; @Li2025review].

**Figura 7.** Mapa de calor dos perfis de cluster de estudo, mostrando a coocorrência de produtos, instrumentos analíticos e algoritmos de machine learning.

![](2-FIGURAS/2-EN/cluster_heatmap_profiles.png){#fig:cluster_heatmap width="80%"}

A quarta arquitetura funcional, identificada por @Meena2024 e @Liu2025 em 47% dos estudos, emprega ML para prever atributos de qualidade (acidez, índice total de fenóis, capacidade antioxidante, textura, perfil sensorial) com base em dados analíticos obtidos rapidamente. @Peng2025 e @Feng2025 distinguem esta aplicação da autenticação por seu objetivo funcional divergente: em vez de responder se um determinado produto é da origem X, o método busca determinar qual qualidade é esperada desta amostra. Nesses casos, o desempenho é quantificado por coeficientes de determinação ($R^2$), MAE e RMSE, que refletem o desvio médio em unidades fisicamente interpretáveis (ex: g/L, unidades de cor, pontuações sensoriais). @Meena2024 documentaram que a regressão constitui a abordagem predominante neste contexto.

Além disso, @Liu2025 e @Rebiai2022 argumentam que esta aplicação possui valor industrial imediato ao permitir avaliação de qualidade rápida, não destrutiva e padronizada, substituindo análises sensoriais subjetivas ou ensaios químicos demorados por previsões espectrométricas instantâneas calibradas por ML. Nesse cenário, a relação entre erro de predição e incerteza analítica torna-se central; modelos cujo RMSE é da mesma ordem de magnitude que o erro instrumental agregam pouco à prática [@Ozaki2021], enquanto modelos onde o RMSE é substancialmente menor que o desvio típico de métodos convencionais criam efetivamente uma nova camada de controle de qualidade acessível a operações de pequena e média escala [@Ferreira2007; @Todeschini2015].

A quinta arquitetura funcional, embora menos prevalente com 19% dos estudos de acordo com @Ramos2025, emprega ML para elucidar fatores que influenciam a aceitação e preferência do consumidor por produtos com indicação geográfica. @Effrosynidis2021 documentaram que estudos nesta categoria frequentemente empregam Modelagem de Equações Estruturais por Mínimos Quadrados Parciais (PLS-SEM) para modelar relações complexas entre atributos analíticos, características demográficas do consumidor e variáveis comportamentais. @Ramos2025 argumentam que esta aplicação é estrategicamente relevante ao permitir a compreensão de como a indicação geográfica agrega valor percebido, identificando segmentos de consumidores dispostos a valorizar a origem territorial e otimizando estratégias de comunicação que conectam assinaturas analíticas (*terroir*) a atributos valorizados pelos consumidores.

## 3.7 Tendências Metodológicas, Lacunas e Direções Futuras

A segmentação da rede de coocorrência usando o algoritmo Louvain [@Blondel2008] (20 nós, 58 arestas, densidade = 0,305, agrupamento = 0,595) identificou três módulos tecnológicos distintos (Tabela A.3, Apêndice A), destacando a organização do campo de ML em IGs em subcampos especializados. Essa estrutura modular sugere que combinações recorrentes de algoritmos, técnicas analíticas e matrizes alimentares consolidam plataformas metodológicas estáveis.

A arquitetura interna dos módulos (Figura 8) revela padrões estruturantes de coesão e especialização. O Módulo 1 (Árvores + Espectroscopia), com alta densidade interna (0,60), vincula Random Forest, Árvores de Decisão e Gradient Boosting a matrizes como vinho e mel, predominando em *terroirs* africanos e europeus. Essa coesão sinaliza a maturidade de uma plataforma onde classificadores baseados em árvores prevalecem na autenticação via assinaturas espectrais NIR, explorando a modelagem de interações não lineares entre marcadores químicos e origem territorial [@Resce2022; @Oganesyants2024].

No Módulo 2 (SVM/KNN + Cromatografia), observou-se uma arquitetura dispersa (densidade = 0,53), associando SVM e KNN com cromatografia de alta resolução (GC-MS, LC-MS) em carnes e produtos regionais asiáticos. Essa configuração reflete um nicho especializado em metabolômica direcionada e *fingerprinting* cromatográfico, onde a separação física de compostos precede a classificação algorítmica, uma estratégia eficaz para matrizes complexas com perfis voláteis e semivoláteis [@Santoma2025; @Shuai2022].

O Módulo 3 (Redes Neurais + Sensores) demonstrou coesão significativa (densidade = 0,68), integrando Redes Neurais, CNNs e Deep Learning com espectroscopia (NIR, FTIR) e sensores portáteis (e-nose) em azeite, queijo e chá, com foco na Europa e Ásia. Este cluster constitui a fronteira tecnológica do domínio, empregando arquiteturas profundas para processamento de sinais hiperespectrais e dados não estruturados, permitindo autenticação *in-situ* e a democratização da certificação [@Gazeli2020; @Fu2023; @Li2025].

Métricas de centralidade confirmam a função estruturante desses módulos: NeuralNetwork detém a maior centralidade global (grau = 15, intermediação = 0,306), atuando como um conector entre o Módulo 3 e os outros, enquanto SVM (grau = 12) e RandomForest (grau = 11) operam como núcleos dos Módulos 2 e 1. A função de ponte das plataformas cromatográficas se destaca (GCMS intermediação = 0,186; LCMS intermediação = 0,105), interconectando o Módulo 2 ao restante, facilitando fluxos informacionais entre nichos metodológicos e a transição entre paradigmas tecnológicos [@Csardi2006].

**Figura 8.** Estrutura interna dos três módulos tecnológicos identificados pelo algoritmo Louvain. Cada painel mostra as conexões entre algoritmos (vermelho), técnicas analíticas (azul), produtos (verde) e regiões (laranja) dentro de cada comunidade especializada.

![](2-FIGURAS/2-EN/louvain_modules_detailed.png){#fig:louvain_modules width="100%"}

@Luan2020 documentaram que a integração de modalidades de dados distintas (metabolômica, perfil elementar, análise isotópica e sensorial) com algoritmos de *ensemble* está crescendo, representando 28% dos estudos recentes (2024-2025). Essa fusão multimodal reconhece que a origem geográfica resulta de interações complexas entre fatores ambientais e práticas de produção, buscando capturar complementaridades informacionais entre diferentes tipos de dados para aumentar o poder discriminativo e a robustez preditiva.

Uma lacuna metodológica crítica surge no *transfer learning* entre regiões geográficas (Figura @fig:louvain_modules). Poucos estudos foram observados testando modelos treinados em uma região quando aplicados a outras. @Chen2020 e @Ramos2025 documentaram que o *transfer learning*, uma técnica onde o conhecimento adquirido em uma tarefa é reutilizado em outra, surge como uma estratégia em desenvolvimento em 12% dos estudos, especialmente em arquiteturas de Deep Learning. A estratégia oferece a possibilidade de que modelos desenvolvidos para vinhos de Bordeaux possam ser adaptados para vinhos de Rioja com amostras limitadas, reduzindo drasticamente a demanda por dados extensivos específicos da região e permitindo a certificação em territórios com recursos analíticos restritos [@Milojevic2011].

@Effrosynidis2021 identificaram uma ênfase crescente, embora ainda minoritária (14% dos estudos), na explicabilidade do modelo de ML por meio de técnicas como SHAP (SHapley Additive exPlanations) e LIME (Local Interpretable Model-agnostic Explanations). Para sistemas de certificação, a interpretabilidade transcende os requisitos técnicos, constituindo uma necessidade regulatória e social. Certificadores e produtores exigem uma compreensão não apenas de qual origem o modelo prevê, mas quais variáveis específicas ,  quais assinaturas analíticas territoriais ,  sustentam cada previsão. Enquanto o Random Forest fornece naturalmente métricas de importância de variáveis, o SHAP permite a atribuição da contribuição específica de cada característica para cada previsão individual, fornecendo explicabilidade granular no nível da amostra que permite a auditoria científica e legal das classificações [@Lundberg2017; @Chen2024].

@Effrosynidis2021 e @Loyal2022 documentaram uma tendência recente (9% dos estudos, concentrados em 2024-2025) focada na implementação de modelos de ML em dispositivos portáteis ou sistemas *in-situ* para análise rápida de autenticidade em campo ou em pontos de venda. Essa miniaturização computacional requer compressão de modelo, quantização de pesos e arquiteturas leves ,  desafios computacionais substantivos, mas viáveis por meio de redes neurais móveis ou algoritmos simplificados operando em subconjuntos selecionados de variáveis discriminativas, democratizando o acesso à tecnologia de autenticação para operações de pequena escala.

A integração de Machine Learning (ML), blockchain e Internet das Coisas (IoT) surge como uma arquitetura de referência para rastreabilidade distribuída e auditável em cadeias de suprimentos modernas. Nesses modelos, sensores IoT coletam dados ambientais ao longo da cadeia; algoritmos de ML comparam padrões observados com perfis esperados para produtos autênticos; e o blockchain registra transações e verificações de forma imutável e descentralizada, criando trilhas de auditoria robustas [@Gong2023; @Zhou2024; @Agyekum2022; @Zhang2022; @Gupta2024; @Wang2022]. Estudos em sistemas agroalimentares apontam essa convergência como relevante tanto para a conformidade regulatória quanto para responder às demandas de consumidores e produtores por autenticidade e sustentabilidade [@Yang2022; @Sun2023].

Apesar da amplitude dos estudos analisados, a análise do corpus revela lacunas metodológicas e epistemológicas que exigem atenção prioritária para o amadurecimento do campo. Uma limitação crítica, observada em apenas 6% dos estudos, é a ausência de validação longitudinal, que testa a robustez do modelo contra variações interanuais. A estabilidade temporal das assinaturas geoquímicas e metabolômicas é uma suposição fundamental para a certificação; no entanto, a variabilidade climática e edáfica entre safras pode degradar o desempenho preditivo de modelos treinados em um único ciclo sazonal, um desafio conhecido na modelagem agroambiental [@Kamilaris2018]. Sem essa validação temporal, a capacidade de generalização dos modelos permanece incerta, limitando sua confiabilidade para fins regulatórios.

Há também uma falta de reflexão crítica sobre os limites da aplicabilidade do modelo de ML. Apenas uma pequena fração dos trabalhos (8%) discute sistematicamente cenários onde algoritmos podem ser inadequados ou condições sob as quais suas previsões falham. Essa tendência de superestimar as capacidades algorítmicas, sem uma análise robusta de suas incertezas e vieses, pode representar um risco à integridade dos sistemas de certificação [@Lones2021]. Finalmente, a escassez de diretrizes para implementação prática em agências certificadoras (11% dos estudos) evidencia uma lacuna na tradução do conhecimento, dificultando a conversão dos avanços da pesquisa acadêmica em impacto regulatório e operacional efetivo [@Liakos2018].

## 3.8 Implicações para Sistemas de Certificação de Indicação Geográfica

A análise dos 25 estudos selecionados indica que as técnicas de Machine Learning têm o potencial de fortalecer os sistemas de certificação de Indicação Geográfica, mas sua implementação prática ainda é limitada por desafios de validação, interpretabilidade e governança. A heterogeneidade nas taxas de acurácia relatadas (82% a 100%) reflete diferenças no rigor metodológico, tamanho da amostra e contexto de aplicação. Em particular, o fato de que apenas 23% dos estudos relatam validação com amostras de regiões não representadas no treinamento, com quedas de desempenho de até 15% nesses cenários [@Chen2020; @Effrosynidis2021; @Kuhn2013], evidencia que a validação espacialmente independente é uma condição indispensável para que modelos baseados em ML sejam legalmente defensáveis.

Simultaneamente, a crescente complexidade dos algoritmos, especialmente em arquiteturas profundas, intensifica o problema da "caixa-preta". Como apenas 14% dos trabalhos empregaram técnicas de explicabilidade como SHAP ou LIME [@Effrosynidis2021], persiste um descompasso entre o desempenho preditivo e a transparência exigida por reguladores e produtores. A preferência por modelos inerentemente interpretáveis, como Random Forest com análise de importância de variáveis ou PLS-DA com *loadings* explícitos, surge como uma estratégia pragmática para equilibrar acurácia e explicabilidade, permitindo a identificação de marcadores territoriais adequados para incorporação em normas técnicas.

De uma perspectiva geográfica e setorial, a concentração de 72% dos estudos em produtos europeus e asiáticos, como vinhos, chás e azeites, abre uma oportunidade evidente para IGs em países em desenvolvimento, incluindo o Brasil, onde café, queijo, cachaça e cacau podem se beneficiar de metodologias já consolidadas [@Li2025; @Frigerio2024]. A aplicação desses modelos a novas matrizes permitiria transformar IGs em ativos intangíveis estrategicamente gerenciados, em termos da Visão Baseada em Recursos [@Barney1991], embora abordagens de valoração econômica (custo, mercado, renda) ainda não estejam integradas aos modelos computacionais [@WIPO2003; @EUCommission2019].

A consolidação do ML em sistemas de IG requer, finalmente, um ecossistema de suporte articulando infraestrutura laboratorial, competências em ciência de dados e governança de dados. Integrar o conhecimento empírico das comunidades produtoras com evidências computacionais, observado em apenas 3% dos estudos, pode ser relevante para a legitimidade social dos modelos [@Huera-Lucero2025]. No contexto brasileiro, marcos legais como a Lei 15.068/2024 (Lei Paul Singer) podem fomentar a criação de Empreendimentos Econômicos Solidários especializados em ML [@Brasil2024; @Mazzucato2013], desde que acompanhados por redes laboratoriais com protocolos harmonizados [@MAPA2020] e arranjos de governança definindo claramente direitos de propriedade intelectual e mecanismos justos de repartição de benefícios derivados do conhecimento territorial.

# 4. Conclusões

Esta revisão de escopo mapeia a convergência de Machine Learning e certificação de origem, revelando um campo em maturação metodológica. As escolhas algorítmicas refletem atualmente uma ecologia de restrições informacionais e regulatórias, em vez de mero progresso tecnológico.

A predominância de validações *in silico* e a escassez de testes longitudinais e espaciais minam a robustez legal dos modelos, necessitando de protocolos de validação rigorosos.

A integração efetiva em sistemas de certificação requer uma mudança de paradigma que priorize a explicabilidade e a reprodutibilidade em detrimento da pura complexidade arquitetural.

Para o Sul Global, o caminho a seguir envolve o desenvolvimento de metodologias adaptadas aos contextos locais e à biodiversidade, integrando equidade e governança na distribuição dos benefícios do conhecimento territorial.

A fragmentação atual em silos de dados dificulta o avanço; criar repositórios públicos padronizados e bibliotecas espectrais compartilhadas é essencial para permitir a validação cruzada global e garantir a transparência necessária para os sistemas de certificação.

# Financiamento

A publicação deste artigo foi financiada pelo Instituto Federal de Sergipe (IFS), através do Edital nº 29/2025/DPP/PROPEX/IFS.

# Agradecimentos

Os autores agradecem à Universidade Federal de Sergipe (UFS), à Universidade Estadual de Feira de Santana (UEFS) e ao Instituto Federal de Sergipe (IFS) pelo apoio institucional e infraestrutural que possibilitou esta pesquisa.

# Conflitos de Interesse

Os autores declaram não haver conflitos de interesse.

# Declaração de Disponibilidade de Dados

O conjunto de dados completo que suporta os resultados deste estudo, incluindo o corpus bibliográfico, scripts de análise e resultados intermediários, está publicamente disponível no repositório Open Science Framework (OSF) sob o DOI: <https://doi.org/10.17605/OSF.IO/2EKYQ>.

# Referências

::: {#refs}
:::

# Apêndices

## Apêndice A: Tabelas Suplementares

### Tabela A.1: Distribuição de Produtos Agroalimentares com Indicações Geográficas por Categoria

| **Categoria de Produto** | **Exemplos Específicos**                            | **Indicações Geográficas Primárias**                   | **Técnicas de ML Predominantes**    | **Frequência Relativa** |
| ------------------------------ | ---------------------------------------------------------- | ---------------------------------------------------------------- | --------------------------------------- | ------------------------------ |
| Vinhos e Bebidas Alcoólicas   | Vinho tinto, vinho branco, rosé; destilados de frutas; vinagres | Douro, Rioja, Bordeaux, Denominação de Origem Controlada (DOC) | Random Forest, SVM, PLS-DA              | 34%                            |
| Chás                          | Chá Wuyi Rock, Liupao, Oolong, Chá Verde                   | China (Fujian, Zhejiang, Yunnan)                                 | NIR + PLS-DA, GC-MS + ML                | 18%                            |
| Carnes Processadas             | Cordeiro, Presunto, Carne Bovina                           | Jinhua (China), Cordeiro Europeu IGP, Carne Halal                | Análise Elementar + SVM, Deep Learning | 15%                            |
| Frutas e Vegetais           | Cítricos, Cebola Tropea, Frutas Vermelhas                    | Sicília, Calábria (Itália), Várias Regiões                   | Metabolômica + Random Forest, NIR      | 12%                            |
| Plantas Medicinais             | Panax notoginseng (Ginseng), Ervas Medicinais              | Yunnan (China), Regiões da Ásia                                   | Metabolômica Untargeted, CNN           | 8%                             |
| Azeites                        | Azeite Extra Virgem, Azeite de Oliva                                | Região do Mediterrâneo, Itália, Espanha                           | Fingerprinting NIR, SVM                 | 8%                             |
| Mel                            | Mel Floral, Mel Silvestre                                  | Lages (Brasil), Regiões da Europa                                  | Espectrometria Elementar, PLS-DA        | 5%                             |

*Fonte: Distribuição de produtos agroalimentares com Indicações Geográficas por categoria, regiões geográficas associadas, técnicas de Machine Learning predominantes e frequência relativa de estudos no corpus analisado (N=148).*

### Tabela A.2: Artigos Selecionados pelo Princípio de Pareto (80/20)

| **Posição** | **Artigo**        | **Pontuação Combinada** | **Principais Contribuições**                |
| ------------------- | ----------------------- | ------------------------------- | --------------------------------------------------- |
| 1                   | Li et al. (2025)        | 95,2                            | Deep Learning para autenticação de chá chinês |
| 2                   | Wang et al. (2025)      | 92,8                            | Blockchain + ML para rastreabilidade                |
| 3                   | Ramos et al. (2025)     | 90,5                            | Metabolômica untargeted em vinhos                  |
| 4                   | Peng et al. (2025)      | 88,9                            | CNN para imagens hiperespectrais                    |
| 5                   | Jiang et al. (2025)     | 87,3                            | Classificação multi-espectral                     |
| 6                   | Xu et al. (2021)        | 85,7                            | Random Forest em perfis elementares                 |
| 7                   | Chen et al. (2020)      | 84,1                            | SVM em carnes processadas                           |
| 8                   | Mohammadi et al. (2024) | 82,6                            | NIR + PLS-DA em azeites                             |
| 9                   | Rebiai et al. (2022)    | 81,2                            | Espectroscopia em vinhos europeus                   |
| 10                  | Feng et al. (2025)      | 79,8                            | Redes neurais em plantas medicinais                 |

*Fonte: 10 artigos selecionados pelo princípio de Pareto (80/20) no corpus de 148 estudos.*

### Tabela A.3: Módulos Tecnológicos Identificados pela Análise de Comunidade Louvain

| **Módulo** | **Algoritmos Principais**                 | **Técnicas Analíticas**               | **Produtos**         | **Região Predominante** |
| :---------------: | :---------------------------------------------- | :-------------------------------------------- | :------------------------- | :----------------------------- |
|   **M1**   | Random Forest, Decision Tree, Gradient Boosting | Espectroscopia (NIR), Quimiometria            | Vinho, Mel                 | África, Europa                |
|   **M2**   | SVM, KNN                                        | Cromatografia (GC-MS, LC-MS, HPLC)            | Carnes, Produtos Regionais | Ásia                          |
|   **M3**   | Neural Networks, CNN, Deep Learning             | Espectroscopia (NIR, FTIR), Sensores (e-nose) | Azeite, Queijo, Chá       | Europa, Ásia                  |

*Fonte: Três principais módulos tecnológicos identificados pela análise de comunidade Louvain aplicada à rede de coocorrência entre algoritmos, técnicas analíticas e produtos com indicação geográfica. A densidade interna de cada módulo indica a força das conexões entre seus componentes.*
