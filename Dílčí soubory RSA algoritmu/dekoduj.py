import gmpy2
import re

n, e, d = 58772303, 6943, 14572879

def zakoduj(text_na_prevod, n, e):
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

    prevedeny_text_na_cislo = preved_retezec_na_cislo(text_na_prevod)
    skok = 2 * (int(len(str(n))/2) - 1)
    split_strings = [(prevedeny_text_na_cislo[i:i+skok]) for i in range(0, len(prevedeny_text_na_cislo), skok)]
    zasifrovany = []
    for m in split_strings:
        zasifrovany.append((int(m)**e)%n)

    return (zasifrovany)

def dekoduj(hodnoty, n, d):

    vsechny_znaky = " abcdefghijklmnopqrstuvwxyzáéíóůúýěčďňřšťž1234567890.,"
    vysledek = ""
    for c in hodnoty:
        #přidávám hodně nul, abych doplnil ty, které se v průběhu konveze str->int ztratí
        vysledek += (str(10000000 + gmpy2.powmod(c, d, n))[2:])
    
    return("".join([vsechny_znaky[kod] for kod in [int(vysledek[int(i):int(i)+2]) for i in range(0, len(vysledek), 2)]]))


    



print(dekoduj([6725706, 2965497, 26082572, 8305383, 23712799, 43609889, 21213230, 10544327, 8212998, 51042532, 21509346, 27850393, 38343783], n, d))