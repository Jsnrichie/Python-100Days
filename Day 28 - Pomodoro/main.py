from tkinter import *
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#519259"
YELLOW = "#F5EEDC"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
tracking_text = ""

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer, reps, tracking_text
    window.after_cancel(timer)

    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text=f"00:00")
    tracking_label.config(text="")
    reps = 0
    tracking_text = ""


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps, tracking_text
    reps += 1
    print(reps)

    work_min_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60


    if (reps % 8) == 0:
        countdown(long_break_secs)
        timer_label.config(text= "Break", fg=RED)
    elif (reps % 2) == 0:
        countdown(short_break_secs)
        timer_label.config(text="Break", fg=PINK)
    elif (reps % 2) != 0 and reps < 8:
        countdown(work_min_secs)
        timer_label.config(text="Work", fg=GREEN)
        tracking_text += "✔"

    tracking_label.config(text=tracking_text)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global reps, timer
    # print(count)
    min = math.floor(count / 60)
    sec = count % 60

    if sec < 10:
        sec = "0" + str(sec)


    canvas.itemconfig(timer_text, text= f"{min}:{sec}")
    if count > 0:
        timer = window.after(10, countdown, count - 1)
    else:
        start_timer()




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx= 100, pady= 50, bg=YELLOW)



# def say_something(thing):
#     print(thing)
#
# window.after(1000, say_something, "Hello")

# Timer Text
timer_label = Label()
timer_label.config(text= "Timer", bg=YELLOW , fg=GREEN, font=(FONT_NAME, 35 , "bold"))
timer_label.grid(column= 1, row= 0)


# Tomato
canvas = Canvas(width= 200, height= 224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img )
timer_text = canvas.create_text(100 , 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column= 1, row= 1)

#Start Button
start_button = Button()
start_button.config(text="Start", bg=YELLOW , fg=GREEN, highlightthickness=0, command=start_timer)
start_button.grid(column= 0, row= 2)

#Tracking label
tracking_label = Label()
tracking_label.config(text="", bg=YELLOW , fg=GREEN)
tracking_label.grid(column= 1, row= 3)

#Reset Button
reset_button = Button()
reset_button.config(text="Reset", bg=YELLOW , fg=GREEN, highlightthickness= 0, command=reset_timer)
reset_button.grid(column= 2, row= 2)

# countdown(5)



window.mainloop()