#coding:utf-8

import hashlib 
import sys

c = 0
passwordHash = str(sys.argv[1]) # commande : python main.py [hash_md5]
attempt = 0 
try:
    passwordFile = open("wordlist.txt", "r") # ouvrir wordlist.txt en mode "read only"
    print("[!] Reading wordlist.txt")
except:
    print("[!] File Not Found! ")
    quit()
    
for word in passwordFile:
    encodedWord = word.encode('utf-8') # encoder en UTF-8
    digest = hashlib.md5(encodedWord.strip()).hexdigest() # hexadecimal
    print("{}\n{}\n{}".format(word, digest, passwordHash)) # line non-obligatoire
    attempt += 1
    if digest == passwordHash:
        print("[!] Password found!\n[*] Password: {} | Attempts: {}".format(word,attempt))
        c = 1
        break
    
if c == 0:
    print("[!] Password Not Found!")


    
