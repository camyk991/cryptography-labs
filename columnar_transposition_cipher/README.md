# Columnar Transposition Cipher

This project contains Python scripts to encrypt and decrypt text using the Columnar Transposition Cipher and generate keys for encryption.

## Files
- **decrypt.py**: Decrypts text.
  - Arguments:
    1. File with text to decrypt (e.g., `encrypted.txt`)
    2. Key (string)
- **encrypt.py**: Encrypts text.
  - Arguments:
    1. File with text to encrypt (e.g., `plain.txt`)
    2. Key (string)
- **key_generator.py**: Generates a key of specified length.
  - Argument:
    1. Key length (integer)

## Text Files
- **plain.txt**: Text to be encrypted.
- **encrypted.txt**: Encrypted text generated from `plain.txt` using the key in `passwd.txt`.
- **passwd.txt**: Key used for encryption and decryption.

## Usage
Example commands:
```bash
python3 encrypt.py plain.txt KEY
python3 decrypt.py encrypted.txt KEY
python3 key_generator.py 4
