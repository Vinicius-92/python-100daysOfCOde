# Write your code below this line 👇


def prime_checker(number):
    if 0 < number < 4:
        print("It's a prime number.")
    for p in range(2, number):
        if number % p == 0:
            print("It's not a prime number.")
            exit()
    print("It's a prime number.")


# Write your code above this line 👆
# Do NOT change any of the code below👇

n = int(input("Check this number: "))
prime_checker(number=n)
