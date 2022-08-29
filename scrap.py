# import json
# # import pandas as pd
# import requests
# from bs4 import BeautifulSoup
# url="https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating"
# response=requests.get(url)
# print(response)
# Soup=BeautifulSoup(response.content,"html.parser")
# movie_data=Soup.findAll("div",class_="lister-item mode-advanced")
# list=[]
# for store in movie_data:
#     dic={}

#     name=store.h3.a.text
#     dic["Movie name"]=name

#     year_of_release=store.h3.find("span",class_="lister-item-year text-muted unbold").text
#     dic["Year"]=year_of_release

#     runtime=store.p.find("span",class_="runtime").text.replace('min','')
#     dic["Time"]=runtime
    
#     # rate=store.find("div",class_="inline-block ratings-imdb-ratings")
#     # dic["Rating"]=rate

#     meta=store.find("span",class_="metascore").text if store.find("span",class_="metascore") else'@'
#     dic["Metascore"]=meta
#     list.append(dic)

#     # value=store.find_all("span",attrs={"name":"mv"})
#     # dic["Votes"]=votes

#     # grosses=value[1].text if len(value)>1 else("**")
#     # dic["Gross"]=grosses
# def fun():
#     with open ("task1.json","w") as f:
#         json.dump(list,f,indent=4)
#         return list
# fun()
#     # print(list)


import req