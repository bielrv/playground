import pandas as pd
import datetime
from functions import dataframe_to_csv

class data():

    def __init__(self):

        from google_trends import trend
        trends = trend(["MasMovil", "Movistar", "Vodafone", "Orange"])
        dataframe_to_csv('trends', trends.df)


        from alpha_api import alpha_stock
        stocks = alpha_stock()
        stocks.df.shape
        dataframe_to_csv('stocks', stocks.df)

        complete_df = trends.df.join(stocks.df)
        complete_df = complete_df.drop(columns='isPartial')

        self.df = complete_df

# from alphavantage import stock
# stocks = stock('ORTH.ILN')
# stocks.df
