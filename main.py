import random

# initialise all necessarry values
punkte = 0
fehler = 0
i = 10

# run while loop for game
while i != 0:
    zahl1 = random.randint(2,10)
    zahl2 = random.randint(2,10)
    print(zahl1,"x",zahl2)
    richtig1 = (zahl1 * zahl2)
    
    loesung = input("Wie lautet die Lösung? (Enter für neue Aufgabe): ")
    if loesung != "":
        if zahl1 * zahl2 == loesung:
            print("Das ist richtig!")
            punkte = punkte + 1
        else:
            print("Das ist falsch! Es wäre",richtig1,"gewesen")
            fehler = fehler + 1
        i -= 1

# print out result
print("Du hattest",punkte,"Aufgaben richtig und",fehler,"Fehler gehabt")
