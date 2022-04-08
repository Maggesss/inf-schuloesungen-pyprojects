def isNumeric(probe):
    try:
        probe = float(probe)
        return True
    except:
        return False

def steigungsberechnung(punkt_1_x, punkt_1_y, punkt_2_x, punkt_2_y):
    if not (isNumeric(punkt_1_x) or isNumeric(punkt_1_y) or isNumeric(punkt_2_y) or isNumeric(punkt_2_y)) == True:
        return print("WOOOW, check your inputs, man!")
    y = float(punkt_2_y) - float(punkt_1_y)
    x = float(punkt_2_x) - float(punkt_1_x)
    steigung = round(y / x, 3)
    print(f"Die Steigung des Graphen ist ungefähr {steigung}.")

steigungsberechnung(input("Punkt 1 x: "), input("Punkt 1 y: "), input("Punkt 2 x: "), input("Punkt 2 y: "))