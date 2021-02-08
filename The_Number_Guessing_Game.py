import random
def guess_random_num():
    attempt_count = 1
    random_number_guess = input("Time to make a guess.  The number that has been generated could be any number within the range of 1 to 10.  What do you think it is?  ")
    random_number_guess = int(random_number_guess)
    if random_number_guess == random_number:
            print("You got it!")
            round_two()
    while random_number_guess != random_number:
        if random_number_guess > random_number:
            print("The randomly generated number is lower.")
        elif random_number_guess < random_number:
            print("The randomly generated number is higher.")
            if random_number_guess > 10 or random_number_guess < 1:
                print("That number is outside of the indicated range.")
        random_number_guess = input("That said...try again.  ")
        random_number_guess = int(random_number_guess)
        attempt_count += 1
        if random_number_guess == random_number:
            print("You got it!  It took you {} tries to determine the randomly generated number.".format(attempt_count))  
            print("'The Number Guessing Game' has officially concluded.")
            round_two()

def round_two():
    play_again = input("Would you like to play again? Y/N? ")
    play_again = play_again.lower()
    if play_again == ("n"):
        print("No problem.  Adios!")
    elif play_again == ("y"):
        guess_random_num()
        
print ("Welcome to...'The Number Guessing Game'!")
random_number = random.randint(1, 10)
try:
    guess_random_num()
except ValueError as error:
    print("Ah you've entered an unrecognizable value.  Please enter a number this time around.")
    guess_random_num()
    
    
    

    

    