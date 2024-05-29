from miniLib import printTitel

#Aufgabe1
printTitel(2, 'Summe der ersten n natürlichen Zahlen')
nS = int(input("bitte gebe eine possitive ganz Zahl an!"))
summe = 0

if nS <= 0: 
  print("Error: bitte nur Positive zahlen")
else:
  for i in range (1, nS+1):
    summe += i

  print("Summe:", str(summe))

#Aufgabe2
printTitel(2, 'Fakulät einer Zahl berechnen')
nF = int(input("bitte gebe eine possitive ganz Zahl an!"))
fakultaet = 1

if nF <= 0: 
  print("Error: bitte nur Positive zahlen")
else:
  for i in range (1, nF + 1):
    fakultaet *= i
  print("Die Fakultät von", nF, "ist:", fakultaet)


#Aufgabe 3
printTitel(2, 'Alle geraden Zahlen in einem Bereich')
start = int(input("Bitte geben Sie start ein"))
end = int(input("Bitte geben sie ein ende ein"))

for i in range (start,end+1):
  print(start)
  if i % 2 != 0:
    continue
  print(i)


#Aufgabe 4
printTitel(2, 'Zählen von Vokalen in einem String')
vokalCount= 0
vokale="aeiouAEIOU"

letters = input("bitte geben sie eine beliebige buchstabenfolge ein")

print("is there a vokal")
#char= zeichen in eingabe
for char in letters:
  if char in vokale:
    print("true")
    break

for char in letters:
  if char in vokale:
    vokalCount += 1
print("Anzahl Vokale ist:", vokalCount)

#Aufgabe 5
printTitel(2, 'Benutzer-Eingabe validieren (mit while-Schleife)')
zahl = 0

while zahl <= 0:
  try: 
    zahl = int(input("bitte gebe eine possitive ganz Zahl an."))
    if zahl < 0:
      print("keine Positive zahl. Versuchs nochmal")

  except ValueError:
    print("das ist keine ganze zahl? bitte nochmal angeben")

#Aufgabe 6
printTitel(2, 'einfache Multiplikationstabelle')
nM = int(input("bitte Zahl eingeben"))

for i in range(1, nM + 1):
    for j in range(1, nM + 1):
        print(f"{i * j:4}", end="")
    print() 

