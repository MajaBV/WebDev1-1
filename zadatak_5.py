a = int(input("Enter an integer(1,2,3...): "))
b = int(input("Enter an integer(1,2,3...): "))
c = int(input("Enter an integer(1,2,3...): "))

if a == b == c == a:
    print("Equilateral triangle")
elif a != b != c != a:
    print("Right triangle")
else:
    print("Isosceles triangle")