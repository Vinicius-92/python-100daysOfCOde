from question_model import Question
from data import question_data, question_data_trivia
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

question_bank2 = []
for question in question_data_trivia:
    question_bank2.append(Question(question["question"], question["correct_answer"]))

quiz = QuizBrain(question_bank2)

while quiz.still_has_questions():
    quiz.next()

print("You've completed the quizz")
print(f"Your final score was: {quiz.user_score}/{quiz.question_number}")
