alfonci = 5000000
velonci = 9000000
years = 0

while velonci >= alfonci:
    years = years + 1
    alfonci = alfonci * 1.06

    if years % 4 == 0:
        velonci = (velonci * 1.05) - 500000
    else:
        velonci = velonci * 1.02
print("The number of Alfonci will exceed the number of Velonci in {0} years. The total number of Alfonci will then be = {1}".format(years, round(alfonci)))