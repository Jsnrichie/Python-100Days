#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

print(logo)

def guessing_game():
  print("Welcome to the Number Guessing Game.")
  print("I'm thinking of a number between 1 and 100") 
  answer = random.randrange(1, 100)
  #print(f"HINT: {answer}")

  game_active = True

  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty == "easy":
    lives = 10
  elif difficulty == "hard":
    lives = 5
  else:
    return

  
  while game_active:
    guess = int(input(f"You have {lives} attempts remaining to guess the number: "))

    if guess == answer:
      print(f"The answer was {answer}! You guessed right!")
      game_active = False
    elif guess > answer:
      print("Too high")
      lives -= 1
    else:
      print("Too low")
      lives -= 1

    #Ran out of lives
    if lives == 0:
      print("Damn son you out of lives. You lose.")
      game_active = False

guessing_game()






