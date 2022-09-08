"""Request real estate offers from LeBonCoin website"""
# =================
# ==== IMPORTS ====
# =================

import sys

import pandas as pd

from bs4 import BeautifulSoup
import requests


# ===================
# ==== FUNCTIONS ====
# ===================



def request_leboncoin(
    city: str, price_min: int=50000, price_max: int=200000, square_min: int=30,
) -> pd.DataFrame:
    """
    """
    URL = f'https://www.leboncoin.fr/recherche?category=9&text=immeuble&locations={city}__' \
        f'50.633472642005586_3.0612005363570756_9880_5000&owner_type=all&real_estate_type=5&' \
        f'price={price_min}-{price_max}&square={square_min}-max'
    page = requests.get(URL)