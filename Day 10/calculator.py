from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

#How we are going to call the functions
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
  }

def calculator():
  print(logo)

  num1 = float(input("What's the first number: "))
  #Loop through dictionary and print out keys
  for key in operations:
    print(key)

  #set flag
  calc_on = True


  while calc_on:
    chosen_op = input("Pick an operation: ")
    num2 = float(input("What's the next number: "))

    #Calculate and print result
    result = operations[chosen_op](num1, num2)
    print(f"{num1} {chosen_op} {num2} = {result}")

    #check if user wants to continue
    still_using = input(f"Type 'y' to continue calculating with {result} or 'n' to exit: ")
    if still_using == "y":
      num1 = result
    elif still_using == "n":
      calc_on = False
      print("Done")
    else :
      calculator()

calculator()




