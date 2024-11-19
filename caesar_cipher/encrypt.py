import sys

def encrypt_text(text, shift):
    encrypted_text = ""
    shift = shift % 26

    for char in text: 

        if (char.isalpha()):
            beginning_of_alphabet = "a"

            if (char.isupper()):
                beginning_of_alphabet = "A"

            shifted_acii = (ord(char) - ord(beginning_of_alphabet) + shift) % 26
            prepared_ascii = shifted_acii + ord(beginning_of_alphabet)

            encrypted_text += chr(prepared_ascii)
        else:
            encrypted_text += char

    return encrypted_text
            
                

filename = sys.argv[1]
shift = int(sys.argv[2])

with open(filename, 'r') as file:
    text_to_encrypt = file.read()


encrypted = encrypt_text(text_to_encrypt, shift)
print(encrypted)


