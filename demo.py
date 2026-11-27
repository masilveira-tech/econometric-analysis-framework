"""Synthetic demonstration: not Brazilian economic data."""
import numpy as np
import pandas as pd
from econometrics import analyze

def sample():
    rng=np.random.default_rng(42)
    n=120
    g=rng.normal(2,1,n); s=rng.normal(8,2,n); shock=np.zeros(n); shock[65:75]=1
    e=rng.normal(0,.25+.1*np.abs(g),n)
    for t in range(1,n): e[t]+=.65*e[t-1]
    return pd.DataFrame({'date':pd.date_range('1995-01-01',periods=n,freq='QS'),'unemployment':9-.6*g+.2*s+1.5*shock+e,'gdp_growth':g,'lagged_rate':s,'shock':shock})

if __name__=='__main__':
    analyze(sample(),'unemployment',['gdp_growth','lagged_rate','shock'],'demo_results',time='date')
