import random
random.seed()

a= random.randint(1,10)
b= random.randint(1,10)
c=a+b

print(f"Die Aufgabe: {a}+{b}")
print("Bitte Lösungsvorschlag eingeben")

loesungvorschlag= int(input())
if loesungvorschlag== c:
    print("deine Antwort ist richtig!")
else :
    print("deine Antwort ist falsch.",
          "Lösung:",c)

