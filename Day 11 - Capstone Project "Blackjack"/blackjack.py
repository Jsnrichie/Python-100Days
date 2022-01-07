import random
from art import logo
print(logo)

#Create dict with cards and their values
card_dict = {
  "A": 11,
  "2": 2,
  "3": 3,
  "4": 4,
  "5": 5,
  "6": 6,
  "7": 7,
  "8": 8,
  "9": 9,
  "10": 10,
  "J": 10,
  "Q": 10,
  "K": 10,
  "A'": 1
}

#play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
#print(len(cards))

#draw 2 random cards from pack of 13
card_names = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

def draw_cards(hand): #works as intended
  """Adds 'n' cards to selected 'hand'"""
  for x in range(2):
    card_drawn = card_names[random.randrange(0,13)]
    hand.append(card_drawn)

def hand_value(hand):
  """Returns current value of 'hand'"""
  value = 0
  for card in hand:
    value += card_dict[card]
  return value

def add_card(hand):
  card_drawn = card_names[random.randrange(0,13)]
  hand.append(card_drawn)
  if hand_value(hand) > 21 and card_drawn == "A":
    hand.pop()
    hand.append("A'")


def blackjack():
  game_active = True
  
  #Dealer serves cards
  player_hand = []
  dealer_hand = []
  draw_cards(player_hand)
  draw_cards(dealer_hand)

  #Starting Info
  print(f"your cards: {player_hand}, current score: {hand_value(player_hand)}")
  print(f"Dealer's first card: {dealer_hand[0]}")

  #Game Starts
  while game_active:
    player_turn = True

    while player_turn:
      test = input("Type 'y' to get another card, type 'n' to pass: ")
      if test == "y":
        add_card(player_hand)
        print(f"your cards: {player_hand}, current score: {hand_value(player_hand)}")
        if hand_value(player_hand) > 21:
          print(f"{player_hand} you went bust")
          print("YOU LOSE")
          player_turn = False
          game_active = False
      
      #Player's Turn ends
      else:
        player_turn = False

        print(f"Computer's hand = {dealer_hand}, Value: {hand_value(dealer_hand)}")#Reveal computer's hand
        if hand_value(dealer_hand) < 16:
          add_card(dealer_hand)
          print(f"The dealer drew a card. Dealer hand: {dealer_hand}. Dealer score: {hand_value(dealer_hand)}")
          if hand_value(dealer_hand) > 21:
            print(f"Dealer hand: {dealer_hand}. The dealer went bust")
            print("YOU WIN")
            game_active = False
    

    #Both turns end - IF GAME STILL ON Check the state of the game and determine winner
    if game_active:
      if hand_value(dealer_hand) == 21:
        print("You lose")
        game_active = False
      elif hand_value(player_hand) == 21:
        print("You win")
        game_active = False
      elif hand_value(dealer_hand) > hand_value(player_hand):
        print("You lose")
        game_active = False
      elif hand_value(player_hand) > hand_value(dealer_hand):
        print("You win")
        game_active = False
      elif hand_value(player_hand) == hand_value(dealer_hand):
        print("Wow, it's a draw.")
        game_active = False

  #Ask the user if they would still like to play  
  play_again = input("Type 'y' to play agin or 'n' to exit: ")
  if play_again == "y":
    blackjack()
  else:
    return

blackjack()
