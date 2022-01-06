from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)

auction_log = {}
auction_live = True

def determine_winner(auction_log):
  highest_bid = 0
  winner = ""

  for key in auction_log:
    if auction_log[key] > highest_bid:
      highest_bid = auction_log[key]
      winner = key
  
  print(f"The winner is {winner} with a bid of ${auction_log[winner]}")

while auction_live:

  name = input("Insert your name:\n")
  bid = int(input("What is your bid?\n$"))

  auction_log[name] = bid

  still_live = input("Any other bidders? Type 'yes' or 'no'\n").lower()
  clear()
  if still_live == "no":
    auction_live = False
    determine_winner(auction_log)
    #print(auction_log)

    # highest_bid = 0
    # winner = ""

    # for key in auction_log:
    #   if auction_log[key] > highest_bid:
    #     highest_bid = auction_log[key]
    #     winner = key
    
    # print(f"The winner is {winner} with a bid of ${auction_log[winner]}")
    



