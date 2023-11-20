def create_playfair_matrix(key):
    # Create a 5x5 matrix filled with zeros
    matrix = [['' for _ in range(5)] for _ in range(5)]
    key = key.replace('J', 'I')  # Replace J with I in the key

    # Initialize variables for tracking used characters and the current row and column
    used_chars = set()
    row, col = 0, 0

    # Fill the matrix with the key
    for char in key + 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if char not in used_chars:
            matrix[row][col] = char
            used_chars.add(char)
            col += 1
            if col == 5:
                col = 0
                row += 1

    return matrix

def prepare_message(message):
    message = message.upper().replace('J', 'I')
    # Remove non-alphabet characters and split into pairs of characters
    pairs = [message[i:i + 2] for i in range(0, len(message), 2)]
    # Add a placeholder 'X' to the end if the last pair has only one character
    if len(pairs[-1]) == 1:
        pairs[-1] += 'X'
    return pairs

def encrypt_playfair(message, key):
    matrix = create_playfair_matrix(key)
    prepared_message = prepare_message(message)
    encrypted_message = ''

    for pair in prepared_message:
        a, b = pair[0], pair[1]
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)

        if row_a == row_b:
            encrypted_message += matrix[row_a][(col_a + 1) % 5] + matrix[row_b][(col_b + 1) % 5]
        elif col_a == col_b:
            encrypted_message += matrix[(row_a + 1) % 5][col_a] + matrix[(row_b + 1) % 5][col_b]
        else:
            encrypted_message += matrix[row_a][col_b] + matrix[row_b][col_a]

    return encrypted_message

def decrypt_playfair(encrypted_message, key):
    matrix = create_playfair_matrix(key)
    prepared_message = prepare_message(encrypted_message)
    decrypted_message = ''

    for pair in prepared_message:
        a, b = pair[0], pair[1]
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)

        if row_a == row_b:
            decrypted_message += matrix[row_a][(col_a - 1) % 5] + matrix[row_b][(col_b - 1) % 5]
        elif col_a == col_b:
            decrypted_message += matrix[(row_a - 1) % 5][col_a] + matrix[(row_b - 1) % 5][col_b]
        else:
            decrypted_message += matrix[row_a][col_b] + matrix[row_b][col_a]

    return decrypted_message

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col

# Example usage
key = input("Enter the key word: ")
message = input("Enter The message: ")
encrypted_message = encrypt_playfair(message, key)
print("Encrypted:", encrypted_message)

decrypted_message = decrypt_playfair(encrypted_message, key)
print("Decrypted:", decrypted_message)
