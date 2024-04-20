import random

def znaky():
    """
    Funkce vrací " abcdefghijklmnopqrstuvwxyzáéíóůúýěčďňřšťžABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓŮÚÝĚČĎŇŘŠŤŽ1234567890.,"
    """
    return  " abcdefghijklmnopqrstuvwxyzáéíóůúýěčďňřšťžABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓŮÚÝĚČĎŇŘŠŤŽ1234567890.,"

vsechny_znaky = znaky()

def text_na_cisla(reterez_na_prevod, skok):
        """
        Funkce převede text na list celých čísel

        Vstup -> text, délka celých čísel (skok)

        Výstup -> list celých čísel o délce "skok"
        """
        global vsechny_znaky
        

        for i in reterez_na_prevod:
            if i not in vsechny_znaky:
                print("toto nelze vykonat, v řetězci se nachází nedovolený znak: " + str(i))
                return
        nerozdeleny_text = ""

        for i in reterez_na_prevod:
            nerozdeleny_text += str(100 + (vsechny_znaky.find(i)))[1:]
            
        rozdeleny_retezec = [(nerozdeleny_text[i:i+skok]) for i in range(0, len(nerozdeleny_text), skok)]
        return rozdeleny_retezec

def cisla_na_text(cisla_na_prevod):
    """
    Funkce převede list celých čísel na text.

    Vstup -> list celých čísel (integerů)

    Výstup -> text
    """
    return("".join([vsechny_znaky[kod] for kod in [int(cisla_na_prevod[int(i):int(i)+2]) for i in range(0, len(cisla_na_prevod), 2)]]))

def generovani_klice():
    """
    Funkce generuje slovník klíčů RSA algoritmu.

    Vstup -> žádný 
    
    Výstup -> ve formátu {"verejny_klic":(n, e), "soukromy_klic":(n, d) }
    """
    def soudelna(cislo_a, cislo_b):
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

    prvocislo_p = udelej_velke_prvocislo()
    prvocislo_q = udelej_velke_prvocislo()

    n = prvocislo_p * prvocislo_q
    #Eulerova funkce 
    phi = (prvocislo_p - 1) * (prvocislo_q - 1)

    #zvolíme náhodné e nesoudělné s phi
    while True:
        # vygenerování náhodného čísla e které je nesoudělné s phi
        e = random.randrange(1000, 10000)
        if soudelna(e, phi) == False:
            break
        
    d = 1
    while True:
        if (d*e)%phi == 1:
            break
        else: 
            d += 1
    return {"verejny_klic":(n, e), "soukromy_klic":(n, d) }


def test_text_na_cisla(retezec):
    """
    Test převodu textu na čísla a zpět. 

    Vstup -> Testovací text

    Výstup -> Úspěšnost testu (True/False)
    """
    return f"Test -> text na cisla funguje : {retezec == cisla_na_text(text_na_cisla(retezec))}"




if __name__ == "__main__":
    help(generovani_klice)
    help(cisla_na_text)
    print(generovani_klice())
    print(test_text_na_cisla(vsechny_znaky))
    

