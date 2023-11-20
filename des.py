from collections.abc import ByteString
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad

key = b"academic"
cipher = DES.new(key,DES. MODE_CBC)
f = open("in.txt", "r")
text =(f.read())
f.close()
plaintext = bytes(text,'utf-8')
ciphertext=cipher.encrypt (pad(plaintext, DES.block_size))
print(ciphertext)
f =open("out.txt", "w")
f.write(str(ciphertext))
f.close()
cipher_decrypt =DES.new(key, DES. MODE_CBC, iv=cipher.iv)
print(unpad (cipher_decrypt.decrypt (ciphertext),DES.block_size).decode('utf-8'))

