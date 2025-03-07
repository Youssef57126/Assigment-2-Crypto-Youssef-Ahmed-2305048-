
english_freq = {
    'E': 12.7, 'T': 9.1, 'A': 8.2, 'O': 7.5, 'I': 7.0,
    'N': 6.7, 'S': 6.3, 'H': 6.1, 'R': 5.9, 'D': 4.3,
    'L': 4.0, 'C': 3.4, 'U': 3.0, 'M': 2.9, 'W': 2.4,
    'F': 2.2, 'G': 2.0, 'Y': 1.9, 'P': 1.9, 'B': 1.5,
    'V': 1.0, 'K': 0.8, 'J': 0.2, 'X': 0.2, 'Q': 0.1, 'Z': 0.1
}


def frequency_analysis(ciphertext):
    letter_counts = {}
    for char in ciphertext.upper():
        if char.isalpha():
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1

    sorted_letters = sorted(letter_counts, key=letter_counts.get, reverse=True)
    return sorted_letters


def decrypt_monoalphabetic(ciphertext):
    sorted_cipher_letters = frequency_analysis(ciphertext)
    sorted_english_letters = sorted(english_freq, key=english_freq.get, reverse=True)

    decryption_map = {}
    for i in range(len(sorted_cipher_letters)):
        if i < len(sorted_english_letters):
            decryption_map[sorted_cipher_letters[i]] = sorted_english_letters[i]

    decrypted_text = ""
    for char in ciphertext.upper():
        decrypted_text += decryption_map.get(char, char)

    return decrypted_text.lower()

encrypted_text = "JLAP FJHERFJL OFE"
decrypted_text = decrypt_monoalphabetic(encrypted_text)
print("Decrypted Text:", decrypted_text)