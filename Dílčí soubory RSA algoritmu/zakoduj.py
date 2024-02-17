import re
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

    x = preved_retezec_na_cislo(text_na_prevod)

    skok = 2 * (int(len(str(n))/2) - 1)

    split_strings = [(x[i:i+skok]) for i in range(0, len(x), skok)]
        



    zasifrovany = []
    for m in split_strings:
        zasifrovany.append((int(m)**e)%n)


        
    return (zasifrovany)

print(zakoduj("šla babička do koše a dala si langoše", 46683839, 3323))