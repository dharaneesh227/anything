def vigenere_encrypt(plain_text, key):
    plain_text = plain_text.upper()
    key = key.upper()
    encrypted_text = ""
    for i in range(len(plain_text)):
        if plain_text[i].isalpha():
            shift = ord(key[i % len(key)]) - ord('A')
            
            encrypted_char = chr(((ord(plain_text[i]) - ord('A') + shift) % 26) + ord('A'))
            encrypted_text += encrypted_char
        else:            
            encrypted_text += plain_text[i]
    return encrypted_text

def vigenere_decrypt(encrypted_text, key):
    encrypted_text = encrypted_text.upper()
    key = key.upper()
    decrypted_text = ""

    for i in range(len(encrypted_text)):
        if encrypted_text[i].isalpha():
            shift = ord(key[i % len(key)]) - ord('A')
            
            decrypted_char = chr(((ord(encrypted_text[i]) - ord('A') - shift) % 26) + ord('A'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += encrypted_text[i]
    return decrypted_text

key = input("Enter the key: ")
message = input("Enter the message: ")
encrypted_message = vigenere_encrypt(message, key)
print("Encrypted:", encrypted_message)

decrypted_message = vigenere_decrypt(encrypted_message, key)
print("Decrypted:", decrypted_message)
