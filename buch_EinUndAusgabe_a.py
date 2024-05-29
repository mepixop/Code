from miniLib import printTitel

#Übung Eingabe Inch
printTitel(2, "Eingabe Zahl")
print("bitte geben sie einen inch wert ein")
inchwert=input()
xganz = float(inchwert)
ergebnis= xganz*2.54
a= 0
print(f"{xganz} inch sind {ergebnis}")

#Übung Eingabe Gehalt
printTitel(2, "Eingabe Zahl mit Steuerberechnung Gehalt")
print("Geben Sie ihr Gehalt in Euro ein:")
gehalt = input()
gehaltzahl =float(gehalt)
steuerabgabe = gehaltzahl/100*18
print(f"Es ergibt sich die Steuer von {steuerabgabe}")


#Übung Verzweigung
printTitel(2, "Verzweigung Steuerberechnung Gehalt")
print("Geben Sie ihr Gehalt in Euro ein:")
gehalt = input()
gehaltzahl =float(gehalt)
if gehaltzahl>=4000:
    steuerabgabe = gehaltzahl/100*26
elif gehaltzahl<2500:
    steuerabgabe = gehaltzahl/100*18
else:
    steuerabgabe = gehaltzahl/100*22
print(f"Es ergibt sich die Steuer von {steuerabgabe}")
