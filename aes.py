from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
def url_print(value):
    for i in value:
        print(str(i)+"/",end="")
key=get_random_bytes(16)
print("URL Encryption")
plaintext = input("Enter URL: ").split('/')
n=len(plaintext)
cipher= AES.new(key,AES.MODE_CBC)
ciphertext=cipher.encrypt(pad(plaintext[n-1].encode('utf-8'),AES.block_size))
plaintext[n-1]=ciphertext
print("Encrypted URL: ")
url_print(plaintext)
print("\n")
cipher_decrypt = AES.new(key,AES.MODE_CBC,iv=cipher.iv)
plaintext[n-1]=unpad(cipher_decrypt.decrypt(ciphertext),AES.block_size).decode('utf-8')
print("Decrypted URL: ")
url_print(plaintext)
print("\n")
