from tkinter import *
from quiz_brain import *

THEME_COLOR = "#375362"
FONT_SCORE = ("Arial", 15, "bold")
FONT_QUESTION = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)
        self.score_label = self.text = Label(text="Score: 0", font=FONT_SCORE, bg=THEME_COLOR, fg="white")
        self.text.grid(column=1, row=0, padx=20, pady=20)
        self.canvas = Canvas(height=250, width=300, bg="white")
        self.canvas.grid(column=0, row=1, pady=50, columnspan=2)
        self.question_text = self.canvas.create_text(
            150, 125,
            width=280,
            text="",
            font=FONT_QUESTION)
        img_true = PhotoImage(file="images/true.png")
        self.btn_true = Button(image=img_true, highlightthickness=0, command=self.check_question_true)
        self.btn_true.grid(row=2, column=0)
        img_false = PhotoImage(file="images/false.png")
        self.btn_false = Button(image=img_false, highlightthickness=0, command=self.check_question_false)
        self.btn_false.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end.")
            self.btn_false.config(state="disabled")
            self.btn_true.config(state="disabled")
        self.canvas.config(bg="white")

    def check_question_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def check_question_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
