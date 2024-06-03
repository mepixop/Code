def get_user_numbers(number_list, number_list_size, first_number, last_number):
  '''
    Takes a list, prints a input request inside the Terminal and adds the input to the list, a spezified amount of times. Input has to be a int and a range of first and last_number. 

    Parameters
    ----------
    number_list: list, in wich the enterd numbers should be added
    number_list_size: int, the size the List should have/the amount of times it askes to add an element to the list (inclusive)
    first_number: int, used to set the first allowed number
    last_number: int, used to set the last allowed number

    Returns
    ----------
    :returns: list
  '''
  print(f"Bitte gebe deine {number_list_size} Tip Zahlen an.")

  while len(number_list) < number_list_size:
    user_number = int(input(f"Hier Nummer {len(number_list)+1} eingeben: "))

    if user_number > last_number or user_number < first_number:
      print(f"die Zahl {user_number} ist nicht erlaubt, bitte neue Zahl angeben. Ganzzahl zwischen {first_number} und {last_number}.")
    else:
      if user_number not in number_list:
        number_list.append(user_number)
      else: 
        print(f"die Zahl {user_number} ist bereits vorhanden, bitte neue Zahl angeben.")
  
  return(number_list)

def calculate_bingo(list_one, list_two):
  '''
  Takes two lists and compares the Elements with each other. Outputs the amount of times which they had matching Elements.

  Parameters
  ----------
  list_one : list of number to compare
  list_two : list of number to compare

  Returns
  ----------
  :returns: Integer, amount of times the two lists matched
  '''
  bingo = 0
  for element in list_one:
    if element in list_two:
      bingo += 1
  return bingo

def print_lotto_solution(user_numbers, lotto_numbers, bingo_amount):
  """
  Prints the Lotto Solution in the Terminal
  """
  print("\n--------------------------\n")
  print(f"Lottonummer: {lotto_numbers}")
  print(f"Deine Nummern: {user_numbers}")
  if bingo_amount > 0:
     print(f"Du hast {bingo_amount} richtige.")
  else: 
     print("Versager! nichts richtig hinbekommen. Das bist du.")
  print("\n--------------------------\n")

def generate_lotto_numbers(lotto_Numbers,amountNumbers,first_number, last_number):
#alternative generating random numbers using randint instead of sample
  import random
  lotto_Numbers = []
  
  while len(lotto_Numbers) < amountNumbers:
      num = random.randint(first_number, last_number)
      if num not in lotto_Numbers:
          lotto_Numbers.append(num)
  print(lotto_Numbers)
  