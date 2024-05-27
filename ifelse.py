print("Geben Sie eine Zahl ein")
zahl = int(input())

if zahl>=0:
  print("die Zahl"  + str(zahl) + "ist positiv")
elif zahl<0:
  print("die Zahl" + str(zahl) + "ist negativ")


print("wie alt sind sie")
zahlJahre = int(input())

if zahlJahre>=18:
  print("du bist volljährig")
elif zahlJahre<18:
  print("du bist minderjährig")

print("geb mir eine note")
zahlNote = int(input())

if zahlNote==1:
    print("Sehr gut")
elif zahlNote==2:
    print("gut")
elif zahlNote==3:
    print("Befriedigend")
elif zahlNote==4:
    print("Ausreichend")
elif zahlNote==5:
    print("Nicht aussreichend")
else:
   print("Ungültig")

print("ich brauche noch eine Zahl")
zahlPrüf = int(input())
if zahlPrüf > 0:
  print("positiv") 
  if (zahlPrüf%2)==0:
    print("gerade")
  else:
     print("ungerade")
elif zahlPrüf == 0:
  print("genau 0")
else:
  print("negativ")

print("geb mir noch eine zahl")
zahlEins = float(input())
print("und noch eine!")
zahlZwei = float(input())

if (zahlEins>0) & (zahlZwei>0):
   print("wir sind beide positiv!")
elif(zahlEins<0) // (zahlZwei<0):
   print("einer von uns ist negativ")
