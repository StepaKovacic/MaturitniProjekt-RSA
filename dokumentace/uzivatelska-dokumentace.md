# Uživatelská dokumentace k Maturitní práci na téma RSA

## RSA 

RSA je asymetrická šifra, která slouží k zakódování a následknému dekódování zpráv. K tomu slouží dva klíče - veřejný (pro všechny uživatele systému) a soukromý (pouze pro uživatele s oprávněním číst zakódované zprávy).

## Generování klíčů

Z principu platí, že soukromý klíč a veřejný klíč na sobě musí být závislé, popřípadě na stejných parametrech (více viz. programátorksá dokumentace). 

Generování klíče zabezpečuje funkce `generovani_klice()` v souboru `utils.py`. Pro maximální efektivitu a bezpečnost funkce nebere žádný argument (podnět) pro vytvoření klíče. Vše je čistě náhodné. 

### Formát výstupu

funkce `generovani_klice()` vrací slovník (dict) se dvěma šifrovacími klíči ve formátu `{"verejny_klic":(n, e), "soukromy_klic":(n, d) }`. Oba klíče jsou ve formátu uspořádané dvojice (tuple).

## Zakódování zprávy 

Pro zakódování zprávy je potřeba mít `veřejný klíč`. 

Zakódování zprávy zpracuje funkce `enc(text_na_prevod, n, e)` ze souboru `kodovani.py`. Funkce přijímá tři povinné argumenty: 

- `text_na_prevod` - jedná se o zprávu, kterou uživatel chce veřejným klíčem zakódovat. Formát vstupt je řetězec (string) do kterého lze dosadit jen následující znaky ` abcdefghijklmnopqrstuvwxyzáéíóůúýěčďňřšťžABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓŮÚÝĚČĎŇŘŠŤŽ1234567890.,`

- `n` - společná část veřejného i soukromého klíče. Je to první člen uspořádané dvojice parametrů veřejného klíče. Formát vstupu je celé číslo (int)

- `e` - unikátní hodnota obsažena pouze ve veřejném klíči. Je to druhý člen uspořádané dvojice parametrů veřejného klíče. Formát vstupu je celé číslo (int)

### Formát výstupu

Funkce `enc(text_na_prevod, n, e)` vrací zakódovaný text ve formě seznamu (list) celých čísel (int). Délka seznamu závisí na délce vstupního textu. 

## Dekódování zprávy 

Pro dekódování zprávy je potřeba mít skouromý klíš a zprávu zakódovanou odpovídajícím veřejným klíčem.  

Funkce `dec(zakodovany_text, n, d)` dekóduje zprávu, jež byla zakódována funkcí `enc()`. Jsou vyžadovány 3 argumenty:

- `zakodovany_text` - seznam (list) celých čísel (int) představujících zakódovaný text

- `n` - společná část veřejného i soukromého klíče. Je to první člen uspořádané dvojice parametrů soukromého klíče. Formát vstupu je celé číslo (int)

- `d` - unikátní hodnota obsažena pouze v soukromém klíči. Je to druhý člen uspořádané dvojice parametrů soukromého klíče. Formát vstupu je celé číslo (int)


### Formát výstupu

Funkce `dec(zakodovany_text, n, d)` vrací řetězec (str). Délka řetězce závisí na délce vstupu. 

## Příklad 

Následující kód demonstruje použití RSA algoritmu. Nejdříve řetězec `text` zakóduje, dekóduje a pak ověří, že se původní a dekódované hodnoty rovnají. 

```python
# main.py
from kodovani import enc, dec
from utils import generovani_klice

text = """Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Mauris tincidunt sem sed arcu. Aliquam in lorem sit amet leo accumsan lacinia. Vivamus porttitor turpis ac leo. Nullam feugiat, turpis at pulvinar vulputate, erat libero tristique tellus, nec bibendum odio risus sit amet ante. Curabitur bibendum justo non orci. Mauris dolor felis, sagittis at, luctus sed, aliquam non, tellus. Nullam eget nisl. Maecenas libero. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo"""


sada_klicu = generovani_klice()

zakodovany_text = enc(text, *sada_klicu["verejny_klic"])

dekodovany_text = dec(zakodovany_text, *sada_klicu["soukromy_klic"])

print(f"Původní text se shoduje s dekódovaným: {text == dekodovany_text}")
```

Tato ukázka by po spuštění měla mít následující výstup:

```bash 
$ python3 main.py
$ Původní text se shoduje s dekódovaným: True
```
