kg = float(input("Luggage weight: "))
fee = 0
if kg < 0:
    print("Nedopusten unos")
elif kg > 50:
    print("Nedopusten unos.")
elif 0 <= kg <= 15:
    print("Nema nadoplate. Ugodan let")
elif 15 < kg <= 50:
    t = kg - 15
    fee = int(round(t * 50))
    print("Nadoplata iznosi " + str(fee) + " kn")

