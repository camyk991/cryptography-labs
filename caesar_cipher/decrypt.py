import sys

def decrypt_text(text, shift):
    decrypted_text = ""
    shift = shift % 26

    for char in text: 

        if (char.isalpha()):
            beginning_of_alphabet = "a"

            if (char.isupper()):
                beginning_of_alphabet = "A"

            shifted_acii = (ord(char) - ord(beginning_of_alphabet) - shift + 26) % 26
            prepared_ascii = shifted_acii + ord(beginning_of_alphabet)

            decrypted_text += chr(prepared_ascii)
        else:
            decrypted_text += char

    return decrypted_text



filename = sys.argv[1]
shift = int(sys.argv[2])

with open(filename, 'r') as file:
    text_to_decrypt = file.read()

print(decrypt_text(text_to_decrypt, shift))