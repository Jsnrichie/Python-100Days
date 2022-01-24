from tkinter import *


def button_click():
    print("Damn he clicked me.")
    my_label.config(text=input_.get())


window = Tk()
window.title("My first GUI")
window.minsize(width=500, height=300)
window.config(padx= 15, pady=15)

# LABEL
my_label = Label(text="I am a LABEL", font=("Arial", 24, "bold"))
# my_label.pack()  # specify how it will be laid out
# my_label.place(x=50,y=0) # place exactly where u wangt it to go
my_label.grid(column= 0, row= 0)

# Button
my_button = Button(text="CLICK ME", command=button_click)
# my_button.pack()
my_button.grid(column= 1, row= 1)

# Entry
input_ = Entry(width=15)
# input_.pack()
input_.grid(column= 3, row= 2)

new_button = Button(text="New new")
new_button.grid(column= 2, row= 0)

# Very end - keeps window open
window.mainloop()
