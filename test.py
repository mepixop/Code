benutzer =""
benutzer_Alter = ''
msgAskForName = "Bitte gebe deinen Namen an."
msgAskForAge = "Bitte gebe dein Alter an."
msgErrorAge= "gebe nur gerade possitive Zahlen für deinen Geburtstag an."
#mit int casting (umwandlung in einen besitmmten datentyp )


print(msgAskForName)
benutzer = input()
print(msgAskForAge)
benutzer_Alter = input()

while not benutzer_Alter.isdigit:
  benutzer_Alter = input()

print("Hallo,", benutzer, "du bist", benutzer_Alter, "Jahre alt!")
