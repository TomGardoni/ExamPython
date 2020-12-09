import random
from colorama import init
init()
from colorama import Fore, Back, Style

print("Bienvenue dans motus sans ami")

essais=8
chances=8

liste = ["castor","cinema","cypres","citron","camion","webcam","ajoute","aligne","bronze","brutal"]
mot = random.choice(liste)

for essais in range (0,8):
	joueuressais = input("Saisis un mots de 6 lettres champion(ne) : ")
	for i in range (0,6):
		if mot[i] == joueuressais [i]:
			print(Fore.RED + joueuressais[i])
		else :
			couleur = False
			for j in range (0,6):
				if mot[i] == joueuressais[j]:
					print(Fore.YELLOW + joueuressais[j])
					couleur = True
			if couleur : False
			print(Fore.BLUE + joueuressais[j])

while plusdechances or mottrouve:
  if len(essaimotlist) != len(motadeviner):
    print("Vous devez entrer un mot de" , len(motadeviner), "lettres! Réessayez!")

if plusdechances:
  print("Vous avez perdu, le mot etait: ",motadeviner )
   
if motadeviner == joueuressais:
  print("Bravo vous avez trouvé le mot avec", essais-chances , "essais !")

input()