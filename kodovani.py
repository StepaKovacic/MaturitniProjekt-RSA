from utils import *

#chci retezec uchovat v ramci kodu jen na jednom miste
vsechny_znaky = znaky()

def enc(text_na_prevod, n, e):
    cisly_vyjadreny_text = text_na_cisla(text_na_prevod)

    skok = 6

    rozdeleny_ciselny_retezec = [(cisly_vyjadreny_text[i:i+skok]) for i in range(0, len(cisly_vyjadreny_text), skok)]

    list_zasifrovanych_substringu = []
    for clen_ciselneho_rezezce in rozdeleny_ciselny_retezec:
        list_zasifrovanych_substringu.append((int(clen_ciselneho_rezezce)**e)%n)

    return list_zasifrovanych_substringu

def dec(zakodovany_text, n, d):
    def powmod(base, exp, mod):
        if exp == 0:
            return 1
        result = powmod(base, exp//2, mod)**2
        if exp % 2 == 1:
            result *= base
        return result % mod
    dekodovany_text = ""

    for cast_zakodovaneho_textu in zakodovany_text:
        #přidávám hodně nul, abych doplnil ty, které se v průběhu konveze str->int ztratí
        dekodovany_text += (str(10000000 + powmod(cast_zakodovaneho_textu, d, n))[2:])

    return cisla_na_text(dekodovany_text)


def test(zprava):
    red_zprava = zprava
    vata = "kkkkkk"
    zprava = zprava + vata
    klic = generovani_klice()
    x = dec(enc(zprava, klic["verejny_klic"][0], klic["verejny_klic"][1]), klic["soukromy_klic"][0], klic["soukromy_klic"][1])
    
    string = list(x[::-1])
    
    for index, item in enumerate(string):
        y = len(vata)
        
        if len(vata)>0:
            
            if item in vata:
                vata = vata.replace(item, "", 1)
            string[index] = ""
        else: 
            break
        
    return str("".join(string)[::-1] == red_zprava) 

if __name__ == "__main__":

    test_usepch_bool = True
    for i in range(10):
        if test(vsechny_znaky) == False:
            test_usepch_bool = False
            break
    print("Byl test úspěšný? " + str(test_usepch_bool).upper())
            
            
