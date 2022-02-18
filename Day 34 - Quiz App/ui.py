from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

QUESTION_FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.answer = ""

        # Window setup
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score
        self.score_label = Label()
        self.score_label.config(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0, pady=(0, 10))

        # White Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2)

        # Question Text
        self.question_label = Label()
        self.question_label.config(
            text="The first televised presidential debate was between Jimmy Carter and Gerald Ford.",
            font=QUESTION_FONT,
            justify="center",
            wraplength=250,
            fg="black",
            bg="white"
        )
        self.question_label.grid(column=0, row=1, columnspan=2)

        # Button Setup
        false_img = PhotoImage(file="images/false.png")
        true_img = PhotoImage(file="images/true.png")

        self.false_button = Button(image=false_img)
        self.false_button.config(command=self.false_pressed)
        self.false_button.grid(column=0, row=2, pady=20)

        self.true_button = Button(image=true_img)
        self.true_button.config(command=self.true_pressed)
        self.true_button.grid(column=1, row=2, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.question_label.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
        else:
            q_text = "Quiz over"

        self.question_label.config(text=q_text)

    def true_pressed(self):
        if self.quiz.check_answer("True"):
            self.canvas.config(bg="green")
            self.question_label.config(bg="green")
        else:
            self.canvas.config(bg="red")
            self.question_label.config(bg="red")
        self.update_score()
        self.window.after(2000, func=self.get_next_question)

    def false_pressed(self):
        if self.quiz.check_answer("False"):
            self.question_label.config(bg="green")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
            self.question_label.config(bg="red")
        self.update_score()
        self.window.after(2000, func=self.get_next_question)

    def update_score(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")



