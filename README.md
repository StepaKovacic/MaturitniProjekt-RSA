# Maturitní projekt na téma RSA šifry

## Hlavní myšlenka 
Projekt by mohl sloužit jako python modul
```python
import rsa 

def encrypt(key, message_file, output_file):
	f = open("message_file", "r")
	output = rsa.encrypt(f)
	r = open("output_file", "w")

def decrypt(key, encrypted_file, output_file):
	f = open("encrypted_file", "r")
	output = rsa.decrypt(f)
	r = open("output_file", "w")
```
nebo jako konzolová aplikace 
```bash
#zakódování souboru unencripted.txt na message.txt veřejným klíčem rsa.key 
rsa.encrypt.py --message unencripted.txt --o message.txt --pubkey rsa.key

#dekódování soubor message.txt na output.txt soukromým klíčem rsa.key.pub
rsa.decrypt.py --message message.txt  --o output.txt --privkey rsa.key.pub
```

## Nápady
