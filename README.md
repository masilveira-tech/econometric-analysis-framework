# Econometric Analysis Framework

Procedimento operacional e biblioteca de prompts para análise econométrica em Python, desenvolvidos por Matheus Silveira a partir de atividades acadêmicas em Ciências Econômicas.

## Objetivo

Padronizar a geração de código, a validação de dados, a estimação por mínimos quadrados ordinários (MQO), os diagnósticos e a interpretação econômica, com rastreabilidade e decisões metodológicas justificadas.

## Conteúdo

- [Prompt mestre universal](PROMPT_MASTER.md) — configuração reutilizável e oito etapas de análise.
- [Prompt de depuração](PROMPT_DEBUG.md) — correção incremental de erros de execução.
- [Exemplo aplicado](examples/desocupacao_pib_selic.md) — configuração de um modelo trimestral de desocupação, PIB real, Selic defasada e pandemia.

## Como utilizar

1. Abra `PROMPT_MASTER.md` e copie seu conteúdo.
2. Preencha o bloco de configuração com os dados de seu projeto.
3. Envie o prompt e a base a um assistente de IA autorizado a processá-la.
4. Execute e confira os blocos Python progressivamente.
5. Compare a estimação, os diagnósticos e a inferência com a base original.

## Métodos

MQO simples e múltiplo, variáveis dummy, F parcial, FIV, Jarque–Bera, Breusch–Pagan, White, Durbin–Watson, Breusch–Godfrey, Ramsey RESET, ADF, distância de Cook, HC3 e Newey–West (HAC).

## Ambiente sugerido

Python com pandas, NumPy, statsmodels, SciPy, Matplotlib e openpyxl para arquivos Excel.

## Limitações

Este repositório contém prompts e um exemplo de configuração, não um pacote Python executável ou resultados empíricos validados. HC3 e HAC tratam a inferência, não eliminam automaticamente as violações dos resíduos. Dados em painel e métodos avançados requerem extensões específicas. O conteúdo não substitui validação econométrica independente.

## Autor

Matheus Silveira — Ciências Econômicas, Universidade Federal Fluminense (UFF).
