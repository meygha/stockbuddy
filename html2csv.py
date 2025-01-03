#!/usr/local/bin/python
from datetime import datetime, timedelta
from pytz import timezone
from bs4 import BeautifulSoup
import csv
import os
import yfinance as yf
from pathlib import Path

input_data_dir = Path('input')
output_data_dir = Path('output')
file_name = 'Magic_Formula_Stocks_2025_01_03'
source_stocks = input_data_dir / f"{file_name}.html"
NUM_LOOKBACK_YEARS = 10

def count_dividend_payout(ticker_obj):
    count = 0
    cutoff_date = datetime.now(tz=timezone('America/New_York')) - timedelta(days=NUM_LOOKBACK_YEARS*365)
    dividend_dates = [ t for t in ticker_obj.dividends.keys() ]
    count = [ d > cutoff_date for d in dividend_dates ].count(True)
    return str(count)


with open(source_stocks) as f:
    html = f.read()

soup = BeautifulSoup(html, features="lxml")
table = soup.select_one("table.divheight")
headers = [th.text.strip("\n") for th in table.select("tr th")]
headers.append(f"Number of dividend payouts in the last {NUM_LOOKBACK_YEARS}")

with open(output_data_dir / f"{file_name}.csv", "w") as f:
    wr = csv.writer(f)
    wr.writerow(headers)
    # breakpoint()
    for row in table.select("tr")[1:]:
        fields = []
        # breakpoint()
        fields = [fd.text for fd in row.find_all("td")]
        ticker = yf.Ticker(fields[1])
        div_payout_cnt = count_dividend_payout(ticker)
        fields.append(div_payout_cnt)
        wr.writerow(fields)
