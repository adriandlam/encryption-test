import random
import string

ALPHA = string.ascii_letters


def make_cipher_alpha(key):
    shuffled = list(ALPHA)
    random.seed(key)
    random.shuffle(shuffled)
    return shuffled


def encrypt(message, key):
    cipher_alpha = make_cipher_alpha(key)
    cipher = ""

    for c in message:
        if c in ALPHA:
            cipher += cipher_alpha[ALPHA.index(c)]
        else:
            cipher += c

    return cipher


def decrypt(cipher, key):
    cipher_alpha = make_cipher_alpha(key)
    m = ""

    for c in cipher:
        if c in cipher_alpha:
            m += ALPHA[cipher_alpha.index(c)]
        else:
            m += c

    return m


m = input("Enter a message to encrypt: ")
k = int(input("Enter a key: "))
cipher = encrypt(m, k)
print(f"cipher: {cipher}")
plaintext = decrypt(cipher, k)
print(f"plaintext: {plaintext}")
