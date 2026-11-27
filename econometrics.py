"""Reproducible OLS diagnostics for numeric CSV and Excel data."""
import argparse
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_breuschpagan, het_white, acorr_breusch_godfrey, linear_reset
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.stats.stattools import durbin_watson, jarque_bera
from statsmodels.tsa.stattools import adfuller


def analyze(data, y, x, out, time=None, lags=4, alpha=.05):
    """Use one complete-case sample; HAC/BG/ADF only for ordered time series."""
    out = Path(out)
    if not x or len(set([y, *x])) != len(x)+1 or time in [y, *x]:
        raise ValueError('Use distinct dependent, regressor and time columns.')
    if not 0 < alpha < 1 or lags < 1:
        raise ValueError('Invalid alpha or lags.')
    d = data[[y, *x, *([time] if time else [])]].copy()
    for c in [y, *x]:
        d[c] = pd.to_numeric(d[c], errors='raise').replace([np.inf, -np.inf], np.nan)
    d = d.dropna()
    if time:
        d[time] = pd.to_datetime(d[time], errors='raise')
        if d[time].duplicated().any():
            raise ValueError('Duplicate timestamps.')
        d = d.sort_values(time)
        # The caller must verify that timestamps form an equally spaced series.
    X = sm.add_constant(d[x], has_constant='add')
    n, k = X.shape
    if n <= k+2 or np.linalg.matrix_rank(X) != k or d[y].nunique() < 2:
        raise ValueError('Insufficient observations, constant outcome or rank-deficient design.')
    if time and lags >= n-k-1:
        raise ValueError('Too many lags for sample size.')
    m = sm.OLS(d[y], X).fit()
    if np.allclose(m.resid, 0):
        raise ValueError('Perfect fit: residual diagnostics are undefined.')
    out.mkdir(parents=True, exist_ok=True)
    models = {'OLS': m, 'HC3': m.get_robustcov_results(cov_type='HC3', use_t=True)}
    if time:
        models['HAC'] = m.get_robustcov_results(cov_type='HAC', maxlags=lags, use_correction=True, use_t=True)
    coef = pd.concat([pd.DataFrame({'method': name, 'term': X.columns, 'coef': r.params, 'se': r.bse, 'p': r.pvalues, 'ci_low': np.asarray(r.conf_int(alpha))[:,0], 'ci_high': np.asarray(r.conf_int(alpha))[:,1]}) for name,r in models.items()], ignore_index=True)
    tests = []
    def record(name, null, fn):
        try:
            stat, p = map(float, fn())
            if not np.isfinite([stat,p]).all():
                raise ValueError('Non-finite result')
            tests.append([name, null, stat, p, 'reject' if p < alpha else 'do not reject', ''])
        except (ValueError, AssertionError, np.linalg.LinAlgError, ZeroDivisionError) as e:
            tests.append([name, null, np.nan, np.nan, 'unavailable', str(e)])
    record('Breusch-Pagan (Koenker)', 'constant variance', lambda: het_breuschpagan(m.resid,X)[:2])
    record('White', 'constant variance', lambda: het_white(m.resid,X)[:2])
    record('Jarque-Bera', 'normal residuals', lambda: jarque_bera(m.resid)[:2])
    record('RESET', 'no omitted powers of fitted values', lambda: (lambda t:(np.asarray(t.fvalue).item(), np.asarray(t.pvalue).item()))(linear_reset(m,power=2,use_f=True)))
    if time:
        record('Breusch-Godfrey', 'no serial correlation through selected lag', lambda: acorr_breusch_godfrey(m,nlags=lags)[:2])
        for c in [y,*x]:
            if d[c].nunique() > 2:
                record('ADF: '+c, 'unit root', lambda c=c: adfuller(d[c],autolag='AIC')[:2])
    diagnostics = pd.DataFrame(tests,columns=['test','null','statistic','p','decision','note'])
    vif = pd.DataFrame({'term':x,'VIF':[variance_inflation_factor(X.to_numpy(),i) for i in range(1,k)]})
    cooks = m.get_influence().cooks_distance[0]
    residuals = pd.DataFrame({'row':d.index,'fitted':m.fittedvalues.to_numpy(),'residual':m.resid.to_numpy(),'cook':cooks,'cook_flag':cooks>4/n})
    if time: residuals[time] = d[time].to_numpy()
    summary = dict(n=int(n), dropped=int(len(data)-n), df_resid=int(m.df_resid), r2=float(m.rsquared), adjusted_r2=float(m.rsquared_adj), f=float(m.fvalue), f_p=float(m.f_pvalue), alpha=alpha, lags=lags if time else None, durbin_watson=float(durbin_watson(m.resid)) if time else None)
    for name,table in [('coefficients',coef),('diagnostics',diagnostics),('vif',vif),('residuals',residuals),('correlations',d[[y,*x]].corr()),('descriptive',d[[y,*x]].describe())]:
        table.to_csv(out/(name+'.csv'),index=name in ['correlations','descriptive'])
    (out/'summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
    (out/'ols.txt').write_text(m.summary().as_text(),encoding='utf-8')
    def save(name):
        plt.tight_layout(); plt.savefig(out/(name+'.svg')); plt.close()
    plt.figure(); plt.scatter(m.fittedvalues,m.resid,s=14,alpha=.7); plt.axhline(0,color='gray'); plt.xlabel('Fitted'); plt.ylabel('Residual'); plt.title('Residuals vs fitted'); save('residuals_fitted')
    sm.qqplot(m.resid,line='s'); plt.title('Normal Q-Q'); save('qq')
    plt.figure(); plt.hist(m.resid,bins=15); plt.xlabel('Residual'); plt.ylabel('Frequency'); save('histogram')
    plt.figure(); plt.stem(np.arange(n),cooks,markerfmt=' '); plt.axhline(4/n,color='gray'); plt.xlabel('Observation'); plt.ylabel("Cook's distance"); save('influence')
    if time:
        plt.figure(); plt.plot(d[time],m.resid); plt.axhline(0,color='gray'); plt.ylabel('Residual'); save('residuals_time')
    return summary,coef,diagnostics


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('file'); p.add_argument('--y',required=True); p.add_argument('--x',nargs='+',required=True)
    p.add_argument('--sheet',default=None); p.add_argument('--time'); p.add_argument('--lags',type=int,default=4)
    p.add_argument('--alpha',type=float,default=.05); p.add_argument('--out',default='output'); p.add_argument('--sep',default=','); p.add_argument('--decimal',default='.')
    a=p.parse_args(); f=Path(a.file)
    if f.suffix.lower()=='.csv': d=pd.read_csv(f,sep=a.sep,decimal=a.decimal)
    elif f.suffix.lower() in ['.xlsx','.xlsm']: d=pd.read_excel(f,sheet_name=a.sheet or 0,decimal=a.decimal)
    else: p.error('Use CSV, XLSX or XLSM.')
    summary,_,_=analyze(d,a.y,a.x,a.out,a.time,a.lags,a.alpha)
    print(json.dumps(summary,indent=2))

if __name__=='__main__': main()
