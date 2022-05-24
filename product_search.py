from bs4 import BeautifulSoup
import requests
import re

gpu = input("What product do want to search for? ")

#Getting the website HTML
url = f"https://www.newegg.ca/p/pl?d={gpu}&N=4131"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

#Querying multiple pages
page_text = doc.find(class_="list-tool-pagination-text").strong
pages = int(str(page_text).split("/")[-2].split(">")[-1][:-1])

items_found = {}

#Finding the products
for page in range(1, pages+1):
  url = f"https://www.newegg.ca/p/pl?d={gpu}&N=4131&page={page}"
  page = requests.get(url).text
  doc = BeautifulSoup(page, "html.parser")

  div = doc.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
  items = div.find_all(text=re.compile(gpu))
  for item in items:
    parent = item.parent
    if parent.name != "a":
      continue
    link = parent['href']

    next_parent = item.find_parent(class_="item-container")
    price = next_parent.find(class_="price-current").strong.string

    items_found[item] = {'Price': int(price.replace(",", "")), 'Link': link}

sorted_items = sorted(items_found.items(), key=lambda x: x[1]['Price'])

for item in sorted_items:
  print(item[0])
  print(f"${item[1]['Price']}")
  print(item[1]['Link'])
  print("----------------------------------------------------------")