import requests
import pandas as pd
import json
import os

from dotenv import load_dotenv
load_dotenv()


class alpha_stock:
    def __init__(self):
        response = requests.get(os.getenv("aplha_url"))

        json_response = response.json()

        df_response = pd.DataFrame.from_dict(json_response["Time Series (60min)"],
                                             orient='index',
                                             dtype=float)

        self.df = df_response
