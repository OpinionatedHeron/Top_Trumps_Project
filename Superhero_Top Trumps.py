import random
import requests

rounds = 0
wins = 0
play_again = "y"

while play_again.lower() == "y":
    superhero_id = random.randint(1, 731)
    print("Your hero ID is {}".format(superhero_id))

    hero = superhero_id
    url = 'https://superheroapi.com/api/10221873999059433/{}/powerstats'.format(hero)
    response = requests.get(url)
    hero = response.json()

    print("Your chosen hero is {}".format(hero["name"]))

    hero_dictionary = {
        "Name": hero["name"],
        "ID": hero["id"],
        "Intelligence": hero["intelligence"],
        "Strength": hero["strength"],
        "Speed": hero["speed"],
        "Durability": hero["durability"],
        "Power": hero["power"],
        "Combat": hero["combat"]
    }

    print("Here are your hero's powerstats: {}".format(hero_dictionary))

    opponent_id = random.randint(1, 731)
    url = 'https://superheroapi.com/api/10221873999059433/{}/powerstats'.format(opponent_id)
    response = requests.get(url)
    v_hero = response.json()

    print("Your Opponent's hero is {}".format(v_hero["name"]))

    print("Let's get ready to RUMBLE!!")
    print(hero["name"], "VS", v_hero["name"])
    print("Which stat would you like to compare:")
    stats = {
        "1": "id",
        "2": "intelligence",
        "3": "strength",
        "4": "speed",
        "5": "durability",
        "6": "power",
        "7": "combat"
    }


    def print_stats(stats):
        for key, value in stats.items():
            print(f"{key}. {value}")


    def chosen(stats):
        while True:
            print_stats(stats)
            choice = input("Select a stat 1, 2, 3, 4, 5, 6, 7: ")
            if choice in stats:
                return stats[choice]
            else:
                print("Invalid stat. Please try again")


    selected_stat = chosen(stats)
    print(f"You have selected: {selected_stat}")

    player = hero[selected_stat]
    cpu = v_hero[selected_stat]

    print(hero["name"], "-", selected_stat + ":", player)
    print(v_hero["name"], "-", selected_stat + ":", cpu)

    if player > cpu:
        print("Your hero:", hero["name"], "wins!")
        wins += 1
    elif cpu > player:
        print("Opponent's hero:", v_hero["name"], "wins! You lose, try again.")
    else:
        print("It's a draw.")

    rounds += 1
    play_again = input("Try another round? (y/n): ")
    if play_again.lower() != "y":
        break

print("Game Over!")
print("Number of Rounds Played: ", rounds)
print("Number of Rounds Won: ", wins)
