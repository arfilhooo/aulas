x = 1
y = 1

while x <= 10:
    while y <= 10:
        multi = x*y

        print(f"{x} * {y} = {multi}")

        y += 1
    print("_____________________________")

    x += 1
    y = 1