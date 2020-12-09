from colorama import init
init()
from colorama import Fore, Back, Style

print("Bienvenue dans motus sans ami")

essais=4
chances=4


l=6*[0]
for i in range(len(l)):
    l[i]=6*[0]
l[0][0]=1
print(l)



list = ["castor","cinema","cypres","citron","camion","webcam","ajoute","aligne","bronze","brutal"]

motadeviner = list [random.randmint (0,5)]

choice(list) = motadeviner = list(motadeviner.lower())


while plusdechances or mottrouve:
  if len(essaimotlist) != len(motadeviner):
    print("Vous devez entrer un mot de" , len(motadeviner), "lettres! Réessayez!")

if plusdechances:
  print("Vous avez perdu, le mot etait: ",motadeviner )
   
if mottrouve:
  print("Bravo vous avez trouvé le mot avec", essais-chances , "essais !")

input()
