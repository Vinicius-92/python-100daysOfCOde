import random

names = "Alex Beth Caroline Dave Eleanor Freddie".split()

students_scores = {name: random.randint(1, 100) for name in names}

passed_students = {n: students_scores[n] for n in students_scores if students_scores[n] > 60}

passed_students1 = {student: score for (student, score) in students_scores.items() if score > 60}

print(passed_students)
