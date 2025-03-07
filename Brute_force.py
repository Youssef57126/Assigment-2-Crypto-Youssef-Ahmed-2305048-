def brute_force_monoalphabetic(ciphertext):
    ciphertext = ciphertext.upper()

    print("Brute Force Decryption Results:")
    print("_" * 30)

    for shift in range(26):
        plaintext = ""

        for char in ciphertext:
            if char.isalpha():
                char_num = ord(char) - ord('A')
                shifted_num = (char_num - shift) % 26
                plaintext += chr(shifted_num + ord('A'))
            else:
                plaintext += char

        print(f"Shift {shift:2d}: {plaintext}")

ciphertext = input("Enter the encrypted message: ")

brute_force_monoalphabetic(ciphertext)

