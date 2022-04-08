generation = 0
jung = 6
erwachsen = 9
alt = 12
while generation < 5:
    hilfVar = jung
    jung = (erwachsen * 4) + (alt * 2)
    alt = erwachsen / 3
    erwachsen = (hilfVar / 2)
    print("Generation", generation + 1, "hat", jung, "junge Mäuse,", erwachsen, "erwachsene Mäuse und", alt, "alte Mäuse.")
    generation = generation + 1