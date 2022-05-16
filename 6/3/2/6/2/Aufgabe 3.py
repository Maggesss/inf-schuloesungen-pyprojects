def isInt(probe):
    try:
        probe = int(probe)
        return True
    except:
        return False

def isFloat(probe):
    try:
        probe = float(probe)
        return True
    except:
        return False

def Wertverlust(Neupreis, Alter):
    if not (isFloat(Neupreis) and isInt(Alter)):
        return print("\nWhoops, was hast du denn da eingegeben?\n")
    Jahr = 0
    Wert = float(Neupreis)
    while Jahr < int(Alter):
        if Jahr == 0:
            Wert = Wert * 0.7
        else:
            Wert = Wert * 0.8
        Jahr += 1
        print(f"Jahr: {Jahr } | Wert: {round(Wert, 2)}")

loop = "y"

while loop == "y":
    Wertverlust(input("\nBitte Neupreis eingeben: "),
                input("Bitte Alter eingeben: ")), 
    loop = input("\nNochmal? y/n: ")