#!/Users/meyghamachado/Library/Python/3.7/bin/
from bs4 import BeautifulSoup
# import urllib3
import csv
import os

folder = '/Users/meyghamachado/Downloads/'
file_name = 'Magic_Formula_Stocks_2024_09_26'
source_stocks = os.path.join(folder, f"{file_name}.html")

with open(source_stocks) as f:
    html = f.read()

soup = BeautifulSoup(html)
table = soup.select_one("table.divheight")
# python3 just use th.text
headers = [th.text.strip("\n") for th in table.select("tr th")]

with open(f"{file_name}.csv", "w") as f:
    wr = csv.writer(f)
    wr.writerow(headers)
    wr.writerows([[td.text for td in row.find_all("td")] for row in table.select("tr")[1:]])
