import random

def roll_the_dice():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("Enter the number of players (2-4): ")
    if players == "exit" or players == "quit":
        print("Goodbye")
        exit()
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Please enter a number between 2 and 4")
    else:
        print("Invalid value, please try again.")


max_score = 50
players_score = [0 for _ in range(players)]

while max(players_score) < max_score:

    for player_idx in range(players):
        print(f"\nPlayer number {player_idx + 1} turn has just started!\n")
        current_score = 0

        while True:
            should_roll = input("Do you want to roll the dice (y/n): ").lower()
            if should_roll != "y":
                break

            value = roll_the_dice()
            if value == 1:
                print("You rolled a 1! Turn one")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a {value}!")

            print(f"Your current score is now {current_score}")

        players_score[player_idx] += current_score
        print(f"Your total score is now: {players_score[player_idx]}")

max_score = max(players_score)
winning_idx = players_score.index(max_score)
print(f"\nThe winner is player {winning_idx + 1} with a score of {max_score}")