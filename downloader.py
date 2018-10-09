import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

headers = {}

r = requests.get("https://trends.google.com/trends/explore?date=now%201-H&geo=ES&q=masmovil,movistar,vodafone,orange", headers=headers)
# parse and retrieve two vital form values
if not r.status_code == 200:
    print('Error:'+str(r.status_code))
