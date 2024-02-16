import re
import random
from generovani_klicu import * 
def preved_retezec_na_cislo(reterez_na_prevod):
    global vsechny_znaky
    reterez_na_prevod = reterez_na_prevod.lower()
    vsechny_znaky = " abcdefghijklmnopqrstuvwxyzáéíóůúýěčďňřšťž1234567890"



    for i in reterez_na_prevod:
        if i not in vsechny_znaky:
            print("toto nelze vykonat, v řetězci se nachází nedovolený znak")
            return
    # l = list(vsechny_znaky)
    # random.shuffle(l)
    # vsechny_znaky = "".join(l)
    vysledek = ""

    for i in reterez_na_prevod:
        vysledek += str(100 + (re.search(i, vsechny_znaky).start()))[1:]
    
    
    split_strings = [int(vysledek[i:i+2]) for i in range(0, len(vysledek), 2)]

    return(vysledek)

        
        
    



