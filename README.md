# data-project-1
Welcome to my Advice API!

Instructions:
1. Download the project-1.py file and open it in VSCode (or the IDE of your choice).
2. In the terminal, execute the following command "uvicorn project-1:app --reload".
3. Follow the link that Uvicorn is running on. It should look something like this "http://127....."
4. Once you open the link, there should be some information in JSON.
5. There are two ways to execute the API: In the search bar, you can type in "/advice/{word}" and input the word of your choice to receive some advice relating to the word. Or, in the search bar, you can type "/docs" and pull up FastAPI. Then, click on "Try it Out" type in a word, and hit "Execute".
6. There are some words with no related advice. If you type in a word with no advicce, an Internal Server Error will result. If this happens, choose a new word and try again!
