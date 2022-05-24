from bs4 import BeautifulSoup
import requests

url = "https://github.com/pranjalikamblekar?tab=repositories"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")
div = doc.find_all(class_="wb-break-all")

repo_dict = {}

for d in div:
  repo_list = d.find("a")
  name = repo_list.string.strip() 
  link = "https://github.com"+repo_list['href']
  repo_dict[name] = link

for k,v in repo_dict.items():
  print(f"{k} : {v}\n")