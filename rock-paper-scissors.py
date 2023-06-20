import random

def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    print("Enter your move: rock, paper, or scissors.")

    while True:
        player_move = input("Your move: ").lower()
        if player_move in ['rock', 'paper', 'scissors']:
            break
        else:
            print("Invalid move. Please choose rock, paper, or scissors.")

    computer_move = random.choice(['rock', 'paper', 'scissors'])

    print(f"\nYou chose {player_move}.")
    print(f"The computer chose {computer_move}.\n")

    if player_move == computer_move:
        print("It's a tie!")
    elif (player_move == 'rock' and computer_move == 'scissors') or \
         (player_move == 'scissors' and computer_move == 'paper') or \
         (player_move == 'paper' and computer_move == 'rock'):
        print("You win!")
    else:
        print("Computer wins!")

    play_again = input("\nDo you want to play again? (yes/no): ")
    if play_again.lower() == 'yes':
        print()
        play_game()
    else:
        print("Thank you for playing!")

# Start the game
play_game()
