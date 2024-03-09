#file: CS112_A1_T2_Game (3)_20230495
#Purpose: Subtract square game by Python
#Author: Yosef Hamdy Aboelmaaty
#ID: 20230495
import random
import math

def determine_winner(player, current_num):
    if current_num == 0:
        return player
    else:
        return None

def make_move(player, starting_number):
    while True:
        try:
            choice = int(input(f'Player {player}: Choose any square number (up to {starting_number}): '))
            if 0 < choice <= starting_number and math.isqrt(choice) ** 2 == choice:
                return choice
            else:
                print(f'Invalid move for Player {player}. Please choose a valid square number.')
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Game loop
while True:
    # Ask the user for the starting option
    starting_option = input("Choose the starting option (user/random): ").lower()

    if starting_option == 'user':
        # User chooses the starting number
        user_starting_num = int(input("Enter the starting number for the game (between 1 and 1000): "))
        current_num = user_starting_num
    else:
        # Computer chooses the starting number randomly
        current_num = random.randint(1, 1000)

    print('Welcome to Subtract Square Game')
    print(f'Starting with the chosen number: {current_num}')

    # Game playing loop
    while 1 <= current_num <= 1000:
        # Player 1's move
        player1_move = make_move(player=1, starting_number=current_num)
        current_num = max(0, current_num - player1_move)
        print(f'Now we have {current_num}')

        # Check if Player 1 has won
        winner = determine_winner(1, current_num)
        if winner is not None:
            print("WINNER WINNER CHICKEN DINNER PLAYER 1")
            break

        # Player 2's move
        player2_move = make_move(player=2, starting_number=current_num)
        current_num = max(0, current_num - player2_move)
        print(f'Now we have {current_num}')

        # Check if Player 2 has won
        winner = determine_winner(2, current_num)
        if winner is not None:
            print("WINNER WINNER CHICKEN DINNER PLAYER 2")
            break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break
