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
- `n` - konstanta, společná část veřejného i soukromého klíče. Je to nultý člen uspořádané dvojice parametrů veřejného klíče. 
- `e` - unikátní konstanta obsažena pouze ve veřejném klíči. Je to první člen uspořádané dvojice parametrů veřejného klíče. 


