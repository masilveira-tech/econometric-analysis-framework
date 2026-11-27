# Technical guide — English

[Back to project](../README.md)

## Workflow
1. Install dependencies with `python -m pip install -r requirements.txt`.
2. Prepare CSV or XLSX/XLSM data with unique headers, numeric variables, and pre-encoded 0/1 dummies. Construct lags in advance. Record sources, units and transformations.
3. Specify `--y`, `--x`, and for time series, an ISO date column with `--time`. Check equal spacing, including after missing observations are removed. Dates are sorted and duplicates rejected; gaps are not checked automatically.
4. Inspect the complete-case sample and residual degrees of freedom (n minus the number of estimated parameters, including the intercept).
5. Compare classical, HC3 and HAC inference. Justify the lag order using frequency, theory and sensitivity analysis.
6. Document limitations; do not select specifications merely to obtain small p-values.

## Diagnostics

| Method | Null or purpose | Interpretation |
| --- | --- | --- |
| Koenker Breusch–Pagan / White | Constant variance | Rejection suggests heteroskedasticity |
| Breusch–Godfrey | No serial correlation through chosen lag | Rejection suggests serial dependence |
| Jarque–Bera | Normal residuals | Rejection suggests departure from normality |
| RESET | Extra fitted-value power has zero coefficient | Rejection flags possible misspecification |
| ADF | Unit root | Failure to reject is not proof; investigate integration and cointegration |
| VIF | Collinearity | Investigate large values; no automatic variable deletion |
| Cook's distance | Influence | 4/n is a screening heuristic |

HC3/HAC modify covariance estimates, not OLS coefficients, residuals or residual degrees of freedom. HC3 does not account for serial dependence. HAC requires appropriate assumptions and lag choices. The reported overall F is the conventional OLS F. None of these methods corrects endogeneity or establishes causation.

## Outputs
`summary.json`: sample and classical fit statistics; `coefficients.csv`: estimates, SEs, p-values and intervals; `diagnostics.csv`: hypotheses and test results; `vif.csv`, `residuals.csv`, `correlations.csv`, `descriptive.csv`, `ols.txt` and SVG plots. Use a new output directory per specification.

## AI-assisted workflow
The original [master prompt](../PROMPT_MASTER.md) (Portuguese) covers additional tasks; the executable code does not call AI services. For English use, instruct an assistant to follow the same configuration and produce documented, executable code without inventing results. Treat AI output as unverified until executed and independently checked.
