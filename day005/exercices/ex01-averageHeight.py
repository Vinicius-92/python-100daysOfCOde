# 🚨 Don't change the code below 👇

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# 🚨 Don't change the code above 👆
# Write your code below this row 👇


def average(students):
    count = 0
    total = 0
    for stu in students:
        count += 1
        total += stu
    return total / count


print(round(average(student_heights)))
