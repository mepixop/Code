from miniLib import printTitel
# lists in python etwas wie Array in anderen sprachen

# Variable, kann einen einzigen Wert speichern
zahl=4
print("zahl:" +str(zahl))

# List kann beliebig viele Werte speichern
# Element: 1 2 3 4
# index:   0 1 2 3 
zahlen = [1,3,7,14]
print("zahlen: " + str(zahlen))
print(zahlen)

print("Ausgabe 1. Element am Index 0: " +str(zahlen[0]))
print("Ausgabe 1. Element am Index 1: " +str(zahlen[1]))
print("Ausgabe 1. Element am Index 2: " +str(zahlen[2]))


#print("Versuch: Ausgabe 4. Element am Index 4" + str(zahlen[4]))
#index error: list index out of range

strings = ["Hund", "Katze", "Maus"]
print("Strings")
print("Ausgabe 1. Element am Index 0: " +str(strings[0]))
print("Ausgabe 1. Element am Index 1: " +str(strings[1]))
print("Ausgabe 1. Element am Index 2: " +str(strings[2]))

#ele zählt automatisch hoch 
for ele in strings:
  print (ele)

for i in range(len(strings)):
  print(strings[i])

#while schleife zur ausgabe aller elemente in my_list
i= 0
while i < len(strings):
  print(str(strings[i]))
  i += 1

#Hinzufügen von Elementen in eine List
printTitel(1,"Hinzufügen von Elementen in Liste")

tiere= []
print("Anzahl der Tiere in Liste vor append")
print(len(tiere))

tiere.append("Hund")
tiere.append("Maus")
tiere.append("Biber")
tiere.append("Elefant")

# print die Anzahl der Tiere in der Liste
print("Anzahl der Tiere in Liste")
print(len(tiere))

# print das letzte Element in Liste (-1 ist hier sehr wichtig, da lenge nicht=letzter Index ist)
print("Letztes Element in Tier-liste")
lastEle=len(tiere)-1
print(tiere[lastEle])

# entfernen von einem konkreten, vorhandenen Element in Liste
printTitel(1, "Entfernen von Elementen in Listen")

print("Anzahl der Tiere in Liste, nach entfernen.")
tiere.remove("Maus")
print(len(tiere))

# pop zusatzeigenschaft: gibt während entfernung den Inhalt des Elements zurück.
tiere.pop(2)
print(len(tiere))
