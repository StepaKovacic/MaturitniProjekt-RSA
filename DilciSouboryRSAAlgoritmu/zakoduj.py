import re

vsechny_znaky = " abcdefghijklmnopqrstuvwxyzáéíóůúýěčďňřšťž1234567890.,"

def zakoduj(text_na_prevod, n, e):
    def preved_retezec_na_cislo(reterez_na_prevod):
        global vsechny_znaky
        reterez_na_prevod = reterez_na_prevod.lower()
        

        for i in reterez_na_prevod:
            if i not in vsechny_znaky:
                print("toto nelze vykonat, v řetězci se nachází nedovolený znak: " + str(i))
                return
        vysledek = ""

        for i in reterez_na_prevod:
            vysledek += str(100 + (re.search(i, vsechny_znaky).start()))[1:]
            
        return(vysledek)

    x = preved_retezec_na_cislo(text_na_prevod)
    print(x)

    skok = 2 * (int(len(str(n))/2) - 1)

    split_strings = [(x[i:i+skok]) for i in range(0, len(x), skok)]
        



    zasifrovany = []
    for m in split_strings:
        zasifrovany.append((int(m)**e)%n)

    return zasifrovany

print(zakoduj("šla babička do koše a dala si langoše", 58772303, 6943))

v = "39120100020102093511010004150011153905000100040112010019090012011407153905"

def test():
    return [v[i:i+2] for i in range(0, len(v), 2)]
print(test())
print([vsechny_znaky[int(i)] for i in test()])


"""
Poznámka : převod na textu na čísla funguje skvěle a bez problému
"""