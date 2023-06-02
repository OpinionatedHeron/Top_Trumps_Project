import random
import requests

# Required Task 1: Generate a random number to use as Pokémon ID
pokemon_id = random.randint(1, 151)
input("Ready player one? (Y/N) ")
if "Y" and "y":
    print("Your Pokemon ID is {}".format(pokemon_id))

# Required Task 2: Use Pokémon API to choose a Pokémon based on the ID Number
card = pokemon_id
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_id)
response = requests.get(url)
pokemon_id = response.json()
print("Your Pokemon is {}".format(pokemon_id["name"]))

# Required Task 3: Create a Dictionary for Pokémon's Name, ID, Height, Weight
pokemon_dictionary = {
    "name": pokemon_id["name"],
    "id": pokemon_id["id"],
    "height": pokemon_id["height"],
    "weight": pokemon_id["weight"]
}
print("Here are your Pokemon's stats: {}".format(pokemon_dictionary))

# Required Task 4: Random Pokémon for Player and Opponent
opponent_card = random.randint(1, 151)
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(opponent_card)
response = requests.get(url)
opponent_pokemon = response.json()
print("Your Opponent's Pokemon is" + opponent_pokemon["name"])

# Decided not to show any of the opponent's stats, so it feels more like a Top Trumps Game.
# Player chooses the stat blind based on their own stats.

# Required Task 5: Ask the User which stat they want to use
print("Stat Options: ID, Weight, Height")
stats = ["ID", "Weight", "Height"]
stat_choice = input("Which stat would you like to compare? ")
if stat_choice in stats:
    print("You chose: {}".format(stat_choice))
else:
    print("You have not selected a valid stat. Stats are case sensitive. Please try again.")

# Required Task 6: Compare Player and Opponent's Pokémon on the chosen stat
if stat_choice == "ID":
    if pokemon_id["id"] >= opponent_pokemon["id"]:
        print("Your Pokemon ID is " + str(pokemon_id["id"]))
        print("Your Opponent's ID is " + str(opponent_pokemon["id"]))
        print("Your ID is higher. You win!")
    else:
        print("Your ID is lower. You lose!")
elif stat_choice == "Weight":
    if pokemon_id["weight"] >= opponent_pokemon["weight"]:
        print("Your Pokemon's Weight is " + str(pokemon_id["weight"]))
        print("Your Opponent's Weight is " + str(opponent_pokemon["weight"]))
        print("Your Weight is higher. You win!")
    else:
        print("Your Weight is lower. You lose!")
elif stat_choice == "Height":
    if pokemon_id["height"] >= opponent_pokemon["height"]:
        print("Your Pokemon's Height is " + str(pokemon_id["height"]))
        print("Your Opponent's Height is " + str(opponent_pokemon["height"]))
        print("Your Height is higher. You win!")
    else:
        print("Your Height is lower. You lose!")
