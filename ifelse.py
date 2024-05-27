print("Geben Sie eine Zahl ein")
zahl = int(input())

if zahl>=0:
  print("die Zahl ist positiv")
elif zahl<0:
  print("die Zahl ist negativ")


print("wie alt sind sie")
zahlJahre = int(input())

if zahlJahre>=18:
  print("du bist volljährig")
elif zahlJahre<18:
  print("du bist minderjährig")

print("geb mir eine note")
zahlNote = input()

if zahlJahre==1:
    print("Sehr gut")
elif zahlJahre==2:
    print("gut")
elif zahlJahre==3:
    print("Befriedigend")
elif zahlJahre==4:
    print("Ausreichend")
elif zahlJahre==5:
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
zahlEins = int(input())
print("und noch eine!")
zahlZwei = int(input())

if (zahlEins>0) & (zahlZwei>0):
   print("wir sind beide positiv!")
elif(zahlEins<0) // (zahlZwei<0):
   print("einer von uns ist negativ")
