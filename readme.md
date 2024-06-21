# Scytale Cipher

This Python script implements the scytale cipher, which is a transposition cipher that uses a cylindrical tool. A strip of parchment is wrapped around the cylinder, and the message is written along the length of the cylinder. When unwrapped, the letters appear jumbled, but when wrapped around a cylinder of the same diameter, the message can be read.

The Scytale cipher is similar to a railfence cipher, but it uses a rail instead of a zigzag. A railfence cipher arranges the plaintext in a zigzag pattern across multiple "rails" (rows) and then reads off each row in sequence to create the ciphertext.


## Description

The Scytale cipher is an ancient form of encryption that uses a cylindrical rod (or "scytale") to encrypt and decrypt messages. The plaintext message is written diagonally across the surface of the rod, and then the ciphertext is read off row by row.

This script provides two main functions:

- **encrypt_str(plaintext, rod_length)**: Encrypts the given plaintext using the Scytale cipher with the specified rod length.
- **decrypt_str(ciphertext, rod_length)**: Decrypts the given ciphertext using the Scytale cipher with the specified rod length.

## Usage

`python scytale_cipher.py`

**_As of this version, the message to be encrypted/decrypted is hardcoded into the script. The next version will incorporate a command-line interface to accommodate provision of a message to encrypt._**

## Example

Suppose we have the plaintext message "IAMHURTVERYBADLYHELP" and a rod length of 4. The encryption process would look like this:

```
I A M H U R T V E R Y B A D L Y H E L P
```

The ciphertext is then read off row by row: "IRYYATBHMVAEHEDLURLP".

To decrypt, we wrap the ciphertext around the rod with the same length and read off the plaintext diagonally:

```
I R Y Y A T B H M V A E H E D L U R L P
```

This gives us the original plaintext message "IAMHURTVERYBADLYHELP".

## Requirements

This script requires Python 3.x and the `math` module from the Python standard library.

## Note

The length of the plaintext message must be evenly divisible by the rod length. If not, the script will add spaces to the message to make it divisible.