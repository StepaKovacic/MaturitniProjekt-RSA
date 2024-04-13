# Uživatelská dokumentace k Maturitní práci na téma RSA

## RSA 

RSA je asymetrická šifra, která slouží k zakódování a následknému dekódování zpráv. K tomu slouží dva klíče - veřejný (pro všechny uživatele systému) a soukromý (pouze pro uživatele s oprávněním číst zakódované zprávy).

## Generování klíčů

Aby asymetrická šifra sloužila efektivně, musí být bezpečná. Z principu platí, že soukromý klíč a veřejný klíč na sobě musí být závislé, popřípadě na stejných parametrech (více viz. programátorksá dokumentace). 

Generování klíče zabezpečuje funkce `generovani_klice()` v souboru `utils.py`.
