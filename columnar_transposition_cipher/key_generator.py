import sys
import string
import random

def generate_key(length):
    if length < 1:
        raise ValueError("Key length should be at least 1 character")

    letters = string.ascii_uppercase 
 
    key = ''.join(letters[i % len(letters)] for i in range(length))

    key_list = list(key)
    random.shuffle(key_list)
    
    return ''.join(key_list)

if __name__ == "__main__":
    length = sys.argv[1]
    key = generate_key(int(length))

    print(key)