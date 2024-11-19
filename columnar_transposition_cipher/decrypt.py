import sys

def decrypt(ciphertext, key):
    keySequence = keySequenceGenerator(key)
    numCols = len(key)
    numRows = len(ciphertext) // numCols
    extraChars = len(ciphertext) % numCols

    table = [[''] * numCols for _ in range(numRows + (1 if extraChars > 0 else 0))]

    currentChar = 0
    for num in range(1, len(keySequence) + 1):
        colPos = keySequence.index(num)
        for row in range(numRows + (1 if colPos < extraChars else 0)):
            if currentChar < len(ciphertext):
                table[row][colPos] = ciphertext[currentChar]
                currentChar += 1

    decrypted = ""
    for row in table:
        decrypted += ''.join(row)
    
    return decrypted


def keySequenceGenerator(key):
    sequence = [0] * len(key)
    sortedKey = sorted(list(key))

    for i, char in enumerate(sortedKey):
        pos = key.index(char)
        sequence[pos] = i + 1
        key = key[:pos] + "*" + key[pos+1:]  

    return sequence



if __name__ == "__main__":
   
    filename = sys.argv[1]  
    key = sys.argv[2]      

    with open(filename, 'r') as file:
        ciphertext = file.read()

    print(f'Klucz szyfru: {key}')

    decrypted = decrypt(ciphertext, key)

    print(f"Odszyfrowane: {decrypted}")
