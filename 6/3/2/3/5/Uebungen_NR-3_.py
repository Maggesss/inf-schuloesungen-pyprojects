# Eingabe
balance  = float(input("Kapital (in Euro):"))
# Verarbeitung
interest_rate = 0.02
bank_interest = balance * interest_rate

balance = balance + bank_interest
# Ausgabe
print(f"Neues Kapital: {balance}")