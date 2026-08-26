from random import choice

choice_box = ["rock", "paper", "scissor"]

emoji_converter = {
    "rock" : "🪨",
    "paper" : "🧻",
    "scissor" : "✂️"
}



with open("data.txt", "a") as file:
    draws = 0
    wins = 0
    loses = 0



while True:
    computer_choice = choice(choice_box)

    player_choice = input("Enter your choice (rock/paper/scissor/q): ").lower()

    if player_choice == computer_choice:

        print("Draw")
        draws += 1

    elif player_choice == "exit" or player_choice == "q":
            print("Thank you for playing")
            break

    elif player_choice not in choice_box:
            print("Invalid choice!")
            continue

    else:
        print("You lost")
        loses += 1


    print(f"Player choice: {emoji_converter[player_choice]}\nComputer choice: {emoji_converter[computer_choice]}")


print(f"You won {wins}\nDraws {draws}\nLoses {loses:}")
