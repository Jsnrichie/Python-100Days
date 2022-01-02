#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Jsnrich Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

total_letters = len(letters) #52
total_num = len(numbers) #10
total_sym = len(symbols) #9

test = 0
password = ""


for x in range (0, nr_letters): #Loops the number of letter requested
  test = random.randint(0, total_letters - 1)
  password += letters[test]

for x in range (0, nr_symbols): #Loops the number of symbol requested
  test = random.randint(0, total_sym - 1)
  password += symbols[test]

for x in range (0, nr_numbers): #Loops the number of numbers requested
  test = random.randint(0, total_num - 1)
  password += numbers[test]

password_holder = list(password) #Converts password to a list for randomizing the order
random.shuffle(password_holder)

password = ''.join(password_holder)
print(f"Your new password is: {password}")
