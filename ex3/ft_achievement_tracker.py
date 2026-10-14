import random


def gen_player_achievements() -> set:
    Achievements = set(
        ["Crafting Genius", "Strategist", "World Savior", "Speed Runner",
         "Survivor", "Master Explorer", "Treasure Hunter", "Unstoppable",
         "First Steps", "Collector Supreme", "Untouchable", "Sharp Mind",
         "Boss Slayer", "Night Owl", "Iron Will", "Perfectionist"]
        )
    Alice = set(random.sample(list(Achievements), 6))
    Bob = set(random.sample(list(Achievements), 7))
    Charlie = set(random.sample(list(Achievements), 9))
    Dylan = set(random.sample(list(Achievements), 5))
    print(f"Player Alice = {Alice}")
    print(f"Player Bob = {Bob}")
    print(f"Player Charlie = {Charlie}")
    print(f"Player Dylan = {Dylan}")
    print()

    Achievements = Alice.union(Bob, Charlie, Dylan)
    print(f"All distinct achievements : {Achievements}")
    print()
    print(f"Common achievements: {Alice.intersection(Bob, Charlie, Dylan)}")
    print(f"Only Alice has: {Alice.difference(Bob, Charlie, Dylan)}")
    print(f"Only Bob has: {Bob.difference(Alice, Charlie, Dylan)}")
    print(f"Only Charlie has: {Charlie.difference(Bob, Alice, Dylan)}")
    print(f"Only Dylan has: {Dylan.difference(Bob, Charlie, Alice)}")
    print()
    print(f"Alice is missing : {Achievements - Alice}")
    print(f"Bob is missing : {Achievements - Bob}")
    print(f"Charlie is missing : {Achievements - Charlie}")
    print(f"Dylan is missing : {Achievements - Dylan}")

    return Achievements


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    gen_player_achievements()
