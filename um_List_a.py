from miniLib import printTitel

#Aufgabe 1
printTitel(2, "Erstellen und Zugreifen")
früchte = ["Apfel","Banane","Limone"]

print(f"Letzte Element: {früchte[-1]}")
print(f"zweite Element: {früchte[1]}")
print(f"zweite Element: {früchte[1]}")

#Aufgabe 2
printTitel(2, "Listslicing")
numbers = [1,13,4,35,16,7,34,8,22,1000]

for count in range(0,5,+1):
  print(f"Erste fünf Zahlen: {numbers[count]}")

for count in range(-1,-4,-1):
  print(f"Lezte drei Zahlen: {numbers[count]} ")

#Aufgabe 3
printTitel(2, "Hinzufügen und Entfernen")
zahlen= []

i= 0
while i < 5:
  zahlen.append(i+1)
  i = i+1
print(zahlen)

zahlen.remove(3)
print(zahlen)

print(f"pop removing: {zahlen.pop(1)}")

#Aufgabe 4
printTitel(2, "Listenlänge")
lenghList= [2,13,4,"ads"]
print(len(lenghList))

#Aufgabe 5
printTitel(2,"Sortieren")
randNum = [2,45,82,94,2,1,8]
randNum.sort()
print(randNum)

#Aufgabe 6
printTitel(2, "Finden von Elementen")
names = ["Sara", "Rahul", "Me", "You"]

if names.count("Sara") > 0 :
  print("true")
else:
  print("false")

#Aufgabe 7
printTitel(2, "Durchschnitt berechnen")
dNum = [1,2,3,4,5,6,7,8,9,0]
summe= 0
durchschnitt= 0

for elem in dNum:
  summe = summe+dNum[elem]
durchschnitt = summe/len(dNum)

print(summe)
print(durchschnitt)

#Aufgabe 8
printTitel(2, "Zusammenführen von Listen")
listeEins = [1,2,3,4,5]
listeZwei = ["a","b","c","d","e"]
listeBoth = []
j = 0
k = 0

while j < len(listeEins):
  listeBoth[j] = listeEins[j]
  j = j+1

print(len(listeBoth))