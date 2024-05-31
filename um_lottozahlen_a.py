#schreibe ein Programm zum lotto spielen
import random
import um_lottoservice_a

first_Number = 1
last_Number = 6
amount_Numbers = 6
lotto_Numbers = []
bet_Numbers = []

bingo= 0
draw_number = 0
playMode= False

while not playMode:
  try:
    selectedMode=input("möchtest du spielen?")
    
    if selectedMode == "ja":
      playMode = True
    elif selectedMode =="Exit":
      break

    while bingo < 6 and playMode:
      #Generate Lottonumbers
      lotto_Numbers= random.sample(range(first_Number, last_Number+1),amount_Numbers)

      #Get the choosen Numbers
      bet_Numbers = um_lottoservice_a.getbetNumbers(bet_Numbers,amount_Numbers,first_Number,last_Number)
      
      #Calculate the amount of times, the same numbers is in the lists
      bingo = um_lottoservice_a.calculateBingo(bet_Numbers,lotto_Numbers)
      
      #Prints the solution to all
      um_lottoservice_a.printSolution(bet_Numbers,lotto_Numbers,bingo)
      
      #counts the attempts
      draw_number += 1

      #reset the game
      playMode = False
      showMenue = True
      bingo = 0
      lotto_Numbers.clear()
      bet_Numbers.clear()

    print(f"Du hast {draw_number} versuche gebraucht umd 6 richtige zu haben.")

  except ValueError:
    print("error, end the game")

#schritt 2
#solange ziehen bis ich 6 richtige habe
#anzahl der versuche zählen
