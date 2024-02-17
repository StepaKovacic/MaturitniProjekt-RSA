import random
def vytvor_klic():
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
    return Vygeneruj_klice(udelej_velke_prvocislo(), udelej_velke_prvocislo())


print(vytvor_klic())