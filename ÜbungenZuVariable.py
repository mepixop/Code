##Aufgaben zum arbeiten mit Variablen

aufgaben_Nummer=0

def printTitel():
  global aufgaben_Nummer
  aufgaben_Nummer +=1
  print( "\n", "Aufgabe {}".format(aufgaben_Nummer))


#Aufgabe 1 - Variablenzuweisung
printTitel()
x = 10
y =5
summe = x+y

print(summe)

#Aufgabe2 - Typen von Variablen ausgeben
printTitel()
a = 3.14
b = "Hallo, Welt!"
c_Bool = True

print(type(a),type(b),type(c_Bool))

#Aufgabe3 - Variablen und String zusammenführen
printTitel()
name = "Sara"
alter = 28

satz = "Mein Name ist ", name, " ich bin ",alter, " Jahre alt."

print(satz)

#Aufgabe4 - Variablenwerte austauschen
printTitel()
c = 15
v = 20

print("Original Nummern: values",c,v)
c,v = v,c
print("swaped",c,v)
c= c+v
v= c-v
c= c-v
print("swaped back!",c,v)

#Aufgabe 5 - Mathematische Operatoren mit Variablen
printTitel()
d = 15
e= 4
summeDE = d+e
diffDE = d-e
prodDE = d*e
quotDE = d/e
modDE = d%e
gZ= d//e #cuts number at decimal (truncate integer)

print("Summe:",summeDE,"\nDifferenze:", diffDE,"\nProdukt:", quotDE, "\nModulo:", modDE)

#Aufgabe6 - Benuzuerinput und Variablen
printTitel()
benutzer =""
benutzer_Alter = ''
msgAskForName = "Bitte gebe deinen Namen an."
msgAskForAge = "Bitte gebe dein Alter an."
msgErrorAge= "gebe nur gerade possitive Zahlen für deinen Geburtstag an."
#mit int casting (umwandlung in einen besitmmten datentyp )

def check(alter_String):
  try:
    return (str(int(alter_String)) == alter_String) and (int(alter_String) > 0)
  except:
   print(msgErrorAge)
   return
  

print(msgAskForName)
benutzer = input()
print(msgAskForAge)
while not check(benutzer_Alter):
  benutzer_Alter = input()
    
print("Hallo,", benutzer, "du bist", benutzer_Alter, "Jahre alt!")

