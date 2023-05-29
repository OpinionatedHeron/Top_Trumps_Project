import random
import requests


def random_pokemon():
    pokemon = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon)
    response = requests.get(url)
    pokemon = response.json()
    return pokemon


player_card = random_pokemon()
opponent_card = random_pokemon()

player_dictionary = {
    "name": player_card["name"],
    "id": player_card["id"],
    "height": player_card["height"],
    "weight": player_card["weight"]
}

opponent_dictionary = {
    "name": opponent_card["name"],
    "id": opponent_card["id"],
    "height": opponent_card["height"],
    "weight": opponent_card["weight"]
}

print("Player's Card:", player_dictionary)
print("Opponent's Card:", opponent_dictionary)

stats = ["id", "weight", "height"]

print("Stat Options: id, height, weight")
choose_stat = input("Which stat would you like to compare?")
if choose_stat in stats:
    print("You have selected: {}".format(choose_stat))
else:
    print("{} is not a stat option. Please choose again.".format(choose_stat))

player = player_card[choose_stat]
opponent = opponent_card[choose_stat]

print("Player Card", player_card["name"], "-", choose_stat + ":", player)
print("Opponent Card", opponent_card["name"], "-", choose_stat + ":", opponent)

if player > opponent:
    print("Player's Pokemon:", player_card["name"], "wins!")
elif opponent > player:
    print("Opponent's Pokemon:", opponent_card["name"], "wins!")
else:
    print("It's a draw!")
