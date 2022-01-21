student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

df = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(df)
nato_lib = {row.letter: row.code for (index, row) in df.iterrows()}
print(nato_lib)

word = input("Give me a word: ").upper()
nato_word = [nato_lib[letter] for letter in word]
print(nato_word)

# TODO 1. Create a dictionary in this format: DONE
# {"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs. DONE
