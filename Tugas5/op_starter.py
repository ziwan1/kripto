import requests

BASE_URL = "http://aes.cryptohack.org/block_cipher_starter"

r = requests.get(f"{BASE_URL}/encrypt_flag") #link cipher text dari website
data = r.json()
ciphertext = data["ciphertext"] #data ciphertext
print("ciphertext", ciphertext)

r = requests.get(f"{BASE_URL}/decrypt/{ciphertext}") #decrypt data ciphertext yang baru saja didapatkan
data = r.json()
plaintext = data["plaintext"]
print("plaintext", plaintext) #data plaintext dalam bentuk hex

print("flag", bytearray.fromhex(plaintext).decode()) #konversi hex ke ASCII
