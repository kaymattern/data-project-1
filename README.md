
# Data Project 1: Discord Integration
Welcome to my Advice API!

# Purpose
The purpose of this project is to create an API that will get random advice relating to a user-inputted word and then post that advice in our DS 3002 #bot Discord channel.

# Instructions
1. Download the project-1.py file and open it in VSCode (or the IDE of your choice).
2. As you can see in the file, the link variable gets an environment variable that I created to store the Discord link to our private #bot channel. Before running the file, you must create an environment variable of your own with the Discord link. In the terminal, type `export discord_link={discord_link}` and paste in the Discord link (from the project submission on Collab). Now, you should have an environment variable with the Discord link!
3. In the terminal, execute the following command `uvicorn project-1:app --reload`.
4. Follow the link that Uvicorn is running on. It should look something like this "http://127....."
5. Once you open the link, there should be some instrutions in JSON (the same instructions as below).
6. There are two ways to execute the API: In the search bar, you can type in "/advice/{word}" and input the word of your choice to receive some advice relating to the word. Or, in the search bar, you can type "/docs" and pull up FastAPI. Then, click on "Try it Out" type in a word, and hit "Execute".
7. There are some words with no related advice. If you type in a word with no advicce, an Internal Server Error will result. If this happens, choose a new word and try again!
