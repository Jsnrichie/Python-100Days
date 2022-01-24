from tkinter import *

# Setup window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width= 200, height=100)
window.config(padx= 15, pady= 15)

def miles_to_km(miles):
    km = round(miles * 1.609)
    return km

def button_click():
    miles = int(miles_input.get())
    answer.config(text=str(miles_to_km(miles)))

#6 widgets

miles_input = Entry()
miles_input.config(width=12)
miles_input.grid(column= 1, row= 0)

miles_label = Label(text="Miles")
miles_label.grid(column= 2, row= 0)

is_eq_to = Label(text="is equal to")
is_eq_to.grid(column= 0, row= 1)

answer = Label()
answer.grid(column= 1, row= 1)

km_label = Label(text="Km")
km_label.grid(column= 2, row= 1)

calc_button = Button(text="Calculate", command=button_click)
calc_button.grid(column= 1, row= 2)



window.mainloop()
