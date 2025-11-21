---
title: "Machine Learning for Geographical Indications: A Scoping Review on Authentication, Certification and Open Data Ecosystems"
author: "Catuxe Varjão de Santana Oliveira, Paulo Roberto Gagliardi, Luiz Diego Vidal Santos, Gustavo da Silva Quirino, Ana Karla de Souza Abud, Cristiane Toniolo Dias"
bibliography: referencias.bib
csl: apa.csl
reference-doc: modelo_formatacao.docx
fig-align: center
table-align: center
lang: pt-BR
---
# Resumo

As Indicações Geográficas (IGs) são ativos estratégicos que vinculam a identidade territorial e o valor do produto em economias do conhecimento. No entanto, a autenticação e a certificação de produtos com IG dependem de metodologias robustas, reproduzíveis e transparentes. Embora a Aprendizagem de Máquina (AM) tenha emergido como uma ferramenta central nesse domínio, ainda não existe uma síntese sistemática de suas aplicações, rigor metodológico e limitações. Esta revisão de escopo mapeia 148 estudos revisados ​​por pares (2010–2025) das bases de dados Scopus e Web of Science, empregando filtragem semântica automatizada (94,2% de precisão), avaliação rigorosa da qualidade (ICC = 0,87) e análise estatística multivariada. Identificamos um crescimento exponencial (aumento superior a 400% desde 2018) nas aplicações de AM para autenticação de IG, organizadas em três módulos tecnológicos estáveis ​​que combinam algoritmos (Random Forest, SVM, Redes Neurais), técnicas analíticas (NIR, LC-MS, metabolômica) e produtos (vinhos, chás, carnes). De forma crítica, as precisões de 80–100% na autenticação contrastam fortemente com a baixa generalização: apenas 23% dos estudos empregaram validação espacialmente independente, e a validação externa mostrou uma degradação de desempenho de 2–15%. Foi identificado de um viés de otimismo estatístico em 77% do corpus, no qual o sucesso da validação in silico obscurece a fragilidade preditiva no mundo real. Documentamos ainda um paradoxo que, embora o aprendizado de máquina alcance uma discriminação de origem quase perfeita, a capacidade preditiva para índices gerais de qualidade permanece modesta (R² = 0,11–0,14). Essas descobertas têm implicações diretas para a conformidade regulatória, a governança da propriedade intelectual e a justiça territorial em sistemas de certificação. É destacada a necessidade de protocolos de validação temporal, implementações de modelos transparentes e estruturas de governança equitativas que integrem aprendizado de máquina em arquiteturas de certificação de informações geográficas. Esta revisão contribui para os métodos computacionais em ciência da informação geográfica e para as práticas de ciência aberta, fornecendo evidências meta-analíticas transparentes e reproduzíveis sobre a viabilidade e as limitações do aprendizado de máquina para autenticação territorial.

**Palavras-chave:** Geographical Indications; Machine Learning; Authentication; Certification; Artificial Intelligence; Food Traceability; Agroecological Products; Intellectual Property; Territorial Justice; Scoping Review.

# 1. Introdução

As Indicações Geográficas (IGs) protegem territórios e produtos na economia do conhecimento, assegurando direitos exclusivos sobre produtos cuja qualidade, reputação e características derivam de sua origem geográfica [@Locatelli2008; @WIPO2018]. Fundamentadas na Convenção de Berna [@berna1886] e no Acordo TRIPS [@trips1994], as IGs conectam territórios produtivos e comunidades locais a mercados diferenciados, vinculando proteção de direitos à preservação do conhecimento tradicional [@Suh2007]. Além de instrumento jurídico, as IGs constituem ativo intangível estratégico no sentido proposto pela teoria da Visão Baseada em Recursos (Resource-Based View), sendo recursos raros, valiosos, inimitáveis e insubstituíveis que fundamentam vantagem competitiva territorial sustentável [@Barney1991]. A apropriação de valor por meio das IGs transcende rentabilidade imediata, servindo como ancoragem para captura de valor futuro através de mercados diferenciados e disposição de consumidores em pagar preços premium por produtos com certificação de origem [@Loureiro2002; @VazquezFontes2010].

No Brasil, as Indicações Geográficas são regulamentadas pela Lei da Propriedade Industrial, Lei nº 9.279 de 14 de maio de 1996, que estabelece dois tipos de reconhecimento com implicações jurídicas e econômicas distintas, Indicação de Procedência e Denominação de Origem [@Brasil1996]. A Indicação de Procedência refere-se ao nome geográfico conhecido pela produção ou fabricação de determinado produto, funcionando como mecanismo de sinalização de origem; a Denominação de Origem designa produtos cujas qualidades ou características se devem exclusiva ou essencialmente ao meio geográfico, incluindo fatores naturais e humanos, constituindo forma de proteção mais robusta que vincula qualidade ao terroir [@MAPA2020].

O controle deste tipo de registro é realizado pelo Instituto Nacional de Propriedade Intelectual (INPI), com apoio do Ministério da Agricultura, Pecuária e Abastecimento, que operacionaliza políticas de fomento e certificação de produtos agrícolas com identidade territorial [@MAPA2020]. Este marco regulatório brasileiro alinha-se à Lei nº 10.973/2004 (Lei de Inovação) e Lei nº 13.243/2016 (Novo Marco Legal de CT&I), que reconhecem Indicações Geográficas como ativos de propriedade intelectual passíveis de proteção estratégica, valoração e comercialização [@Brasil2004; @Brasil2016].

No contexto brasileiro, produtos artesanais e agroalimentares com potencial para registro de Indicação Geográfica representam manifestações culturais relevantes e oportunidades estratégicas para captura de valor territorial. Estudos demonstram que características únicas de produtos regionais, como a cerâmica artesanal do Baixo São Francisco ou produtos vinícolas especializados, estão intimamente relacionadas a atributos geográficos da localização de produção, incluindo características edafoclimáticas (solo, clima, altitude) e métodos únicos de cultivo ou produção [@Bureau2018; @Azevedo2011; @Santos2018; @Fonzo2015; @SantosJC2019]. A caracterização territorial desses produtos, necessária para o reconhecimento como Denominação de Origem conforme estabelecido no artigo 178 da Lei nº 9.279/1996 [@Brasil1996], demanda análises técnicas específicas que comprovem, com rigor científico, a relação entre qualidade e fatores geográficos [@GoncalvesMaduro2020]. Neste contexto, apresenta-se uma questão central de que forma os sistemas de certificação podem validar, rigorosamente e objetivamente, a relação entre origem geográfica e qualidade de produtos.

As tecnologias de Aprendizado de Máquina (ML) emergem como resposta estratégica a essa lacuna, transmutando dados analíticos complexos em conhecimento certificável sobre autenticidade e origem. Diferentemente dos métodos de análise sensorial tradicionais, dependentes de expertise humana tácita e limitados pela subjetividade e escalabilidade, os algoritmos de ML operam sob uma lógica indutiva ou abdutiva. Eles processam automaticamente dados multidimensionais, identificando padrões não lineares e relações latentes que escapam à modelagem estatística clássica baseada em testes de hipóteses dedutivos. Essa capacidade de construir modelos com formas funcionais flexíveis permite revelar estruturas de dados não previamente especificadas pela teoria, conferindo robustez matemática à certificação territorial [@Ramos2025; @Chen2020].

No âmbito das Indicações Geográficas, o Machine Learning tem sido mobilizado para autenticação de origem, detecção de fraudes, controle preditivo de qualidade e rastreabilidade integral, operando sobre assinaturas químicas, isotópicas, espectrais e geoespaciais que capturam a relação entre produto e território [@longo2021; @acquarelli2021; @rodrigues2022; @rana2023]. Essas aplicações demonstram que a integração entre dados instrumentais de alta dimensionalidade e modelos supervisionados permite discriminar origens, identificar adulterações e estimar atributos sensoriais e físico‑químicos com precisão compatível com requisitos de certificação [@Jiang2025; @Peng2025; @Santoma2025; @Li2025; @Wang2025].

A seleção de variáveis e a escolha de algoritmos, em particular Random Forest, SVM, PLS‑DA, PCA e métodos de seleção como Boruta e RFE, deixam de ser apenas decisões técnicas para se tornar componente da arquitetura regulatória, pois definem quais marcadores territoriais serão reconhecidos como evidências de autenticidade [@Salam2021; @Malik2023; @Iranzad2025; @Effrosynidis2021; @Loyal2022; @Chen2020; @Rebiai2022].

Apesar do interesse acadêmico e tecnológico atual, não existem revisões de escopo que sistematizem as evidências científicas disponíveis, identifiquem as técnicas empregadas, avaliem seu desempenho em diferentes produtos e contextos geográficos, ou apontem direções para pesquisas futuras. Esta limitação afeta o desenvolvimento metodológico na área e a transferência de conhecimento para sistemas de certificação e controle de Indicações Geográficas.

Esta revisão de escopo busca mapear sistematicamente as aplicações de Machine Learning em Indicações Geográficas, utilizando o framework PCC (*Population, Concept, Context*) para identificar e sintetizar evidências científicas sobre a integração entre Machine Learning e aspectos territoriais de Indicações Geográficas. Hipotiza-se que as técnicas de Aprendizado de Máquina têm sido empregadas para apoiar processos de autenticação, avaliação e tomada de decisão relacionados às Indicações Geográficas, revelando padrões metodológicos que contribuem para a consolidação de conhecimento orientado ao desenvolvimento de modelos computacionais aplicados à certificação geográfica.

# 2. Materiais e Métodos

Esta revisão de escopo segue as diretrizes da extensão PRISMA-ScR (*Preferred Reporting Items for Systematic Reviews and Meta-Analyses extension for Scoping Reviews*) para garantir transparência e reprodutibilidade metodológica. O protocolo foi registrado no Open Science Framework, facilitando o acesso público e a replicabilidade.

## 2.1 Questão de Pesquisa

O estudo foi estruturado utilizando o framework PCC (*Population, Concept, Context*), que fundamenta a questão de pesquisa: *Como técnicas de Aprendizado de Máquina têm sido aplicadas para autenticação, avaliação e apoio à decisão em sistemas de Indicações Geográficas?*

| Elemento                  | Descrição                                                                                                                                                                                                                                                                                                                                                                                     |
| :------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **P (População)** | Indicações Geográficas, Denominações de Origem e Indicações de Procedência reconhecidas nacional e internacionalmente, abrangendo produtos agroalimentares (vinhos, queijos, cafés, carnes, azeites), artesanatos e outros produtos com identidade territorial.                                                                                                                        |
| **C (Conceito)**    | Técnicas de Aprendizado de Máquina, Inteligência Artificial, algoritmos de classificação e predição, métodos quimiométricos, Mineração de Dados e Processamento de Linguagem Natural aplicados a contextos de Indicações Geográficas.                                                                                                                                             |
| **C (Contexto)**    | Autenticação de origem geográfica, avaliação de potencialidade de IGs, identificação de determinantes territoriais (solo, clima, métodos de produção), classificação e discriminação de produtos, sistemas de apoio à decisão para certificação, controle de qualidade, rastreabilidade, detecção de fraudes e adulterações, e estratégias de valorização territorial. |

*Tabela 1. Estrutura da revisão de escopo segundo o framework PCC.*

Este trabalho se propõe a identificar e caracterizar as aplicações de ML reportadas na literatura científica, categorizando as técnicas empregadas segundo tipo de algoritmo, abordagem metodológica e métricas de desempenho. Ainda, analisar a distribuição das aplicações por tipo de produto, região geográfica e período temporal. E por fim, identificar lacunas metodológicas, limitações e direções para pesquisas futuras.

## 2.1.1 Fluxograma Metodológico PRISMA-ScR

A Figura 1 apresenta o fluxograma metodológico da revisão de escopo, estruturado em quatro fases sequenciais segundo as diretrizes PRISMA-ScR: (1) Estratégia de Busca nas principais bases de dados, (2) Filtragem Automatizada com sistema de pontuação ponderada, (3) Análise Manual de Qualidade com avaliação multidisciplinar, e (4) Análise Bibliométrica e Síntese Qualitativa** integrando metodologias quantitativas e documentais. O fluxograma detalha o percurso metodológico desde a identificação de registros até a síntese final com recomendações para implementação de Machine Learning em sistemas de Indicações Geográficas.

![Fluxograma da revisão de Escopo sobre Aplicações de Machine Learning em Indicações Geográficas. ](2-FIGURAS/2-EN/ml_indicacoes_geograficas.png){#fig:ml_indicacoes width="80%"}

## 2.3 Estratégia de Busca e Extração dos Estudos

A busca foi realizada nas bases de dados científicas Scopus (Elsevier) e Web of Science (Clarivate Analytics). A estratégia de busca foi fundamentada na intersecção de três domínios temáticos principais: técnicas de machine learning e inteligência artificial; sistemas de certificação geográfica; e Indicações Geográficas e Denominações de Origem.

Os descritores foram estruturados utilizando terminologia controlada em língua inglesa, articulados por operadores booleanos (AND, OR, NOT), abrangendo publicações dos últimos 15 anos (2010-2025) para capturar o estado da arte em machine learning aplicado a Indicações Geográficas. A estratégia de busca foi construída seguindo a lógica:

*("machine learning" OR "artificial intelligence" OR "deep learning" OR "supervised learning" OR "unsupervised learning" OR "ensemble methods") AND ("geographical indications" OR "denominations of origin" OR "appellations of origin" OR "protected designations of origin") AND ("authentication" OR "traceability" OR "quality control" OR "fraud detection" OR "geospatial analysis")*.

Os critérios de inclusão contemplaram os artigos completos publicados em periódicos revisados por pares, escritos em inglês, português ou espanhol, que apresentassem aplicações de técnicas de ML em contextos de Indicações Geográficas, autenticação de origem ou controle de qualidade territorial. Os descritores primários deveriam estar presentes nos campos título, resumo ou palavras-chave dos manuscritos. Foram excluídos trabalhos não revisados por pares, aqueles sem aplicação prática de ML, e estudos focados exclusivamente em aspectos não territoriais.

## 2.4 Primeira Fase: Sistema de Filtragem Automatizada por Relevância Temática

### 2.4.1 Algoritmo de Pontuação Ponderada

Para complementar a triagem manual, foi desenvolvido um sistema de filtragem automatizada que atribui pontuações de relevância temática aos registros com base na presença e na localização de descritores específicos em título, resumo e palavras‑chave. O algoritmo foi implementado em Python (NLTK, spaCy) e estruturado como um esquema de pesos hierárquicos aplicado a cada termo identificado. A pontuação de cada artigo foi calculada pela Equação 1.

$$
S_i = \sum_{j=1}^{n} w_j \cdot l_i \cdot f_{ij}
$$

onde:

- $S_i$ = pontuação total do artigo $i$
- $w_j$ = peso associado ao termo $j$ (categorizado em 5 níveis: 5, 3, 2, 1, ou -5/-3/-2 pontos)
- $l_i$ = multiplicador de localização do termo (1,5 para título, 1,2 para palavras‑chave, 1,0 para abstract)
- $f_{ij}$ = frequência de ocorrência do termo $j$ no artigo $i$
- $n$ = número total de termos avaliados

O sistema de pontuação hierárquica seguiu princípios do Método de Análise Hierárquica (AHP), organizando os descritores em cinco categorias com pesos diferenciados [@SAATY1991]. Termos Prioritários (5 pontos) representam o núcleo conceitual da revisão e incluem expressões como *geographical indications, denominations of origin, appellations of origin, protected designations of origin, traceability, authentication, quality control*. Termos de Alta Relevância (3 pontos) capturam conceitos metodológicos centrais, como *machine learning, artificial intelligence, deep learning, neural networks, fraud detection, geospatial analysis*. Termos de Relevância Média (2 pontos) cobrem temas complementares, a exemplo de *chemometrics, data mining, classification*, enquanto Termos de Contexto (1 ponto) indicam ambientes ou aplicações potenciais, como *regional products, certification, prediction, validation*. Termos de Exclusão recebem pesos negativos e penalizam registros fora do escopo, sobretudo em domínios como *medical/clinical/pharmaceutical* (−5), *urban planning/smart cities* (−3) e *finance/economics/business* (−2) [@MUNN2018; @tricco2018].

### 2.4.2 Implementação e Validação do Sistema Automatizado

Para cada registro, o algoritmo varre título, resumo e palavras‑chave, aplica os pesos definidos para cada categoria de termo (Prioritário = 5; Alta Relevância = 3; Relevância Média = 2; Contexto = 1; Exclusão = valores negativos) e multiplica cada ocorrência pelo fator de localização correspondente (1,5 para título, 1,2 para palavras‑chave, 1,0 para resumo). A pontuação final é a soma desses produtos ao longo de todos os termos identificados em cada registro.

O limiar mínimo de inclusão foi definido a partir da distribuição empírica das pontuações, identificando-se o ponto de inflexão na curva acumulada (critério tipo Pareto/elbow) e ajustando-o por validação manual com amostragem estratificada de registros contendo termos‑chave como *machine learning*, *geographical indications* e *authentication*. O valor final representou o melhor compromisso entre sensibilidade e especificidade, estabilizando a concordância interavaliadores nos casos limítrofes.

### 2.4.3 Validação Participativa e Refinamento Algorítmico

Para assegurar a validade científica do processo de seleção, foi implementado um protocolo de validação envolvendo três revisores independentes, especialistas em machine learning, sistemas de certificação geográfica e Indicações Geográficas. O protocolo incluiu uma revisão manual sistemática, com análise criteriosa dos 272 estudos identificados nas bases Scopus (140) e Web of Science (132) para verificar a aderência aos critérios de inclusão e relevância temática. Adicionalmente, foi realizado um teste de concordância interavaliadores para verificar a consistência na classificação dos estudos.

O processo também contemplou a análise de casos limítrofes, com investigação qualitativa dos estudos de aderência parcial para apoiar a decisão de inclusão ou exclusão, e o refinamento iterativo dos critérios de elegibilidade com base nas características observadas no corpus. O processo de validação confirmou a consistência metodológica do sistema, com concordância entre os revisores na identificação de estudos relevantes para a revisão de escopo.

### 2.4.4 Verificação de Cobertura Bibliográfica e Categorização Automatizada

Foi desenvolvido sistema automatizado para verificar a cobertura bibliográfica das citações metodológicas. O procedimento avalia completude e consistência da base de referências, garantindo rastreabilidade entre citações textuais e arquivos bibliográficos.

O corpus bibliográfico consolidado foi submetido à categorização automatizada com técnicas de Processamento de Linguagem Natural (PLN). Os registros foram identificados e organizados segundo domínios metodológicos relevantes, aplicando abordagens de revisões sistemáticas automatizadas [@OforiBoateng2024; @Sawicki2023]. Foi construído pipeline computacional que extrai, tokeniza e vetorializa metadados e resumos das referências, usando modelos supervisionados e regras semânticas para reconhecimento de padrões [@Young2019; @Casey2021]. As referências foram classificadas em categorias metodológicas previamente definidas, abrangendo áreas como técnicas de aprendizado de máquina e sistemas de indicações geográficas.

Para quantificação da cobertura bibliográfica e adequação dos estudos selecionados, foram aplicadas duas métricas complementares [@tranfield2003; @webster2002]. A primeira, de cobertura de citações, foi calculada pela Equação 2.

$$
Cobertura = \frac{C_{encontradas}}{C_{totais}} \times 100
$$

Onde:

- $C_{encontradas}$ = número de citações do manuscrito presentes no corpus
- $C_{totais}$ = número total de citações únicas no manuscrito

A segunda métrica, de taxa de uso do corpus bibliográfico, foi estruturada conforme a Equação 3.

$$
Taxa\_Uso = \frac{R_{citadas}}{R_{totais}} \times 100
$$

Onde:

- $R_{citadas}$ = número de referências do corpus citadas no manuscrito
- $R_{totais}$ = número total de referências presentes no corpus

A partir dessas métricas é possivel avaliar quantitativamente a utilização efetiva da base de referências e garantir que os estudos selecionados reflitam adequadamente o escopo temático da revisão.

## 2.5 Segunda Fase: Análise Manual de Qualidade Metodológica

Na segunda fase, três revisores independentes avaliaram manualmente a qualidade metodológica dos estudos selecionados, assegurando análise multidisciplinar e reduzindo vieses interpretativos. Adaptamos a escala MMAT [@pluye2009; @hong2018] para estudos interdisciplinares envolvendo machine learning e sistemas de certificação geográfica, estruturando oito indicadores em escala Likert de 3 pontos. Os indicadores incluíram rigor metodológico, validação técnica dos algoritmos, aderência a protocolos éticos para comunidades produtivas, reprodutibilidade dos experimentos, integração entre métodos quantitativos e qualitativos territoriais, impacto para sistemas de IG, documentação completa e generalizabilidade dos métodos (Tabela 2).

Cada indicador recebeu pontuação de 0 a 2, sendo zero quando o critério não foi atendido ou apresenta deficiências substantivas; um ponto quando atendido parcialmente com limitações reconhecidas; dois pontos quando completamente atendido com evidências claras. Escolhemos escala de 3 pontos porque avaliações dicotômicas (sim/não) não capturam adequadamente a complexidade de estudos interdisciplinares, enquanto escalas maiores (5+ pontos) geram inconsistência entre avaliadores [@Likert3vs5_2025].

| Código | Indicador                                                                     | Domínio                |
| ------- | ----------------------------------------------------------------------------- | ----------------------- |
| RIG     | Rigor metodológico na coleta e processamento de dados territoriais           | Qualidade Territorial   |
| VAL     | Validação técnica dos algoritmos com métricas apropriadas                 | Qualidade Computacional |
| ETI     | Aderência a protocolos éticos para pesquisa com comunidades produtivas      | Qualidade Ética        |
| REP     | Reprodutibilidade dos experimentos computacionais                             | Qualidade Técnica      |
| INT     | Integração efetiva entre métodos quantitativos e qualitativos territoriais | Qualidade Metodológica |
| IMP     | Impacto e aplicabilidade dos resultados para sistemas de IG                   | Qualidade Social        |
| DOC     | Documentação completa dos algoritmos e procedimentos de certificação      | Qualidade Documental    |
| GEN     | Generalizabilidade e transferibilidade dos métodos propostos                 | Qualidade Científica   |

*Tabela 2. Indicadores de qualidade metodológica para estudos ML-Indicações Geográficas.*

### 2.5.1 Procedimentos de Consenso e Validação Interavaliadores

O processo de avaliação manual incluiu protocolo de consenso entre avaliadores. Inicialmente, os três revisores avaliaram independentemente uma amostra piloto de 30 estudos (aproximadamente 11% do corpus) para calibração dos critérios e estabelecimento de consenso interpretativo. Para o corpus completo, casos de discordância entre avaliadores, caracterizados por diferença igual ou superior a dois pontos na pontuação total, foram submetidos a processo de consenso envolvendo reavaliação individual cega, discussão fundamentada nos critérios estabelecidos, e decisão por maioria simples quando necessário.

O coeficiente de correlação intraclasse foi calculado pela Equação 4 [@shrout1979].

$$
ICC = \frac{BMS - EMS}{BMS + (k-1) \cdot EMS}
$$

Onde:

- $BMS$ = quadrado médio entre avaliadores
- $EMS$ = quadrado médio de erro
- $k$ = número de avaliadores

O coeficiente foi calculado obtendo-se ICC igual a 0,87 com intervalo de confiança de 95% entre 0,84 e 0,91, indicando boa concordância.

### 2.5.2 Critérios Específicos para Estudos Interdisciplinares

Considerando a natureza interdisciplinar dos estudos analisados, foram estabelecidos critérios de qualidade que examinam a coerência na integração entre métodos quantitativos e qualitativos territoriais, a validação dos resultados em múltiplos contextos geográficos, o grau de transparência algorítmica (documentação de código, dados e procedimentos), a aderência a protocolos éticos específicos para comunidades produtivas e a aplicabilidade prática dos achados para certificação e valorização territorial em sistemas de Indicações Geográficas.

Esta segunda fase resultou na seleção de 25 estudos com qualidade metodológica adequada (score ≥ 20 pontos) a partir do corpus inicial de 272 artigos, que constituíram a base para as análises subsequentes da revisão de escopo, focando em aplicações de machine learning em contextos de Indicações Geográficas e autenticação de produtos. A distribuição dos artigos selecionados foi: 1 artigo de excelência (≥40 pts), 2 de alta relevância (≥30 pts) e 22 adequados (≥20 pts).

## 2.6 Terceira Fase: Análise Bibliométrica

Na terceira fase, foi analisada a produtividade científica através da Lei de Lotka [@lotka1926], que examina a distribuição de autores segundo o número de publicações. A Lei de Lotka descreve a distribuição não-linear de produtividade entre autores, identificando se a produção científica segue padrão concentrado ou disperso.

A Lei de Lotka foi aplicada conforme a Equação 5.

$$
f(a) = \frac{K}{a^n}
$$

Onde:

- $f(a)$ = número de autores que publicaram exatamente $a$ artigos
- $K$ = constante de proporcionalidade
- $a$ = número de artigos publicados por um autor
- $n$ = expoente (tipicamente aproximado a 2 para ciências)

A análise de cocitação e acoplamento bibliográfico não foram realizadas devido à ausência de campos de referências citadas nos arquivos bibliográficos disponíveis.

## 2.7 Quarta Fase: Síntese Qualitativa e Integração com Análise Documental

Na quarta fase, foram integrados sistematicamente os achados das fases anteriores com análise documental de marcos regulatórios, fundamentando as recomendações metodológicas da revisão.

A síntese final combinou análise qualitativa temática com seleção baseada no princípio de Pareto (80/20), priorizando os 20% dos artigos com maior pontuação combinada (40% qualidade metodológica, 35% relevância temática, 25% impacto bibliométrico).

A pontuação combinada final foi calculada pela Equação 6.

$$
P_{final} = (0.40 \cdot Q_{met}) + (0.35 \cdot Q_{tem}) + (0.25 \cdot Q_{biblio})
$$

Onde:

- $P_{final}$ = pontuação final de seleção
- $Q_{met}$ = qualidade metodológica normalizada (0-1)
- $Q_{tem}$ = relevância temática normalizada (0-1)
- $Q_{biblio}$ = impacto bibliométrico normalizado (0-1)

## 2.8 Análises Estatísticas

Para caracterizar sistematicamente o corpus bibliográfico e identificar padrões emergentes, as análises estatísticas foram implementadas no ambiente R [@RCoreTeam2024] utilizando o RStudio [@RStudioTeam2023] e pacotes específicos. A Análise de Correspondência Múltipla (MCA) foi adotada para investigar associações entre variáveis categóricas (algoritmos, produtos, regiões, técnicas analíticas), conforme metodologia consolidada por @Le2008 e @Greenacre2017, utilizando o pacote `FactoMineR` para extração das dimensões principais e interpretação das relações conceituais da área. Com base nas mesmas variáveis, procedeu-se, em seguida, à Análise de Clusters (k-means e hierárquica), implementada com `FactoMineR` e `factoextra`, para identificar agrupamentos recorrentes de combinações produto‑instrumento‑algoritmo, que sintetizam as “famílias tecnológicas” discutidas na seção 3.8.

A análise de redes foi implementada para mapear coocorrências entre algoritmos, produtos e regiões, seguindo procedimentos de análise de redes complexas [@Csardi2006; @Schoch2020]. Utilizando os pacotes `igraph` e `ggraph`, foi construído grafo não direcionado com cálculo de centralidades de grau, autovetor e intermediação, e a detecção de comunidades foi realizada com o algoritmo de Louvain [@Blondel2008] para identificar módulos temáticos, cujos resultados estruturam as interpretações apresentadas na seção 3.9.

A evolução temporal das publicações (2010–2025) foi analisada por meio de séries temporais e tendência não paramétrica, empregando o teste de correlação de Spearman [@Spearman1904] para detectar tendências significativas no número de estudos por ano e na adoção relativa dos principais algoritmos. As visualizações foram geradas com o pacote `ggplot2`, utilizando suavização LOESS [@Cleveland1979] para ilustrar a dinâmica de crescimento do campo e a transição entre paradigmas algorítmicos.

Por fim, foram ajustados modelos preditivos globais para avaliar em que medida variáveis bibliométricas e metodológicas permitem antecipar um índice contínuo de pontuação dos estudos e uma classificação dicotômica entre trabalhos de alto e baixo score. Modelos de regressão (Mínimos Quadrados Ordinários, Ridge, Lasso e Random Forest) e de classificação (Regressão Logística e Random Forest) foram estimados com `caret` e `randomForest`, utilizando validação cruzada k-fold estratificada para controle de sobreajuste. O desempenho foi avaliado por RMSE e $R^2$ na regressão, e por acurácia, precisão, sensibilidade e F1-score na classificação, em consonância com os resultados discutidos na seção 3.7.

### 2.8.1 Análise de Correspondência Múltipla (MCA)

A Análise de Correspondência Múltipla (MCA) foi adotada para investigar associações entre as variáveis categóricas (algoritmos, produtos, regiões, etc.), conforme metodologia consolidada por @Le2008 e @Greenacre2017. A análise, conduzida com o pacote `FactoMineR` para a interpretação das relações conceituais da área.

### 2.8.2 Análise de Redes (Network Analysis)

A análise de redes foi implementada para mapear co-ocorrências entre algoritmos, produtos e regiões, seguindo procedimentos de análise de redes complexas [@Csardi2006; @Schoch2020]. Utilizando os pacotes `igraph` e `ggraph`, foi construído um grafo não-direcionado ponderado, onde os nós representam entidades (algoritmos, instrumentos analíticos, produtos e regiões) e as arestas indicam co-ocorrência nos estudos, com pesos proporcionais à frequência de co-ocorrência. Foram calculadas métricas de centralidade (grau, intermediação e autovetor) para identificar elementos estruturalmente centrais na rede de conhecimento do campo.

A detecção de comunidades foi realizada com o algoritmo de Louvain [@Blondel2008], método hierárquico baseado em otimização gulosa da modularidade que identifica partições da rede maximizando a densidade de conexões intra-módulo em relação a conexões inter-módulos. O algoritmo opera em duas fases iterativas: (i) otimização local, onde cada nó é atribuído à comunidade que maximiza o ganho de modularidade; e (ii) agregação, onde comunidades identificadas são colapsadas em super-nós para construção de uma nova rede em nível superior. A modularidade *Q* é definida como:

$$Q = \frac{1}{2m} \sum_{ij} \left[ A_{ij} - \frac{k_i k_j}{2m} \right] \delta(c_i, c_j)$$

onde $m$ é o número de arestas, $A_{ij}$ representa a matriz de adjacência, $k_i$ e $k_j$ são os graus dos nós $i$ e $j$, e $\delta(c_i, c_j) = 1$ se os nós pertencem à mesma comunidade. A estrutura modular resultante foi interpretada como módulos tecnológicos temáticos, cujos resultados estruturam as interpretações apresentadas na seção 3.9.

### 2.8.3 Análise Temporal

A evolução temporal das publicações (2010–2025) foi analisada por meio de séries temporais, empregando o teste de correlação de Spearman [@Spearman1904] para detectar tendências significativas. As visualizações foram geradas com o pacote `ggplot2`, utilizando suavização LOESS [@Cleveland1979] para ilustrar a dinâmica de crescimento do campo e a adoção de diferentes tecnologias.

# 3. Resultados e Discussão

## 3.1 Síntese Executiva da Revisão de Escopo

A revisão de escopo, estruturada segundo PRISMA-ScR (Figura 2), identificou e analisou 272 estudos (140 Scopus, 132 Web of Science) publicados entre 2010-2025, selecionando 148 artigos relevantes após filtragem automatizada e avaliação manual de qualidade metodológica. A base de dados para as análises estatísticas foi constituída a partir deste processo sistemático de seleção, resultando em um corpus representativo das aplicações de Machine Learning em Indicações Geográficas. O corpus demonstra crescimento recente: 68% das publicações concentram-se em 2021-2025, indicando convergência entre certificação territorial e transformação digital, acompanhando tendências globais de inovação em sistemas agroalimentares [@Hu2024].

![Fluxograma da revisão de Escopo sobre Aplicações de Machine Learning em Indicações Geográficas. ](2-FIGURAS/2-EN/prisma_flowdiagram.png){#fig:prisma2020 width="80%"}

A filtragem automatizada por análise semântica e pontuação, alcançou precisão temática de 94,2%, superando o limiar de 85% estabelecido. A abordagem de triagem computacional mostrou-se adequada para revisões com grandes volumes bibliográficos, indicando que sistemas automatizados calibrados contribuem para reduzir vieses de seleção e aumentar a reprodutibilidade [@OforiBoateng2024]. A reprodutibilidade de 100% em execuções múltiplas do algoritmo, associada à concordância interavaliadores de κ = 0.89, garante que os achados refletem, com alta confiabilidade, o estado atual da literatura científica neste domínio.

A avaliação manual de qualidade metodológica alcançou coeficiente de correlação intraclasse (ICC), de 0,87 (intervalo de confiança de 95%: 0,84–0,91), confirmando boa concordância entre avaliadores e legitimando os critérios de inclusão utilizados [@streiner2008health]. Esta validação assegura que os estudos selecionados para análise sintética atendem a requisitos adequados de rigor metodológico.

## 3.2 Análise Estrutural e Temporal do Corpus Científico

A Análise de Correspondência Múltipla (MCA) foi aplicada para mapear a evolução temporal das aplicações de Machine Learning em Indicações Geográficas, focando na relação entre abordagens metodológicas (algoritmos, instrumentos e aplicações), produtos investigados e períodos de publicação. As duas primeiras dimensões da MCA explicaram 9.59% da inércia total (Dim1: 4.82%, Dim2: 4.77%), valor coerente com a alta dimensionalidade do corpus analisado (148 estudos, 33 variáveis categóricas binárias), indicando uma estrutura conceitual diversificada no campo (Figura 3).

![Biplot de Análise de Correspondência Múltipla (ACM) sobre a evolução temporal das aplicações de ML para autenticação de indicações geográficas (2010-2025).](2-FIGURAS/2-EN/mca_biplot_temporal_completo.png){#fig:mca_temporal width="80%"}

*Nota: As elipses coloridas (intervalos de confiança de 95%) representam três períodos temporais: 2010-2018 (verde, n=26), 2019-2021 (laranja, n=27) e 2022-2025 (roxo, n=95). Cada ponto representa um estudo individual, com formas indicando a abordagem metodológica principal: círculos representam estudos focados em algoritmos, quadrados representam estudos focados em instrumentos/técnicas analíticas, e triângulos representam estudos focados em aplicações. Rótulos de produtos (Wine, Honey, Olive, Coffee) são exibidos sobre os pontos correspondentes. As dimensões 1 e 2 explicam 4,82% e 4,77% da variância total, respectivamente.*

Como pode ser visto na Figura 3, o padrão temporal revela três fases. Entre 2010 e 2018, predomina uma fase de consolidação metodológica, concentrada em produtos tradicionais europeus (especialmente vinhos) e em técnicas espectroscópicas consolidadas (NIR, FTIR) combinadas a algoritmos clássicos como PLS-DA e SVM, com relativa homogeneidade de abordagens [@Mohammadi2024; @Rebiai2022]. O período intermediário (2019–2021) marca uma transição, na qual a democratização de ferramentas de ML e o acesso ampliado a técnicas analíticas avançadas favorecem a diversificação de produtos (incluindo chás e plantas medicinais asiáticos) e a adoção gradual de algoritmos como Random Forest e redes neurais [@Liakos2018]. A fase recente (2022–2025), que concentra 64% do corpus, corresponde a uma expansão rápida e heterogênea, com crescimento das aplicações de Deep Learning, metabolômica *untargeted*, abordagens multimodais e estratégias de transfer learning [@He2024; @Liu2025; @Wang20218065; @Peng2025; @Feng2025]. A Figura 4 apresenta a análise de redes de co-ocorrência.

![Análise de Redes de Co-ocorrência. (a) Rede completa mostrando as comunidades temáticas entre algoritmos, produtos e técnicas. (b) Rede focada na co-ocorrência entre algoritmos de ML e produtos.](2-FIGURAS/2-EN/network_centrality_metrics.png){#fig:network_analysiss}
{#fig:network_analysis_B}

A dinâmica temporal da produção científica (Figura 5 (a)) revela crescimento exponencial superior a 400% entre 2018 e 2024, reflexo da democratização de ferramentas de ML e da expansão de técnicas analíticas de alta performance [@Liakos2018]. Paralelamente, a transição paradigmática nos algoritmos empregados (Figura 5 (b)) evidencia a substituição gradual de métodos quimiométricos clássicos (PLS-DA, predominante até 2018) por algoritmos com maior capacidade preditiva e flexibilidade (Random Forest, SVM a partir de 2019), culminando na emergência de Deep Learning e CNNs após 2022, voltados ao processamento de dados hiperespectrais e não estruturados [@Lavine2005; @Shah2019].

![Evolução temporal de (a) número de publicações e (b) adoção dos principais algoritmos de Machine Learning em estudos de IGs.](2-FIGURAS/2-EN/evolucao_temporal.png){#fig:temporal_algoritmos width="80%"}

## 3.3 Domínios de Aplicação, Produtos e Padrões de Distribuição Geográfica

A análise do corpus revelou que as aplicações de Machine Learning em Indicações Geográficas concentram-se predominantemente em produtos agroalimentares, com ênfase em bebidas alcoólicas, carnes processadas e produtos agrícolas especializados (Tabela 3). Essa distribuição reflete a convergência entre mercados de elevada remuneração, incidência significativa de fraude e adulteração e ampla disponibilidade de métodos analíticos capazes de gerar grandes volumes de dados multivariados adequados ao processamento por ML.

A Tabela 3 apresenta síntese dos principais produtos e regiões geográficas estudadas no corpus, destacando a prevalência de determinadas aplicações por categoria de produto.

| **Categoria de Produto** | **Exemplos Específicos**                            | **Indicações Geográficas Primárias**                   | **Técnicas ML Predominantes**    | **Frequência Relativa** |
| ------------------------------ | ---------------------------------------------------------- | ---------------------------------------------------------------- | --------------------------------------- | ------------------------------ |
| Vinhos e Bebidas Alcoólicas   | Vinho tinto, branco, rosé; destilados de frutas; vinagres | Douro, Rioja, Bordeaux, Denominação de Origem Controlada (DOC) | Random Forest, SVM, PLS-DA              | 34%                            |
| Chás                          | Wuyi Rock Tea, Liupao, Oolong, Green Tea                   | China (Fujian, Zhejiang, Yunnan)                                 | NIR + PLS-DA, GC-MS + ML                | 18%                            |
| Carnes Processadas             | Cordeiro, Presunto, Carne Bovina                           | Jinhua (China), Cordeiro Europeu PGI, Carne Halal                | Elemental Analysis + SVM, Deep Learning | 15%                            |
| Frutas e Hortaliças           | Citros, Cebola Tropea, Frutos Vermelhos                    | Sicília, Calabria (Itália), Regions diversas                   | Metabolômica + Random Forest, NIR      | 12%                            |
| Plantas Medicinais             | Panax notoginseng (Ginseng), Ervas Medicinais              | Yunnan (China), Regiões Ásia                                   | Metabolômica Untargeted, CNN           | 8%                             |
| Azeites                        | Azeite Extra Virgem, Azeite                                | Região Mediterrânea, Italia, España                           | Fingerprinting NIR, SVM                 | 8%                             |
| Mel                            | Mel Floral, Mel Silvestre                                  | Lages (Brasil), Regiões Europa                                  | Espectrometria Elementar, PLS-DA        | 5%                             |

*Tabela 3: Distribuição de produtos agroalimentares com Indicações Geográficas por categoria, regiões geográficas associadas, técnicas de Machine Learning predominantes e frequência relativa de estudos no corpus analisado (N=148).*

Vinhos de origem protegida, como os das denominações Douro, Rioja e Bordeaux, e chás com indicação geográfica, como o Wuyi Rock Tea, constituem a principal frente de aplicação. Nesses estudos, a discriminação de origem é construída a partir de *fingerprinting* metabolômico e análise de traços elementares, demonstrando que o perfil químico dessas bebidas está intimamente associado às condições geográficas de produção e a fatores ambientais do terroir [@Ramos2025; @Xu2021]. Carnes e produtos cárneos (por exemplo, cordeiro de regiões específicas e presunto de Jinhua) configuram um segundo bloco relevante, no qual a discriminação de origem se baseia sobretudo em assinaturas elementares e isotópicas processadas por algoritmos como Random Forest e SVM [@Chen2020].

Segmentos como frutas, hortaliças e plantas medicinais expandem esse quadro para uma diversidade maior de matrizes. Em frutas e hortaliças, o ML é empregado para rastrear origem a partir de *fingerprints* metabólicos e perfis nutricionais, explorando a hipótese de que a assinatura bioquímica dos produtos reflete condições edafoclimáticas específicas [@Luan2020; @Peng2025]. No caso de plantas medicinais como o *Panax notoginseng*, a certificação de origem relaciona-se também à potência farmacológica, reforçando o vínculo entre localização geográfica, composição bioativa e valor agregado [@Feng2025].

Do ponto de vista geográfico, observa-se predominância de estudos conduzidos em instituições da Ásia, particularmente na China, seguida pela Europa. Brasil e outras economias emergentes aparecem em proporção menor, o que reflete, por um lado, os investimentos recentes chineses em tecnologias de rastreabilidade [@Wang2025] e, por outro, a consolidação de infraestrutura analítica em contextos europeus. Para o Brasil, essa assimetria evidencia uma lacuna e, simultaneamente, uma oportunidade estratégica para desenvolver aplicações de ML voltadas à proteção e valorização de IGs nacionais.

### 3.3.1 Análise Bibliométrica

A Lei de Lotka, foi aplicada ao corpus de 148 estudos filtrados, revelando uma distribuição de produtividade autoral que segue aproximadamente o padrão esperado pela lei, com expoente n ≈ 2. A análise identificou 869 autores únicos, dos quais 623 (71,7%) publicaram apenas um artigo, 152 (17,5%) publicaram dois artigos, e apenas 1 autor publicou 28 artigos (Li), indicando uma concentração moderada de produtividade em poucos autores. Essa distribuição sugere que o campo de ML em IGs é colaborativo, com muitos pesquisadores contribuindo esporadicamente, mas com alguns autores altamente produtivos, possivelmente especialistas em quimiometria ou análise instrumental.

A aplicação do princípio de Pareto (80/20) resultou na seleção dos 20% dos artigos com maior pontuação combinada, calculada pela Equação 6 (40% qualidade metodológica, 35% relevância temática, 25% impacto bibliométrico). A Tabela 4 apresenta os 10 artigos selecionados com maior pontuação.

| **Posição** | **Artigo**        | **Pontuação Combinada** | **Principais Contribuições**                |
| ------------------- | ----------------------- | ------------------------------- | --------------------------------------------------- |
| 1                   | Li et al. (2025)        | 95.2                            | Deep Learning para autenticação de chás chineses |
| 2                   | Wang et al. (2025)      | 92.8                            | Blockchain + ML para rastreabilidade                |
| 3                   | Ramos et al. (2025)     | 90.5                            | Metabolômica untargeted em vinhos                  |
| 4                   | Peng et al. (2025)      | 88.9                            | CNN para imagens hiperespectrais                    |
| 5                   | Jiang et al. (2025)     | 87.3                            | Classificação multi-espectral                     |
| 6                   | Xu et al. (2021)        | 85.7                            | Random Forest em perfis elementares                 |
| 7                   | Chen et al. (2020)      | 84.1                            | SVM em carnes processadas                           |
| 8                   | Mohammadi et al. (2024) | 82.6                            | NIR + PLS-DA em azeites                             |
| 9                   | Rebiai et al. (2022)    | 81.2                            | Espectroscopia em vinhos europeus                   |
| 10                  | Feng et al. (2025)      | 79.8                            | Redes neurais em plantas medicinais                 |

*Tabela 4: 10 artigos selecionados pelo princípio de Pareto (80/20) no corpus de 148 estudos.*

## 3.4 Técnicas de Machine Learning Empregadas

## 3.5 O Ecossistema Algorítmico na Autenticação de IGs

A análise do corpus bibliográfico revela um ecossistema algorítmico diversificado, mas estruturado em torno de poucos núcleos tecnológicos. Longe de indicar fragmentação, essa variedade reflete que diferentes matrizes, tamanhos amostrais e contextos regulatórios exigem soluções computacionais ajustadas. Predominam algoritmos de classificação supervisionada, com Random Forest e Support Vector Machines (SVM) respondendo, em conjunto, por cerca de dois terços das aplicações. @Xu2021 empregaram Random Forest para discriminar a origem de vinhos a partir de perfis elementares, alcançando acurácia superior a 95%, enquanto @Mohammadi2024 integraram SVM com kernel RBF para autenticar azeites a partir de espectroscopia NIR em um cenário de alta dimensionalidade.

Do ponto de vista funcional, esses modelos podem ser entendidos como dispositivos que transformam vetores de características $x$, compostos por intensidades espectrais, concentrações elementares ou abundâncias de metabolitos em decisões sobre origem geográfica. Nos estudos com PLS-DA e SVM, essa transformação assume, em sua forma mais simples, a estrutura de uma função de decisão linear $f(x) = w^\top x + b$, na qual a combinação ponderada das variáveis ($w$) sintetiza um “hiperplano territorial” que separa amostras de diferentes regiões. A formulação em espaços de alta dimensionalidade, sobretudo no caso de SVM com kernels não lineares, permite que essa fronteira de decisão capture relações complexas entre marcadores químicos e território, mantendo, ao mesmo tempo, a possibilidade de interpretar $w$ como vetor que concentra os pesos das evidências analíticas em favor de cada origem.

O uso amplo do Random Forest decorre de sua capacidade de modelar interações não lineares em dados multivariados, lidar com classes desbalanceadas e, sobretudo, fornecer medidas de importância de variáveis (VIM) que permitem identificar marcadores territoriais com valor regulatório. Em termos formais, esses modelos operam como comitês de classificadores $h_m(x)$, agregados em uma decisão final $\hat{y} = \mathrm{agg}(h_1(x), \dots, h_M(x))$, usualmente por maioria de votos ou média de probabilidades. Em estudos como @Li2025, essa arquitetura de comitê foi explorada para isolar subconjuntos de variáveis químicas e elementares que sustentam, de forma transparente, alegações de autenticidade geográfica, uma vez que as VIM indicam quais componentes de $x$ mais contribuem para alterar $\hat{y}$ de uma denominação para outra.

Em domínios com dados de imagem ou sinais hiperespectrais, modelos de Deep Learning, especialmente Redes Neurais Convolucionais (CNNs), constituem o padrão emergente. @Peng2025 utilizaram CNNs para classificar chás com IG a partir de imagens hiperespectrais, obtendo discriminação precisa entre diferentes regiões produtoras; @Feng2025 aplicaram arquiteturas profundas para autenticar visualmente plantas medicinais. Nesses modelos, a operação central de convolução pode ser descrita como $(K * X)(i,j) = \sum_{u,v} K(u,v) \cdot X(i-u, j-v)$, em que um filtro $K$ varre a matriz de entrada $X$ (imagem ou “cubo” espectral) para extrair padrões locais característicos. Essa formalização reforça que a autenticação não se apoia apenas em valores pontuais de intensidade, mas em estruturas espaciais ou espectrais recorrentes que codificam o terroir de forma distribuída.

Para dados espectrais e quimiométricos, a Análise Discriminante por Mínimos Quadrados Parciais (PLS-DA) permanece central em quase metade dos estudos, consolidando um paradigma bem estabelecido em quimiometria. @Rebiai2022 demonstraram que PLS-DA, acoplada a espectroscopia NIR, discrimina azeites de múltiplas denominações com elevada acurácia, explorando sua robustez frente à multicolinearidade e ao regime $n < p$. Diferentemente da Análise de Componentes Principais (PCA), que busca representar a variância total dos dados, a PLS-DA otimiza explicitamente a separação entre classes, o que a torna particularmente adequada para problemas de autenticação de origem.

O manejo da alta dimensionalidade aparece como eixo transversal. A PCA é utilizada em mais da metade dos estudos como etapa de pré-processamento para redução de dimensionalidade, diminuição de ruído e visualização exploratória, frequentemente antes da aplicação de classificadores supervisionados. @Ramos2025, por exemplo, aplicaram PCA para condensar milhares de variáveis metabolômicas de vinhos em poucos componentes principais interpretáveis, que em seguida alimentaram um modelo de Random Forest. Em paralelo, métodos de seleção de *features* como RF-RFE e Boruta, presentes em cerca de um terço dos trabalhos, são empregados para identificar subconjuntos de variáveis com maior poder discriminante. @Salam2021 mostraram que o uso de Boruta permitiu reduzir de 80 para 15 elementos traço em estudos com carnes, sem perdas significativas de desempenho. Essa combinação entre redução/seleção de variáveis e classificadores robustos é central não apenas para controlar o risco de sobreajuste e reduzir custos computacionais, mas também para chegar a conjuntos compactos de marcadores territoriais com potencial de serem incorporados em protocolos oficiais de certificação.

Neste sentido, o ecossistema algorítmico observado neste corpus indica que a escolha de modelos em IGs não segue uma lógica meramente incremental (substituir um algoritmo por outro "mais moderno"), mas é condicionada pela natureza da matriz, pela estrutura dos dados e pelo grau de exigência regulatória. Random Forest, SVM, PLS-DA e CNNs ocupam posições complementares em uma paisagem metodológica em que desempenho preditivo, interpretabilidade e adequação ao tipo de dado precisam ser negociados caso a caso.

Essa necessidade de interpretabilidade transcende o domínio técnico, constituindo-se em requisito fundamental para a validade jurídica e a legitimidade social das decisões de certificação. Em contextos regulatórios como os das Indicações Geográficas, onde a prova de origem deve ser defensável em processos administrativos ou judiciais, algoritmos como Random Forest e PLS-DA, que fornecem medidas de importância de variáveis ou *loadings* explicitáveis, oferecem uma vantagem crítica sobre modelos de "caixa-preta" como redes neurais profundas. Essa transparência algorítmica não apenas facilita a auditoria científica, mas também reforça a confiança dos stakeholders, produtores, consumidores e reguladores, na integridade do sistema de certificação, transformando a ML de uma ferramenta técnica em um instrumento de governança territorial [@Lundberg2017; @He2024].

## 3.7 Desempenho Preditivo dos Modelos

A análise do corpus revela que os modelos de Machine Learning alcançam um desempenho preditivo substancial, com acurácias frequentemente situadas entre 80% e 100%, o que sugere que a assinatura geográfica dos produtos é computacionalmente detectável. Em termos formais, esses modelos podem ser representados como funções $\hat{y} = f(x)$ que mapeiam vetores de entrada $x$ (perfís espectrais, vetores elementares, painéis metabolômicos) para saídas categóricas (origem, presença de fraude) ou contínuas (parâmetros de qualidade). Quando o objetivo é regressão de atributos como acidez, teor de fenóis ou intensidade aromática, a qualidade do ajuste passa a ser expressa pela discrepância entre valores observados $y$ e preditos $\hat{y}$, usualmente medida por métricas como erro absoluto médio (MAE) e raiz do erro quadrático médio (RMSE), que sintetizam, em escalas distintas, a magnitude típica de $|y - \hat{y}|$ no espaço de decisão.

Contudo, essa performance é altamente heterogênea e sua interpretação depende criticamente do rigor metodológico empregado, especialmente no que tange à validação. Acurácias de 100%, por exemplo, foram relatadas em contextos de classificação binária com alta separabilidade entre classes, como na distinção do presunto de Jinhua ou do chá Wuyi Rock, onde marcadores químicos ou isotópicos únicos podem, teoricamente, permitir uma diferenciação perfeita [@Chen2020; @Effrosynidis2021]. Esse cenário corresponde empiricamente a situações em que o risco observado, calculado a partir da média de uma função de perda $L(y, \hat{y})$ sobre o conjunto de treinamento, tende a zero. O ceticismo em relação a tais resultados é justificado, pois raramente são acompanhados de validação externa robusta que permita estimar o risco verdadeiro, isto é, o desempenho esperado quando o modelo é exposto a novas amostras distribuídas segundo o mesmo processo gerador, mas não utilizadas no ajuste dos parâmetros de $f$.

Um padrão de desempenho mais comum e realista, observado em problemas multiclasse como a discriminação entre múltiplas denominações de origem de vinhos, situa-se na faixa de 88% a 99%. Estudos que alcançam alta performance, como sensibilidade superior a 99,3% na discriminação de espécies de carne, frequentemente empregam procedimentos de validação cruzada rigorosos, como repeated k-fold e leave-one-out, que conferem maior confiabilidade aos achados [@Mohammadi2024; @Meena2024]. A detecção de fraudes e adulterações, uma aplicação central presente em 54% dos estudos, ilustra bem essa dinâmica. Nesses casos, o desempenho é frequentemente medido em termos de sensibilidade e especificidade para evitar falsos negativos, e técnicas para lidar com o desbalanceamento de classes são comuns.

O ponto mais crítico identificado nesta revisão, contudo, é a lacuna na generalização dos modelos. Apenas 23% dos estudos analisados empregaram validação externa com amostras de origens geográficas não representadas no conjunto de treinamento. Quando essa validação foi realizada, observou-se uma queda na acurácia entre 2% e 15%, um fenômeno consistente com a degradação de desempenho esperada quando modelos são confrontados com distribuições levemente deslocadas em relação àquelas usadas para estimar $f(x)$ [@Kuhn2013]. Em termos de risco, essa discrepância entre o erro empírico (medido no conjunto de treinamento ou em validações internas) e o risco verdadeiro (associado ao uso do modelo em certificação real) revela que muitos sistemas operam, de fato, em condições de otimismo estatístico não controlado. Esta observação possui uma implicação direta para a prática da certificação pois, para que um modelo de ML seja juridicamente defensável e cientificamente robusto, ele deve ser obrigatoriamente testado em amostras que desafiem sua capacidade de generalização para além das condições vistas durante o treinamento, incluindo safras, regiões e lotes distintos.

Essa falha de validação externa não representa apenas uma limitação metodológica, mas um risco reputacional e econômico substancial para as Indicações Geográficas. Um modelo superestimado pode levar à certificação incorreta de produtos, erodindo a confiança do consumidor no selo de origem e depreciando o valor premium associado ao terroir [@He2024]. Em termos econômicos, a exposição de fraudes não detectadas ou falsos positivos pode resultar em litígios, perda de mercado e desvalorização de ativos intangíveis, transformando o otimismo estatístico em uma vulnerabilidade sistêmica que ameaça a sustentabilidade das IGs como estratégia de desenvolvimento territorial.

Complementarmente, foi conduzida uma análise de modelagem preditiva global para avaliar em que medida os padrões estatísticos capturados pelas variáveis do corpus permitem antecipar um índice contínuo de pontuação dos estudos e uma classificação dicotômica entre trabalhos de "alto score" e demais artigos. Na tarefa de regressão, comparando modelos lineares e não lineares, a performance foi modesta: o erro médio quadrático (RMSE) variou entre 11,8 e 12,5 e o coeficiente de determinação $R^2$ permaneceu baixo (0,11–0,14) mesmo para os melhores modelos (Ridge e Random Forest). Segundo @Hair2010, valores de $R^2$ abaixo de 0,25 indicam relações fracas entre as variáveis preditoras e a variável dependente. Esse resultado indica que, embora os modelos de ML sejam altamente eficazes para discriminar a origem geográfica de produtos, a predição de um índice sintético de qualidade/impacto dos estudos a partir de variáveis bibliométricas e metodológicas agregadas é substancialmente mais difícil, reforçando o papel insubstituível do julgamento humano na avaliação qualitativa dos artigos [@Wang2013]. 

Na tarefa de classificação (alto score vs. demais), o modelo de Regressão Logística apresentou desempenho superior ao Random Forest (acurácia de 0,69 e F1-score de 0,70, contra 0,53 de acurácia para Random Forest), sugerindo que o padrão que distingue os estudos mais bem avaliados é relativamente simples e pode ser capturado adequadamente por fronteiras de decisão aproximadamente lineares [@Rudin2019]. Em conjunto, esses achados apontam para uma assimetria que, os mesmos algoritmos que atingem acurácias próximas de 100% em autenticação de produtos mostram desempenho apenas moderado quando aplicados à avaliação global da qualidade dos estudos. A Figura 6 destaca as abordagens lineares simples que apresentam desempenho semelhante a algoritmos mais complexos na predição do score e da categoria de alto score.

![Comparação do desempenho de modelos de regressão e classificação para predição do score contínuo e da categoria de alto score dos estudos.](2-FIGURAS/2-EN/model_metricas_comparacao.png){#fig:model_metricas width="80%"}

## 3.8 Aplicações Temáticas Identificadas

A análise temática do corpus revelou cinco arquiteturas funcionais predominantes nas aplicações de Machine Learning em Indicações Geográficas, cada qual respondendo a demandas específicas de certificação, controle de qualidade e rastreabilidade. Essas arquiteturas refletem a diversidade dos desafios enfrentados na autenticação de produtos com IG, assim como, representam uma evolução paradigmática na própria governança da prova de origem [@Zhang2024]. Ao mover a validação territorial de um domínio de expertise tácita e subjetiva para um de evidência computacional auditável, o ML redefine o que constitui "prova de origem", transformando a certificação de um processo empírico em um sistema de verificação algorítmica que integra dados analíticos, conhecimento territorial e marcos regulatórios.

A primeira arquitetura, mais frequente no corpus analisado (79% dos estudos), visa estabelecer procedência territorial através de análise multivariada de assinaturas analíticas. @Xu2021 fundamentam teoricamente esta aplicação no pressuposto de que origem geográfica inscreve impressão química detectável, fingerprints metabolômicos, assinaturas elementares, perfis isotópicos, que manifestam padrões distintivos entre regiões devido a interações gene × ambiente × microbiota específicas de cada terroir. Em termos operacionais, esses estudos constroem funções de decisão $f(x)$ que particionam o espaço de características em regiões associadas a denominações específicas, de modo que cada vetor $x$ de intensidades ou concentrações seja mapeado para uma origem estimada $\hat{y}$. A fronteira entre essas regiões, aprendida a partir de dados rotulados, representa, em termos matemáticos, a noção de prova de origem ao traduzir diferenças físico-químicas em classificações reprodutíveis.

Autores como @Li2025 e @Ratnasekhar2025 demonstraram que fingerprinting metabolômico integrado a Random Forest, análise de traços elementares via ICP-MS acoplada a SVM, e caracterização isotópica de proporções ¹²C/¹³C, ¹⁴N/¹⁵N, ¹H/²H e ³²S/³⁴S processada por LDA ou PLS-DA constituem as estratégias metodológicas predominantes. @Chen2020 e @Luan2020 reportaram acurácias variando entre 82% e 99%, com concentração modal entre 90% e 97%, evidenciando que discriminação computacional de origem é não apenas exequível, mas alcança níveis de confiabilidade compatíveis com requisitos de certificação formal em múltiplos contextos territoriais.

A segunda arquitetura funcional, focada na identificação de produtos falsificados, adulterados ou misturados, foi documentada por @Salam2021 e @Loyal2022 como presente em 54% dos estudos, respondendo a desafios econômicos críticos em mercados de alto valor agregado. @Mohammadi2024 categorizaram práticas fraudulentas específicas identificadas onde, a adição de etanol industrial a bebidas alcoólicas, mistura de produtos de denominação protegida com não-protegidos (conhecido como "corte" de vinhos), e falsificação de processos tradicionais mediante envelhecimento artificial versus natural em presuntos. Nesses cenários, os modelos deixam de apenas atribuir rótulos de origem e passam a aproximar probabilidades $\hat{p}(y = \text{fraude} \mid x)$, a partir das quais se estabelece um limiar de decisão $t$ tal que amostras com $\hat{p} \geq t$ são classificadas como suspeitas. A escolha de $t$, frequentemente calibrada por curvas ROC, reflete explicitamente a assimetria de custos entre falsos negativos (fraude não detectada) e falsos positivos (produto autêntico indevidamente sinalizado), deslocando a arquitetura para regimes em que sensibilidade máxima é priorizada mesmo à custa de alguma perda de especificidade.

Em estudos similares, @Salam2021 e @Loyal2022 demonstraram que esta aplicação emprega predominantemente classificação binária (autêntico versus adulterado), frequentemente beneficiando-se de estratégias de balanceamento de classes, oversampling de amostras fraudulentas, undersampling de autênticas, para maximizar sensibilidade à fraude, priorizando a não ocorrência de falsos negativos. @Chen2020 e @Effrosynidis2021 enfatizam que métricas de desempenho são reportadas preferencialmente em termos de sensibilidade e especificidade, ao invés de acurácia global, refletindo a criticidade assimétrica dos erros onde falhar em detectar fraude possui consequências regulatórias, econômicas e reputacionais substancialmente mais graves que classificar erroneamente produto autêntico como suspeito.

Representando a terceira arquitetura funcional, @Wang2025 identificaram que 31% dos estudos abordam estabelecimento de continuidade entre produto final e origem de matéria-prima, respondendo a demandas crescentes de transparência e responsabilidade em cadeias complexas de suprimento. @Gong2023 documentaram tendência emergente particularmente inovadora neste domínio. A integração de Machine Learning com blockchain, observada em 21% dos estudos de rastreabilidade, onde modelos preditivos são codificados em smart contracts que verificam autenticidade de lotes em cada etapa distributiva.

Autores como @Wang2025 argumentam que esta arquitetura híbrida, algoritmos de ML operando sobre dados imutáveis em blockchain, permite auditoria computacional de cadeia de suprimento, reduzindo fraude intermediária através de verificação descentralizada e tamper-proof. @Hu2024 demonstraram aplicação prática desta convergência tecnológica em cadeias de chá chinês, onde sensores IoT capturam dados ambientais durante processamento e transporte, ML valida conformidade com perfis esperados, e blockchain registra permanentemente cada verificação, criando "passaporte digital" rastreável do produto.

A análise de agrupamento (k-means e hierárquico) organizada sobre as variáveis de produto, instrumento analítico, algoritmo e tipo de aplicação revelou a existência de dez clusters bem definidos, que sintetizam famílias tecnológicas recorrentes no campo. Entre eles, destacam-se um cluster centrado em aplicações de autenticação e detecção de fraude em mel, combinando espectroscopia NIR com classificadores SVM e KNN, com forte presença de estudos asiáticos, um cluster dominado por queijos europeus, nos quais redes neurais e espectroscopia NIR são mobilizadas para discriminação de origem, e um conjunto de estudos que integra LC-MS e GC-MS em matrizes como mel e carnes, associadas a SVM, Random Forest e métodos baseados em árvores decisórias.

Outro cluster relevante reúne aplicações com ICP-MS em carnes e produtos cárneos, nas quais a análise de traços elementares é combinada a algoritmos de classificação para autenticação territorial (Figura 7). Esses agrupamentos mostram que a adoção de técnicas de ML demostra que, instrumentos e algoritmos tendem a se articular em ecossistemas coerentes, nos quais determinadas combinações (por exemplo, NMR + redes neurais em vinhos, FTIR + SVM em azeites) se consolidam como arquiteturas de referência para problemas específicos. Do ponto de vista metodológico, essa estrutura em clusters reforça a existência de caminhos tecnológicos preferenciais, que podem orientar decisões de desenho experimental em futuras aplicações de ML em Indicações Geográficas [@Qi2021; @Li2025review].

A Figura 7 apresenta o heatmap dos perfis de clusters, evidenciando como combinações específicas de produtos, instrumentos analíticos e algoritmos se organizam em dez famílias tecnológicas recorrentes.

![Heatmap dos perfis de clusters de estudos, mostrando a coocorrência de produtos, instrumentos analíticos e algoritmos de machine learning em dez grupos principais.](2-FIGURAS/2-EN/cluster_heatmap_profiles.png){#fig:cluster_heatmap width="80%"}

A quarta arquitetura funcional, identificada por @Meena2024 e @Liu2025 em 47% dos estudos, emprega ML para predição de atributos de qualidade, acidez, índice de fenóis totais, capacidade antioxidante, textura, perfil sensorial, com base em dados analíticos rapidamente obtidos. @Peng2025 e @Feng2025 distinguem esta aplicação da autenticação por seu objetivo funcional divergente. Ao invés de responder, que determinado produto é de origem X, o método busca-se determinar qual qualidade espera-se desta amostra. Nesses casos, a função $f(x)$ é estimada para aproximar, com erro mínimo, as variáveis contínuas de interesse, e o desempenho é quantificado por coeficientes de determinação (R²), MAE e RMSE que refletem o desvio médio entre $y$ e $\hat{y}$ em unidades fisicamente interpretáveis (por exemplo, g/L, unidades de cor, escores sensoriais). @Meena2024 documentaram que regressão constitui a abordagem predominante neste contexto (ao invés de classificação), com avaliação de desempenho através de R², MAE e RMSE, refletindo natureza contínua das variáveis de qualidade.

Ainda, @Liu2025 e @Rebiai2022 argumentam que esta aplicação possui valor industrial imediato ao viabilizar avaliação rápida, não-destrutiva e padronizada de qualidade, substituindo análises sensoriais subjetivas ou ensaios químicos demorados por predições espectrométricas instantâneas calibradas por ML. Nesse cenário, a relação entre erro de predição e incerteza analítica torna-se central, modelos cujo RMSE é da mesma ordem de magnitude que o erro instrumental pouco agregam à prática @Ozaki2021, ao passo que modelos em que o RMSE é substancialmente inferior ao desvio típico de métodos convencionais criam, de fato, uma nova camada de controle de qualidade acessível a operações de pequena e média escala [@Ferreira2007; @Todeschini2015].

Por fim, a quinta arquitetura funcional, embora menos prevalente com 19% dos estudos conforme @Ramos2025, emprega ML para elucidar fatores que influenciam aceitação e preferência de consumidores por produtos com indicação geográfica, abordando dimensão mercadológica relevante para a sustentabilidade econômica destes sistemas. @Effrosynidis2021 documentaram que estudos nesta categoria frequentemente empregam Partial Least Squares Structural Equation Modeling (PLS-SEM) para modelar relações complexas entre atributos analíticos (composição química, perfil sensorial), características demográficas do consumidor (idade, renda, educação) e variáveis comportamentais (intenção de compra, disposição a pagar premium). @Ramos2025 argumentam que, embora menos frequente que autenticação técnica, esta aplicação é estrategicamente relevante ao permitir compreender como indicação geográfica agrega valor percebido, identificar segmentos de consumidores dispostos a valorizar origem territorial, e otimizar estratégias de comunicação que conectem assinaturas analíticas (terroir) a atributos valorizados pelos consumidores, fechando o ciclo entre autenticação técnica e valorização mercadológica.

## 3.9 Tendências Metodológicas, Lacunas e Direções para Pesquisa Futura

A análise de comunidades com o algoritmo de Louvain [@Blondel2008] aplicada à rede de coocorrências (20 nós, 58 arestas, densidade = 0,305, clustering = 0,595) revelou três módulos tecnológicos bem definidos, sintetizados na Tabela 5. Essa estrutura modular indica que o campo de ML para IGs está organizado em subcampos especializados, onde combinações recorrentes de algoritmos, técnicas analíticas e matrizes alimentares conformam plataformas metodológicas estáveis.

| **Módulo** | **Algoritmos Principais**                 | **Técnicas Analíticas**               | **Produtos**         | **Região Predominante** |
| :---------------: | :---------------------------------------------- | :-------------------------------------------- | :------------------------- | :----------------------------- |
|   **M1**   | Random Forest, Decision Tree, Gradient Boosting | Espectroscopia (NIR), Quimiometria            | Vinho, Mel                 | África, Europa                |
|   **M2**   | SVM, KNN                                        | Cromatografia (GC-MS, LC-MS, HPLC)            | Carnes, Produtos Regionais | Ásia                          |
|   **M3**   | Neural Networks, CNN, Deep Learning             | Espectroscopia (NIR, FTIR), Sensores (e-nose) | Azeite, Queijo, Chá       | Europa, Ásia                  |

*Tabela 5: Módulos tecnológicos identificados pela análise de comunidades de Louvain na rede de coocorrências de algoritmos, técnicas analíticas e produtos com Indicação Geográfica.*

A estrutura interna de cada módulo, visualizada na Figura 8, revela padrões de coesão e especialização que fundamentam a organização do campo. O Módulo 1 (Árvores + Espectroscopia) apresenta alta densidade interna (0,60), conectando fortemente Random Forest, Decision Tree e Gradient Boosting a produtos como vinho e mel, com predomínio de aplicações em terroirs africanos e europeus. Essa coesão reflete a consolidação de uma plataforma metodológica madura, na qual classificadores de árvore dominam a autenticação por assinaturas espectrais NIR, explorando a capacidade desses algoritmos de modelar interações não-lineares entre marcadores químicos e origem territorial [@Resce2022; @Oganesyants2024].

O Módulo 2 (SVM/KNN + Cromatografia) caracteriza-se por uma arquitetura mais dispersa (densidade = 0,53), conectando SVM e KNN a técnicas cromatográficas de alta resolução (GC-MS, LC-MS) aplicadas predominantemente a carnes e produtos regionais asiáticos. Essa configuração reflete um nicho metodológico especializado em metabolômica direcionada (*targeted*) e huellado cromatográfico, no qual a separação física de compostos precede a classificação algorítmica, uma abordagem particularmente efetiva para matrizes complexas com perfis voláteis e semivoláteis [@Santoma2025; @Shuai2022].

O Módulo 3 (Redes Neurais + Sensores), e internamente coeso (densidade = 0,68), integra Neural Networks, CNN e Deep Learning a instrumentos espectroscópicos (NIR, FTIR) e sensores portáteis (e-nose) aplicados a azeite, queijo e chá, com estudos concentrados em contextos europeus e asiáticos. Esse módulo representa a fronteira tecnológica do campo, explorando arquiteturas profundas capazes de processar sinais hiperespectrais e dados não estruturados, viabilizando autenticação *in-situ* e democratização de certificação [@Gazeli2020; @Fu2023; @Li2025].

As métricas de centralidade corroboram o papel estruturante desses módulos em que, `NeuralNetwork` apresenta a maior centralidade global (degree = 15, betweenness = 0,306), atuando como conector entre o Módulo 3 e os demais, enquanto `SVM` (degree = 12) e `RandomForest` (degree = 11) funcionam como núcleos dos Módulos 2 e 1, respectivamente. Destaca-se o papel de ponte desempenhado por plataformas cromatográficas (`GCMS` betweenness = 0,186; `LCMS` betweenness = 0,105), que conectam o Módulo 2 aos demais, viabilizando fluxos informacionais entre nichos metodológicos e facilitando a transição entre paradigmas tecnológicos [@Csardi2006].


![Estrutura interna dos três módulos tecnológicos identificados pelo algoritmo de Louvain. Cada painel mostra as conexões entre algoritmos (vermelho), técnicas analíticas (azul), produtos (verde) e regiões (laranja) dentro de cada comunidade especializada.](2-FIGURAS/2-EN/louvain_modules_detailed.png){#fig:louvain_modules width="100%"}

@Luan2020 documentaram que a integração de modalidades de dados distintas (metabolômica, perfil elementar, análise isotópica e sensorial) com algoritmos de *ensemble* vem crescendo, representando 28% dos estudos recentes (2024-2025). Essa fusão multimodal reconhece que a origem geográfica resulta de interações complexas entre fatores ambientais e práticas produtivas, e busca capturar complementaridades informacionais entre diferentes tipos de dados para aumentar poder discriminativo e robustez preditiva.

Uma lacuna metodológica crítica surge na transferência de aprendizagem entre regiões geográficas. Foram observados poucos estudos que testam modelos treinados em uma região quando aplicados a outras regiões. @Chen2020 e @Ramos2025 documentaram que transfer learning, técnica onde conhecimento adquirido em uma tarefa é reutilizado em outra, emerge como estratégia em desenvolvimento em 12% dos estudos, sobretudo em arquiteturas de Deep Learning. A estratégia oferece a possibilidade de que modelos desenvolvidos para vinhos de Bordeaux poderiam ser adaptados para vinhos de Rioja com amostras limitadas, reduzindo dramaticamente demanda por dados extensivos específicos de cada região e viabilizando certificação em territórios com recursos analíticos restritos [@Milojevic2011].

@Effrosynidis2021 identificaram ênfase crescente, embora ainda minoritária (14% dos estudos), em explicabilidade de modelos de ML através de técnicas como SHAP (SHapley Additive exPlanations) e LIME (Local Interpretable Model-agnostic Explanations). Para sistemas de certificação, interpretabilidade transcende requisito técnico constituindo-se em necessidade regulatória e social. Certificadores e produtores demandam compreensão não apenas de qual origem o modelo prevê, mas quais variáveis específicas, quais assinaturas analíticas territoriais, fundamentam cada predição. Enquanto Random Forest fornece naturalmente métricas de importância de variáveis, SHAP permite atribuição de contribuição específica de cada feature a cada predição individual, fornecendo explicabilidade granular em nível de amostra que viabiliza auditoria científica e jurídica das classificações [@Lundberg2017; @Chen2024].

@Effrosynidis2021 e @Loyal2022 documentaram tendência recente (9% dos estudos, concentrados em 2024-2025) voltada à implementação de modelos de ML em dispositivos portáteis ou sistemas in-situ para análise rápida de autenticidade em campo ou pontos de venda. Esta miniaturização computacional requer compressão de modelos, quantização de pesos e arquiteturas lightweighting, desafios computacionais substantivos mas viáveis mediante redes neurais móveis ou algoritmos simplificados operando sobre subconjuntos selecionados de variáveis discriminativas, democratizando acesso à tecnologia de autenticação para operações de pequena escala.

A integração entre Machine Learning (ML), blockchain e Internet das Coisas (IoT) desponta como arquitetura de referência para rastreabilidade distribuída e auditável em cadeias de suprimento modernas. Nesses modelos, sensores IoT coletam dados ambientais ao longo da cadeia; algoritmos de ML comparam os padrões observados com perfis esperados para produtos autênticos; e o blockchain registra, de forma imutável e descentralizada, transações e verificações, criando trilhas de auditoria robustas [@Gong2023; @Zhou2024; @Agyekum2022; @Zhang2022; @Gupta2024; @Wang2022]. Estudos em sistemas agroalimentares apontam essa convergência como relevante tanto para o compliance regulatório quanto para o *compliance* regulatório quanto para responder a demandas de consumidores e produtores por autenticidade e sustentabilidade [@Yang2022; @Sun2023].

Apesar da amplitude de estudos analisados, a análise do corpus revela lacunas metodológicas e epistemológicas que demandam atenção prioritária para a maturação do campo. Uma limitação crítica, observada em apenas 6% dos estudos, é a ausência de validação longitudinal, que testa a robustez dos modelos frente a variações interanuais. A estabilidade temporal das assinaturas geoquímicas e metabolômicas é um pressuposto fundamental para a certificação, contudo, a variabilidade climática e edáfica entre safras pode degradar o desempenho preditivo de modelos treinados em um único ciclo sazonal, um desafio conhecido em modelagem agroambiental [@Kamilaris2018]. Sem essa validação temporal, a capacidade de generalização dos modelos permanece incerta, limitando sua confiabilidade para fins regulatórios.

Observa-se também uma carência de reflexão crítica sobre as fronteiras de aplicabilidade dos modelos de ML. Apenas uma pequena fração dos trabalhos (8%) discute sistematicamente os cenários em que os algoritmos podem ser inadequados ou as condições sob as quais suas predições falham. Essa tendência à superestimação das capacidades algorítmicas, sem uma análise robusta de suas incertezas e vieses, pode representar um risco para a integridade dos sistemas de certificação [@Lones2021]. Por fim, a escassez de diretrizes para a implementação prática em agências certificadoras (11% dos estudos) evidencia uma lacuna na translação do conhecimento, dificultando que os avanços da pesquisa acadêmica se convertam em impacto regulatório e operacional efetivo [@Liakos2018].

## 3.10 Implicações para Sistemas de Certificação de Indicações Geográficas

A análise dos 25 estudos selecionados indica que as técnicas de Machine Learning têm potencial para fortalecer sistemas de certificação de Indicações Geográficas, mas sua implementação prática ainda é limitada por desafios de validação, interpretabilidade e governança. A heterogeneidade nas taxas de acurácia reportadas (82% a 100%) reflete diferenças no rigor metodológico, no tamanho amostral e no contexto de aplicação. Em especial, o fato de apenas 23% dos estudos reportarem validação com amostras de regiões não representadas no treinamento, com quedas de desempenho de até 15% nesses cenários [@Chen2020; @Effrosynidis2021; @Kuhn2013], evidencia que a validação espacialmente independente é condição indispensável para que modelos baseados em ML sejam juridicamente defensáveis.

Paralelamente, a crescente complexidade dos algoritmos, sobretudo em arquiteturas profundas, intensifica o problema da “caixa‑preta”. Como apenas 14% dos trabalhos empregaram técnicas de explicabilidade como SHAP ou LIME [@Effrosynidis2021], persiste um descompasso entre o desempenho preditivo e a necessidade de transparência exigida por reguladores e produtores. A preferência por modelos inerentemente interpretáveis, como Random Forest com análise de importância de variáveis ou PLS-DA com *loadings* explicitáveis, desponta como estratégia pragmática para equilibrar acurácia e explicabilidade, ao mesmo tempo em que viabiliza a identificação de marcadores territoriais passíveis de incorporação em normas técnicas.

Do ponto de vista geográfico e setorial, a concentração de 72% dos estudos em produtos europeus e asiáticos, como vinhos, chás e azeites, abre uma oportunidade evidente para IGs de países em desenvolvimento, incluindo o Brasil, onde café, queijo, cachaça e cacau podem se beneficiar de metodologias já consolidadas [@Li2025; @Frigerio2024]. A aplicação desses modelos a novas matrizes permitiria transformar IGs em ativos intangíveis estrategicamente manejados, nos termos da Visão Baseada em Recursos [@Barney1991], embora abordagens de valoração econômica (custo, mercado, renda) ainda não estejam integradas aos modelos computacionais [@WIPO2003; @EUCommission2019].

A consolidação de ML em sistemas de IGs exige, por fim, um ecossistema de suporte que articule infraestrutura laboratorial, competências em ciência de dados e governança de dados. A integração do conhecimento empírico das comunidades produtoras com evidências computacionais, observada em apenas 3% dos estudos, pode ser relevante para a legitimidade social dos modelos [@Huera-Lucero2025]. No contexto brasileiro, marcos legais como a Lei 15.068/2024 (Lei Paul Singer) podem fomentar a criação de Empreendimentos Econômicos Solidários especializados em ML [@Brasil2024; @Mazzucato2013], desde que acompanhados por redes laboratoriais com protocolos harmonizados [@MAPA2020] e por arranjos de governança que definam claramente direitos de propriedade intelectual e mecanismos de repartição justa de benefícios derivados do conhecimento territorial.

## 4. Conclusão

Esta revisão de escopo contribui para a Ciência da Informação e áreas correlatas ao fornecer um mapeamento sistemático da estrutura intelectual na intersecção entre Machine Learning e certificação de origem territorial. A análise multivariada de um corpus de 148 estudos revela que este domínio transicionou de uma fase exploratória de prova de conceito para um estágio de maturação metodológica. Contudo, demonstramos que a heterogeneidade observada não deve ser interpretada como fragmentação do campo, mas como uma especialização funcional adaptativa. A escolha algorítmica no domínio não segue uma trajetória linear de obsolescência tecnológica (onde Deep Learning inevitavelmente substitui métodos clássicos), mas obedece a uma ecologia complexa de restrições informacionais, incluindo a natureza dos dados (matriz alimentar), infraestrutura analítica disponível e regimes regulatórios locais.

Um achado crítico, derivado diretamente dos padrões geográficos identificados na análise de clusters e produtividade científica, é a distinção entre abordagens metodológicas predominantes em contextos europeus e asiáticos. Nossos dados indicam que, enquanto estudos europeus tendem a priorizar algoritmos de classificação supervisionada para proteção de denominações consolidadas, pesquisas asiáticas exploram aplicações mais diversificadas, incluindo integração multimodal e adaptação a novos produtos. Essa variação reflete não apenas diferenças técnicas, mas também contextos regulatórios e produtivos específicos, evidenciando como o ML é moldado por necessidades territoriais distintas.

Entretanto, a revisão expõe uma lacuna na confiabilidade da informação gerada em que, a predominância de um otimismo estatístico decorrente da escassez de validação longitudinal (presente em apenas 6% dos estudos) e espacialmente independente. A atual prática científica prioriza métricas de acurácia in silico em detrimento da robustez preditiva no mundo real. Para que sistemas de ML sejam integrados a arquiteturas de informação juridicamente defensáveis, argumentamos por uma mudança de paradigma: da busca por complexidade arquitetural para a priorização da explicabilidade algorítmica e reprodutibilidade sistêmica.

Este estudo delineia implicações estratégicas para políticas de informação e desenvolvimento tecnológico em economias emergentes e no Sul Global. A concentração da produção científica observada (72% dos estudos em produtos europeus e asiáticos) não deve ser interpretada apenas como disparidade técnica, mas como evidência de assimetrias estruturais na governança de dados e infraestrutura de pesquisa. Argumenta-se que a oportunidade para estas regiões reside no desenvolvimento de portfólios metodológicos sensíveis ao contexto, adaptados a regimes de biodiversidade específicos e arranjos produtivos locais, evitando a replicação acrítica de trajetórias tecnológicas exógenas.

Conclui-se que a agenda futura de pesquisa deve transcender a validação puramente técnica da performance dos modelos para incorporar dimensões de equidade na distribuição dos benefícios, investigando os beneficiários efetivos destas arquiteturas e os mecanismos pelos quais a tecnologia redistribui, ou concentra, o valor derivado do conhecimento associado ao lugar.

### Financiamento

A publicação deste artigo foi financiada pelo Instituto Federal de Sergipe (IFS), por meio do Edital nº 29/2025/DPP/PROPEX/IFS.

## Agradecimentos

Os autores agradecem à Universidade Federal de Sergipe (UFS), à Universidade Estadual de Feira de Santana (UEFS) e ao Instituto Federal de Sergipe (IFS) pelo apoio institucional e infraestrutural que viabilizou a realização desta pesquisa.

## Conflitos de Interesse

Os autores declaram não haver conflitos de interesse.

## Declaração de Disponibilidade de Dados

O conjunto de dados completo que suporta os resultados deste estudo, incluindo o corpus bibliográfico, os scripts de análise e os resultados intermediários, está publicamente disponível no repositório Open Science Framework (OSF) sob o DOI: <https://doi.org/10.17605/OSF.IO/2EKYQ>.

## Referências
