def prepare_text(text):
    text = ''.join(filter(str.isalpha, text)).upper().replace('J', 'I')
    prepared_text = ''
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else 'X'
        if a == b:
            prepared_text += a + 'X'
            i += 1
        else:
            prepared_text += a + b
            i += 2
    return prepared_text


def create_matrix(keyword):
    keyword = ''.join(filter(str.isalpha, keyword)).upper().replace('J', 'I')
    seen = set()
    matrix = []
    for char in keyword + 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if char not in seen:
            seen.add(char)
            matrix.append(char)
    return [matrix[i:i + 5] for i in range(0, 25, 5)]


def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    raise ValueError(f"Character {char} not found in matrix")


def playfair_cipher(text, matrix, mode='encrypt'):
    processed_text = ''
    text = prepare_text(text)
    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)
        if row_a == row_b:
            col_a = (col_a + 1) % 5 if mode == 'encrypt' else (col_a - 1) % 5
            col_b = (col_b + 1) % 5 if mode == 'encrypt' else (col_b - 1) % 5
        elif col_a == col_b:
            row_a = (row_a + 1) % 5 if mode == 'encrypt' else (row_a - 1) % 5
            row_b = (row_b + 1) % 5 if mode == 'encrypt' else (row_b - 1) % 5
        else:
            col_a, col_b = col_b, col_a
        processed_text += matrix[row_a][col_a] + matrix[row_b][col_b]
    return processed_text



keyword = input("Enter keyword: ")
matrix = create_matrix(keyword)
print("Playfair Matrix:")
for row in matrix:
    print(' '.join(row))

choice = input("Do you want to encrypt or decrypt? (e/d): ")
text = input("Enter text: ")
try:
    result = playfair_cipher(text, matrix, mode='encrypt' if choice == 'e' else 'decrypt')
    print("Result:", result)
except ValueError as e:
    print("Error:", e)








