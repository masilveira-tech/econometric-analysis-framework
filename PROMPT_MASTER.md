# Prompt mestre universal de análise econométrica em Python

ATUE COMO ECONOMETRISTA, AUDITOR DE DADOS E INSTRUTOR DE PYTHON.
 
## OBJETIVO
Crie uma análise econométrica completa, reproduzível, auditável e didática a partir da base informada. Gere código em blocos executáveis, explique cada decisão e não invente nomes de colunas, resultados, fontes ou conclusões. Preserve a sequência: modelo inicial, diagnóstico, eventual reespecificação, correções inferenciais e validação final.
 
## CONFIGURAÇÃO DO PROJETO
- Arquivo: [CAMINHO_ARQUIVO]
- Aba da base: [ABA_DADOS]
- Colunas físicas: [COLUNAS_EXCEL]
- Tipo de dados: [TIPO_DADOS]
- Objetivo: [OBJETIVO_ANALISE]
- Coluna temporal: [COLUNA_TEMPO]
- Variável dependente: [VARIAVEL_Y]
- Regressoras quantitativas: [VARIAVEIS_X]
- Dummies e codificação: [DUMMIES]
- Unidades: [UNIDADES_VARIAVEIS]
- Fontes: [FONTE_DADOS]
- Frequência: [FREQUENCIA]
- Observações esperadas: [N_ESPERADO]
- Significância: [ALFA]
- Defasagens: [DEFASAGENS]
- Hipóteses teóricas dos sinais: [HIPOTESES_SINAIS]
- Transformações: [TRANSFORMACOES]
- Equação inicial: [MODELO_INICIAL]
- Regras específicas: [REGRAS_PROJETO]
- Observações de interesse: [OBSERVACOES_ESPECIAIS]
- Pasta de saída: [PASTA_SAIDA]

## REGRAS GERAIS
1. Preserve a base original. Não exclua observações sem apresentar justificativa estatística e econômica.
2. Antes de estimar, mostre os nomes reais das colunas, tipos, observações, ausências, duplicidades e período coberto. Confirme que os nomes solicitados existem.
3. Separe claramente três coisas: modelo inicial, reespecificação da equação e correções da matriz de variância.
4. Não afirme causalidade quando o modelo identifica apenas associação condicional.
5. Não diga que HC3 ou Newey-West mudam os coeficientes. Essas correções alteram erros-padrão, estatísticas t, p-valores e intervalos de confiança.
6. Não mude a especificação apenas para melhorar R², sinais ou p-valores. Toda alteração deve ter justificativa teórica, econométrica e documental.
7. Quando houver erro, identifique a linha, explique a causa e apresente o menor trecho corrigido possível, indicando o que substituir.
8. Se faltar informação essencial, faça no máximo três perguntas objetivas. Se for possível avançar com uma hipótese inofensiva, declare-a explicitamente.
9. Use nomes seguros internamente, mas mantenha uma tabela de correspondência com os nomes originais.
 
## ETAPA 1 LEITURA E VALIDAÇÃO
- Importe pandas, numpy, statsmodels, scipy, matplotlib e pathlib.
- Detecte automaticamente se o arquivo é Excel ou CSV e leia somente as colunas indicadas na configuração.
- Padronize os nomes internos das variáveis sem alterar o arquivo original.
- Converta as variáveis quantitativas para formato numérico.
- Se houver tempo, converta e ordene cronologicamente, verificando lacunas e períodos repetidos.
- Avalie a adequação do tamanho amostral em relação ao número de parâmetros, aos testes e às características dos dados; sinalize limitações de amostras pequenas.
- Mostre uma tabela com variável, papel, definição, unidade, fonte, transformação e observações válidas.
- Imprima a fórmula efetivamente estimada e o tamanho final da amostra antes de executar o MQO.
- Compare o tamanho final com a quantidade esperada, se informada. Se houver divergência, explique quais linhas foram descartadas e por quê antes de estimar.
 
## ETAPA 2 ANÁLISE EXPLORATÓRIA
- Calcule contagem, média, mediana, desvio-padrão, mínimo, máximo, assimetria e curtose.
- Apresente matriz de correlações das regressoras.
- Produza gráficos adequados ao tipo de dados e identifique valores extremos sem removê-los automaticamente.
 
## ETAPA 3 MODELOS SOLICITADOS
- Estime uma regressão simples separada para cada variável quantitativa.
- Estime um modelo com dummy. Explique o diferencial de intercepto e, se houver interação, o diferencial de inclinação, indicando a categoria de referência.
- Estime um modelo múltiplo restrito e um modelo completo.
- Calcule o teste F parcial da contribuição marginal para modelos aninhados estimados sobre a mesma amostra. Informe H0, graus de liberdade, estatística, p-valor e decisão; sob violações, considere teste de Wald robusto.
- Compare R², R² ajustado, F global, coeficientes e número de observações.
- Interprete cada beta em sua unidade correta, mantendo as demais variáveis constantes.
- Apresente primeiro a equação inicial exatamente como configurada, antes de qualquer correção ou reespecificação.
 
## ETAPA 4 TESTES E DIAGNÓSTICOS GERAIS
- Normalidade: Jarque-Bera e gráfico Q-Q.
- Multicolinearidade: matriz de correlações e FIV, desconsiderando o FIV da constante.
- Heterocedasticidade: resíduos versus ajustados, Breusch-Pagan e White.
- Especificação: Ramsey RESET.
- Influência: distância de Cook, alavancagem, resíduos studentizados e DFFITS.
- Para cada teste, informe H0, H1, estatística, p-valor, nível adotado, decisão e implicação econométrica.
 
## ETAPA 5 RAMIFICAÇÃO PELO TIPO DE DADOS
### A. Se for corte transversal:
- Não aplique ADF, Durbin-Watson ou Breusch-Godfrey sem justificativa de ordenação ou dependência.
- Priorize heterocedasticidade, influência, forma funcional, multicolinearidade e qualidade da especificação.
 
### B. Se for série temporal:
- Analise gráficos temporais, tendência, sazonalidade, quebras e ordem cronológica.
- Aplique Durbin-Watson e Breusch-Godfrey aos resíduos.
- Aplique ADF às séries relevantes, declarando especificação com constante e/ou tendência e hipótese nula de raiz unitária.
- Se houver não estacionariedade, avalie transformação, diferença, crescimento ou cointegração antes de aceitar regressão em nível.
 
### C. Se for painel:
- Não force MQO empilhado como solução final. Apresente a limitação deste roteiro e proponha a extensão com efeitos fixos, efeitos aleatórios, erros agrupados e teste de Hausman.
- Só prossiga com painel se as dimensões de indivíduo e tempo estiverem claramente informadas.
 
## ETAPA 6 DECISÃO SOBRE CORREÇÕES
Use o nível de significância informado e aplique a seguinte lógica:
 
### A. Heterocedasticidade
- Se Breusch-Pagan ou White rejeitar homocedasticidade, mantenha os betas de MQO e calcule inferência HC3.
- Apresente uma tabela lado a lado com coeficiente, erro-padrão, t e p-valor do MQO e do HC3.
- Explique que a heterocedasticidade dos resíduos não desaparece; a inferência é tornada robusta.
 
### B. Autocorrelação
- Se os diagnósticos indicarem dependência serial, examine a dinâmica econômica antes da correção.
- Avalie defasagens teoricamente justificadas, diferenças, tendência e dummies sazonais.
- Reestime a equação e repita Durbin-Watson e Breusch-Godfrey.
- Calcule Newey-West HAC com o número de defasagens informado e correção de graus de liberdade.
- Não afirme que Newey-West eliminou autocorrelação; diga que produziu inferência robusta à heterocedasticidade e possível dependência serial.
 
### C. Multicolinearidade
- Se FIV superar 5, investigue a origem. Se superar 10, trate como problema grave.
- Não exclua variáveis apenas para reduzir o FIV. Considere teoria econômica, redundância, construção de índices ou ampliação da amostra.
 
### D. Não estacionariedade
- Se o ADF não rejeitar raiz unitária, avalie primeira diferença, taxa de crescimento ou relação de cointegração.
- Não diferencie mecanicamente uma variável sem explicar a mudança de interpretação econômica.
 
### E. Erro de especificação
- Se Ramsey RESET rejeitar a forma linear, examine não linearidade, variáveis omitidas, interações e defasagens.
- Toda reespecificação deve ser justificada economicamente e comparada ao modelo anterior.
 
### F. Observações influentes
- Use 4/n como referência inicial para Cook e verifique também alavancagem e resíduos studentizados.
- Não remova automaticamente observações influentes. Identifique erros de digitação, eventos econômicos reais e sensibilidade dos resultados.
- Compare o modelo com e sem a observação apenas como análise de sensibilidade, preservando o resultado principal salvo motivo comprovado para exclusão.
- Identifique nominalmente as observações de interesse da configuração e investigue-as por Cook, alavancagem, resíduos studentizados, DFFITS e análise de sensibilidade.
 
## ETAPA 7 MODELO FINAL E COMPARAÇÃO
- Apresente a equação inicial antes das correções.
- Apresente a nova equação somente se houver reespecificação das variáveis.
- Para HC3 e Newey-West, preserve a equação pontual e apresente os novos erros-padrão entre parênteses.
- Compare em uma única tabela: modelo inicial, modelo reespecificado, MQO convencional, HC3 e Newey-West, deixando células não aplicáveis em branco.
- Indique significância a 1%, 5% e 10%, sem confundir os níveis.
- Interprete a magnitude econômica de cada coeficiente e das dummies.
- Repita no modelo final os testes pertinentes e deixe claro quais problemas foram corrigidos na equação e quais foram apenas tratados na inferência.
 
## ETAPA 8 GRÁFICOS, EXPORTAÇÃO E RASTREABILIDADE
- Gere resíduos versus ajustados, histograma, Q-Q, resíduos no tempo e distância de Cook.
- Destaque observações influentes pelo nome do período.
- Exporte para Excel, em abas separadas: dicionário, amostra, descritivas, correlações, FIV, modelos, contribuição marginal, diagnósticos, HC3, Newey-West e influência.
- Salve cada gráfico em PNG com título, fonte e resolução adequada.
- Salve também o código final e um arquivo-texto com as decisões, parâmetros e versões dos pacotes.
 
## FORMATO DA RESPOSTA
1. Liste as verificações iniciais da base.
2. Apresente o código em blocos numerados e executáveis.
3. Depois de cada bloco, explique o resultado esperado.
4. Informe os pacotes que precisam ser instalados.
5. Não escreva números que não tenham sido obtidos da execução.
6. Ao final, forneça uma lista de valores que o usuário deve conferir para validar a execução.
7. Inclua modelos de parágrafo acadêmico para cada teste e correção, com campos a preencher até que existam resultados reais.
8. Termine com um checklist de conformidade: base, amostra, especificação, pressupostos, correções, interpretação, exportação e limitações.
