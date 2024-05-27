#Variablen und Datentypen
#pyton Typed-Variablen von selbst
# Raute für 

##Integer##
ganzezahl = 0
print(ganzezahl)
##Ca,eö-Case Notation
ganzeZahl = 1
print(ganzeZahl)
##Snake-Case Notation (Konvention in Python)
ganze_Zahl = 2
print("ganze_Zahl:", ganze_Zahl) #übergabe von zwei Argumenten an den Builtin print, Buildin: in Python eingebaute Funktion

##Gleitkommazahlen##
komma_zahl = 2.14 #Punkt ist der dezimaltrenner, daher müssenwir den Punkt als Trennzeichen nehmen
print("komma_zahl:", komma_zahl)

#type() produziert selbst keine Ausgabe und gibt nur den Wert zurück, daher brauchen wir zusätzlich print()
datentype_komma_zahl = (type(komma_zahl))
print(datentype_komma_zahl)

print(type(komma_zahl))