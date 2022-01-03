import random
import hangman_art
import hangman_words

end_of_game = False
lives = len(hangman_art.stages) - 1
word_list = hangman_words.word_list
chosen_word = random.choice(word_list) # choose random word out of list
print(f"HINT: {chosen_word}")

# Create blank display
display = []
for x in chosen_word:
  display.append("_")
#print(display)

#GAME START
while not end_of_game:
  #Make a guess
  guess = input("Make a guess: \n").lower()

  index = 0
  #Right answer - put correct letters in the word
  if guess in chosen_word:
    for x in chosen_word:
      if guess == chosen_word[index]:
        display[index] = guess
      index += 1
  #Wrong answer - lose a life
  else:
    lives -= 1
    print("wrong answer")

  # Check if player won or lost
  if not "_" in display:
    end_of_game = True
    print("YOU WIN")
  elif lives == 0:
    end_of_game = True
    print("YOU LOSE")

  #show hangman status + word progress
  print(hangman_art.stages[lives])
  print(f"{' '.join(display)}")

    







