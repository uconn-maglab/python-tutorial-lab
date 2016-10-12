starter = [1, 2, 45, "string", 12, 10, [1,2,3], 6, 33]
good = []

for n in starter:
    try:
        if n > 10:
            good.append(n)
        elif n == 10:
            print("Fine, but it's supposed to be greater than 10.")
            good.append(n)
        else:
            print(str(n) + " isn't greater than 10!")
    except TypeError:
        print("That's not even a number...")
        continue
print(good)
