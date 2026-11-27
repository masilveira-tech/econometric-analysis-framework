# Desocupação, PIB e Selic / Unemployment, GDP and interest rates

Research question: how are real GDP growth, a lagged policy rate and a shock indicator associated with unemployment?

Use quarterly observations with consistent definitions. For an empirical application, source the unemployment and GDP series from IBGE and the policy rate from Banco Central do Brasil, document the exact series IDs, aggregation rule, sample window, vintage and lag construction. Align all dates and remove incomplete cases only after inspecting gaps. No official dataset is bundled.

Illustrative specification: unemployment = intercept + b1*gdp_growth + b2*lagged_rate + b3*shock + error. Theoretical signs are conditional on definitions and lag length, not guarantees. Use the [synthetic demonstration](../demo.py) to practice; it must not be represented as Brazilian evidence.

```bash
python econometrics.py data.xlsx --sheet "DADOS AGRUPADOS" --y unemployment --x gdp_growth lagged_rate shock --time date --lags 4 --out output
```

Check stationarity, structural breaks, reverse causality and lag sensitivity before any empirical interpretation. For levels with unit roots, consider transformations or a suitable cointegration model rather than relying on robust SEs alone.
