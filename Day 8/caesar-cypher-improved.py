alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(text, shift, direction):

  still_running = True

  while still_running == True:
    end_text = ""
    if direction == "encode":
      end_message = "Your encrypted message is: "
    elif direction == "decode":
      end_message = "Your decrypted message is: "

    if direction == "decode": #negative shift(go backwards) if you are decrypting
      shift *= -1

    for letter in text:
      if letter in alphabet: # check is char is a letter
        position = alphabet.index(letter)
        new_position = (position + shift) % len(alphabet)# shift by required amt in correct direction
        end_text += alphabet[new_position]
      else:
        end_text += letter
      
    end_message += end_text

    print(end_message)
  
    still_using = input("Type 'yes' or 'no' to use the cypher again or end the program\n")
    if still_using == "no":
      still_running = False
      print("Goodbye")
    elif still_using == "yes":
      direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
      text = input("Type your message:\n").lower()
      shift = int(input("Type the shift number:\n"))


  # if direction == "encode":
  #   encryption = ""
  #   for letter in text:
  #     if letter != " ": #if not a space switch out letter
  #       position = alphabet.index(letter) #get the position of letter in word given 
  #       new_position = (position + shift) % len(alphabet) #shift letter by amount of shift
  #       encryption += alphabet[new_position] #replace letter with letter 'shift' spaces away -> has to be a list
  #   print(f"Here is your encryption: {encryption}")

  # elif direction == "decode":
  #   decryption = ""
  #   for letter in text:
  #     if letter != " ": #if not a space switch out letter
  #       position = alphabet.index(letter) #get the position of letter in word given 
  #       new_position = (position - shift) % len(alphabet) #shift letter by amount of shift
  #       decryption += alphabet[new_position] #replace letter with letter 'shift' spaces away -> has to be a list
    
  #   print(f"Here is your encryption: {decryption}")

  # else:
  #   print("Error")

caesar(text, shift, direction)
