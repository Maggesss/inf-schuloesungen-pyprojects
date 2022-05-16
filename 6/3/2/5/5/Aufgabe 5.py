def isNumeric(probe):
    try:
        probe = float(probe)
        return True
    except:
        return False

def KreisSchnittDing(x1, y1, r1, x2, y2, r2):
    if not (isNumeric(x1) and isNumeric(y1) and isNumeric(r2) and isNumeric(x2) and isNumeric(y2) and isNumeric(r2)):
        return print("Whoops, was hast du denn da eingegeben?\n")
    if (((abs(abs(float(x1)) - abs(float(x2))) and (abs(abs(float(y1)) - abs(float(y2))))) <= (float(r1) + float(r2)))):
        return print("Die Kreise schneiden sich!\n")
    return print("Die Kreise schneiden sich nicht!\n")

loop = "y"

while loop == "y":
    KreisSchnittDing(input("\nBitte X Koordinate von Kreis 1 eingeben: "),
                    input("Bitte Y Koordinate von Kreis 1 eingeben: "), 
                    input("Bitte Radius von Kreis 1 eingeben: "),
                    input("\nBitte X Koordinate von Kreis 2 eingeben: "),
                    input("Bitte Y Koordinate von Kreis 2 eingeben: "),
                    input("Bitte Radius von Kreis 2 eingeben: "))
    loop = input("Nochmal? y/n: ")