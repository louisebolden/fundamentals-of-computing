# a fun rock-paper-scissors-lizard-Spock game

import random

# helper functions

def name_to_number(name):
  """
  Convert a string called 'name' into an integer
  that represents its number for game scoring
  """
  if name == 'rock':
    return 0
  elif name == 'Spock':
    return 1
  elif name == 'paper':
    return 2
  elif name == 'lizard':
    return 3
  elif name == 'scissors':
    return 4
  else:
    print 'Error: name not recognised'


def number_to_name(number):
  """
  Convert an integer between 0-4 into its
  corresponding name
  """
  if number == 0:
    return 'rock'
  elif number == 1:
    return 'Spock'
  elif number == 2:
    return 'paper'
  elif number == 3:
    return 'lizard'
  elif number == 4:
    return 'scissors'
  else:
    print 'Error: invalid number'
    
# main game function

def rpsls(player_choice):     
  # print a blank line to separate consecutive games
  print

  # print out the message for the player's choice
  print 'Player chooses ' + player_choice

  # convert the player's choice to player_number using the function name_to_number()
  player_number = name_to_number(player_choice)
  
  # compute random guess for comp_number using random.randrange()
  comp_number = random.randrange(0,5)
  
  # convert comp_number to comp_choice using the function number_to_name()
  comp_choice = number_to_name(comp_number)
  
  # print out the message for computer's choice
  print 'Computer chooses ' + comp_choice

  # compute difference of comp_number and player_number modulo five
  difference = (player_number - comp_number) % 5
  
  # use if/elif/else to determine winner, print winner message
  if difference == 0:
    print 'Player and computer tie!'
  elif difference == 1 or difference == 2:
    print 'Player wins!'
  else:
    print 'Computer wins!'

    
# tests for the rpsls function
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
