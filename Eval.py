from colorama import init
init()
from colorama import Fore, Back, Style

mot1 = "castor"
mot2 = "cinema"
mot3 = "cypres"
mot4 = "citron"
mot5 = "camion"
mot6 = "webcam"
mot7 = "ajoute"
mot8 = "aligne"
mot9 = "bronze"
mot10= "brutal"


print("Bienvenue dans motus sans ami")



l=6*[0]
for i in range(len(l)):
    l[i]=6*[0]
l[0][0]=1
print(l)

essais=4
chances=4

motadeviner=input("entrez le mot a deviner:")
MOT=motadeviner
motadeviner=list(motadeviner.lower())

while plusdechances or mottrouve:
  if len(essaimotlist) != len(motadeviner):
    print("Vous devez entrer un mot de" , len(motadeviner), "lettres! Réessayez!")

if plusdechances:
  print("Vous avez perdu, le mot etait: ",MOT )
   
if mottrouve:
  print("Bravo vous avez trouvé le mot avec", essais-chances , "essais !")

input()