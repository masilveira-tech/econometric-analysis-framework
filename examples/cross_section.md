# Cross-sectional illustration / Corte transversal

A possible application is an association between household consumption, income and a binary employment indicator. Use anonymized data, inspect sampling design and units, encode dummies and document missing observations. Survey weights and complex designs are outside this implementation.

```bash
python econometrics.py households.csv --y consumption --x income employed --out household_output
```

Omit time-series diagnostics because there is no ordered temporal dimension. Compare OLS and HC3; investigate nonlinearities, leverage and endogeneity. No empirical household results are claimed.
