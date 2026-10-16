import random


def main() -> None:
    players = ["Alice", "bob", "Charlie", "dylan", "Emma",
               "Gregory", "john", "kevin", "Liam"]
    print(f"Initial list of players: {players}\n")

    mod_players = [x.capitalize() for x in players]
    print(f"New list with all names capitalized: {mod_players}\n")

    mod_pla_WC = [x for x in players
                  if x.capitalize() in x]
    print(f"New list of capitalized names only:"
          f"{mod_pla_WC}\n")
    my_dict = {
        k: random.randint(1, 1000) for k in mod_players
    }
    print(f"Score dict: {my_dict}")
    average: float = 0
    for name in mod_players:
        average += my_dict[name]
    average = round(average / len(my_dict), 2)
    print(average)

    my_dict3 = {
        k: my_dict[k] for k in mod_players if my_dict[k] > average
    }
    print(my_dict3)


if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    main()
