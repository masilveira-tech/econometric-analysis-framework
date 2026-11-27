import tempfile
import unittest
import numpy as np
from demo import sample
from econometrics import analyze

class TestFramework(unittest.TestCase):
    def test_time_series(self):
        with tempfile.TemporaryDirectory() as d:
            s,c,t=analyze(sample(),'unemployment',['gdp_growth','lagged_rate','shock'],d,time='date')
            self.assertEqual(s['df_resid'],116)
            self.assertTrue(np.isclose(s['r2'],.752610097139588))
            self.assertTrue(np.allclose(c[c.method=='OLS'].coef,c[c.method=='HAC'].coef))
            self.assertLess(t.loc[t.test=='Breusch-Godfrey','p'].iloc[0],.05)
    def test_cross_section(self):
        with tempfile.TemporaryDirectory() as d:
            s,c,t=analyze(sample(),'unemployment',['gdp_growth','lagged_rate','shock'],d)
            self.assertEqual(set(c.method),{'OLS','HC3'})
    def test_rank_deficiency(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ValueError):
                analyze(sample().assign(duplicate=sample().gdp_growth),'unemployment',['gdp_growth','duplicate'],d)

if __name__=='__main__': unittest.main()
