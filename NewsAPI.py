import requests
import json


newstofind=input("What would you like to know today ? ")
url=f"https://newsapi.org/v2/everything?q={newstofind}&from=2024-06-11&sortBy=publishedAt&apiKey=c14085da5c32419cb3cac679a3e378fe"
r=requests.get(url)

news=json.loads(r.text)   


for article in news["articles"]:
  print(article["title"])
  print(article["description"])
  print("--x--")