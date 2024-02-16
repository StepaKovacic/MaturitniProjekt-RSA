from generovani_klicu import *
from retezec_na_cisla import *

x = preved_retezec_na_cislo("mám rád brambory a kokolokamotsrvxczhbasesdfvlkasdhjfg asdfgv oasdhfoahakjshdf oiahfoih asodfha josvůojahs v")
print("text převedený na číslo je " + str(x))

n = (Vygeneruj_klice(udelej_velke_prvocislo(), udelej_velke_prvocislo())["verejny_klic"][0])
print("n je " + str(n))

#chci aby čísla byla stále dlouhá 2p čísel
skok = 2 * (int(len(str(n))/2) - 1)

split_strings = [(x[i:i+skok]) for i in range(0, len(x), skok)]
print(split_strings)
print(len(split_strings[0]))
