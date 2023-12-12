import random
def get_user_choice():
    user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
    return user_choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return f"You win! {user_choice.capitalize()} beats {computer_choice}."
    else:
        return f"Computer wins! {computer_choice.capitalize()} beats {user_choice}."
def play_game():
    print("Welcome to Rock, Paper, Scissors!")   
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose {user_choice.capitalize()}.")
        print(f"Computer chose {computer_choice.capitalize()}.")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing. Goodbye!")
            break
if __name__ == "__main__":
    play_game()
