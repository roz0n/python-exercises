import random

def launch_game_menu():
    print("Welcome to the lottery game!")
    
    user_numbers = get_player_numbers()
    winning_numbers = generate_winning_numbers()
    calculate_winnings(user_numbers, winning_numbers)

def get_player_numbers():
    numbers = input("Enter eight numbers separated by commas: ")
    number_list = numbers.split(",")

    # Remove duplicates
    number_set = {int(number) for number in number_list}
    return number_set

def generate_winning_numbers():
    total_numbers = 8
    winning_numbers = set()

    while len(winning_numbers) < total_numbers:
        winning_numbers.add(random.randint(0, 20))
    return winning_numbers

def calculate_winnings(user_numbers, winning_numbers):
    winnings_per_number = 1000
    correct_numbers = user_numbers.intersection(winning_numbers)
    total_earnings = (winnings_per_number ** len(correct_numbers))

    if len(correct_numbers) > 0:
        print("Congratulations! You won ${}! You big-baller, you. Go buy yourself something nice."
                  .format(total_earnings))
        print("The winning numbers were {}".format(winning_numbers))
        print("You guessed {}, of which {} were correct."
                  .format(str(user_numbers), str(len(correct_numbers))))
    else:
        print("You win nothing... nothing! Go home! You LOSE! \n Game over, you have no one except yourself to blame.")

launch_game_menu()
