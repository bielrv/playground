from alpha_vantage.timeseries import TimeSeries
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import sys
import os
import numpy as np

ts = TimeSeries(key='1ORS1XLM1YK1GK9Y') # Not my key ;)

# Get json object with the intraday data and another with  the call's metadata
data, meta_data = ts.get_intraday('0RTH.ILN')

data
