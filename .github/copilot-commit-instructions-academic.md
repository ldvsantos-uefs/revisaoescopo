# 🧭 Diretrizes para Mensagens de Commit em Pesquisa Científica

## 1. Objetivo

Este documento padroniza o **formato e o conteúdo das mensagens de commit** para este repositório, que é focado no desenvolvimento de artigos científicos, scripts de análise de dados e documentação técnica na área de **Bioengenharia de Solos, Geocompostos e Ciências Ambientais**. O objetivo é assegurar **clareza, rastreabilidade e consistência** em todas as alterações, seguindo o padrão **Conventional Commits** adaptado ao rigor e à especificidade da pesquisa científica.

---

## 2. Formato Padrão do Commit

Adote o seguinte formato, baseado no padrão *Conventional Commits*:

```
<tipo>(<escopo>): <descrição curta>

<corpo opcional detalhando as mudanças>

<rodapé opcional com metadados e referências>
```

### Exemplo de Estrutura Completa

```
feat(analise-estatistica): adiciona análise de componentes principais (PCA) e MANOVA

- Implementa script em R para análise multivariada dos dados de solo.
- A PCA revelou dois componentes principais, explicando 68% da variância total.
- A MANOVA confirmou diferenças significativas entre os tratamentos (p < 0.05).
- Gráficos de biplot foram gerados e salvos no diretório /resultados/figuras.

Dados: /dados/coleta_campo_final.csv
Ref: polymers-16-00632, jcs-05-00109-v2
```

---

## 3. Tipos de Commit (`<tipo>`)

| Tipo | Descrição | Exemplo de Uso |
|---|---|---|
| **feat** | Inclusão de uma nova análise, seção no artigo, metodologia ou script. | `feat(ensaio-mecanico): adiciona resultados do teste de tração` |
| **fix** | Correção de erros (código), revisão textual, ajuste de dados ou formatação. | `fix(introducao): corrige citação e melhora a fluidez do parágrafo` |
| **docs** | Alterações em documentação, README, guias de metodologia ou instruções. | `docs(metodologia): detalha o procedimento de extração das fibras` |
| **style** | Ajustes de formatação que não alteram o conteúdo ou a lógica (ex: ABNT). | `style(referencias): formata todas as citações para o padrão APA 7` |
| **refactor** | Reestruturação de código ou texto sem alterar o resultado final. | `refactor(script-r): otimiza a função de leitura de dados para performance` |
| **test** | Adição ou modificação de testes de validação para scripts e análises. | `test(modelo-weibull): adiciona teste de validação para a análise de confiabilidade` |
| **chore** | Tarefas de manutenção, como atualização de pacotes ou organização de arquivos. | `chore(renv): atualiza o arquivo de lock com novas dependências` |

---

## 4. Escopos de Commit (`<escopo>`)

O escopo deve identificar a seção do projeto ou do artigo que foi modificada.

| Escopo | Aplicação Típica |
|---|---|
| **resumo** | Modificações no resumo (Abstract) do artigo. |
| **introducao** | Alterações na seção de Introdução. |
| **metodologia** | Ajustes nos materiais e métodos. |
| **resultados** | Inclusão ou revisão dos resultados e discussões. |
| **conclusao** | Alterações na seção de Conclusão. |
| **analise-estatistica** | Scripts e resultados de análises estatísticas (PCA, MANOVA, GLM, etc.). |
| **ensaio-laboratorio** | Dados e análises de ensaios específicos (FTIR, TGA, MEV, tração, etc.). |
| **geocomposito** | Modificações relacionadas ao desenvolvimento ou caracterização do material. |
| **artigo-X** | Alterações globais em um artigo específico (ex: `artigo-cafe`). |

---

## 5. Exemplos Práticos

### Exemplo 1: Adição de Análise Laboratorial
`feat(ensaio-laboratorio): integra resultados da análise termogravimétrica (TGA)`

`- Curvas de TGA mostram estabilidade térmica do biocompósito até 285 °C.`
`- A análise foi realizada no equipamento PerkinElmer Spectrum Two.`

`Dados: /dados/brutos/tga_amostra_01.csv`

### Exemplo 2: Revisão da Introdução
`fix(introducao): aprimora a contextualização sobre degradação de polímeros`

`- Adiciona parágrafo sobre o impacto da radiação UV em compósitos.`
`- Inclui duas novas referências-chave (Wang et al., 2024; Dhakal et al., 2023).`

`Ref: polymers-16-00632, polymers-15-01229-v2`

### Exemplo 3: Refatoração de Script
`refactor(analise-estatistica): otimiza script de análise de confiabilidade em R`

`- Substitui o loop 'for' por uma função da família 'apply' para melhor performance.`
`- Nenhuma alteração nos resultados finais, apenas na estrutura do código.`

### Exemplo 4: Atualização de Documentação
`docs(metodologia): detalha o protocolo de envelhecimento acelerado`

`- Descreve os ciclos de radiação UV e condensação (5h + 1h).`
`- Especifica a câmara de envelhecimento utilizada (EN 12224:2001).`

---

## 6. Boas Práticas

## 🧠 Boas Práticas

1. **Atomicidade:** cada commit deve representar uma única alteração lógica e completa.  
   - Evite misturar ajustes não relacionados (ex.: não combine refatoração com adição de novas seções).  

2. **Clareza:** a descrição curta deve ser autoexplicativa.  
   - Use o corpo do commit para detalhar o contexto, o motivo e o impacto da modificação.  

3. **Consistência:** mantenha o mesmo estilo, terminologia e formatação em todos os commits.  
   - Evite abreviações não padronizadas e garanta uniformidade nos escopos.  

4. **Relevância:** registre apenas alterações significativas.  
   - Ajustes triviais podem ser agrupados em um único commit (`chore`).  

5. **Coerência temporal:** realize commits frequentes e pequenos.  
   - Isso facilita o controle de versão e o rastreamento de mudanças em artigos científicos.  

6. **Contextualização científica:** descreva brevemente o tipo de modificação analítica ou textual.  
   - Ex.: “Integra modelo GLM com variáveis de estabilidade de agregados” ou “Reorganiza introdução segundo hipóteses funcionais”.  

7. **Referências e métricas:** quando possível, registre dados quantitativos e fontes.  
   - Ex.: "1625 palavras, 10 referências Q1 (2019–2024), β = 0.67 no modelo PLS-SEM".  

8. **Pontuação acadêmica:** evite o uso de travessões (—) como substituto de parênteses ou vírgulas.  
   - ❌ Incorreto: "A análise das variáveis — N-S, N-AF e N-AH — demonstrou..."  
   - ✅ Correto: "A análise das variáveis, N-S, N-AF e N-AH, demonstrou..."  
   - Justificativa: Travessões em textos científicos devem ser reservados para ênfase ou ruptura maior no pensamento. Use vírgulas para inserir informações complementares, seguindo as boas práticas de escrita científica.

9. **Verificação final:** antes de confirmar, leia o commit como se fosse uma entrada de relatório.  
   - Se for inteligível fora do contexto, está bem escrito.


---