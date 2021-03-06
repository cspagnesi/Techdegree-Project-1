import random
def guess_random_num():
    try:
        attempt_count = 1
        random_number_guess = input("Time to make a guess.  The number that has been generated could be any number within the range of 1 to 10.  What do you think it is?  ")
        random_number_guess = int(random_number_guess)
        if random_number_guess == random_number:
                print("You got it on the first try!")
        while random_number_guess != random_number:
            if random_number_guess > random_number:
                print("The randomly generated number is lower.")
                if random_number_guess > 10 or random_number_guess < 1:
                    print("That number is outside of the indicated range.")
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
            play_again = input("Would you like to play again? Y/N? ")
            play_again = play_again.lower()
            if play_again == ("n"):
                print ("No problem.  Adios!")
                return False
            elif play_again == ("y"):
                print ("Another round incoming...")
                guess_random_num()
            else:
                raise ValueError
    except ValueError as error: 
        print("Ah you've entered an unrecognizable value. Please enter a number this time around.")
        guess_random_num()       
                        

print ("Welcome to...'The Number Guessing Game'!")
random_number = random.randint(1, 10)
guess_random_num()


        

    

    
    

    