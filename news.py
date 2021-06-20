import requests
api_address= ('https://newsapi.org/v2/top-headlines?country=us&apiKey=54703bd8678b43b4ab72820379ca7fac')
json_data = requests.get(api_address).json()

ar=[]

def news():
    for i in range(3):
       ar.append("Number "+str(i+1) +" "+ json_data["articles"][i]["title"]+".")
    return ar

arr=news()
print(arr)