import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choice = [rock, paper, scissors]
choice_word = ["rock", "paper", "scissors"]

print("Welcome to the Rock, Paper, Scissors Local Championship")

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
boss = random.randint(0,2)

print(f"You chose {choice_word[user]} {choice[user]}")
print(f"The champ chose {choice_word[boss]} {choice[boss]}")

if user == boss:
  print("It's a Tie!")

elif (user == 0 and boss == 1) or (user == 1 and boss == 2) or (user == 2 and boss == 0):
  print("You lost bozo...")

else:
  print("I can't believe it. YOU WON!")


