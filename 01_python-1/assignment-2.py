# "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui

# helper function to start and restart the game
def new_game():
    """
    Start a new guessing game.
    """

    # initialize global variables
    global range_upper_limit
    global secret_number
    global allowed_guesses

    # adjust the number of allowed guesses based on the
    # range that will be used to generate secret_number
    if range_upper_limit < 1000:
        allowed_guesses = 7
    else:
        allowed_guesses = 10

    # generate the secret_number as a random number
    # between zero and the chosen range_upper_limit
    # (which will be 100 for the first game)
    secret_number = random.randrange(0, range_upper_limit)

    print "----------"
    print "Starting new game!"
    print "Please guess a number between 0 and " + str(range_upper_limit) + "."
    print "(You are allowed up to %s guesses.) " % allowed_guesses

# define event handlers for control panel
def range100():
    """
    Start a new game with an upper limit of 100 for the
    range used to generate a secret_number.
    """
    global range_upper_limit
    range_upper_limit = 100
    new_game()

def range1000():
    """
    Start a new game with an upper limit of 1000 for the
    range used to generate a secret_number.
    """
    global range_upper_limit
    range_upper_limit = 1000
    new_game()

def input_guess(guess):
    """
    Examine the user's guess (converted to an integer) to
    see whether it is higher, lower or equal to the game's
    generated secret_numer. Respond with a message to let
    the user know whether to guess higher or lower next.
    """
    global allowed_guesses

    print "-"
    print "You made a guess! Your guess was %s." % guess

    allowed_guesses = allowed_guesses - 1
    print "You have %s guesses remaining." % allowed_guesses

    if allowed_guesses == 0:
        print "* You're out of guesses. Game over! The number was %s." % secret_number
        new_game()
    else:
        guess_int = int(guess)

        if guess_int < secret_number:
            print "Guess higher!"
        elif guess_int > secret_number:
            print "Guess lower!"
        else:
            print "* Your guess is correct! Nice job. Starting new game..."
            new_game()

# create frame
frame = simplegui.create_frame("Guessing Game", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0,100)", range100, 200)
frame.add_button("Range is [0,1000)", range1000, 200)
frame.add_input("Enter your guess below and press enter:", input_guess, 200)

# call new_game, after setting an initial value for the range's upper limit
range_upper_limit = 100
new_game()
