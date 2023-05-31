import re
import json

data = {}

with open("./access.log", "r") as file:     # Ouverture en mode écriture du fichier
    for line in file.readlines():   # On créé une boucle for pour tout le fichier ligne par ligne, où l'on met la valeur de la ligne dans une variable
        address_ip = line.split(" ")[0]     # On split la ligne grâce au espace et on récupère le première élément
        code_statut = line.split(" ")[8]    # Le 9eme élément

        if code_statut == "\"-\"":  # On créé un première condition qui vient exclure une chaine de charactère précis puis on pass directement à la prochaine ligne
            continue
        if data.get(address_ip):    # Si qqch alors on continue
            if data[address_ip].get(code_statut):   # Si le code_statut existe alors on continue
                data[address_ip][code_statut] += 1  # On incrément de 1
            else:   # Si le code_statut existe alors on continue 
                data[address_ip][code_statut] = 1   # On le créé et on met 1
        else:   # S'il n'y a rien alors on créé la valeur dans le dictionnaire
            data[address_ip] = {}
            data[address_ip][code_statut] = 1

with open("data.json", "w") as json_file_pointer:   # On finit par créer le fichier .json avec l'aide du dictionnaire final
  json.dump(data, json_file_pointer,indent=1)