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

Soubor `utils.py` obsahuje nástroje a proměné využívané v souboru `kodovani.py`. Jedná se o funkci generující sadu RSA klíčů, funkci, která konvertuje text na čísla a funkci, která konvertuje čísla na text. Dále se v souboru nachází funkce testující konvertování.  

### Všechny znaky 

Řetězec `vsechny_znaky` obsahuje všechny znaky v jednotném pořadí (kvůli indexům), které se v průběhu kódování a dekódování používají. Slouží jak při konvertování čísel na text tak při konvertování textu na čísla. Proměnou lze přepsat, pokud je potřeba změnit povolené znaky, musí však zůstat maximální délka 98 znaků. 

### Skok

Hodnota `skok=6` je odvozená od hodnoty `n`. Slouží k tomu, aby rozdělovala 

Musí platit, že $$ n \in [1000^2; 10000^2] \land n \in Z$$






### Text na čísla 

funkce `text_na_cisla` převád


## Kódování

Všechny funkce které slouží k zakódování a dekódování se nachází v souboru `kodovani.py`. Jedná o funkce:

### Encode (enc)

Funkce `enc()` využívá rovnici 
$$ m = c^e \mod n$$
kde `c` je původní zpráva a `n` a `e` jsou součásti veřejného klíče. Výsledné `m` je zašifrovaná zpráva. 


### Decode (dec)




