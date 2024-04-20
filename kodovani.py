from utils import *

vsechny_znaky = znaky()

def enc(text_na_prevod, n, e):
    """
    Funkce zakóduje zprávu pomocí RSA.

    Vstup -> 
        text_na_prevod  - text
        n               - celé číslo (integer)
        e               - celé číslo (integer)

    Výstup -> list celých čísel o délce 6
    """
    rozdeleny_ciselny_retezec = text_na_cisla(text_na_prevod)
    list_zasifrovanych_podretezcu = []
    for clen_ciselneho_rezezce in rozdeleny_ciselny_retezec:
        list_zasifrovanych_podretezcu.append((int(clen_ciselneho_rezezce)**e)%n)
    return list_zasifrovanych_podretezcu

def dec(zakodovany_text, n, d):
    """
    Funkce dekóduje zašifrovanou zprávu pomocí RSA.

    Vstup -> 
        zakodovany_text - list celých čísel o délce 6
        n               - celé číslo (integer)
        d               - celé číslo (integer)

    Výstup -> text
    """
    def _powmod(base, exp, mod):
        if exp == 0:
            return 1
        result = _powmod(base, exp//2, mod)**2
        if exp % 2 == 1:
            result *= base
        return result % mod
    dekodovany_text = ""
    for cast_zakodovaneho_textu in zakodovany_text:
        #přidávám hodně nul, abych doplnil ty, které se v průběhu konveze str->int ztratí
        dekodovany_text += (str(10000000 + _powmod(cast_zakodovaneho_textu, d, n))[2:])
    return cisla_na_text(dekodovany_text)

def _test(zprava, ind):
    klic = generovani_klice()
    x = dec(enc(zprava, klic["verejny_klic"][0], klic["verejny_klic"][1]), klic["soukromy_klic"][0], klic["soukromy_klic"][1])
    bool_knihovna = {True:"úspěšný ✅", False:"neúspěšný ❌"}
    return f"Test zakódovaní a zpětného dekódování číslo {ind} ->  {bool_knihovna[x==zprava]} \n"

if __name__ == "__main__":
    for i in range(10):
        print(_test(vsechny_znaky.replace("#", ""), i+1))
    