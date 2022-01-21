import pandas
from turtle import Turtle

FONT = ("Courier", 10, "normal")


class Quiz_Brain:
    def __init__(self):
        data = pandas.read_csv("50_states.csv")

        self.states = data.state.to_list()
        self.x_cor = data.x.to_list()
        self.y_cor = data.y.to_list()
        self.correct_states = []
        self.correct_ans = 0

        self.pen = Turtle()
        self.pen.hideturtle()
        self.pen.penup()

        print(self.states)
        print(self.x_cor)
        print(self.y_cor)

    def check_state(self, guess):
        if guess in self.states:
            if guess not in self.correct_states:
                # print("Yessir")
                index = self.states.index(guess)
                self.pen.goto(x=self.x_cor[index], y=self.y_cor[index])
                self.pen.write(f"{self.states[index]}", align="center", font=FONT)
                self.correct_states.append(self.states[index])
                self.correct_ans += 1
            else:
                print("You already guessed that.")
        else:
            print("You guessed wrong.")


    def states_to_learn(self):
        # print(self.correct_states)
        # data = pandas.read_csv("50_states.csv")
        #
        # just_states = data.drop(columns=["x", "y"])
        # print(just_states)
        #
        # # for state in range(len(self.correct_states)):
        # #     just_states = just_states.loc[just_states.state != self.correct_states[state]]
        #
        # for state in self.correct_states:
        #     just_states = just_states.loc[just_states.state != state]
        #     just_states.to_csv("states_to_learn.csv")
        #     print(just_states)
        #
        # # filtered = data[data.state != self.correct_states]
        # # print(filtered)

        states_to_learn = [state for state in self.states if (state not in self.correct_states)]
        df = pandas.DataFrame(states_to_learn)
        df.to_csv("states_to_learn.csv")

        print(states_to_learn)
