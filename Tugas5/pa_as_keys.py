from Crypto.Cipher import AES
import hashlib
import random
import requests
import binascii
import sys

wordlist = requests.get('https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words')
wordlist = wordlist.text
wordlist = wordlist.split('\n')

encrypt_flag = requests.get('http://aes.cryptohack.org/passwords_as_keys/encrypt_flag/')
data = encrypt_flag.json()
ciphertext = data["ciphertext"]
ciphertext = bytes.fromhex(ciphertext) # encode ciphertext

for key in wordlist: # Our key
    print(key)
    key = hashlib.md5(key.encode()).digest() # encode key
    print(key)
    cipher = AES.new(key, AES.MODE_ECB)
    #print(cipher)
    try:
        decrypted = cipher.decrypt(ciphertext) # encode flag
        result = binascii.unhexlify(decrypted.hex())
        print(result)
        if result.startswith('crypto{'.encode()):
            print("key is %s" % key)
            print(result.decode('utf-8'))
            sys.exit(0)
    except ValueError as e:
        continue