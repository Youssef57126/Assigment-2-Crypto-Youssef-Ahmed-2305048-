ciphertext = "Wklv lv d whvw phvvdjh."

english_freq_order = "etaoinshrdlcumwfgypbvkjxqz"

cipher_freq = {}
for char in ciphertext.lower():
    if char.isalpha():
        cipher_freq[char] = cipher_freq.get(char, 0) + 1

cipher_sorted_letters = []
for letter in cipher_freq:
    inserted = False
    for i in range(len(cipher_sorted_letters)):
        if cipher_freq[letter] > cipher_freq[cipher_sorted_letters[i]]:
            cipher_sorted_letters.insert(i, letter)
            inserted = True
            break
    if not inserted:
        cipher_sorted_letters.append(letter)

possible_key = {}
for i in range(len(cipher_sorted_letters)):
    possible_key[cipher_sorted_letters[i]] = english_freq_order[i]


def decrypt_with_key(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            new_char = key.get(char.lower(), char)
            if char.isupper():
                new_char = new_char.upper()
            plaintext += new_char
        else:
            plaintext += char
    return plaintext


plaintext_guess = decrypt_with_key(ciphertext, possible_key)
print("Decrypted Text (Guess):", plaintext_guess)


def brute_force_decrypt(ciphertext):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    from random import shuffle

    for _ in range(10):
        shuffle(alphabet)  # Properly shuffle the alphabet
        key = {}
        for i in range(len(alphabet)):
            key[chr(97 + i)] = alphabet[i]  # Map a-z to shuffled letters

        decrypted_text = decrypt_with_key(ciphertext, key)
        print("Trying key:", alphabet)
        print("Decrypted Text:", decrypted_text, "\n")


brute_force_decrypt(ciphertext)