# from urllib import request
import requests
import json
import pyttsx4

url = "https://official-joke-api.appspot.com/random_ten"
response = requests.get(url)


class Joke:
    def __init__(self, setup, punchline) -> None:
        self.setup = setup
        self.punchline = punchline
    
    #override the string method
    def __str__(self) -> str:
        return f"Setup {self.setup} Punchline {self.punchline}"
    

print(response.status_code)

jsonData = json.loads(response.text)
print(jsonData)

jokes = []

for j in jsonData:
    setup = j["setup"]
    punchline = j["punchline"]
    joke = Joke(setup, punchline)
    jokes.append(joke)

print(f"length of jokes : {len(jokes)}")
for idx, joke in enumerate(jokes, start=1):
    print(f"joke :{idx} : {joke}")
    pyttsx4.speak(joke.setup)
    pyttsx4.speak(joke.punchline)