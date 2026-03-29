import string

ALPHA = string.ascii_letters


def encrypt(message, key):
    cipher = ""

    for c in message:
        if c in ALPHA:
            i = ALPHA.index(c)
            cipher += ALPHA[(i + key) % len(ALPHA)]
        else:
            cipher += c

    return cipher


def decrypt(cipher, key):
    m = ""

    for c in cipher:
        if c in ALPHA:
            i = ALPHA.index(c)
            m += ALPHA[(i - key) % len(ALPHA)]
        else:
            m += c

    return m


m = input("Enter a message to encrypt: ")
k = int(input("Enter a shift key: "))
cipher = encrypt(m, k)
print(f"cipher: {cipher}")
plaintext = decrypt(cipher, k)
print(f"plaintext: {plaintext}")
