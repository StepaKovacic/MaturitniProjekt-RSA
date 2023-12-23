# Maturitní projekt na téma RSA šifry

## Hlavní myšlenka 
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


## Nápady
