alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt (text, shift):
  text_list = list(text) # convert text to a list
  text_len = len(text_list)

  for x in range(text_len):
    if text_list[x] != " ": #if not a space switch out letter
      index = alphabet.index(text_list[x]) #get the position of letter in word given 
      #print(index)
      index = (index + shift) % len(alphabet) #shift letter by amount of shift
      #print(index)
      text_list[x] = alphabet[index] #replace letter with letter 'shift' spaces away -> has to be a list
  
  #print(text_list)
  encryption = ''.join(text_list) #put encrypted letters into one word
  print(f"Here is your encryption: {encryption}")

def decode (text, shift):
  text_list = list(text) # convert text to a list
  text_len = len(text_list)

  for x in range(text_len):
    if text_list[x] != " ":
      index = alphabet.index(text_list[x]) #get the position of letter in word given 
      #print(index)
      index = (index - shift) % len(alphabet) #shift letter by amount of shift
      #print(index)
      text_list[x] = alphabet[index] #replace letter with letter 'shift' spaces away -> has to be a list
  
  #print(text_list)
  solution = ''.join(text_list) #put encrypted letters into one word
  print(f"Your code has been deciphered: {solution}")

if direction == "encode":
  encrypt (text, shift)
elif direction == "decode":
  decode (text, shift)
else:
  print("Wrong input")
