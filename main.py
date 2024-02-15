import random

def Soudelna(cislo_a, cislo_b):
    delitele_cisla_a = []
    for i in range(1, cislo_a+1):
        if cislo_a%i == 0:
            delitele_cisla_a.append(i)
    #print(delitele_cisla_a)
    for i in delitele_cisla_a:
        if cislo_b%i == 0 and i!=1:
            return True 
    return False

def Vygeneruj_klice(prvocislo_p, prvocislo_q):
    n = prvocislo_p * prvocislo_q

    #Eulerova funkce 
    phi = (prvocislo_p - 1) * (prvocislo_q - 1)

    #zvolíme náhodné e nesoudělné s phi
    while True:
        e = random.randrange(1000, 10000)
        if Soudelna(e, phi) == False:
            break
    # print("e", e)
    # print("phi", phi)
    x = 1
    while True:
        
        if (x*e)%phi == 1:
            break
        else: 
            x += 1
    return {"verejny_klic":(n, e), "soukromy_klic":(n, x) }

def udelej_velke_prvocislo():
    while True:
        x = random.randrange(1000, 10000)
        is_prime = True
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                is_prime = False
                break
        if is_prime:
            return x



print(Vygeneruj_klice(udelej_velke_prvocislo(), udelej_velke_prvocislo()))

import re
def preved_retezec_na_cislo(reterez_na_prevod):
    reterez_na_prevod = reterez_na_prevod.lower()
    

    vsechny_znaky = " abcdefghijklmnopqrstuvwxyzáéíóůúýěčďňřšťž1234567890"

    for i in reterez_na_prevod:
        if i not in vsechny_znaky:
            print("toto nelze vykonat, v řetězci se nachází nedovolený znak")
            return
    l = list(vsechny_znaky)
    random.shuffle(l)
    vsechny_znaky = "".join(l)

    vysledek = ""

    for i in reterez_na_prevod:
        vysledek += str(100 + (re.search(i, vsechny_znaky).start()))[1:]
    
    
    split_strings = [vysledek[i:i+2] for i in range(0, len(vysledek), 2)]

    print(split_strings)

        
        
    


preved_retezec_na_cislo("abcdefghijklmnopqrstuvwxyz")

#mohl bych do tý šifry přidat pořadí vsechny_znaky