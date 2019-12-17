bloodtype_d = input("Donor blood type: ").lower()
rh_d = input("Donor Rh factor: ").lower()
bloodtype_r = input("Recipient blood type: ").lower()
rh_r = input("Recipient Rh factor: ").lower()

if rh_r == "-" and rh_d == "+":
    print("This is not compatible.")
elif bloodtype_r == "0" and bloodtype_d == "0":
    print("Match.")
elif bloodtype_r == "ab":
    print("Match.")
elif bloodtype_r == "a" and bloodtype_d == "a" or bloodtype_d == "0":
    print("Match.")
elif rh_d == "-" and bloodtype_r == "a":
    print("This is not compatible.")
elif bloodtype_r == "b" and bloodtype_d == "b" or bloodtype_d == "0":
    print("Match.")
elif rh_d == "-" and bloodtype_r == "b":
    print("This is not compatible.")
elif rh_r == "-" and rh_d == "-" and bloodtype_r != "0":
    print("Match.")
else:
    print("This is not compatible.")




