# Guia técnico — Português

[Voltar ao projeto](../README.md)

## Fluxo de trabalho
1. Instale as dependências com `python -m pip install -r requirements.txt`.
2. Prepare uma base CSV ou XLSX/XLSM com cabeçalhos únicos, variáveis numéricas e dummies 0/1. Não inclua totais ou notas de rodapé. Construa defasagens antes da execução e documente unidades, fontes e transformações.
3. Informe a variável dependente em `--y`, as regressoras em `--x` e, para séries temporais, datas ISO e `--time`. Verifique periodicidade regular, inclusive após excluir ausentes; o programa ordena datas e rejeita duplicatas, mas não verifica lacunas automaticamente.
4. Execute o modelo e examine a amostra: n, observações excluídas e graus de liberdade n-k (k inclui a constante).
5. Interprete diagnósticos e compare a inferência clássica, HC3 e HAC. Escolha defasagens a partir da frequência, teoria e análise de sensibilidade.
6. Documente limitações; não escolha especificações apenas para atingir p<0,05.

## Diagnósticos

| Teste | H0 ou finalidade | Interpretação |
| --- | --- | --- |
| Koenker Breusch–Pagan / White | Homocedasticidade | Rejeição indica evidência de variância não constante |
| Breusch–Godfrey | Ausência de autocorrelação até a ordem escolhida | Rejeição exige investigar dinâmica e inferência |
| Jarque–Bera | Normalidade dos resíduos | Rejeição indica desvio da normalidade |
| RESET | Coeficiente da potência adicional dos ajustados igual a zero | Rejeição sugere possível má especificação |
| ADF | Raiz unitária | Não rejeitar não comprova raiz unitária; investigar integração e cointegração |
| VIF | Colinearidade | Valores altos exigem investigação, sem exclusão automática |
| Cook | Influência | 4/n é triagem, não regra de exclusão |

HC3 e Newey–West não alteram coeficientes ou graus de liberdade residuais do MQO, nem eliminam a autocorrelação/heterocedasticidade dos resíduos. HC3 não trata dependência serial. HAC depende de hipóteses assintóticas e da escolha de defasagens. O F em summary.json é o F clássico, não robusto.

## Saídas
`summary.json`: tamanho amostral, R² e F clássico; `coefficients.csv`: coeficientes, erros-padrão, p e IC; `diagnostics.csv`: teste, hipótese, resultado e erros; `vif.csv`, `residuals.csv`, `correlations.csv`, `descriptive.csv`, `ols.txt` e gráficos SVG. Use uma pasta nova para cada modelo.

## IA
O [prompt mestre](../PROMPT_MASTER.md) orienta etapas adicionais. A ferramenta não envia dados à IA; o uso dos prompts é separado e deve respeitar confidencialidade. O código é um ponto de partida, não substitui julgamento econométrico.
