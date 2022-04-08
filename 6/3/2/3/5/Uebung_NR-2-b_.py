# === Letter-Check (string) ===
def hasNumber(probe):
    return any(letter.isdigit() for letter in probe)

def greeting(name):
    # check if name has numbers in it...
    if hasNumber(name) == True:
        return print("WOOOW, there are names with numbers in it, {name}?")
    #the case for normal names.
    return print(f"Hallo, {name}\nNett von Dir, dass Du Dich mit mir befasst!")

# loop erstellen und Funktion "aktivieren", in Funktion nach input "fragen"
loop = "y"
while (loop == "y"):
    greeting(input("Gib bitte Deinen Namen ein: "))
    loop = input("Nochmal? y/n: ")