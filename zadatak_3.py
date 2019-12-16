x = 0
y = 0

while True:
    ask = input("U(p), D(own), L(eft), R(ight): ")
    t = [x, y]
    if ask.lower() == "u":
        y += 1
        print(t)
    elif ask.lower() == "d":
        y -= 1
        print(t)
    elif ask.lower() == "l":
        x -= 1
        print(t)
    elif ask.lower() == "r":
        x += 1
        print(t)

    elif ask.lower() == "q":
        print(t)
        break
    else:
        print("Error")

