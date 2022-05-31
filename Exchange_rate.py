from datetime import datetime, timedelta

import requests
from bs4 import BeautifulSoup

today = datetime.now()


def exchange_rate(soup):
    day = today.strftime('%d/%m/%Y')
    curs = f'https://www.cbr.ru/scripts/XML_daily.asp?date_req={day}'
    curs = requests.get(curs).text
    soup = BeautifulSoup(curs, features="xml")
    return soup


def exchange_rate_usd(usd):
    usd = exchange_rate(soup='').find(ID='R01235').Value.string
    return usd


def exchange_rate_euro(euro):
    euro = exchange_rate(soup='').find(ID='R01239').Value.string
    return euro


def exchange_rate_gold(gold):
    yesterday = (today - timedelta(days=1))
    new_today = today.strftime('%d/%m/%Y')
    while True:
        try:
            met = f'https://www.cbr.ru/scripts/xml_metall.asp?date_req1={new_today}&date_req2={new_today}'
            met = requests.get(met).text
            soup = BeautifulSoup(met, features="xml")
            gold = soup.find(Code="1").Buy.string
            return gold
            break
        except:
            yesterday = (yesterday - timedelta(days=1))
            new_today = yesterday.strftime('%d/%m/%Y')
            continue
