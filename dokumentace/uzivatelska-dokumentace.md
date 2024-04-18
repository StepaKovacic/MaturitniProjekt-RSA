# Uživatelská dokumentace k Maturitní práci na téma RSA

## RSA 

RSA je asymetrická šifra, která slouží k zakódování a následknému dekódování zpráv. K tomu slouží dva klíče - veřejný (pro všechny uživatele systému) a soukromý (pouze pro uživatele s oprávněním číst zakódované zprávy).

## Generování klíčů

Aby asymetrická šifra sloužila efektivně, musí být bezpečná. Z principu platí, že soukromý klíč a veřejný klíč na sobě musí být závislé, popřípadě na stejných parametrech (více viz. programátorksá dokumentace). 

Generování klíče zabezpečuje funkce `generovani_klice()` v souboru `utils.py`. Pro maximální efektivitu a bezpečnost funkce nebere žádný argument (podnět) pro vytvoření klíče. Vše je čistě náhodné. 

### Formát výstupu

funkce `generovani_klice()` vrací slovník (dictionary) se dvěma šifračními klíči ve formátu `{"verejny_klic":(n, e), "soukromy_klic":(n, d) }`. Separátní klíče jsou ve formátu uspořádané dvojice o dvou konstantách (tuple).

## Zakódování zprávy 

Pro zakódování zprávy je potřeba mít `veřejný klíč`. 

Zakódování zprávy zpracuje funkce `enc(text_na_prevod, n, e)` ze souboru `kodovani.py`. Funkce přijímá tři povinné argumenty: 

- `text_na_prevod` - jedná se o zprávu, kterou uživatel chce veřejným klíčem zakódovat. Formát vstupt je řetězec (string)

- `n` - konstanta, společná část veřejného i soukromého klíče. Je to nultý člen uspořádané dvojice parametrů veřejného klíče. Formát vstupu je celé číslo (integer)

- `e` - unikátní konstanta obsažena pouze ve veřejném klíči. Je to první člen uspořádané dvojice parametrů veřejného klíče. Formát vstupt je celé číslo (integer)

### Formát výstupu

Funkce `enc(text_na_prevod, n, e)` vrací zakódovaný text ve formě listu celých čísel.

## Dekódování zprávy 

Funkce `dec(zakodovany_text, n, d)` je zodpovědná za dekódování zprávy, jež byla zakódována. Jsou vyžadovány 3 argumenty:

- `zakodovany_text` - list celých čísel představujících zakódovaný text

- `n` - konstanta, společná část veřejného i soukromého klíče. Je to nultý člen uspořádané dvojice parametrů soukromého klíče. Formát vstupu je celé číslo (integer)

- `d` - nikátní konstanta obsažena pouze v soukromém klíči. Je to první člen uspořádané dvojice parametrů soukromého klíče. Formát vstupu je celé číslo (integer)


## Příklad 

```python
# main.py
import kodovani
import utils 

text = """Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Mauris tincidunt sem sed arcu. Aliquam in lorem sit amet leo accumsan lacinia. Vivamus porttitor turpis ac leo. Nullam feugiat, turpis at pulvinar vulputate, erat libero tristique tellus, nec bibendum odio risus sit amet ante. Curabitur bibendum justo non orci. Mauris dolor felis, sagittis at, luctus sed, aliquam non, tellus. Nullam eget nisl. Maecenas libero. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo"""


sada_klicu = generovani_klice()

zakodovany_text = enc(text, sada_klicu["verejny_klic"][0], sada_klicu["verejny_klic"][1])

dekodovany_text = dec(zakodovany_text, sada_klicu["soukromy_klic][0], sada_klicu["soukromy_klic"][1])

print(f"Původní text se shoduje s dekódovaným: {text == dekodovany_text}")
```

Tato ukázka by po spuštění měla mít následující výstup:

```bash 
$ python3 main.py
$ Původní text se shoduje s dekódovaným: True
```
