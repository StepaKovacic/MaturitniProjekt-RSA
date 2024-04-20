from utils import *

vsechny_znaky = znaky()

def enc(text_na_prevod, n, e):
    skok = 6
    
    rozdeleny_ciselny_retezec = text_na_cisla(text_na_prevod, skok)
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

def test(zprava, ind):
    klic = generovani_klice()
    x = dec(enc(zprava, klic["verejny_klic"][0], klic["verejny_klic"][1]), klic["soukromy_klic"][0], klic["soukromy_klic"][1])
    print(x)
    print(vsechny_znaky)
    bool_knihovna = {True:"úspěšný", False:"neúspěšný"}
    return f"Test {ind} {bool_knihovna[x==zprava]}"

if __name__ == "__main__":
    for i in range(10):
        print(test(vsechny_znaky, i+1))
    
            
            
