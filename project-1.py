from fastapi import FastAPI
import requests
import json

app = FastAPI()

@app.get("/advice/{word}")
def get_advice(word: str):
    url = "https://api.adviceslip.com/advice/search/"
    url_word = url + word
    advice = requests.get(url_word)
    advice_json = advice.json()
    quote = advice_json['slips'][0]['advice']
    data = { 
    "content": quote,
    "username": "kaymattern",
    "avatar_url": "REPLACE_WITH_CREATIVE_URL"
    } 
    link = "https://discord.com/api/webhooks/xxxxx/yyyyy"
    response = requests.post(link, json = data)
    print(response)
