# Programátorská dokumentace k Maturitní práci na téma RSA

## Úvod
Maturitní práce na téma RSA je python kód, který využívá RSA algoritmu k zakódování a dekódovaní textu. 

Jediná knihovna použitá v kódu je `random`. 

Kód není vhodný na implementaci v projektech, kvůli velké časové komplexitě, která je zapříčeněná malou efektivitou některch funkcí, jako například `_generovani_prvocisla()`. Tato funkce by šla nahradit Eratosthenovým sítem, z důvodu edukativního cíle práce není použita. 

## Rozdělení
Soubory k programu Maturitní príce na téma RSA jsou rozděleny do dvou soborů: 

- `kodovani.py`
- `utils.py`

Soubor `utils.py` slouží jako pomocný soubor ke `kodovani.py` do kterého se importují jeho funkce a jeho výzhnam je pouze pro přehlednost. 

## Utils 

Soubor `utils.py` obsahuje nástroje a proměné využívané v souboru `kodovani.py`. Jedná se o funkci generující sadu RSA klíčů, funkci, která konvertuje text na čísla a funkci, která konvertuje čísla na text, seznam všech možných znaků a konstantu skok. Dále se v souboru nachází funkce testující konvertování.  

### Všechny znaky 

Řetězec `vsechny_znaky` obsahuje všechny znaky v jednotném pořadí (kvůli indexům), které se v průběhu kódování a dekódování používají. Slouží jak při konvertování čísel na text tak při konvertování textu na čísla. Proměnou lze přepsat, pokud je potřeba změnit povolené znaky, musí však zůstat maximální délka 100 znaků. 

### Text na čísla 

funkce `text_na_cisla` převede text na čísla. Funguje na principu, že každý znak, který lze kódovat a dekódovat se nachází v řetězci `vsechny_znaky`, jež se nemění. 

Každý znak se v řetězci vyskytuje pouze jednou a jeho index je jedinečný. problém je v tom, že prvních 10 znaků má jednociferný index a indexy se ukládají jako dvouciferná čísla, proto je potřeba ukládat jeho hodnotu jako string ve formátu (pro příklad znaku `c`) `"03"`. Pro to se využívá `str(10**2+index)[1:]` 

tímto způsobem přeloží funkce text na čísla a vznikne jeden dlouhý řetězec. V některých případech se však může stát, že řetězec bude tak dlouhý, že nebude možné s ním provádět aritmetiku požadovanou RSA. Z toho důvodu je potřeba řetězec rozdělit, přičemž velikost zprávy jež bude zakódována musí být menší než `n`. 

#### Skok

Hodnota `skok=6` je odvozená od hodnoty `n`. Slouží k tomu, aby rozdělovala zmíněný přeložený řetězec.

Musí platit, že 
```math
n \in [1000^2; 10000^2] \land n \in Z
```

jelikož `preložený řetězec < n` a minimální hodnota `n` je 10^6 postačí aby řetězce byly dlouhé maximálně 6 jelikož nikdy nenabydou hodnoty 10^6 a více. 

#### Vata

Vata je série stejných znaků, přesněji `#` které nelze použít ve zprávě. Jedná se o speciální znak používaný v kontrolování správného množství mezer, kterým odpovídá číslo `"00"`. Všechny položky v listu mají délku skok, ale může se stát, že poslední člen listu bude mít méně než `skok` znaků. tímto se zajistí, že poslední znaky budou na správném místě a `#` se budou ignorovat.


### Čísla na text 

Funkce sloučí list stupu, který obsahuje řetězce s čísly. Následně každé dvojčíslí použije jako index v řetězci `vsechny_znaky` a na závěr odstraní výplňové znaky `#`. 

### Generování klíče

Funkce generuje dictionary s klíči `soukromy_klic` a `verejny_klic`. Uvnitř funkce `generovani_klice` se nachází několik dalších funkcí, použitých interně. 

při hledání čísla `e` je požadováno, aby se nejednalo o prvočíslo. Z matematického hlediska může být, není to však nutné.



## Kódování

Všechny funkce které slouží k zakódování a dekódování se nachází v souboru `kodovani.py`. Jedná o funkce:

### Encode (enc)

Funkce `enc()` využívá k zakódování rovnici 
```math
c = m^e \mod n
```
kde `m` je původní zpráva a `n` a `e` jsou součásti veřejného klíče. Výsledné `c` je zašifrovaná zpráva. 


### Decode (dec)

funcke `dec` dekóduje pomocí rovnice 
```math
 m = c^d \mod n 
 ```

pro neztrácení dat byla doposavaď data skladována jako string nikoliv jako int, jelikož nuly na začátku by byly ztraceny. nyní po dekódování je potřeba doplnic výsledné položky listu na délku skok. k tomu se použije `str(10**(skok) + cislo_s_nedostatecnou_delkou)[1:]`
