# === Numeric-Check (float) ===
def isNumeric(probe):
    try:
        probe = float(probe)
        return True
    except:
        return False

# === Berechnung des BMI ===
def bmi_rechnung(weight, height):
    # abbrechen, wenn keine validen Zeichen / Zahlen eingegeben wurden
    if (isNumeric(weight) or isNumeric(height)) == False:
        return print("WOOOW, check your inputs, man!")
    # Berechnung bei Normalfall
    bmi = float(weight) / (float(height) * float(height))
    # Output
    return print(f"Bei einem Gewicht von {weight} und einer Größe von {height} haben Sie einen BMI von {round(bmi, 1)}.")

# loop erstellen und Funktion "aktivieren", in Funktion nach input "fragen"
loop = "y"
while (loop == "y"):
    bmi_rechnung(input("Bitte Gewicht eingeben: "), input("Bitte Größe eingeben: "))
    loop = input("Nochmal? y/n: ")