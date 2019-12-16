rows = int(input("How many rows do you want: "))
brojac = 1
for i in range(1, rows + 1):
    for m in range(1, i + 1):
        print(brojac, end=' ')
        brojac = brojac + 1
    print()