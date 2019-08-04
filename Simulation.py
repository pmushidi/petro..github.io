# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 18:24:07 2019

Authors: Petro Mushidi Tshakwanda & Akinyemi Friday Owolabi

July, 29, 2019

Capstone Project ---- Group E
"""
# Importing necessary modules
from pandas import DataFrame
from pandas.io.parsers import TextFileReader
import numpy as np
from scipy import stats
import scipy as sp
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pymc3 import Normal, StudentT
import pymc3 as pm
import statsmodels.api as sm
from statsmodels.tsa.regime_switching.tests.test_markov_autoregression import rgnp
from scipy.stats import t
import matplotlib.pyplot as plt

# import Data & Convert Index to DateTime
# # Get the data set
path = './'

# returns = pd.read_csv(path + 'returns.csv', index_col='date')

df = pd.read_csv('returns.csv', index_col=0, parse_dates=True)
# df = pd.read_csv('returns.csv', index_col='date')

# Show example
print(df.returns.head())

# Plot the datasets
df.returns.plot(label='SP&500', figsize=(16, 8), title='Daily Returns of S&P500')
plt.legend()
plt.show()

data_sp500 = df.returns

# Fitted result on SP500 daily returns data set using MS Gaussian distribution
mod_hamilton = sm.tsa.MarkovAutoregression(data_sp500, k_regimes=2, order=1, switching_ar=True, trend='c',
                                           switching_exog=True)
res_hamilton = mod_hamilton.fit()
print(res_hamilton.summary())

ax = res_hamilton.smoothed_marginal_probabilities[0].plot(figsize=(8, 4))
ax.set(title='Parameters and regime probabilities from Hamilton Markov Switching Model')
plt.legend()
plt.show()

# Fitted result on S&P500 daily returns data set using MS Student T distribution

rv = t(df=3, loc=0, scale=1)
x = np.linspace(rv.ppf(0.0001), rv.ppf(0.9999), 100)
returns = rv.sf(data_sp500)

y = df.returns
print(y)
mod_hamilton = sm.tsa.MarkovAutoregression(y, k_regimes=2, order=1, switching_ar=True)
res_hamilton = mod_hamilton.fit()
print(res_hamilton.summary())

ax = res_hamilton.smoothed_marginal_probabilities[0].plot(figsize=(8, 4))
ax.set(title='Parameters and regime probabilities from Hamilton Markov Switching Model (Student-T')
plt.legend()
plt.show()
