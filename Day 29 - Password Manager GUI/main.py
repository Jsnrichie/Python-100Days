from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random


def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    pass_list_let = [random.choice(letters) for _ in range(nr_letters)]
    pass_list_sym = [random.choice(symbols) for _ in range(nr_symbols)]
    pass_list_num = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = pass_list_let + pass_list_num + pass_list_sym

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# Save data into file data . txt

def save_data():
    website = web_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty")
        return

    line_list = [website, email, password]
    line = " | ".join(line_list)

    # messagebox.showinfo(title= "Title", message="Message")
    is_ok = messagebox.askokcancel(title=website,
                                   message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it okay to save?")

    if is_ok:
        with open("data.txt", mode="a") as file:
            file.write(line + "\n")

        web_input.delete(0, END)
        password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

# Logo
canvas = Canvas(width=200, height=200, highlightthickness=0, bg="white")
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Website
web_label = Label()
web_label.config(text="Website: ", bg="white", fg="black")
web_label.grid(column=0, row=1)

web_input = Entry(width=38, bg="white", fg="black", highlightbackground="white")
web_input.grid(column=1, row=1, columnspan=2)
web_input.focus()

# Email/Username
email_label = Label()
email_label.config(text="Email/Username: ", bg="white", fg="black")
email_label.grid(column=0, row=2)

email_input = Entry(width=38, bg="white", fg="black", highlightbackground="white")
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "jsnrich428@gmail.com")

# Password
password_label = Label()
password_label.config(text="Password: ", bg="white", fg="black")
password_label.grid(column=0, row=3)

password_input = Entry(width=21, bg="white", fg="black", highlightbackground="white")
password_input.grid(column=1, row=3)

password_button = Button()
password_button.config(text="Generate Password", bg="white", fg="black", highlightthickness=0,
                       highlightbackground="white", command=gen_password)
password_button.grid(column=2, row=3)

# Add
add_button = Button(width=36)
add_button.config(text="Add", bg="white", fg="black", highlightthickness=0, highlightbackground="white",
                  command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
