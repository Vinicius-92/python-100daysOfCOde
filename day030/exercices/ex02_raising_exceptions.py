height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Godzilla it's not real.")

print(weight / height ** 2)