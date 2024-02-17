import random
import re
import gmpy2


def main(text_na_prevod):
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


    def Vygeneruj_klice(prvocislo_p, prvocislo_q):
        n = prvocislo_p * prvocislo_q

        #Eulerova funkce 
        phi = (prvocislo_p - 1) * (prvocislo_q - 1)

        #zvolíme náhodné e nesoudělné s phi
        while True:
            # vygenerování náhodného čísla e které je nesoudělné s phi
            e = random.randrange(1000, 10000)
            if Soudelna(e, phi) == False:
                break
        # print("e", e)
        # print("phi", phi)
        d = 1
        while True:
            
            
            if (d*e)%phi == 1:
                break
            else: 
                d += 1
        return {"verejny_klic":(n, e), "soukromy_klic":(n, d) }


    def preved_retezec_na_cislo(reterez_na_prevod):
        global vsechny_znaky
        reterez_na_prevod = reterez_na_prevod.lower()
        vsechny_znaky = " abcdefghijklmnopqrstuvwxyzáéíóůúýěčďňřšťž1234567890.,"

        for i in reterez_na_prevod:
            if i not in vsechny_znaky:
                print("toto nelze vykonat, v řetězci se nachází nedovolený znak: " + str(i))
                return
        vysledek = ""

        for i in reterez_na_prevod:
            vysledek += str(100 + (re.search(i, vsechny_znaky).start()))[1:]
        
        
        split_strings = [int(vysledek[i:i+2]) for i in range(0, len(vysledek), 2)]

        return(vysledek)



    x = preved_retezec_na_cislo(text_na_prevod)
    #print("text převedený na číslo je " + str(x))

    hodnoty = Vygeneruj_klice(udelej_velke_prvocislo(), udelej_velke_prvocislo())

    n = hodnoty["verejny_klic"][0]
    e = hodnoty["verejny_klic"][1]
    d = hodnoty["soukromy_klic"][1]
    

    #chci aby čísla byla stále dlouhá 2p čísel
    skok = 2 * (int(len(str(n))/2) - 1)

    split_strings = [(x[i:i+skok]) for i in range(0, len(x), skok)]
    


    dectionary_puvodni_a_zasifrovany = {}
    zasifrovany = []
    for m in split_strings:
        dectionary_puvodni_a_zasifrovany[m] = (int(m)**e)%n
        zasifrovany.append((int(m)**e)%n)


    
    print(zasifrovany)


    vysledek = ""
    for c in zasifrovany:
        vysledek += (str(10000000 + gmpy2.powmod(c, d, n))[2:])
        


    

    # print([kod for kod in [int(vysledek[int(i):int(i)+2]) for i in range(0, len(vysledek), 2)]])
    # return("".join([vsechny_znaky[kod] for kod in [int(vysledek[int(i):int(i)+2]) for i in range(0, len(vysledek), 2)]]))



main("aspdofghasdhfawoehfo asdhfohaswoehfoasdhfh")