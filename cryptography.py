# cryptography.py

def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.isupper():
                encrypted_text += chr((shifted - 65) % 26 + 65)
            else:
                encrypted_text += chr((shifted - 97) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def playfair_encrypt(text, key):
    text = text.upper().replace("J", "I")  # Convert to uppercase and replace 'J' with 'I'
    text = "".join(char if char.isalpha() else "" for char in text)  # Remove non-alphabetic characters
    pairs = [(text[i], text[i + 1] if i + 1 < len(text) else 'X') for i in range(0, len(text), 2)]

    key_matrix = [[0] * 5 for _ in range(5)]
    key += "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    # Populate key matrix
    for i in range(5):
        for j in range(5):
            key_matrix[i][j] = key[i * 5 + j]

    encrypted_text = ""
    for pair in pairs:
        row1, col1 = divmod(key.index(pair[0]), 5)
        row2, col2 = divmod(key.index(pair[1]), 5)

        if row1 == row2:
            encrypted_text += key_matrix[row1][(col1 + 1) % 5] + key_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted_text += key_matrix[(row1 + 1) % 5][col1] + key_matrix[(row2 + 1) % 5][col2]
        else:
            encrypted_text += key_matrix[row1][col2] + key_matrix[row2][col1]

    return encrypted_text

def playfair_decrypt(text, key):
    text = text.upper().replace("J", "I")  # Convert to uppercase and replace 'J' with 'I'
    text = "".join(char if char.isalpha() else "" for char in text)  # Remove non-alphabetic characters
    pairs = [(text[i], text[i + 1] if i + 1 < len(text) else 'X') for i in range(0, len(text), 2)]

    key_matrix = [[0] * 5 for _ in range(5)]
    key += "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    # Populate key matrix
    for i in range(5):
        for j in range(5):
            key_matrix[i][j] = key[i * 5 + j]

    decrypted_text = ""
    for pair in pairs:
        row1, col1 = divmod(key.index(pair[0]), 5)
        row2, col2 = divmod(key.index(pair[1]), 5)

        if row1 == row2:
            decrypted_text += key_matrix[row1][(col1 - 1) % 5] + key_matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            decrypted_text += key_matrix[(row1 - 1) % 5][col1] + key_matrix[(row2 - 1) % 5][col2]
        else:
            decrypted_text += key_matrix[row1][col2] + key_matrix[row2][col1]

    return decrypted_text

def monoalphabetic_encrypt(text):
    key = "QWERTYUIOPASDFGHJKLZXCVBNM"
    mapping = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", key))
    encrypted_text = "".join(mapping.get(char, char) for char in text.upper())
    return encrypted_text

def monoalphabetic_decrypt(text):
    key = "QWERTYUIOPASDFGHJKLZXCVBNM"
    mapping = dict(zip(key, "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    decrypted_text = "".join(mapping.get(char, char) for char in text.upper())
    return decrypted_text
