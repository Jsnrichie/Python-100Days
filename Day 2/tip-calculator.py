#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")

bill_amt = float(input("What was the total bill? \n$"))
tip = float(input("How much tip would you like to give? 10, 12, or 15?\n"))
tip /= 100 
num_ppl = int(input("How many people to split the bill?\n"))

amt_per = ((bill_amt / num_ppl) * (1 + tip))
# amt_per_rounded = round(amt_per, 2)
# amt_per_formatted = "{:.2f}".format(amt_per_rounded)

amt_per_formatted = "{:.2f}".format(amt_per)

print(f"Each person would have to pay ${amt_per_formatted}.")

