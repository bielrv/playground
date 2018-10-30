import pandas as pd
import datetime
import os


def dataframe_to_csv(csv_name, df):
    csv_name = '{}_{}.csv'.format(
        csv_name, datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
    path = os.getcwd()
    path = path + '/data/'
    df.to_csv(path + csv_name)
