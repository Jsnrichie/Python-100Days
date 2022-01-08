from random import randint
from game_data import data
# from replit import clear
import art

#Picks celeb out of data and removes it from the list
def pick_celeb():
  celeb = data[randint(0, len(data) - 1)]
  data.pop(data.index(celeb))
  return celeb

#compares the answer to the two celebs follower count
def check_answer(choice, celeb1, celeb2):
  if celeb1['follower_count'] > celeb2['follower_count']:
    if choice == "a":
      return True
    else: 
      return False
  else:
    if choice == "b":
      return True
    else: 
      return False


print(art.logo)

game_active = True
score = 0

celeb1 = pick_celeb()
celeb2 = pick_celeb()

while game_active:
  print(f"Compare A: {celeb1['name']}, {celeb1['description']}, from {celeb1['country']}.")
  print(art.vs)
  print(f"Against B: {celeb2['name']}, {celeb2['description']}, from {celeb2['country']}.")
  choice = input("Who has more followers? Type 'A' or 'B': ").lower()

  #clear()
  
  if check_answer(choice, celeb1, celeb2):
    score += 1
    print(f"You're right! Current score: {score}")
    celeb1 = celeb2
    celeb2 = pick_celeb()
  else:
    print(f"Aw you got it wrong. You scored {score} points")
    game_active = False

