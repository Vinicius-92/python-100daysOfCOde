class QuizBrain:

    def __init__(self, questions):
        self.user_score = 0
        self.question_number = 0
        self.question_list = questions

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.user_score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your score is: {self.user_score}/{self.question_number}")
        print()

    def next(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {question.text} (True/False): ").lower()
        self.check_answer(answer, question.answer)


