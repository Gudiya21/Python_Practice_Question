import requests
import json
x=requests.get("https://jsonplaceholder.typicode.com/posts")
a=x.json()
# print(a)
# print(x)
def my():
    with open("data.json","w") as f:
        json.dump(a,f,indent=4)
        return a
my()
