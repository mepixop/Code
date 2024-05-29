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
anzahl_zahlen= 10

for ele in range(1,anzahl_zahlen+1):
  zahlen.append(ele)

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
names = ["Sara", "Rahul", "Me", "Me"]
name_to_find = "Sara"

if names.count(name_to_find) > 0 :
  print("true")
else:
  print("false")

#kurzschreibweise in pyton mit "in"
if name_to_find in names:
  print("ist enthalten!!!!!")

#Aufgabe 7
printTitel(2, "Durchschnitt berechnen")
dNum = [1,2,3,4,5,6,7,8,9,0]
summe= 0
average= 0

average = sum(dNum) / len(dNum)

print(summe)
print(average)

#Aufgabe 8
printTitel(2, "Zusammenführen von Listen")
listeEins = [1,2,3,4,5]
listeZwei = ["a","b","c","d","e"]
listeBoth = []

listeBoth= listeEins + listeZwei

#Vorsicht hier wird liste 2 als element hinzugefügt! nicht nur inhalte
listeEins.append(listeZwei)
print(listeEins)

print(listeBoth)

#Aufgabe 9
printTitel(2, "Listenverschachtelungsmatrix")

allMightList = []
allMightList.append([1,2,3])
allMightList.append([4,5,6])
allMightList.append([7,8,9])

matrix = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(0,3):
  print(allMightList[i])

for row in allMightList:
  for col in row:
    print(col, end=" ") #end= endet mit leerzeichen anstelle von Zeile
  print()

#since Pyton 3 * goes threw all elements and asign them to variables wich then are given back
for j in allMightList:
  print(*j)

#element 1/2
print(allMightList[1][2])