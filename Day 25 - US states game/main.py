from turtle import Screen
from quiz_brain import Quiz_Brain

SCREEN_WIDTH = 725
SCREEN_HEIGHT = 491
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("U.S. States Quiz")
screen.bgpic("blank_states_img.gif")

quiz_brain = Quiz_Brain()

# While game is on , guess input, print input on the screen
still_playing = True
while still_playing:
    state_guess = screen.textinput(title=f"State guesses: {quiz_brain.correct_ans}/50", prompt="Guess a State").title()
    if state_guess == "Done":
        still_playing = False
        break
    else:
        quiz_brain.check_state(state_guess)


quiz_brain.states_to_learn()

screen.exitonclick()
