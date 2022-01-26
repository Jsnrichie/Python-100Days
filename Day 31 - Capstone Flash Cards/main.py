from tkinter import *
import pandas
from random import choice
from os.path import exists

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_TEXT_FONT = ("Arial", 40, "italic")
BOTTOM_TEXT_FONT = ("Arial", 60, "bold")
flip = None
pick = None

# ------------------------------- FLASH CARD FUNCTIONS ------------------------------- #
if exists("data/words_to_learn.csv"):
    dataframe = pandas.read_csv("data/words_to_learn.csv")
else:
    dataframe = pandas.read_csv("data/french_words.csv")

to_learn = dataframe.to_dict(orient="records")


# print(to_learn)

def gen_card():
    global flip, pick
    pick = choice(to_learn)

    card_canvas.itemconfig(current_img, image=front_image)
    card_canvas.itemconfig(language_text, text="French", fill="black")
    card_canvas.itemconfig(word_text, text=f"{pick['French']}", fill="black")

    flip = window.after(3000, flip_card, pick)


def flip_card(pick):
    global flip
    card_canvas.itemconfig(current_img, image=back_image)
    card_canvas.itemconfig(language_text, text="English", fill="white")
    card_canvas.itemconfig(word_text, text=f"{pick['English']}", fill="white")

    window.after_cancel(flip)


# ------------------------------- SAVE TO FILE ------------------------------- #

def remove_word():
    global pick
    to_learn.remove(pick)
    # print(to_learn)
    # print(len(to_learn))


def update_csv():
    df = pandas.DataFrame(to_learn)
    df.to_csv("data/words_to_learn.csv", index=False)
    print(df)


# ------------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Flash Card Canvas
card_canvas = Canvas()
card_canvas.config(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
current_img = card_canvas.create_image(400, 263, image=front_image)  # Location + image
# TEXT
language_text = card_canvas.create_text(400, 163, text="", font=LANGUAGE_TEXT_FONT, fill="black")
word_text = card_canvas.create_text(400, 263, text="", font=BOTTOM_TEXT_FONT, fill="black")

card_canvas.grid(column=0, row=0, columnspan=3)

# Wrong Button Canvas
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image)
wrong_button.config(width=100, height=100, highlightbackground=BACKGROUND_COLOR, command=gen_card)
wrong_button.grid(column=0, row=1)

# Right Button Canvas
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image)
right_button.config(width=100, height=100, highlightbackground=BACKGROUND_COLOR,
                    command=lambda: [gen_card(), remove_word(), update_csv()])
right_button.grid(column=2, row=1)

gen_card()

window.mainloop()
