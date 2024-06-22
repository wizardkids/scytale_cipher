# Scytale Cipher

This Python script implements the scytale cipher, which is a transposition cipher that uses a cylindrical tool. A strip of parchment is wrapped around the cylinder, and the message is written along the length of the cylinder. When unwrapped, the letters appear jumbled, but when wrapped around a cylinder of the same diameter, the message can be read.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Skytale.png/800px-Skytale.png" width="320" height="183">

Source: <a href="https://en.wikipedia.org/wiki/Scytale">https://en.wikipedia.org/wiki/Scytale</a>

The best way to envision this cipher in operation is to take a strip of paper and wrap the strip around a rod, such as a broomstick. Write your message on the strip, writing down the length of the broomstick. When you remove the strip of paper, the message will appear "jumbled" (encrypted). When the recipient wraps the strip on a similar broomstick, the original  message can be read.

The Scytale cipher is similar to a railfence cipher, but the text wraps around a single rail (rod) instead of a zigzagging. A railfence cipher arranges the plaintext in a zigzag pattern across multiple "rails" (rows) and then reads off each row in sequence to create the ciphertext.

## Functions

This script provides two main functions, accessible through a command-line interface (CLI):

- **encrypt_str(plaintext, rod_length)**: Encrypts the provided plaintext using the Scytale cipher with the specified rod length.
- **decrypt_str(rod_length)**: Decrypts the given ciphertext using the Scytale cipher with the specified rod length.

## Usage
```
Usage: scytale_cipher.py [OPTIONS] [PLAINTEXT]

  Encrypt/decrypt [PLAINTEXT] using a scytale cipher.

Options:
  -r, --rod INTEGER  Diameter of the rod  [default: 5]
  --version          Show the version and exit.
  --help             Show this message and exit.

  --rod is defined as the diameter of the rod, but practically
  speaking, it is the number of characters that can fit around the
  diameter of the rod. For this reason, [PLAINTEXT] length must be
  evenly divisible by --rod. If not, [PLAINTEXT] is padded with
  spaces.

  If a value for --rod is non-default, that same value must be used
  for both encryption and decryption.
```

### Example usage:

**Encryption:**

`python scytale_cipher.py -r 8 "plaintext message to encrypt"`

**Decryption:**

`python scytale_cipher.py -r 8`

Providing a rod length is optional. If a message is provided, it will be encrypted and the encrypted text will be saved in "encrypted.txt" using the default rod length of 5 (unless specified). If there is no message on the command line, then the text in "encrypted.txt" will be decrypted and the decrypted text will be saved in "decrypted.txt".

## Rod length: key to the cipher
Rod length must be the same for both encryption and decryption. Rod length defaults to 5 but can be any integer value. However, a rod length equal to or greater than message length will not encrypt the message, even though the program runs without error. If rod length equals message length, then the message simple goes around the rod once! There's no encryption! Even rod lengths close to the message length won't do a reasonable job of encrypting. For example,

given this message of length 29...

```
"The boats launch at midnight."
```
when encrypted with a rod length of 26 yields:
```
"Thhte.  b o a t s   l a u n c h   a t   m i d n i g "
```
We can still guess the meaning. A rod length of 5 is better:
```
"Tolhmghaa ihetuadt sntn.b c i "
```

## Example

Suppose we have the plaintext message "IAMHURTVERYBADLYHELP" and a rod length of 5. The encryption process would look like this:

```
IAMHURTVERYBADLYHELP
```

The plaintext message is wrapped around the rod, and then the ciphertext is read off row by row:

```
IRYYATBHMVAEHEDLURLP
```

To decrypt, we wrap the ciphertext around the rod with the same length and read off the plaintext diagonally:

This gives us back the original plaintext message.

## Notes
- The length of the plaintext message must be evenly divisible by the rod length. If not, the script will add spaces to the message to make it divisible.
- The scytale cipher method is obviously not particularly secure since rods of various diameters could be employed to "brute force" a decryption. Since there is a practical limit to the diameter of a rod, brute force would require having a stock of reasonably sized rods. On the other hand, at the time in history when this method was used, having such a stock would likely involve state-level "hackers".

## Dependencies
- [click](https://click.palletsprojects.com/en/8.1.x/) (for command-line interface)