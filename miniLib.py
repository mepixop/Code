#count excercise numbers and print Title with the Number and optionaly description
aufgaben_Nummer=0
def printTitel(type=0,name=''):
  global aufgaben_Nummer
  aufgaben_Nummer +=1
  types=(['','Übung','Aufgabe'])

  print( "\n", "{}".format(aufgaben_Nummer), name)

#prints Multiplikationtable nM-times
def printPrettyMultipliTable(number):
  print("   ", end="")
  for i in range(1, number + 1):
      print(f"{i:4}", end="")
  print("\n" + "----" * (number + 1))

  for i in range(1, number + 1):
      print(f"{i:2} |", end="")
      for j in range(1, number + 1):
          print(f"{i * j:4}", end="")
      print()

#Summe von Aufeinanderfolgenden positiven, Natürlichen Zahlen (Fibonacci)
def countFib(number):
  summe =0
  if number < 0: 
    print("Error: bitte nur Positive zahlen")
  else:
    for i in range (1, number+1):
      summe += i

    print("Summe:", str(summe))