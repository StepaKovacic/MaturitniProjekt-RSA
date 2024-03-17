from utils import *
import re
import gmpy2

vsechny_znaky = " abcdefghijklmnopqrstuvwxyzáéíóůúýěčďňřšťž1234567890.,"

def enc(text_na_prevod, n, e):
    cisly_vyjadreny_text = text_na_cisla(text_na_prevod)

    # skok = 2 * (int(len(str(n))/2) - 1)
    # minimalni delka n je 7 a skok musi byt mensi nez n
    skok = 6

    rozdeleny_ciselny_retezec = [(cisly_vyjadreny_text[i:i+skok]) for i in range(0, len(cisly_vyjadreny_text), skok)]
    # print(rozdeleny_ciselny_retezec) tohle asi nepotrebuju
    # jen je videt ze posledni retezec je nejkratsi
    zasifrovany = []
    for clen_ciselneho_rezezce in rozdeleny_ciselny_retezec:
        zasifrovany.append((int(clen_ciselneho_rezezce)**e)%n)

    return zasifrovany

def dec(zakodovany_text, n, d):
    dekodovany_text = ""

    for cast_zakodovaneho_textu in zakodovany_text:
        #přidávám hodně nul, abych doplnil ty, které se v průběhu konveze str->int ztratí
        # dekodovany_text += (str(10000000 + gmpy2.powmod(cast_zakodovaneho_textu, d, n))[2:])
        dekodovany_text += (str(10000000 + gmpy2.powmod(cast_zakodovaneho_textu, d, n))[2:])
        #tech nul se tam prida asi az moc
    
    return("".join([vsechny_znaky[kod] for kod in [int(dekodovany_text[int(i):int(i)+2]) for i in range(0, len(dekodovany_text), 2)]]))
    print(dekodovany_text)


def test(zprava):
    # print(zprava)
    red_zprava = zprava
    vata = "kkkkkk"
    zprava = zprava + vata
    klic = generovani_klice()
    # print(zprava == dec(enc(zprava, klic["verejny_klic"][0], klic["verejny_klic"][1]), klic["soukromy_klic"][0], klic["soukromy_klic"][1]).replace("      ", ""))
    # print(dec(enc(zprava, klic["verejny_klic"][0], klic["verejny_klic"][1]), klic["soukromy_klic"][0], klic["soukromy_klic"][1]).replace("dddddd", "") in zprava)
    x = dec(enc(zprava, klic["verejny_klic"][0], klic["verejny_klic"][1]), klic["soukromy_klic"][0], klic["soukromy_klic"][1])
    # print(re.sub(x, "", zprava))
    
    string = list(x[::-1])
    
    for index, item in enumerate(string):
        y = len(vata)
        
        if len(vata)>0:
            
            if item in vata:
                vata = vata.replace(item, "", 1)
            string[index] = ""
        else: 
            break
        
    print("".join(string)[::-1])
    print("shoduje se původní zpráva s dekodovanou:" +  str("".join(string)[::-1] == red_zprava) )

    # print()
    # print(str(re.sub(vata, "", x ))[::-1], re.sub(vata, "", zprava))
    # print("----")
    # print(dec(enc(zprava, klic["verejny_klic"][0], klic["verejny_klic"][1]), klic["soukromy_klic"][0], klic["soukromy_klic"][1]))



if __name__ == "__main__":
    for i in range(10):
        test("asjdf oiqwhedof hasdoifh oqwadhcdsahoei fhcoyxhcoiiewqh ofihcaohxc oweqhdfo haxocheqwoihd oajsnc oqwe d")