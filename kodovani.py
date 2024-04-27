from utils import text_na_cisla, cisla_na_text, generovani_klice, vsechny_znaky, skok



def enc(text_na_prevod, n, e):
    """
    Funkce zakóduje zprávu pomocí RSA.
    Vstup -> 
        text_na_prevod  - text
        n               - celé číslo (integer)
        e               - celé číslo (integer)
    Výstup -> list řetězců obsahujcích 6  (integerů)
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
        """
        Funkce vrací zbytek po dělení exponenciálního výrazu
        Vstup -> 
            base - celé číslo (integer)
            exp  - celé číslo (integer)
            mod  - celé číslo (integer)
        Výstup -> text
        """
        if exp == 0:
            return 1
        result = _powmod(base, exp//2, mod)**2
        if exp % 2 == 1:
            result *= base
        return result % mod
    dekodovany_text = ""
    for cast_zakodovaneho_textu in zakodovany_text:
        #přidávám hodně nul, abych doplnil ty, které se v průběhu konveze str->int ztratí
        dekodovany_text += (str(10**(skok) + _powmod(cast_zakodovaneho_textu, d, n))[1:])
    return cisla_na_text(dekodovany_text)

def _test(zprava, ind):
    klic = generovani_klice()
    # x = dec(enc(zprava, klic["verejny_klic"][0], klic["verejny_klic"][1]), klic["soukromy_klic"][0], klic["soukromy_klic"][1])
    x = dec(enc(zprava, *klic["verejny_klic"]), *klic["soukromy_klic"])
    vystup =  "úspěšný ✅" if x==zprava else "neúspěšný ❌"
    return f"Test zakódovaní a zpětného dekódování číslo {ind} ->  {vystup} \n"

if __name__ == "__main__":
    for i in range(5):
        # print(_test(vsechny_znaky.replace("#", ""), i+1))
        print(_test("gasdogfhasdfh aisdfha skdjfkjjščřěščěščř  ", i+1))
    