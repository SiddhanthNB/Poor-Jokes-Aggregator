from colorama import init
from requests import get
from pyfiglet import figlet_format 
from termcolor import colored
from random import choice
from colorama import init


init()

header = figlet_format("!! poor jokes !!")
header = colored(header, color="magenta",attrs=["blink"])
print(header)

term = input("Let me tell you a joke! Give me a topic: ")
print("p.s. process depends on your internet bandwidth. patience is appriciated")
response_json = get(
    "https://icanhazdadjoke.com/search",
    headers={"Accept": "application/json"},
    params={"term": term}
).json()
results = response_json["results"]
total_jokes = response_json["total_jokes"]
if total_jokes > 1:
    print(
        f"I've got {total_jokes} jokes about {term}. Here's one:\n",
        choice(results)['joke']
    )
elif total_jokes == 1:
    print(
        f"I've got one joke about {term}. Here it is:\n",
        results[0]['joke']
    )
else:
    print(f"Sorry, I don't have any jokes about {term}! Please try again.")
