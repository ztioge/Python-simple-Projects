import random

def guess(x):
    
    random_number = random.randint(1, x)
    guess = 0
    guesses = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        guesses = guesses + 1
        if guess < random_number:
                print('Wrong! Too low! Try again.')

        elif guess > random_number:
                print('Wrong! Too high! Try again.')
    
    print(f'Congratulations! You have guessed the number {random_number} correctly. It took {guesses} tries.')
   
guess(10)
            

