import random
import requests

def random_pokemon():
    pokemon = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon)
    response = requests.get(url)
    pokemon = response.json()
    return pokemon

stats = random_pokemon()["stats"]

for name in stats:
    print(name["name"])
