from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

crypto = {}

table_body = doc.tbody
table_rows = table_body.contents
for tr in table_rows[:10]:
  name, price = tr.contents[2:4]
  fixed_name = name.p.string
  fixed_price = price.a.string
  crypto[fixed_name] = fixed_price
 
for k, v in crypto.items():
  print(f"{k}:{v}")
  



