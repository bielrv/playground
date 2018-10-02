import json
import sys
import pandas as pd
import requests
import os
os.getcwd()
import time
import csv
from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)

class trend:
    def __init__(self, kw_list):
        self.kw_list = kw_list

        pytrends.build_payload(
            kw_list, cat=0, timeframe='today 5-y', geo='ES', gprop='')

        self.df = pytrends.get_historical_interest(kw_list,
                                                     year_start=2018,
                                                     month_start=1,
                                                     day_start=1,
                                                     hour_start=0,
                                                     year_end=2018,
                                                     month_end=2,
                                                     day_end=1,
                                                     hour_end=0,
                                                     cat=0,
                                                     geo='ES',
                                                     gprop='',
                                                     sleep=0)

# pytrends.related_queries()
