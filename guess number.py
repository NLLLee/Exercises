logo = '''
                                        __  .__                                 ___.                 
   ____  __ __   ____   ______ ______ _/  |_|  |__   ____     ____  __ __  _____\_ |__   ___________ 
  / ___\|  |  \_/ __ \ /  ___//  ___/ \   __\  |  \_/ __ \   /    \|  |  \/     \| __ \_/ __ \_  __ \
 / /_/  >  |  /\  ___/ \___ \ \___ \   |  | |   Y  \  ___/  |   |  \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \___  /|____/  \___  >____  >____  >  |__| |___|  /\___  > |___|  /____/|__|_|  /___  /\___  >__|   
/_____/             \/     \/     \/             \/     \/       \/            \/    \/     \/       
'''

print (logo)

from random import randint

easy_level = 10
hard_level = 5


def check_answer(guess, answer, turns):
    '''checks answer again guess. Returns the number of turns remaining.'''
    if guess > answer:
        print("It's too high.")
        return turns -1
    elif guess < answer:
        print("It's too low.")
        return turns -1
    else:
        print(f"You got it! The answer was {answer}")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return easy_level
    else:
        return hard_level
def game():
    print("Welcome to the number guessing game!\n I'm thinking of a number between 1 and 100. ")
    answer = randint(1, 100)
    print(f"psst, the correct answer is {answer}")

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess:"))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")
game()
