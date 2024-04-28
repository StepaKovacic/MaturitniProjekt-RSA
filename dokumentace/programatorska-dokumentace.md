# Programátorská dokumentace k Maturitní práci na téma RSA

## Úvod
Maturitní práce na téma RSA je python kód, který využívá RSA algoritmu k zakódování a dekódovaní textu. 

Jediná knihovna použitá v kódu je `random`. 

Kód není vhodný na implementaci v projektech, kvůli velké časové komplexitě, která je zapříčeněná malou efektivitou některch funkcí, jako například `_generovani_prvocisla()`. Tato funkce by šla nahradit Eratosthenovým sítem, z důvodu edukativního cíle práce však není použita. 

## Rozdělení
Program Maturitní príce na téma RSA je rozdělen do dvou soborů: 

- `kodovani.py`
- `utils.py`

Soubor `utils.py` slouží jako pomocný soubor k souboru `kodovani.py` do kterého se importují jeho funkce a jeho výnam je pouze pro přehlednost. 

## Utils 

Soubor `utils.py` obsahuje nástroje a proměnné využívané v souboru `kodovani.py`. Jedná se o funkci generující sadu RSA klíčů; funkci, která konvertuje text na čísla; funkci, která konvertuje čísla na text; seznam všech možných znaků a konstantu skok. Dále se v souboru nachází funkce testující konvertování.  

### Všechny znaky 

Řetězec `vsechny_znaky` obsahuje všechny znaky v jednotném pořadí (kvůli indexům), které se v průběhu kódování a dekódování používají. Slouží jak při konvertování čísel na text, tak při konvertování textu na čísla. Proměnou lze přepsat, pokud je potřeba změnit povolené znaky, musí však zůstat maximální délka 100 znaků. 

### Text na čísla 

Funkce `text_na_cisla` převede text na čísla. Funguje na principu, že každý znak, který lze kódovat a dekódovat se nachází v řetězci `vsechny_znaky`, jež se nemění. 

Každý znak se v řetězci vyskytuje pouze jednou a jeho index je jedinečný. Prvních 10 znaků má jednociferný index a indexy se ukládají jako dvouciferná čísla, proto je potřeba ukládat jeho hodnotu jako string ve formátu (pro příklad znaku `c`) `"03"`. Pro to se využívá `str(10**2+index)[1:]` 

Tímto způsobem přeloží funkce text na čísla a vznikne jeden dlouhý řetězec. V některých případech se však může stát, že řetězec bude tak dlouhý, že nebude možné s ním provádět aritmetiku požadovanou RSA. Z toho důvodu je potřeba řetězec rozdělit, přičemž velikost zprávy, jež bude zakódována musí být menší než `n`. 

#### Skok

Hodnota `skok=6` je odvozená od hodnoty `n`. Slouží k tomu, aby určovala délku rozdělení  zmíněného přeloženého řetězce.

Musí platit, že 
```math
n \in [1000^2; 10000^2] \land n \in Z
```

jelikož `preložený řetězec < n` a minimální hodnota `n` je 10^6 postačí, aby řetězce byly dlouhé maximálně 6, jelikož nikdy nenabydou hodnoty 10^6 a více. 

#### Vata

Vata je série stejných znaků `#`, které se nesmí použít ve zprávě. Jedná se o speciální znak používaný v kontrolování správného množství mezer, kterým odpovídá číslo `"00"`. Všechny položky v listu mají délku skok, ale může se stát, že poslední člen listu bude mít méně než `skok` znaků. Tímto se zajistí, že poslední znaky budou na správném místě a `#` se budou ignorovat.


### Čísla na text 

Funkce sloučí list vstupu, který obsahuje řetězce s čísly. Následně každé dvojčíslí použije jako index v řetězci `vsechny_znaky` a na závěr odstraní výplňové znaky `#`. 

### Generování klíče

Funkce generuje dictionary s klíči `soukromy_klic` a `verejny_klic`. Uvnitř funkce `generovani_klice` se nachází několik dalších funkcí, použitých interně. 

## Kódování

Všechny funkce které slouží k zakódování a dekódování se nachází v souboru `kodovani.py`. Jedná se o funkce:

### Encode (enc)

Funkce `enc` využívá k zakódování rovnici 
```math
c = m^e \mod n
```
kde `m` je původní zpráva a `n` a `e` jsou součásti veřejného klíče. Výsledné `c` je zašifrovaná zpráva. 


### Decode (dec)

funcke `dec` dekóduje pomocí rovnice 
```math
 m = c^d \mod n 
 ```

Pro neztrácení dat byla doposavaď data skladována jako string nikoliv jako int, jelikož nuly na začátku by byly ztraceny. nyní po dekódování je potřeba doplnic výsledné položky listu na délku skok. k tomu se použije `str(10**(skok) + cislo_s_nedostatecnou_delkou)[1:]`


## Zdroje 
+ [https://cs.wikipedia.org/wiki/RSA](https://cs.wikipedia.org/wiki/RSA)

+ [https://en.wikipedia.org/wiki/RSA_(cryptosystem)](https://en.wikipedia.org/wiki/RSA_(cryptosystem))

+ [https://stackoverflow.com/questions/9475241/split-string-every-nth-character](https://stackoverflow.com/questions/9475241/split-string-every-nth-character)

+ [https://www.w3schools.com/python/default.asp](https://www.w3schools.com/python/default.asp)

+ Konzultace s vedoucím práce Mgr. Adamem Domincem

+ Konzultace s Lukášem Novákem
