from alpha_vantage.timeseries import TimeSeries
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import sys
import os
import numpy as np

from dotenv import load_dotenv
load_dotenv()

class stock:
     def __init__(self,stock_code):
         self.stock_code = stock_code
         ts = TimeSeries(key=os.getenv("alpha_vantage_key_2"), output_format='pandas')
         self.df, self.meta_data = ts.get_intraday(stock_code,interval='60min', outputsize='full')
