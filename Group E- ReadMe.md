WorldQuant University
Course : Capstone Project (MScFE 690 - C18-S3T2)
Project Title: Modelling Market Regime: Comparison Between Gaussian and Non-Gaussian Markovic Models
Author: Group E 
        
    Petro Mushidi Tshakwanda, Sutdent Member, IEEE, petro.tshakwanda@gmail.com
    Akinyemi Friday Owolabi, Sutdent Member, IEEE, friday4real567@yahoo.com
   
Date: August-05-2019

Platforms
----------------------
IDE: PyCharm
Version of Python: 3.7.3

Description
----------------------
1. Most   traditional   asset   pricing   strategies   assume constant  volatilities  in  their  models  and  mostly  hedge  only  the risk  of  price  
fluctuation  in  the  underlying  asset.  However,  the assumption  of  constant  volatility  makes  such  traditional  models (e.g  Black  Scholes) 
inadequate  since  there  is  constant  volatility jumps  in  real  market  situation.  This  volatility  jumps  introduce another  risk  commonly  
called  the  Market  Price  of  Volatility Risk   (MPVR).   The   MPVR   is   state-dependent   with   different levels of risk or volatility states. 
To understand and capture the effect  of  varying  states  of  volatility,  alternative  methods  knownas  Regime  switching  models  have  become  common. 
Broadly speaking, two types of regime switching models exist- Threshold Models  (TM)  and  Markov  Switching  Models  (MSM).  
Between the  two  types  of  switch  models  the  Markov  Switch  Models (MSMs)  has  been  chosen  for  this  research  because,  unlike  the Threshold 
models   that   rely   on   an   exogenous   state   variable, MSM  capture  the  state  change  signals  that  are  inherent  in the data.
In empirical research,Gaussian-based parameters have been  commonly  applied  with  MSM  implementation.  However,considering  the  fact  that  financial data  contains  skewness,  fattail and excess kurtosis, the results/ forecasts of these Gaussian-parameterized models may not be adequate. 
As an alternative, we propose to implement a non-Gaussian parameterization-StudentT (STUD)  distribution to see if a better model performance is possible.

2. To actualise this objective, the following activities were performed:  
   
- First we implement Markov Models (Gaussian, Non-Gaussian Student-T distributions) and use it to split the studied period into different regimes.
- Second we present specification tests  for  autocorrelations  and  for  the  first-order  Markov  as-sumption of the Student-T.
- Third we perform a simulation study of both Gaussian and Student-T Markov Switching models andevaluate  them  by  comparing  its  performance  using  the  S&P500 index dataset get from Yahoo Finance. 
3. We then analysed both models using appropriate model selection criteria.
4. Developed appropriate graphs to visualise results.

System and Hardware Requirements
--------------------------------
Higher than Pentium II processor
Higher than 4 RAM and 500GB HDD space
Windows 7/8/10 Professional (32 or 64 bits).

Installation
--------------
1. Install the IDE "Pycharm is available here <https://pycharm-community-edition.en.softonic.com/download>:
2. Install Python 3.7.3 - https://www.python.org/downloads/
3. Use "$ pip install <put the name of the Package>" to install the package

Packages Used
-------------
To run the code, make sure to install the following basic packages:
- Pandas
- Numpy
- scipy 
- seaborn
- matplotlib
- pymc3
- statsmodels.api

License
-------
Python 3.7.3
The Scientific Python Development Environment 
