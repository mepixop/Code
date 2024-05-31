def getbetNumbers(betNumbers, amountNumbers, firstNumber, lastNumber):
  print(f"Bitte gebe deine {amountNumbers} Tip Zahlen an.")

  while len(betNumbers) < amountNumbers:
    number = int(input(f"Hier Nummer {len(betNumbers)+1} eingeben: "))

    if number > lastNumber or number < firstNumber:
      print(f"die Zahl {number} ist nicht valide, bitte neue Zahl angeben. Ganzzahl zwischen {firstNumber} und {lastNumber}.")
    else:
      if number not in betNumbers:
        betNumbers.append(number)
      else: 
        print(f"die Zahl {number} ist bereits vorhanden, bitte neue Zahl angeben.")
  
  return(betNumbers)

def calculateBingo(betNumbers, lottoNumbers):
  bingo = 0
  for element in betNumbers:
    if element in lottoNumbers:
      bingo += 1
  return bingo

def printSolution(betNumbers, lottoNumbers, bingo):
  print("\n--------------------------\n")
  print(f"Lottonummer: {lottoNumbers}")
  print(f"Deine Nummern: {betNumbers}")
  if bingo > 0:
     print(f"Du hast {bingo} richtige.")
  else: 
     print("Versager! nichts richtig hinbekommen. Das bist du.")
  print("\n--------------------------\n")

def generateLottoNumbers(lotto_Numbers,amountNumbers,firstNumber, lastNumber):
#alternative generating random numbers using randint instead of sample
  import random
  lotto_Numbers = []
  #for i in range(first, last )
  while len(lotto_Numbers) < amountNumbers:
      num = random.randint(firstNumber, lastNumber)
      if num not in lotto_Numbers:
          lotto_Numbers.append(num)
  print(lotto_Numbers)
  