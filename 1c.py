def generate_key_matrix(key):
    key_matrix = [[0, 0], [0, 0]]
    key_matrix[0][0] = ord(key[0]) - ord('A')
    key_matrix[0][1] = ord(key[1]) - ord('A')
    key_matrix[1][0] = ord(key[2]) - ord('A')
    key_matrix[1][1] = ord(key[3]) - ord('A')
    return key_matrix

def encrypt(plain_text, key_matrix):
    plain_text = plain_text.upper().replace(" ", "")
    if len(plain_text) % 2 != 0:
        plain_text += 'X'

    encrypted_text = ""
    for i in range(0, len(plain_text), 2):
        char1 = ord(plain_text[i]) - ord('A')
        char2 = ord(plain_text[i + 1]) - ord('A')

        result_char1 = (key_matrix[0][0] * char1 + key_matrix[0][1] * char2) % 26
        result_char2 = (key_matrix[1][0] * char1 + key_matrix[1][1] * char2) % 26

        encrypted_text += chr(result_char1 + ord('A')) + chr(result_char2 + ord('A'))

    return encrypted_text

def decrypt(encrypted_text, key_matrix):
    det = key_matrix[0][0] * key_matrix[1][1] - key_matrix[0][1] * key_matrix[1][0]
    det_inverse = 0

    # Find modular multiplicative inverse of the determinant
    for i in range(26):
        if (det * i) % 26 == 1:
            det_inverse = i
            break

    key_matrix_inverse = [[0, 0], [0, 0]]
    key_matrix_inverse[0][0] = (key_matrix[1][1] * det_inverse) % 26
    key_matrix_inverse[0][1] = (-key_matrix[0][1] * det_inverse) % 26
    key_matrix_inverse[1][0] = (-key_matrix[1][0] * det_inverse) % 26
    key_matrix_inverse[1][1] = (key_matrix[0][0] * det_inverse) % 26

    decrypted_text = ""
    for i in range(0, len(encrypted_text), 2):
        char1 = ord(encrypted_text[i]) - ord('A')
        char2 = ord(encrypted_text[i + 1]) - ord('A')

        result_char1 = (key_matrix_inverse[0][0] * char1 + key_matrix_inverse[0][1] * char2) % 26
        result_char2 = (key_matrix_inverse[1][0] * char1 + key_matrix_inverse[1][1] * char2) % 26

        decrypted_text += chr(result_char1 + ord('A')) + chr(result_char2 + ord('A'))

    return decrypted_text

# Example usage
key = input("Enter the key: ")
key_matrix = generate_key_matrix(key)

message = input("Enter the message: ")
encrypted_message = encrypt(message, key_matrix)
print("Encrypted:", encrypted_message)

decrypted_message = decrypt(encrypted_message, key_matrix)
print("Decrypted:", message)
