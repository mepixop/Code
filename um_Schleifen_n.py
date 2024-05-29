from miniLib import printTitel
#Loops
#strg+c bricht ab

#Aufgabe1
printTitel()
zahl=7
while zahl < 10:
  print(str(zahl) + "ist kleiner als 10.")
  zahl += 1

#Aufgabe2
printTitel()
number=19
while number >= 10:
  print(number)
  number -= 1
else:
  print("es wurden ausgegeben" +str(number+1))

#Aufgabe3
#break bricht schleifen ab 
printTitel()
i=1
while i <=100:
  print(i)
  i +=1
  if i == 20:
    break

#for schleife
for count in range(10):
  print(count)

print("for loop mit range und start/stop argumenten mit schritten (start 10 bis 20 mit -5schritte)")
for count in range(100,20,-5):
  print(count)  

#range will always take same amount of memory nomather what the range represents