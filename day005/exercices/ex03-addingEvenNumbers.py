# Write your code below this row 👇

total = 0
total_two = 0
for n in range(1, 101):
    total += n if n % 2 == 0 else 0

for n in range(2, 101, 2):
    total_two += n

print(total_two)
print(total)
