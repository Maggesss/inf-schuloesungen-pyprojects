generation = input("Wie viele Generationen sollen betrachtet werden?: ")
young = input("Wie viele junge Mäuse gibt es am Anfang?: ")
grown_up = input("Wie viele alte Mäuse gibt es am Anfang?: ")
old = input("Wie vile alte Mäuse gibt es am Anfang?: ")

def isNumeric(probe):
    try:
        probe = float(probe)
        return True
    except:
        return False

def generationCalc(gen, young, grown_up, old):
    if isNumeric(gen) or isNumeric(young) or isNumeric(grown_up) or isNumeric(old) == False: 
        return print("WOOOW, check your inputs, man!")
    while gen > 0:
        helper = round(young)
        young = round((grown_up * 4) + (old * 2))
        old = round(grown_up / 3)
        grown_up = round(helper / 2)
        print(f"{young}junge Mäuse, {grown_up} erwachsene Mäuse und {old} alte Mäuse. Noch {gen - 1} Generationen übrig.\n")
        gen = gen - 1

generationCalc(generation, young, grown_up, old)