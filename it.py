import random

while True:
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    player_choice = input("Your turn: ").lower()
    while player_choice not in options:
        player_choice = input(
            "Invalid choice. Choose rock, paper, or scissors: ").lower()

    print("Computer's choice:", computer_choice)
    print("Player's choice:", player_choice)

    if computer_choice == "rock":
        if player_choice == "paper":
            print("You win! Paper covers rock.")
        elif player_choice == "scissors":
            print("Computer wins! Rock smashes scissors.")
        else:
            print("It's a draw!")

    elif computer_choice == "paper":
        if player_choice == "scissors":
            print("You win! Scissors cut paper.")
        elif player_choice == "rock":
            print("Computer wins! Paper covers rock.")
        else:
            print("It's a draw!")

    elif computer_choice == "scissors":
        if player_choice == "rock":
            print("You win! Rock smashes scissors.")
        elif player_choice == "paper":
            print("Computer wins! Scissors cut paper.")
        else:
            print("It's a draw!")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break
