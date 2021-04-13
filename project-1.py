from fastapi import FastAPI
import requests
import json
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Welcome to Kay Mattern's advice API!",
    "Instructions": "In the search bar above, type /advice/{word} and type in any word. Press Enter and you should receive some advice relating to the word!",
    "No advice?": "If you see Internal Server Error returned to you, that means no advice was found relating to your word. Pick a new word and try again!",
    "Want to try using FastAPI?": "In the search bar, type /docs to pull up FastAPI. Then, click Try it Out, type in your word, and hit Execute!"}

@app.get("/advice/{word}")
def get_advice(word: str):
    try:
        url = "https://api.adviceslip.com/advice/search/"
        url_word = url + word
        advice = requests.get(url_word)
        advice_json = advice.json()
        quote = advice_json['slips'][0]['advice']
        data = { 
        "content": quote,
        "username": "Golden Retriever",
        "avatar_url": "https://www.pngitem.com/pimgs/m/113-1132668_5-golden-retriever-puppy-golden-retriever-cartoon-png.png"
        } 
        link = os.getenv('discord_link')
        #response = requests.post(link, json = data)
        #print(response)
        return quote
    except 'Internal Server Error':
        return "There was no advice relating to that word. Please try again with a new word!"
