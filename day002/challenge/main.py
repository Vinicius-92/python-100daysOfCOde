print("Welcome to the tip calculator!")
totalBillValue = float(input("What was the total bil? $"))
tipPercentage = int(input("What percentage tip would you like to give? 10, 12 or 15?" ))
amountOfPeople = int(input("How many people to split the bill? "))


def bill_calculator(bill, people, percentage):
    return (bill / people) + (percentage / 100) * bill


total = bill_calculator(totalBillValue, amountOfPeople, tipPercentage)
print(f"Each person sould pay: ${'{:.2f}'.format(total)}")

