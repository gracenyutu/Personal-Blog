import requests,json

def get_quotes():
    response = requests.get('https://famous-quotes4.p.rapidapi.com/random')
    if response.status_code == 200:
        quote = response.json()
        return quote


# querystring = {"category":"all","count":"2"}

# headers = {
# 	"X-RapidAPI-Host": "famous-quotes4.p.rapidapi.com",
# 	"X-RapidAPI-Key": "47e5fb643cmsh4c25729c915f11fp1f6156jsn60e461baee47"
# }

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)