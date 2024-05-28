#count excercise numbers and print Title with the Number
aufgaben_Nummer=0
def printTitel(name=''):
  global aufgaben_Nummer
  aufgaben_Nummer +=1
  print( "\n", "Aufgabe {}".format(aufgaben_Nummer), name)

def printPrettyMultipliTable(nM):
  print("   ", end="")
  for i in range(1, nM + 1):
      print(f"{i:4}", end="")
  print("\n" + "----" * (nM + 1))

  for i in range(1, nM + 1):
      print(f"{i:2} |", end="")
      for j in range(1, nM + 1):
          print(f"{i * j:4}", end="")
      print()