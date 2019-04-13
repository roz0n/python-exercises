import random

random_number = random.randint(0, 9)
numbers = [random_number, random_number]
total_attempts = int(input("How many attempts would you like? "))
solved = False

def number_guesser(current_attempt, remaining_attempts):
    global solved
    user_number = input("Guess a number... ")
    
    if int(user_number) in numbers:
        solved = True
        return "You guessed {}, and that was correct! You got it in {} attempt(s).".format(user_number, current_attempt)
    elif int(user_number) not in numbers:
        return "You guessed {}, but that was incorrect. You have {} attempt(s) remaining.".format(user_number, remaining_attempts)

def start_game(attempts):        
    for attempt in range(attempts):
        current_attempt = (attempt + 1)
        remaining_attempts = (total_attempts - current_attempt)
        
        print(number_guesser(current_attempt, remaining_attempts)) # number_guesser returns a str

        if solved == True:
            print("Game over... you win!")
            break
        elif remaining_attempts == 0:
            print("Looks like you failed to guess the secret numbers...")
            print("Game over... you lose.")
            break

start_game(total_attempts)
