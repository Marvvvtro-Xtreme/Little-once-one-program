import random
punkte = 0
fehler = 0
repeat 10:
    zahl1 = random.randint(1,10)
    zahl2 = random.randint(1,10)
    zahl3 = random.randint(1,10)
    zahl4 = random.randint(1,10)
    print zahl1,"x",zahl2
    neu = input("Willst du eine neue Aufgabe? Dann gebe in die Konsole 1 ein")
    richtig2 = (zahl3 * zahl4)
    if neu == 1:
        print zahl3,"x",zahl4
        loesung = input("Wie lautet die Lösung?")
        if zahl3 * zahl4 == loesung:
            print "Das ist richtig!"
            punkte = punkte + 1
        else:
            print "Das ist falsch! Es wäre",richtig2,"gewesen"
            fehler = fehler + 1
    richtig1 = (zahl1 * zahl2)
    if neu != 1:
        loesung = input("Wie lautet die Lösung?")
        if zahl1 * zahl2 == loesung:
            print "Das ist richtig!"
            punkte = punkte + 1
        else:
            print "Das ist falsch! Es wäre",richtig1,"gewesen"
            fehler = fehler + 1
print "Du hattest",punkte,"Aufgaben richtig und",fehler,"Fehler gehabt"
