#!/usr/bin/env python
# coding: utf-8

# # Portfolio Analysis

# ### Does the historical perfomance of a company predict its future performance? 
# For the project, you will give a hypothesis to this question. You will implement and test a simple investment strategy: buying the best peforming stocks. <br> This strategy is an example of *momentum investing*. This means you believe the stocks will continue to perform well based on historical data and trends. You can learn more about this strategy <a href="https://www.investopedia.com/terms/m/momentum_investing.asp">here</a>. <br> To compare this strategy you will test it against another strategy: buying the worst perfoming stocks. For a given dataset you will find which are the best and worst stocks and you will also test their performance in the "future".
# 
# **But before we go into the strategies, let's take a look at the data we have available.**

# For this project we have available historical stock returns from beggining of 2012 until the end of 2021 for 419 different companies that are part of the [Standard and Poor's 500 list](https://en.wikipedia.org/wiki/S%26P_500). The symbol used in trading for this list is `SPX`.
# 
# Your first task is to create a function that loads our dataset as a pandas DataFrame. Data can be found in the file  named `spx_price_data_clean.pk`.

# In[ ]:





# In[17]:


import pandas as pd
import yfinance as yf
import price_analysis as pa
import spx_data as spx


def load_spx_data() -> pd.DataFrame:
    
    px_clean = spx.get_cached_clean_price_data()
    return px_clean

spx_dataa = load_spx_data()
spx_dataa
 #function is now saved, return returns a value/ datafram, can now pull function as "spx_dataa"
    


# The dataset contains the daily stock prices in column `adj_close` and other metadata about the stock or price. To do meaningful analysis on the stocks, you will might need to enrich the dataset with additional important stock data. 
# 
# You will start by creating a function that given the dataset, a start year and an end year (both inclusive), it returns a copy of the dataset but with a new column that contains the daily returns per stock (ticker). Daily return is defined as the percentage change between any two consecutive days' prices.

# In[15]:


# Add any necessary imports here


def add_daily_returns(dataset: pd.DataFrame, start_year: int, end_year: int) -> pd.DataFrame:
    pass  # delete this line before implementing the function
    # TODO


# In[ ]:


spx_data_with_daily_returns = add_daily_returns(spx_data, 2012, 2021)


# Now let's take a look at the daily returns. 
# 
# Pick your favorite stock (Google - GOOG, Tesla - TSLA, Apple - AAPL etc.) and plot a graph of the daily return versus date for that stock for all of its historical data available in the dataset.

# In[ ]:


# Add any necessary imports here


# TODO
# Write code that plots the graph of *daily* returns versus date for your stock choice


# In a few words, what can you tell about the daily returns based on the graph you plotted? 

# In[ ]:


# TODO 
# Write down your observations about the graph above

#
#
#


# Now implement a function that given a dataset that has the daily returns, it returns a copy of the dataset with a new column that contains the total returns per stock per date in the timeframe. The total return for a given date is equal to the percentage change between the price at the start of the period and price on that date.

# In[ ]:


# Add any necessary imports here


def add_total_returns(dataset: pd.DataFrame, start_year: int, end_year: int) -> pd.DataFrame:
    pass  # delete this line before implementing the function
    # TODO


# In[ ]:


spx_data_with_total_returns = add_total_returns(spx_data_with_daily_returns, 2012, 2021)


# Similarly, for the same stock you picked, plot a graph of the total return versus date for all of its historical data available in the dataset and comment with your observations.

# In[ ]:


# Add any necessary imports here


# TODO
# Write code that plots the graph of *total* returns versus date for your stock choice


# In[ ]:


# TODO 
# Write down your observations about the graph above

#
#
#


# Now that you are more familiar with our dataset and know how to add necessary stock returns to it, let's dive into the investment strategy.
# 
# For this project you will implement two very similar strategies, where we will create an equally weighted portfolio by:
# 
# 1. **Picking the top 10 performing stocks over a time period**
# 2. **Picking the bottom 10 performing stocks over a time period**
# 
# To be able to test the performace of your investment strategy we will "split" the dataset in two periods. The first period will be between start of 2012 and end of 2015. Data from this time period will be used to pick top and bottom performing stocks. The rest of the dataset, between start of 2016 and end of 2021, will be used to test the performace of the picked stocks.
# 
# You will start by implementing a function that given the dataset, a start year, and an end year, returns a list with top 10 performing stocks (try to make the function generic so that it works for any number of stocks and for either best or worst performing stocks).

# In[ ]:


from typing import List
# Add any necessary imports here

def top_performing_stocks(dataset: pd.DataFrame, start_year:int, end_year:int, number_stocks:int = 10) -> List[str]:
    pass  # delete this line before implementing the function
    # TODO


# In[ ]:


# Run code below to test your function

# (JOLI - Might want to add more test cases here or in general)

assert set(top_performing_stocks(spx_data, 2012, 2012)) == {'REGN', 'PHM', 'AAL', 'WHR', 'EXPE', 'EQIX', 'BAC', 'LEN', 'STX', 'MPC'}, "Your function did not return the correct set of top 10 stock performers for year 2012 only"


# What are top 10 performing stocks for the period between 2012 and 2015?

# In[ ]:


# TODO - Get top stocks and print them here
top_stocks = top_performing_stocks(...)


# Similarly make a function that returns a list with the worst performing stocks. If needed, feel free to modify the function `top_performing_stocks` to support this functionality. 
# 
# What are the worst 10 performing stocks for the period between 2012 and 2015?

# In[ ]:


# TODO - Answer here

#
#


# Now that you are able to get lists of best and worst performing stocks, it's time to test how each of these lists would perform in the "future". 
# 
# Implement the function below that given the dataset, a start year, an end year, and a list of stocks (tickers), it returns a pandas dataset that contains the dates and the total return per each date of the portfolio that consists of the given list of stocks. 

# In[ ]:


# Add any necessary imports here


def get_portfolio_returns(dataset: pd.DataFrame, start_year: int, end_year: int, tickers: List[str]) -> pd.DataFrame:
    pass  # delete this line before implementing the function
    # TODO


# Now use the function you just implemented to get the total returns between 2016 and 2021 for the porfolio with top 10 perfoming stocks of the period between 2012 and 2015. 
# 
# Plot the total returns of the portfolio versus date.

# In[ ]:


# TODO
# Write code that plots the graph of total returns versus date for the portfolio with *top* stocks


# Now repeat the step above, but for the porfolio with the worst perfoming stocks of the period between 2012 and 2015.

# In[ ]:


# TODO
# Write code that plots the graph of total returns versus date for the portfolio with *worst* stocks


# ### Conclusions
# 
# What can you tell about the investment strategy based on the results you got? Is buying the top performing stocks a successful strategy? Is it the best strategy? How does it compare to the strategy of buying the worst performing stocks? 

# In[ ]:


# TODO - Answer here


# ## What's your investment strategy? 
#  
# Come up with an investment strategy different from the ones above and implement it below. You would need to justify your porfolio choice and test it using data different from the one used to build the portfolio.
# Feel free to use the dataset that's available or the code in `spx_data.py` to load a different dataset. 
# 
# <br>**<a href="https://www.investopedia.com/investing/investing-strategies/">Here</a> are some basic investment strategies to get you started!**

# In[ ]:




