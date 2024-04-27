import random
skok = 6

vsechny_znaky = " abcdefghijklmnopqrstuvwxyzáéíóůúýěčďňřšťžABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓŮÚÝĚČĎŇŘŠŤŽ1234567890.,#"

def text_na_cisla(reterez_na_prevod):
    """
    Funkce převede text na list celých čísel
    Vstup -> text, délka celých čísel (skok)
    Výstup -> list řetězců (str) celých čísel o délce "skok"
    """
        
    vata = "#"*skok
    reterez_na_prevod = reterez_na_prevod + vata
    for i in reterez_na_prevod:
        if i not in vsechny_znaky:
            print("toto nelze vykonat, v řetězci se nachází nedovolený znak: " + str(i))
            return
    nerozdeleny_text = ""
    for i in reterez_na_prevod:
        nerozdeleny_text += str(10**2 + (vsechny_znaky.find(i)))[1:]
    rozdeleny_retezec = [(nerozdeleny_text[i:i+skok]) for i in range(0, len(nerozdeleny_text), skok)]
    # print(rozdeleny_retezec)
    return rozdeleny_retezec

def cisla_na_text(cisla_na_prevod):
    """
    Funkce převede list řetězců z celých čísel na text.
    Vstup -> list řetězců (str) o délce skok
    Výstup -> text
    """
    slouceno_dohromady = "".join(cisla_na_prevod)
    rozsekane_na_indexy = [int(slouceno_dohromady[x:x+2]) for x in range(0, len(slouceno_dohromady), 2)]
    retezec_neocisteny = "".join([vsechny_znaky[index_znaku] for index_znaku in rozsekane_na_indexy])
    posledni_hashtag_index = retezec_neocisteny.find("#")
    return retezec_neocisteny[:posledni_hashtag_index]

    
def generovani_klice():
    """
    Funkce generuje slovník klíčů RSA algoritmu.
    Vstup -> žádný 
    Výstup -> ve formátu {"verejny_klic":(n, e), "soukromy_klic":(n, d) }
    """
    def _soudelna(cislo_a, cislo_b):
        delitele_cisla_a = []
        for i in range(1, cislo_a+1):
            if cislo_a%i == 0:
                delitele_cisla_a.append(i)
        #print(delitele_cisla_a)
        for i in delitele_cisla_a:
            if cislo_b%i == 0 and i!=1:
                return True 
        return False

    def _generovani_prvocisla():
        while True:
            x = random.randrange(1000, 10000)
            is_prime = True
            for i in range(2, int(x**0.5) + 1):
                if x % i == 0:
                    is_prime = False
                    break
            if is_prime:
                return x

    prvocislo_p = _generovani_prvocisla()
    prvocislo_q = _generovani_prvocisla()
    while prvocislo_p == prvocislo_q:
        prvocislo_q = _generovani_prvocisla()
    n = prvocislo_p * prvocislo_q
    phi = (prvocislo_p - 1) * (prvocislo_q - 1)
    #zvolíme náhodné e nesoudělné s phi
    while True:
        # vygenerování náhodného čísla e které je nesoudělné s phi
        e = random.randrange(5000, 10000)
        if _soudelna(e, phi) == False:
            break
    d = 1
    while True:
        if (d*e)%phi == 1:
            break
        else: 
            d += 1
    return {"verejny_klic":(n, e), "soukromy_klic":(n, d) }

def _test_text_na_cisla(retezec):
    """
    Test převodu textu na čísla a zpět. 
    Vstup -> Text text
    Výstup -> Boolean
    """
    vystup =  "úspěšný ✅" if retezec == cisla_na_text(text_na_cisla(retezec)) else "neúspěšný ❌"
    print(f"Test prevodu textu na cisla ->  {vystup}")

if __name__ == "__main__":
    _test_text_na_cisla(vsechny_znaky.replace("#", ""))
    
    