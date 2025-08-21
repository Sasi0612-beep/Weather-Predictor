import random
import cowsay

def get_user_choice():
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        cowsay.tux("Invalid choice. Please choose rock, paper, or scissors.")
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
    return choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def decide_winner(user, computer):
    if user == computer:
        return "draw"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        return "user"
    else:
        return "computer"

def play_game():
    cowsay.cow("Welcome to Rock, Paper, Scissors!")
    user = get_user_choice()
    computer = get_computer_choice()

    cowsay.dragon(f"You chose: {user}")
    cowsay.turtle(f"Computer chose: {computer}")

    winner = decide_winner(user, computer)

    if winner == "draw":
        cowsay.beavis("It's a draw!")
    elif winner == "user":
        cowsay.cow("You win! 🎉")
    else:
        cowsay.daemon("Computer wins! 😢")

if __name__ == "__main__":
    play_game()
