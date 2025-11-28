---
title: "Digital Terroir A Critical Review of Machine Learning for Environmental Governance in Geographical Indications"
author: "Catuxe Varjão de Santana Oliveira, Paulo Roberto Gagliardi, Luiz Diego Vidal Santos, Gustavo da Silva Quirino, Ana Karla de Souza Abud, Cristiane Toniolo Dias"
bibliography: referencias.bib
csl: apa.csl
reference-doc: modelo_formatacao.docx
fig-align: center
table-align: center
lang: pt-BR
---
# Resumo

As Indicações Geográficas (IGs) operam como sistemas socioecológicos acoplados, onde a tipicidade do produto emerge de interações complexas entre solo, clima e biota. A auditoria desses sistemas demanda métodos analíticos robustos capazes de validar serviços ecossistêmicos e prevenir fraudes. Esta revisão de escopo objetiva analisar como algoritmos de Aprendizado de Máquina (ML) processam assinaturas analíticas (espectrais, elementares e isotópicas) para sustentar a auditoria ambiental, a detecção de fraudes e a prevenção de greenwashing, propondo o conceito de Terroir Digital como mecanismo de governança. Seguindo as diretrizes PRISMA-ScR, realizou-se uma busca sistemática por estudos revisados por pares publicados entre 2010 e 2025. Foram incluídos 148 artigos que aplicaram ML na autenticação de IGs. Embora os algoritmos demonstrem alta acurácia discriminante (80–100%), a predominância de aplicação unitaria de modelos estáticos inviabiliza a operacionalização do "Terroir Digital". A função de Gêmeo Digital Inferencial é comprometida pela ausência crítica de validação longitudinal sob variabilidade climática (94%), testes espacialmente independentes (77%) e explicabilidade algorítmica (86%), limitando a aplicabilidade regulatória. O ML deve evoluir de uma ferramenta de classificação para um mecanismo de auditoria socioecológica verificável. Conclui-se com recomendações para a implementação de protocolos de validação externa rigorosos, repositórios espectrais de acesso aberto e estruturas participativas, visando fortalecer a credibilidade das IGs como instrumentos de conservação da agrobiodiversidade e mitigação climática.

**Palavras‑chave:** Indicações Geográficas; Aprendizado de Máquina; Auditoria Ambiental; Greenwashing; Rastreabilidade; Serviços Ecossistêmicos.
---------------------------------------------------------------------------------------------------------------------------------------------------

# 1. Introdução

As Indicações Geográficas (IGs) transcendem sua função original como propriedade intelectual ao surgir como instrumentos estratégicos para a governança ambiental e a conservação da agrobiodiversidade no Antropoceno [@Belletti2017; @Vandecandelaere2009]. Em um cenário global marcado pela crise climática e pela erosão da biodiversidade, as IGs operam como sistemas socioecológicos que vinculam a qualidade do produto à integridade dos serviços ecossistêmicos do território [@Berkes2003; @Bramley2013]. Elas representam mecanismos para valorizar práticas agrícolas regenerativas e manter paisagens culturais, onde o *terroir* é redefinido não apenas como um atributo sensorial, mas como uma impressão digital do produto e da resiliência climática [@Giovannucci2010; @Fonzo2015].

A regulamentação internacional, fundamentada no Acordo TRIPS e no Regulamento (UE) n.º 1151/2012, estabelece a base jurídica, mas é a capacidade de auditoria ambiental que confere legitimidade contemporânea a esses ativos [@EU2012; @WTO1994]. A distinção entre Indicação Geográfica Protegida (IGP) e Denominação de Origem Protegida (DOP) reflete diferentes graus de dependência dos ciclos naturais, exigindo sistemas de verificação robustos para evitar o *greenwashing* e garantir que o prêmio de mercado financie efetivamente a conservação ambiental [@Locatelli2008; @WIPO2020]. A credibilidade desses selos depende, portanto, da capacidade de comprovar cientificamente que as características do produto derivam de interações ambientais específicas e não replicáveis.

O terroir pode ser compreendido como um sistema socioecológico intrinsecamente acoplado, no qual solo, clima, biota e cultura se articulam por meio de interações não lineares, feedbacks e forte heterogeneidade espacial e temporal, configurando um território onde processos biofísicos e práticas sociais são co-produzidos [@LeFloc2016S]. Essa complexidade sistêmica e a natureza difusa de seus acoplamentos limitam a detecção dos serviços ecossistêmicos que sustentam a tipicidade e o valor do produto por métricas convencionais [@Levin1998ComplexAdaptiveSystems]. Consequentemente, a valoração desses serviços e a governança de bens comuns são fragilizadas, facilitando práticas de greenwashing [@Gale2023]. A ausência de instrumental analítico capaz de decifrar esses acoplamentos sistêmicos compromete o monitoramento e a fiscalização ambiental em biomas extensos, impactando a sustentabilidade em escala global [@Liao2023].

Nesse contexto, o Aprendizado de Máquina (ML) mostra-se uma abordagem computacional intrínseca para a análise de sistemas complexos. Ao processar padrões e relações não-lineares em dados multiescalares, que incluem informações espectrais, isotópicas e metabolômicas, o ML converte a incerteza intrínseca desses sistemas em evidência auditável [@Li2022KGML_ag]. Essa capacidade é fundamental para a governança ambiental e a preservação da soberania epistêmica das comunidades [@Suh2007, @Santos2007Epistemologies]. Em escalas geográficas amplas, o ML torna possível a auditabilidade de serviços ecossistêmicos, estabelecendo uma ligação verificável entre a conformidade ambiental e o prêmio de mercado, e mitigando as assimetrias informacionais que propiciam fraudes e apropriação indevida [@Kshetri2014DigitalDivide].

Contudo, a literatura carece de um framework conceitual unificado que integre as capacidades inferencias do ML com os requisitos regulatórios de certificação ambiental. Esta lacuna limita a tradução de avanços metodológicos em protocolos operacionais para sistemas de Indicação Geográfica, perpetuando a fragmentação entre pesquisa acadêmica e governança territorial.

Neste sentido, esta revisão mapeia sistematicamente as aplicações de Aprendizado de Máquina em Indicações Geográficas, com foco em seu potencial para autenticação ambiental e prevenção de fraudes. A partir da síntese de 148 estudos revisados por pares (2010–2025), propõe-se o conceito de 'Terroir Digital' como framework analítico para operacionalizar a auditoria inferencial de serviços ecossistêmicos. Postula-se que a modelagem dos acoplamentos não-lineares entre variáveis ambientais (genótipo territorial) e assinaturas quimiométricas (fenótipo do produto) pode gerar evidências auditáveis de conformidade ambiental, convertendo alegações difusas de sustentabilidade em dados verificáveis e fundamentando políticas de conservação baseadas no mercado.

# 2. Materiais e Métodos

Esta revisão segue as diretrizes PRISMA-ScR ( Preferred Reporting Items for Systematic Reviews and Meta-Analyses extension for Scoping Reviews ) como uma estrutura de transparência para garantir clareza metodológica e reprodutibilidade. O protocolo está registrado no Open Science Framework para facilitar o acesso público e a replicabilidade.

## 2.1 Questão de Pesquisa

O estudo utiliza a estrutura PCC ( População, Conceito, Contexto ) para formular a seguinte questão de pesquisa: Como as técnicas de Aprendizado de Máquina têm sido aplicadas para autenticação, avaliação e apoio à decisão em sistemas de Indicações Geográficas?

**Tabela 1.** Estrutura da revisão de acordo com o modelo PCC.

| Elemento                  | Descrição                                                                                                                                                                                                                                                                                                                                                                              |
| :------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **P (População)** | Indicações Geográficas, Denominações de Origem e Indicações de Procedência reconhecidas nacional e internacionalmente, abrangendo produtos agroalimentares (vinhos, queijos, cafés, carnes, azeites), artesanato e outros produtos com identidade territorial.                                                                                                                  |
| **C (Conceito)**    | Aprendizado de Máquina, Inteligência Artificial, algoritmos de classificação e predição, métodos quimiométricos, Mineração de Dados e Processamento de Linguagem Natural aplicados a contextos de Indicações Geográficas.                                                                                                                                                   |
| **C (Contexto)**    | Autenticação de origem geográfica, avaliação do potencial de IG, identificação de determinantes territoriais (solo, clima, métodos de produção), classificação e discriminação de produtos, sistemas de apoio à decisão para certificação, controle de qualidade, rastreabilidade, detecção de fraudes e adulterações e estratégias de valorização territorial. |

Este estudo identifica e caracteriza aplicações de aprendizado de máquina (ML) relatadas na literatura, categorizando as técnicas por tipo de algoritmo, abordagem metodológica e métricas de desempenho. Além disso, analisa a distribuição das aplicações por tipo de produto, região geográfica e período, identificando lacunas metodológicas, limitações e direções para pesquisas futuras.

## 2.1.1 Fluxograma Metodológico PRISMA-ScR

A Figura 1 apresenta o fluxograma metodológico, estruturado em quatro fases sequenciais: (1) Estratégias principais de busca na base de dados, (2) Filtragem automatizada com um sistema de pontuação ponderada, (3) Avaliação manual da qualidade com avaliação multidisciplinar e (4) Análise bibliométrica e síntese qualitativa integrando metodologias quantitativas e documentais. O fluxograma detalha o caminho desde a identificação dos registros até a síntese final, oferecendo recomendações para a implementação de Aprendizado de Máquina em sistemas de Indicações Geográficas.

**Figura 1.** Fluxograma de triagem, elegibilidade e síntese para aplicações de aprendizado de máquina em Indicações Geográficas.

![Fluxograma do processo de revisão ML-GI](2-FIGURAS/2-EN/ml_indicacoes_geograficas.png){#fig:ml_indicacoes width="80%"}

## 2.3 Estratégia de Busca e Extração de Estudos

As buscas foram direcionadas ao Scopus (Elsevier) e ao Web of Science (Clarivate Analytics), cruzando três principais domínios temáticos: técnicas de aprendizado de máquina e inteligência artificial; sistemas de certificação geográfica; e Indicações Geográficas/Denominações de Origem.

Os descritores empregaram terminologia controlada em inglês e operadores booleanos (AND, OR, NOT), abrangendo publicações de 2010 a 2025 para capturar o estado da arte. A estratégia de busca seguiu esta lógica:

*("aprendizado de máquina" OU "inteligência artificial" OU "aprendizado profundo" OU "aprendizado supervisionado" OU "aprendizado não supervisionado" OU "métodos de conjunto") E ("indicações geográficas" OU "denominações de origem" OU "denominações de origem protegidas") E ("autenticação" OU "rastreabilidade" OU "controle de qualidade" OU "detecção de fraude" OU "análise geoespacial")* .

Os critérios de inclusão compreenderam artigos revisados por pares em inglês, português ou espanhol que apresentassem aplicações de aprendizado de máquina em contextos de IG (Informação Geográfica), autenticação de origem ou controle de qualidade territorial. Descritores primários eram obrigatórios no título, resumo ou palavras-chave. Trabalhos não revisados por pares, estudos sem aplicação prática de aprendizado de máquina e aqueles focados exclusivamente em aspectos não territoriais foram excluídos.

############ aqui###########
Embora a busca inicial tenha sido ampla, a síntese qualitativa priorizou estudos que estabeleceram ligações explícitas entre marcadores analíticos e variáveis ambientais (por exemplo, composição do solo, padrões de precipitação, altitude), filtrando estudos estritamente focados em processamento industrial. Isso garantiu que a revisão abordasse a auditabilidade dos serviços ecossistêmicos e a validade do conceito de terroir, em vez de se concentrar exclusivamente no controle de qualidade da produção.

A extração de dados utilizou um formulário padronizado para registrar metadados bibliográficos (autor, ano, título), características geográficas (país de origem, região, tipo de IG), detalhes do produto (categoria, denominação específica), abordagem metodológica (algoritmos de aprendizado de máquina, técnicas analíticas/instrumentais, tamanho da amostra) e métricas de desempenho (precisão, sensibilidade, especificidade, RMSE).

## 2.4 Primeira Fase: Sistema Automatizado de Filtragem por Relevância Temática

### 2.4.1 Algoritmo de Pontuação Ponderada

Complementando a triagem manual, um sistema de filtragem automatizado atribui pontuações de relevância temática com base na presença e localização dos descritores no título, resumo e palavras-chave. Implementado em Python (NLTK, spaCy), o algoritmo aplica um esquema de ponderação hierárquica a cada termo identificado. O sistema de pontuação segue os princípios do Processo Analítico Hierárquico (AHP). A Equação (1) organiza os descritores em cinco categorias com pesos diferenciados [@SAATY1991].

$$
S_i = \sum_{j=1}^{n} w_j \cdot l_i \cdot f_{ij}
$$

onde:

- $S_i$ = pontuação total do artigo $i$
- $w_j$ = peso associado ao termo $j$ (categorizado em 5 níveis: 5, 3, 2, 1 ou -5/-3/-2 pontos)
- $l_i$ = multiplicador de localização (1,5 para título, 1,2 para palavras-chave, 1,0 para resumo)
- $f_{ij}$ = frequência de ocorrência do termo $j$ no artigo $i$
- $n$ = número total de termos avaliados

Os termos prioritários (5 pontos) representam a revisão conceitual central (por exemplo, *indicações geográficas, rastreabilidade, autenticação* ). Os termos de alta relevância (3 pontos) abrangem conceitos metodológicos centrais (por exemplo, *aprendizado de máquina, aprendizado profundo, redes neurais* ). Os termos de relevância média (2 pontos) cobrem temas complementares (por exemplo, *quimiometria, mineração de dados* ), enquanto os termos de contexto (1 ponto) indicam ambientes potenciais (por exemplo, *produtos regionais, certificação* ). Os termos de exclusão recebem pesos negativos para penalizar registros fora do escopo, particularmente nos domínios *médico/clínico* (−5), *planejamento urbano* (−3) e *financeiro* (−2) [@MUNN2018; @tricco2018].

### 2.4.2 Implementação e Validação do Algoritmo

Para cada registro, o algoritmo examina o título, o resumo e as palavras-chave, aplica os pesos das categorias e multiplica cada ocorrência pelo fator de localização. A pontuação final soma esses produtos para todos os termos identificados.

A distribuição empírica dos escores definiu o limiar mínimo de inclusão, identificando o ponto de inflexão na curva cumulativa (critério de Pareto/cotovelo) e ajustando-o por meio de validação manual com amostragem estratificada. O valor final representa o equilíbrio ideal entre sensibilidade e especificidade, estabilizando a concordância entre avaliadores em casos limítrofes.

### 2.4.3 Validação Participativa e Refinamento de Algoritmos

Para garantir a validade científica, foi implementado um protocolo de validação envolvendo três revisores independentes especializados em aprendizado de máquina e sistemas GI. O protocolo incluiu uma revisão manual sistemática de 272 estudos para verificar a adesão aos critérios de inclusão. Um teste de concordância interavaliadores verificou a consistência da classificação [@Tricco2018].

O processo envolveu a investigação qualitativa de casos limítrofes e o refinamento iterativo dos critérios de elegibilidade. A validação resultou numa taxa de concordância de 90,2% entre o sistema automatizado e a avaliação manual, indicando elevada eficácia algorítmica na triagem temática.

### 2.4.4 Verificação de Cobertura e Categorização Automatizada

Um sistema automatizado verificou a abrangência bibliográfica, garantindo a integridade e a consistência entre as citações textuais e os arquivos bibliográficos.

O corpus consolidado foi submetido à categorização automatizada usando Processamento de Linguagem Natural (PLN). Um pipeline computacional extraiu, tokenizou e vetorizou metadados e resumos de referência, usando modelos supervisionados e regras semânticas para reconhecimento de padrões [@Young2019; @Casey2021]. As referências foram classificadas em categorias metodológicas predefinidas, incluindo técnicas de aprendizado de máquina e sistemas de informação geográfica.

Para quantificar a abrangência e a adequação dos estudos, foram aplicadas métricas de cobertura de citações e taxas de utilização bibliográfica do corpus [@tranfield2003; @webster2002]. Essas métricas permitem a avaliação quantitativa da utilização da base de referências, garantindo que os estudos selecionados reflitam adequadamente o escopo temático da revisão.

## 2.5 Segunda Fase: Avaliação Manual da Qualidade Metodológica

Na segunda fase, três revisores independentes avaliaram a qualidade metodológica dos estudos selecionados, garantindo uma análise multidisciplinar e reduzindo o viés interpretativo. A escala MMAT [@pluye2009; @hong2018] foi adaptada para estudos interdisciplinares envolvendo aprendizado de máquina e sistemas gastrointestinais, estruturando oito indicadores em uma escala Likert de 3 pontos. Os indicadores incluíram rigor metodológico, validação do algoritmo, adesão ao protocolo ético, reprodutibilidade, integração quantitativa-qualitativa, impacto nos sistemas gastrointestinais, completude da documentação e generalização do método (Tabela 2).

Cada indicador recebeu uma pontuação de 0 a 2: zero para critérios não atendidos ou deficiências substanciais; um para atendimento parcial com limitações; e dois para atendimento completo com evidências claras. Uma escala de 3 pontos foi selecionada porque avaliações dicotômicas não conseguem capturar a complexidade interdisciplinar, enquanto escalas maiores geram inconsistência entre avaliadores [@Likert3vs5_2025].

**Tabela 2.** Indicadores de qualidade metodológica para estudos de ML-GI.

| Código | Indicador                                                                    | Domínio                |
| ------- | ---------------------------------------------------------------------------- | ----------------------- |
| RIG     | Rigor metodológico na coleta e processamento de dados territoriais          | Qualidade Territorial   |
| VAL     | Validação técnica de algoritmos com métricas apropriadas                 | Qualidade Computacional |
| ETI     | Adesão a protocolos éticos para pesquisa com comunidades produtoras        | Qualidade Ética        |
| REP     | Reprodutibilidade de experimentos computacionais                             | Qualidade técnica      |
| INT     | Integração eficaz entre métodos territoriais quantitativos e qualitativos | Qualidade Metodológica |
| IMP     | Impacto e aplicabilidade dos resultados para sistemas gastrointestinais      | Qualidade Social        |
| DOC     | Documentação completa de algoritmos e procedimentos de certificação      | Qualidade Documental    |
| GEN     | Generalização e transferibilidade dos métodos propostos                   | Qualidade Científica   |

### 2.5.1 Procedimentos de consenso e validação entre avaliadores

A avaliação manual incluiu um protocolo de consenso. Inicialmente, os revisores avaliaram independentemente uma amostra piloto de 30 estudos (aproximadamente 11% do corpus) para calibrar os critérios. Para o corpus completo, os casos de discordância (diferença ≥ 2 pontos) foram submetidos a reavaliação cega e discussão para se chegar a um consenso. O coeficiente de correlação intraclasse (CCI) foi calculado de acordo com @shrout1979, obtendo-se um valor de 0,87 (IC 95%: 0,84–0,91), indicando boa concordância.

### 2.5.2 Critérios Específicos para Estudos Interdisciplinares

Dada a natureza interdisciplinar dos estudos, os critérios de qualidade examinaram a coerência da integração quantitativa-qualitativa, a validação em múltiplos contextos geográficos, a transparência algorítmica, a adesão ética e a aplicabilidade prática para certificação.

Esta fase resultou na seleção de 25 estudos com qualidade metodológica adequada (pontuação ≥ 20 pontos) dentre os 272 artigos iniciais. Estes constituíram a base para as análises subsequentes. A distribuição incluiu 1 artigo de excelência (≥40 pontos), 2 de alta relevância (≥30 pontos) e 22 adequados (≥20 pontos).

## 2.6 Terceira Fase: Análise Bibliométrica

A Lei de Lotka [@lotka1926] analisou a produtividade científica, descrevendo a distribuição não linear da produtividade dos autores para identificar padrões de concentração ou dispersão. Análises de acoplamento bibliográfico e co-citação não foram realizadas devido à ausência de campos de referência citados nos arquivos bibliográficos disponíveis.

## 2.7 Quarta Fase: Síntese Qualitativa e Integração com Análise Documental

A quarta fase integrou sistematicamente as conclusões com a análise documental dos quadros regulamentares para fundamentar as recomendações metodológicas.

A síntese final combinou a análise temática qualitativa com a seleção baseada no princípio de Pareto (80/20), priorizando os 20% melhores artigos pela pontuação combinada (40% qualidade metodológica, 35% relevância temática, 25% impacto bibliométrico).

A pontuação combinada final foi calculada usando a Equação (2):

$$
P_{final} = (0,40 \cdot Q_{met}) + (0,35 \cdot Q_{tem}) + (0,25 \cdot Q_{biblio})
$$

Onde:

- $P_{final}$ = pontuação final de seleção
- $Q_{met}$ = qualidade metodológica normalizada (0-1)
- $Q_{tem}$ = relevância temática normalizada (0-1)
- $Q_{biblio}$ = impacto bibliométrico normalizado (0-1)

## 2.8 Análises Estatísticas

As análises estatísticas em R [@RCoreTeam2024] usando o RStudio [@RStudioTeam2023] caracterizaram sistematicamente o corpus e identificaram padrões emergentes. A Análise de Correspondência Múltipla (ACM) investigou associações entre variáveis categóricas (algoritmos, produtos, regiões, técnicas analíticas), seguindo @Le2008 e @Greenacre2017, usando o `FactoMineR` para extrair as principais dimensões. Posteriormente, a Análise de Cluster (k-means e hierárquica) usando o `FactoMineR` e o `factoextra` identificou agrupamentos recorrentes de produto-instrumento-algoritmo, sintetizando as "famílias tecnológicas" discutidas na Seção 3.8.

A análise de rede mapeou as coocorrências entre algoritmos, produtos e regiões [@Csardi2006; @Schoch2020]. Usando `igraph` e `ggraph`, um grafo não direcionado foi construído, calculando métricas de centralidade (grau, autovetor, intermediação), e a detecção de comunidades foi realizada com o algoritmo de Louvain [@Blondel2008] para identificar módulos temáticos (Seção 3.9).

Séries temporais e o teste de correlação de Spearman [@Spearman1904] analisaram a evolução temporal das publicações (2010–2025) para detectar tendências no volume de estudos e na adoção de algoritmos. Visualizações geradas com `ggplot2` utilizaram suavização LOESS [@Cleveland1979] para ilustrar a dinâmica de crescimento.

Por fim, modelos preditivos globais avaliaram se variáveis bibliométricas e metodológicas poderiam antecipar as pontuações dos estudos. Modelos de regressão (OLS, Ridge, Lasso, Random Forest) e modelos de classificação (Regressão Logística, Random Forest) foram estimados usando `caret` e `randomForest` com validação cruzada k-fold estratificada. O desempenho foi avaliado por meio de RMSE e R² para regressão e acurácia, precisão, sensibilidade e pontuação F1 para classificação (Seção 3.7).

### 2.8.1 Análise de Correspondência Múltipla (ACM)

A Análise de Correspondência Múltipla (MCA) investigou associações entre variáveis categóricas, utilizando o software `FactoMineR` para interpretar relações conceituais. A análise revelou três dimensões principais que explicam 45,2% da variância: a Dimensão 1 (28,4%) contrastando produtos europeus (vinhos, queijos) com produtos asiáticos (chás, carnes); a Dimensão 2 (11,3%) separando técnicas espectroscópicas de métodos cromatográficos; e a Dimensão 3 (5,5%) diferenciando algoritmos supervisionados de abordagens não supervisionadas.

### 2.8.2 Análise de Redes

A análise de redes mapeou as coocorrências, construindo um grafo não direcionado ponderado onde os nós representam entidades e as arestas indicam coocorrência. Métricas de centralidade identificaram elementos estruturalmente centrais. O grafo era composto por 58 nós e 142 arestas (densidade = 0,43), com as Redes Neurais apresentando a maior centralidade de grau (15), seguidas por SVM (12) e Floresta Aleatória (11). A análise de modularidade identificou três comunidades com Q = 0,62, representando padrões de especialização tecnológica.

A detecção de comunidades usando o algoritmo de Louvain [@Blondel2008] interpretou a estrutura modular resultante como módulos tecnológicos temáticos (Seção 3.9).

### 2.8.3 Análise Temporal

A evolução temporal (2010–2025) foi analisada usando o teste de correlação de Spearman [@Spearman1904] e visualizações `ggplot2` com suavização LOESS [@Cleveland1979] para ilustrar o crescimento do campo e os padrões de adoção de tecnologia ao longo do período de estudo.

## 2.9 Terroir Digital como Sistema de Auditoria Inferencial

A partir da análise sistemática do corpus bibliográfico, identificou-se que as aplicações de ML em IGs carecem de um framework conceitual que integre capacidades computacionais com requisitos regulatórios de auditoria ambiental. Para preencher essa lacuna, propõe-se o conceito de **Terroir Digital** como sistema de auditoria inferencial derivado empiricamente da revisão.

### 2.9.1 Definição Constitutiva

Terroir Digital designa a reconstrução computacional dinâmica e contínua das interações sistêmicas entre solo, clima, biota e práticas humanas (o genótipo territorial) e a expressão quimiométrica final do produto (o fenótipo), operando como um Gêmeo Digital (*Digital Twin*) inferencial [@Pylianidis2021; @Hensel2021]. Diferentemente da cartografia estática tradicional, que fornece representação pontual do espaço físico, o Terroir Digital correlaciona, em tempo quase real, variáveis ambientais com assinaturas analíticas de alta dimensionalidade, convertendo incerteza ecológica em evidências auditáveis de autenticidade e conformidade ambiental [@Guerena2024; @Nasirahmadi2022].

Essa formulação dialoga com o arcabouço de Gêmeos Digitais aplicado a agroecossistemas [@Pylianidis2021] e com o entendimento de terroir como acoplamento socioecológico [@Bramley2013; @LeFloc2016S], integrando inferência computacional com fundamentos territoriais. O conceito estabelece vínculo auditável entre produto e serviços ecossistêmicos [@Vandecandelaere2018FAO; @Belletti2017GeographicalIndications], transformando a identidade do lugar em hipótese testável e matematicamente verificável.

### 2.9.2 Critérios Operacionais de Validação

Para reconhecimento técnico como Terroir Digital, um sistema computacional deve atender aos seguintes critérios operacionais, derivados das lacunas metodológicas identificadas na revisão:

1. **Robustez de Validação**: Demonstrar desempenho consistente mediante:
   - Validação espacialmente independente com particionamento geográfico [@Kuhn2013]
   - Séries temporais longitudinais representativas de variabilidade climática interanual
   - Testes de transferência entre safras, lotes e regiões comparáveis

2. **Transparência Algorítmica**: Implementar métodos de Inteligência Artificial Explicável (XAI) [@Lundberg2017; @Rudin2019]:
   - Identificação de marcadores territoriais com plausibilidade físico-química
   - Rastreabilidade das decisões de autenticação até variáveis ambientais causais
   - Rejeição de correlações espúrias sem fundamentação ecológica

3. **Governança de Dados Abertos**: Operar sob padrões FAIR [@Wilkinson2021]:
   - Metadados padronizados permitindo validação cruzada independente
   - Repositórios espectrais/metabolômicos de acesso público
   - Protocolos de amostragem documentados e replicáveis

4. **Auditabilidade Regulatória**: Incorporar mecanismos de verificação:
   - Trilhas de auditoria documentando histórico de inferências
   - Registro imutável de certificações (e.g., blockchain) quando pertinente [@Kshetri2014]
   - Limites de degradação de desempenho previamente definidos e monitorados

### 2.9.3 Aplicação Analítica do Framework

O framework Terroir Digital foi empregado nesta revisão como lente analítica para avaliar a maturidade metodológica dos estudos. Cada publicação foi examinada quanto à conformidade com os critérios operacionais, permitindo identificar:

- Proporção de estudos com validação espacial/temporal adequada (Critério 1)
- Adoção de métodos XAI para interpretabilidade (Critério 2)
- Disponibilidade de dados/protocolos em repositórios abertos (Critério 3)
- Implementação de sistemas de auditoria contínua (Critério 4)

Essa abordagem possibilitou quantificar as lacunas entre o estado atual da literatura e os requisitos para operacionalização de sistemas de auditoria inferencial em IGs, fundamentando as recomendações metodológicas apresentadas nas conclusões.

**Figura 2.** Diagrama de fluxo no estilo PRISMA para identificação, triagem e inclusão.

![Diagrama de fluxo no estilo PRISMA](2-FIGURAS/2-EN/prisma_flowdiagram.png){#fig:prisma2020 width="50%"}

A filtragem automatizada por meio de análise semântica e pontuação alcançou uma precisão temática de 94,2%, superando o limite estabelecido de 85%. Essa abordagem de triagem computacional mostrou-se eficaz para revisões envolvendo grandes volumes bibliográficos, sugerindo que sistemas automatizados calibrados reduzem o viés de seleção e aumentam a reprodutibilidade [@OforiBoateng2024]. A reprodutibilidade de 100% em múltiplas execuções do algoritmo, combinada com uma concordância interavaliadores de κ = 0,89, garante que esses resultados reflitam de forma confiável o estado atual da literatura científica nessa área.

A avaliação manual da qualidade metodológica resultou em um coeficiente de correlação intraclasse (CCI) de 0,87 (IC 95%: 0,84–0,91), confirmando uma robusta confiabilidade interavaliadores e validando os critérios de inclusão [@streiner2008health]. Essa validação confirma que os estudos selecionados para a síntese atendem a padrões metodológicos rigorosos.

# 3. Resultados e Discussão

## 3.1 Panorama das aplicações de aprendizado de máquina em indicações geográficas

A análise de 148 estudos revisados por pares (2010–2025) demonstrou que algoritmos de aprendizado supervisionado constituíram a abordagem predominante para autenticação de origem em sistemas de Indicação Geográfica. Random Forest e Support Vector Machines apresentaram aplicação consolidada em espectroscopia e cromatografia para vinhos, carnes e chás, alcançando acurácias de 80–100% em ambientes controlados [@Xu2021; @Mohammadi2024]. Essa predominância de arquiteturas supervisionadas sobre métodos não supervisionados reflete a disponibilidade de conjuntos de dados rotulados e a pressão por métricas de acurácia quantificáveis, conforme documentado por @Liakos2018 em análise sobre tendências de Machine Learning na agricultura de precisão. Redes Neurais Convolucionais emergiram especificamente para processamento de dados hiperespectrais, enquanto PLS-DA manteve relevância no pré-processamento quimiométrico [@Peng2025; @Feng2025; @Rebiai2022], estabelecendo um paradigma instrumental que favorece produtos de alto valor agregado (vinhos, azeites) em detrimento de matrizes alimentares complexas.

A distribuição geográfica dos estudos apresentou concentração em produtos europeus e asiáticos (72%), com vinhos representando 34%, chás 18% e azeites 8% do corpus. Essa concentração revela assimetrias epistêmicas, onde sistemas de IG consolidados recebem maior atenção científica, enquanto produtos do Sul Global permanecem sub-representados, perpetuando desigualdades no acesso a ferramentas de autenticação e proteção de mercado. A análise temporal demonstrou crescimento substancial das publicações (ρ de Spearman = 0,89, p < 0,001), com adoção de Deep Learning aumentando de 5% (2010–2015) para 28% (2020–2025). Contudo, essa expansão metodológica não foi acompanhada por infraestrutura de validação adequada: a ausência de validação longitudinal em 94% dos estudos significa que modelos treinados em safras específicas tornam-se obsoletos sob variabilidade climática, impossibilitando sua função como sistemas de auditoria ambiental contínua [@Iranzad2025].

A generalização dos modelos apresentou limitações documentadas. Apenas 23% dos estudos empregaram validação espacialmente independente, com quedas de desempenho de 2–15% sob deslocamentos de distribuição [@Kuhn2013; @Effrosynidis2021], demonstrando sobreajuste a contextos locais. Esse comportamento é consistente com observações de @Kuhn2013 sobre a importância de validação cruzada espacial em modelos preditivos ambientais. A explicabilidade algorítmica, medida pela adoção de SHAP ou LIME, ocorreu em apenas 14% dos estudos [@Lundberg2017; @He2024], comprometendo a auditabilidade regulatória: órgãos certificadores exigem rastreabilidade das decisões algorítmicas, incompatível com modelos "caixa-preta" de Deep Learning.

A detecção de fraudes empregou predominantemente classificação binária, onde SVM e KNN integraram dados multimodais para estimar probabilidades de adulteração em mel e azeite [@Mohammadi2024; @Isangediok2022Fraud]. Essa abordagem dicotômica (autêntico/fraudulento) ignora adulterações parciais e zonas de transição geográfica, onde produtos limítrofes apresentam características híbridas não capturadas por esquemas de IG tradicionais. Modelos de regressão predisseram atributos de qualidade como acidez e capacidade antioxidante, oferecendo alternativas não destrutivas aos ensaios laboratoriais [@Meena2024; @Liu2025]. Tecnologias híbridas de blockchain e ML apareceram em 21% dos estudos de rastreabilidade [@Gong2023; @Wang2025], representando tentativa de resolver o paradoxo da confiança digital: blockchains garantem imutabilidade dos registros, mas não a veracidade dos dados de entrada. Modelos de ML funcionam como "oráculos" que traduzem assinaturas químicas em certificados criptográficos, mas sua adoção permanece limitada por custos computacionais e falta de interoperabilidade entre consórcios de certificação.

A análise de redes identificou três módulos tecnológicos com densidade de 0,53–0,68, evidenciando compartimentalização metodológica. Redes Neurais apresentaram maior centralidade de grau (15), seguidas por SVM (12) e Random Forest (11), com modularidade Q = 0,62 indicando especialização por produto-instrumento-algoritmo [@Blondel2008; @Chen2020]. Essa compartimentalização limita a transferência de conhecimento interdisciplinar: conhecimento gerado em um módulo produto-algoritmo-instrumento não se transfere para outros domínios, problema agravado pela convergência em torno de espectroscopia NIR e cromatografia GC-MS como técnicas analíticas padrão.

## 3.2 Evolução temporal de produtos e algoritmos

A análise temporal dos produtos registrados demonstrou padrões distintos entre categorias de IG. Vinhos mantiveram representação constante com 14 produtos (2010–2025), apresentando picos em 2021 e 2023 (3 registros cada). Mel demonstrou crescimento concentrado em 2021–2024 (12 registros), enquanto produtos à base de azeitona apresentaram distribuição esporádica (6 no total). Queijo e café permaneceram sub-representados (4 e 1 registros, respectivamente). A correlação de Spearman confirmou tendência ascendente para vinhos (ρ = 0,615, p = 0,011), indicando expansão sistemática após 2020 [@Liakos2018]. Essa consolidação de vinhos como categoria dominante reflete tanto a maturidade dos sistemas de IG europeus quanto a disponibilidade de dados espectrais padronizados, contrastando com a fragmentação observada em categorias emergentes como café, onde a heterogeneidade de métodos de processamento dificulta a criação de assinaturas químicas universais.

A adoção algorítmica apresentou transição mensurável. PLS-DA, dominante até 2018, foi progressivamente substituída por Random Forest e SVM a partir de 2019, acompanhando a disponibilidade de bibliotecas de ML de código aberto (scikit-learn, caret) e o aumento da capacidade computacional [@Lavine2005]. A análise de correlação temporal demonstrou mudanças significativas para SVM (ρ = 0,788, p < 0,001) e Random Forest (ρ = 0,677, p = 0,004). Redes Neurais constituíram a técnica mais adotada em 2020–2025 (33 aplicações), seguidas por SVM (32) e Random Forest (21). Deep Learning e CNNs emergiram após 2022 especificamente para processamento de dados hiperespectrais [@Shah2019], embora sua opacidade interpretativa limite a adoção em contextos regulatórios. A distribuição regional manteve estabilidade, com 72% dos estudos concentrados em Europa e Ásia. A representação do Sul Global aumentou marginalmente de 18% para 22% no período analisado, sugerindo barreiras persistentes relacionadas a infraestrutura laboratorial e acesso a financiamento científico.

**Figura 3.** Evolução temporal de (a) produtos com Indicação Geográfica (IG) registrados por categoria (Vinho, Mel, Azeitona, Café, Queijo) e (b) adoção dos principais algoritmos de Aprendizado de Máquina em estudos de IG.

![Evolução temporal de publicações e algoritmos](2-FIGURAS/2-EN/evolucao_temporal.png){#fig:temporal_evolution width="90%"}

## 3.3 Limitações metodológicas e desafios de generalização

Os modelos demonstraram alta precisão (80–100%) em ambientes laboratoriais, mas validação externa revelou quedas de 2–15%, expondo limitações de generalização [@Kuhn2013; @Effrosynidis2021]. Random Forest, SVM e PLS-DA dominam o processamento de dados de alta dimensionalidade provenientes de espectroscopia e cromatografia, fornecendo importância de características interpretável [@Xu2021; @Mohammadi2024; @Rebiai2022], característica essencial para identificar marcadores químicos específicos do terroir. A opacidade do Deep Learning, contudo, limita sua adoção em contextos regulatórios que exigem explicação de marcadores territoriais [@He2024], criando um trade-off entre acurácia e auditabilidade que ainda não foi resolvido pela comunidade científica.

Modelos treinados em conjuntos de dados estáticos não capturaram mudanças dinâmicas do terroir sob alterações climáticas, comprometendo a confiabilidade certificatória [@Iranzad2025]. A validação longitudinal, presente em apenas 6% dos estudos, revelou que safras de anos subsequentes podem apresentar desvios de até 20% nas concentrações de compostos fenólicos, tornando obsoletos modelos calibrados em períodos únicos. Essa deficiência é particularmente crítica no contexto de mudanças climáticas, onde fenômenos como ondas de calor e secas extremas alteram irreversivelmente a composição química de produtos perenes.

A análise convergente identificou três deficiências estruturais: generalização espacial e temporal (validação longitudinal em 6% dos estudos), interpretabilidade algorítmica (adoção de XAI em 14%) e testes de transferência inter-regionais (12%). A análise de redes delineou três módulos tecnológicos com densidade 0,53–0,68, evidenciando compartimentalização persistente [@Blondel2008]. A área apresentou crescimento exponencial em publicações, mas os modelos permaneceram confinados a contextos acadêmicos sem tradução para estratégias de conservação operacionais [@Liakos2018], indicando uma lacuna entre a produção científica e a implementação prática em sistemas de certificação.

## 3.4 Famílias Tecnológicas e Aplicações

A Análise de Correspondência Múltipla (Figura 4) de 148 estudos demonstrou associações estruturadas entre variáveis categóricas, explicando 45,2% da variância em três dimensões: a Dimensão 1 (28,4%) contrastou produtos europeus (vinhos 34%, queijos 12%) com produtos asiáticos (chás 18%, carnes 15%); a Dimensão 2 (11,3%) separou técnicas espectroscópicas (NIR, FTIR) de métodos cromatográficos (GC-MS, LC-MS); e a Dimensão 3 (5,5%) diferenciou algoritmos supervisionados (Random Forest, SVM) de abordagens não supervisionadas (PCA, agrupamento). Essa segregação dimensional reflete não apenas diferenças metodológicas, mas também tradições científicas regionais: laboratórios europeus consolidaram espectroscopia NIR para vinhos e queijos, enquanto instituições asiáticas privilegiaram cromatografia de alta resolução para chás, estabelecendo paradigmas analíticos geograficamente específicos.

As coordenadas da ACM demonstraram que vinhos apresentaram convergência com Random Forest e espectroscopia NIR (0,85, 0,32), contrastando com a associação entre chás, SVM e GC-MS (-0,67, 0,91). Essa análise identificou tríades específicas de algoritmo-instrumento-produto que se consolidaram na literatura, evoluindo para arquiteturas funcionais abrangendo discriminação de origem, detecção de fraudes, rastreabilidade blockchain, controle preditivo de qualidade e modelagem de preferências [@Salam2021; @Wang2025; @Meena2024]. A delimitação desses agrupamentos tecnológicos, exemplificada pela aplicação consolidada de SVM e NIR para mel, indicou compartimentalização metodológica que limita inovação interdisciplinar [@Blondel2008], criando "silos de conhecimento" onde avanços em uma tríade não beneficiam outras combinações produto-técnica-algoritmo.

A análise estatística demonstrou que fusão multimodal representou 28% dos estudos recentes (2024–2025), enquanto integração com blockchain permaneceu em 9%. Dispositivos portáteis de ML ofereceram aplicação in situ, mas requereram compressão de modelos para viabilizar democratização do acesso [@Effrosynidis2021]. Essa tendência para miniaturização reflete demandas de produtores rurais por ferramentas de autenticação field-deployable, embora a acurácia de sensores portáteis permaneça 10–15% inferior aos equipamentos laboratoriais, segundo @Meena2024, criando tensão entre portabilidade e confiabilidade metrológica.

## 3.5 Implicações para certificação e governança ambiental

A análise de 148 estudos demonstrou que algoritmos de Aprendizado de Máquina alcançaram acurácias de 82–100% na discriminação de origem de produtos sob condições laboratoriais controladas, confirmando a viabilidade inferencial do ML para autenticação de Indicações Geográficas. No entanto, a heterogeneidade nas taxas de precisão relatadas refletiu variações no rigor metodológico, com apenas 23% dos trabalhos empregando validação espacialmente independente [@Chen2020; @Effrosynidis2021]. Testes externos revelaram quedas de desempenho de 2–15%, indicando superajustamento a contextos locais [@Kuhn2013]. Esse comportamento é análogo ao documentado por @Kuhn2013 em modelos ecológicos, onde a ausência de validação espacial resulta em sobreestimação da capacidade preditiva em até 30%, comprometendo a aplicabilidade prática dos modelos em regiões não contempladas no treinamento.

A ausência de validação longitudinal em 94% dos estudos limitou a aplicabilidade dos modelos sob condições de variabilidade climática [@Iranzad2025]. Modelos treinados em conjuntos de dados estáticos não capturaram a dinâmica temporal do terroir, comprometendo sua função como instrumentos de auditoria ambiental contínua. A concentração geográfica de 72% dos estudos em produtos europeus e asiáticos reforçou essa limitação, restringindo a transferibilidade para regiões com características ambientais distintas. Essa lacuna é particularmente crítica no contexto de mudanças climáticas, onde eventos extremos como secas prolongadas podem alterar permanentemente o perfil de compostos voláteis e minerais, tornando obsoletos modelos calibrados em condições pré-distúrbio.

A explicabilidade algorítmica, medida pela adoção de técnicas como SHAP ou LIME, ocorreu em 14% dos estudos [@Lundberg2017; @He2024]. Modelos de Deep Learning, apesar de apresentarem alta precisão, operaram como sistemas opacos que dificultaram a identificação de marcadores territoriais biologicamente plausíveis. Random Forest, SVM e PLS-DA mantiveram predominância justamente por oferecerem importância de características interpretável [@Xu2021; @Mohammadi2024; @Rebiai2022], requisito fundamental para incorporação em normas técnicas de certificação. A transparência algorítmica não é apenas uma exigência regulatória, mas também um mecanismo de confiança social: produtores e consumidores precisam compreender quais atributos químicos justificam a autenticação, evitando a "caixa-preta" que caracteriza sistemas proprietários.

### 3.5.1 Conformidade com os Critérios do Terroir Digital 

Aplicando os critérios operacionais, a análise revelou déficits críticos na conformidade dos estudos. Quanto à robustez de validação, apenas 23% empregaram validação espacialmente independente, e 6% incluíram séries longitudinais. Quedas de desempenho de 2–15% em testes externos [@Kuhn2013; @Effrosynidis2021] evidenciam superajustamento a contextos locais, inviabilizando a função de Gêmeo Digital adaptativo sob variabilidade climática [@Iranzad2025]. No que concerne à transparência algorítmica, a adoção de XAI ocorreu em apenas 14% dos estudos [@Lundberg2017; @He2024], indicando predominância de modelos opacos incompatíveis com auditoria regulatória. A preferência por Random Forest, SVM e PLS-DA justifica-se pela interpretabilidade, essencial para rastreabilidade de marcadores territoriais [@Xu2021; @Mohammadi2024]. Sob a perspectiva da governança de dados abertos, menos de 8% dos estudos disponibilizaram dados em repositórios públicos conformes aos princípios FAIR [@Wilkinson2021]. Essa fragmentação impede validação cruzada independente e perpetua assimetrias epistêmicas entre regiões com infraestrutura laboratorial consolidada e o Sul Global [@Kshetri2014]. Finalmente, quanto à auditabilidade regulatória, a integração com blockchain apareceu em 21% dos estudos de rastreabilidade [@Gong2023; @Wang2025], mas sem implementação de trilhas de auditoria contínua ou limites de degradação monitorados, comprometendo a confiabilidade certificatória em longo prazo.

A operacionalização do Terroir Digital demanda infraestrutura de governança de dados que endereça essas lacunas. A criação de repositórios públicos, onde bibliotecas espectrais e metabolômicas abertas permitam validação cruzada independente, constitui requisito para democratizar o acesso tecnológico [@Wilkinson2021]. A padronização de metadados viabiliza o desenvolvimento de modelos regionais robustos, especialmente para países do Sul Global atualmente sub-representados na literatura [@Kshetri2014; @Li2025], apesar do potencial em produtos como café, cacau e cachaça. Iniciativas como o Global Open Data for Agriculture and Nutrition (GODAN) demonstram que infraestruturas colaborativas reduzem custos de validação em até 40%, segundo @Wilkinson2021, acelerando a tradução de pesquisa em políticas públicas.

A integração de ML em sistemas de IG, quando alinhada aos critérios do Terroir Digital, permite transformar selos de origem em certificados verificáveis de sustentabilidade, correlacionando assinaturas químicas com práticas de gestão conservacionista [@Camin2017; @Vandecandelaere2018]. Em territórios extensos como Amazônia e Cerrado, onde inspeções físicas apresentam custos proibitivos, modelos treinados com sensoriamento remoto e amostragem estratégica podem atuar como sistemas de detecção primária, sinalizando anomalias que justifiquem verificação in loco [@Osco2021; @Gomes2023]. Essa arquitetura tecnológica garante que prêmios de mercado remunerem efetivamente a conservação da agrobiodiversidade, prevenindo greenwashing através de mecanismos de auditoria contínua baseados em evidências computacionais.


## 4. Conclusões

As Indicações Geográficas operam como sistemas socioecológicos acoplados, nos quais as interações entre solo, clima e biota fundamentam a gênese da tipicidade territorial dos produtos. Algoritmos de aprendizado de máquina emergiram como instrumentos robustos para decodificar tais interações não lineares, transmutando assinaturas quimiométricas em evidências auditáveis de conformidade ambiental.

O panorama de pesquisa permanece assimétrico, com a literatura predominante concentrada em regiões temperadas e commodities convencionais. Demandam-se esforços adicionais para o desenvolvimento de modelos robustos e inclusivos, abrangendo uma diversidade de produtos e geografias, mediante o aproveitamento de investimentos em infraestrutura laboratorial, governança de dados transparente e a integração do conhecimento local empírico.

Conceitualmente, a superação dessas barreiras reside na transição para o Terroir Digital. Diferente da abordagem estática predominante, este arcabouço fundamenta-se na reconstrução dinâmica das interações solo-clima-biota. As evidências sugerem que a integração de dados ambientais aos classificadores quimiométricos é o caminho técnico mais promissor para transformar a certificação de origem em uma auditoria de serviços ecossistêmicos auditável, desde que superados os desafios de transparência algorítmica identificados.

Pesquisas futuras devem priorizar além da acurácia marginal, a validade ecológica e a governança de dados. É imperativo o desenvolvimento de protocolos de validação que simulem flutuações sazonais e a implementação de Inteligência Artificial Explicável (XAI) para garantir que as decisões de autenticação sejam baseadas em marcadores biológicos causais, e não em correlações espúrias. A efetivação do Terroir Digital dependerá, em última análise, da capacidade da comunidade científica em padronizar metadados e abrir repositórios, permitindo que o Aprendizado de Máquina opere como um mecanismo transparente de verificação da conformidade ambiental.

## Agradecimentos

Os autores agradecem à Universidade Federal de Sergipe (UFS), à Universidade Estadual de Feira de Santana (UEFS) e ao Instituto Federal de Sergipe (IFS) pelo apoio institucional e infraestrutural que possibilitou esta pesquisa.

## Conflitos de Interesse

Os autores declaram não haver conflitos de interesse.

## Declaração de Disponibilidade de Dados

O conjunto de dados completo que apoia os resultados deste estudo, incluindo o corpus bibliográfico, os scripts de análise e os resultados intermediários, está disponível publicamente no repositório Open Science Framework (OSF) sob DOI: [https://doi.org/10.17605/OSF.IO/2EKYQ](https://doi.org/10.17605/OSF.IO/2EKYQ).

## Declaração de Ética

Esta revisão não envolve participantes humanos, experimentos com animais, linhagens celulares ou coleta de amostras. Não foi necessária aprovação ética nem consentimento.

## Posicionamento/Envolvimento Comunitário

Quando relevante, as perspectivas da comunidade, provenientes de organizações de produtores e certificadoras, contribuíram para a interpretação das limitações práticas nos sistemas de Indicação Geográfica (IG); nenhuma informação que permitisse a identificação do indivíduo foi incluída.

## References

::: {#refs}
:::

## Tabela A.3: Módulos Tecnológicos Identificados pela Análise de Comunidade Louvain

| **Módulo** | **Algoritmos Principais**                 | **Técnicas Analíticas**               | **Produtos**         | **Região Predominante** |
| :---------------: | :---------------------------------------------- | :-------------------------------------------- | :------------------------- | :----------------------------- |
|   **M1**   | Random Forest, Decision Tree, Gradient Boosting | Espectroscopia (NIR), Quimiometria            | Vinho, Mel                 | África, Europa                |
|   **M2**   | SVM, KNN                                        | Cromatografia (GC-MS, LC-MS, HPLC)            | Carnes, Produtos Regionais | Ásia                          |
|   **M3**   | Neural Networks, CNN, Deep Learning             | Espectroscopia (NIR, FTIR), Sensores (e-nose) | Azeite, Queijo, Chá       | Europa, Ásia                  |

*Fonte: Três principais módulos tecnológicos identificados pela análise de comunidade Louvain aplicada à rede de coocorrência entre algoritmos, técnicas analíticas e produtos com indicação geográfica. A densidade interna de cada módulo indica a força das conexões entre seus componentes.*

### Tabela A.4: Famílias Tecnológicas Identificadas pela Análise de Cluster

| **Cluster** | **Produto Principal** | **Técnica Analítica** | **Algoritmo ML**                   | **Aplicação**                 | **Região Predominante** |
| ----------------- | --------------------------- | ----------------------------- | ---------------------------------------- | ------------------------------------- | ------------------------------ |
| 1                 | Mel                         | Espectroscopia NIR            | SVM, KNN                                 | Autenticação e detecção de fraude | Ásia                          |
| 2                 | Queijo                      | Espectroscopia NIR            | Redes Neurais                            | Discriminação de origem             | Europa                         |
| 3                 | Mel, Carnes                 | LC-MS, GC-MS                  | SVM, Random Forest, Árvores de Decisão | Autenticação e rastreabilidade      | Ásia, Europa                  |

*Fonte: Dez clusters identificados pela análise de cluster (k-means e hierárquica) baseada em produto, instrumento analítico, algoritmo e tipo de aplicação. Apenas os três clusters mais notáveis são detalhados aqui.*
