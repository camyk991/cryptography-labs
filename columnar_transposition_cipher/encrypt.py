import string
import sys


def encrypt(message, key):
    table = createCipherTable(len(key), message)
    keySequence = keySequenceGenerator(key)

    ciphertext = ""
    for num in range(1, len(keySequence) + 1):
        pos = keySequence.index(num)
        for row in table:
            if len(row) > pos:
                ciphertext += row[pos]
    return ciphertext


def keySequenceGenerator(key):
    sequence = [0] * len(key)
    sortedKey = sorted(list(key))

    for i, char in enumerate(sortedKey):
        pos = key.index(char)
        sequence[pos] = i + 1
        key = key[:pos] + "*" + key[pos+1:]  

    return sequence


def createCipherTable(width, message):
    table = []
    row = []
    for ch in message:
        row.append(ch)
        if len(row) == width:
            table.append(row)
            row = []
    
    if row:
        table.append(row)  

    return table


if __name__ == "__main__":
    filename = sys.argv[1]
    key = sys.argv[2]

    with open(filename, 'r') as file:
        text_to_encrypt = file.read()

    print(f'Klucz szyfru: {key}')

    encrypted = encrypt(text_to_encrypt, key)
    print(f"Zaszyfrowane: {encrypted}")

    # Uncomment to save result to file
    # with open("shuffle_proprietary.txt", 'w') as file:
      #  file.write(encrypted)
    
