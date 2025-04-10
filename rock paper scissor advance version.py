#                                      Task - 2

#                              Rock-Paper-Scissors Game

#  Create a program that allows the user to play the classic game of rock, paper,
#  scissors against the computer.

import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    user_score = 0
    computer_score = 0
    print("Welcome to Rock, Paper, Scissors!")

    while True:
        print("\nRound Start!")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose {user_choice}")
        print(f"Computer chose {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"\nScore - You: {user_score}, Computer: {computer_score}")

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
