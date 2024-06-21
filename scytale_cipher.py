"""
    Filename: scytale_cipher.py
     Version: 0.1
      Author: Richard E. Rawson
        Date: 2023-05-01
 Description:
scytale ("baton, cylinder", also σκύταλον skútalon) is a tool used to perform a transposition cipher, consisting of a cylinder with a strip of parchment wound around it on which is written a message.

Suppose the rod allows one to write four letters around in a circle and five letters down the side of it. The plaintext could be: "I am hurt very badly help".

To encrypt, one simply writes across the leather:
_____________________________________________________________
        | I | a | m | h | u |
        | r | t | v | e | r |
        | y | b | a | d | l |
        | y | h | e | l | p |
_____________________________________________________________
so the ciphertext becomes, "Iryyatbhmvaehedlurlp" after unwinding.

To decrypt, all one must do is wrap the leather strip around the rod and read across. The ciphertext is: "Iryyatbhmvaehedlurlp" Every fifth letter will appear on the same line, so the plaintext (after re-insertion of spaces) becomes: "I am hurt very badly help".

Source: https://en.wikipedia.org/wiki/Scytale

"""

from math import ceil

import click
from icecream import ic

VERSION = "2.0"

@click.command(help="Encrypt/decrypt [PLAINTEXT] using a scytale cipher.", epilog="--rod is defined as the diameter of the rod, but practically speaking, it is the number of characters that can fit around the diameter of the rod. For this reason, the message length must be evenly divisible by --rod. If not, the message is padded with spaces.\n\nIf a value for --rod is non-default, that same value must be used for both encryption and decryption.")
@click.argument("plaintext", required=False)
@click.option("-r", "--rod", type=int, default=5, show_default=True, help="Diameter of the rod")
@click.version_option(version=VERSION)
def cli(plaintext: str, rod: int) -> None:
    """
    This is the entry point for the CLI.

    Parameters
    ----------
    plaintext : str -- plaintext message to encrypt.
    rod : int -- diameter of the rod
    """
    print()
    try:
        ic(len(plaintext))
    except TypeError:
        pass
    ic(plaintext)
    print()

    if plaintext:
        # The message to encrypt is required to be evenly divisible by "rod".
        # If it's not, then pad the message accordingly.
        p: int = len(plaintext) % rod
        if p != 0:
            padding_length: int = rod - p
            plaintext += " " * padding_length
            encrypt_str(plaintext, rod)
    else:
        decrypt_str(rod)


def encrypt_str(msg: str, rod: int) -> None:
    """
    Encrypt the plain text string "s". To do this, the "size of the "rod" must be known.

    Parameters
    ----------
    s : str -- the encrypted message
    rod : int -- the size of the rod

    Returns
    -------
    str -- the message and the size of the rod, allowing decryption.

    Example
    -------
    "IAMHURTVERYBADLYHELPME   " --> ['I', 'R', 'Y', 'Y', 'M']
                                    ['A', 'T', 'B', 'H', 'E']
                                    ['M', 'V', 'A', 'E', ' ']
                                    ['H', 'E', 'D', 'L', ' ']
                                    ['U', 'R', 'L', 'P', ' ']
    """

    # Create an empty 2-D list.
    outer_list: list[list[str]] = [[] for n in range(rod)]

    # Characters from "msg" are taken one at a time in sequence and added one at a time to each of each sublists (there are "rod" sublists). The first iteration adds a character to index 0 in each sublist. The next iteration adds a character to index 1 in each sublist...and so on.
    char_num: int = 0
    while char_num < len(msg):
        for row in range(rod):
            outer_list[row].append(msg[char_num])
            char_num += 1
            if char_num >= len(msg):
                break

    encrypted_msg_list: list[str] = flatten_list(outer_list)

    encrypted_msg: str = "".join(encrypted_msg_list)
    print(f'Encrypted message:\n"{encrypted_msg}"', sep="")

    # Save the encrypted message to encrypted.txt.
    with open("encrypted.txt", "w", encoding="utf-8") as f:
        f.write(encrypted_msg)


def flatten_list(target: list[list[str]]) -> list:
    """
    Flattens the two-dimensional list (outer_list).

    Parameters
    ----------
    target : list -- a two-dimensional list

    Returns
    -------
    list -- flattened list

    Example
    [['T', 'o', 'l', 'h', 'm', 'g'], ['h', 'a', 'a', ' ', 'i', 'h'], ['e', 't', 'u', 'a', 'd', 't'], [' ', 's', 'n', 't', 'n', '.'], ['b', ' ', 'c', ' ', 'i', ' ']]

    -->

    ['T', 'o', 'l', 'h', 'm', 'g', 'h', 'a', 'a', ' ', 'i', 'h', 'e', 't', 'u', 'a', 'd', 't', ' ', 's', 'n', 't', 'n', '.', 'b', ' ', 'c', ' ', 'i', ' ']
    """
    return sum((flatten_list(sub) if isinstance(sub, list) else [sub] for sub in target), [])


def create_2d_list(s: str, num_cols: int) -> list[list[str]]:
    """
    Given a string "s", divide the string into sublists, where each sublist has "num_cols" characters from "s".

    Parameters
    ----------
    s : str -- string
    num_cols : int -- length of each sublist in [outer_list]

    Returns
    -------
    list[list[str]] -- 2-dimensional list from "s"

    Example
    --------
    s = 'IRYYMATBHEMVAE HEDL URLP ' -->

        ['I', 'R', 'Y', 'Y', 'M']
        ['A', 'T', 'B', 'H', 'E']
        ['M', 'V', 'A', 'E', ' ']
        ['H', 'E', 'D', 'L', ' ']
        ['U', 'R', 'L', 'P', ' ']
    """

    outer_list: list = []

    # Iterate through the string in chunks of "num_cols" characters
    for i in range(0, len(s), num_cols):
        chunk = s[i:i + num_cols]
        outer_list.append(list(chunk))

    return outer_list


def decrypt_str(rod: int) -> None:
    """
    Given a string "s" that was encrypted by encrypt_str(), decrypt the message. Rod length used in decryption must be the same as rod length used for encryption.

    Parameters
    ----------
    s : str -- encrypted message
    rod : int -- rod length

    Returns
    -------
    str -- decrypted message

    Examples
    --------
    'IRYYMATBHEMVAE HEDL URLP '  -->  'IAMHURTVERYBADLYHELPME   '
    """

    with open("encrypted.txt", 'r', encoding="utf-8") as f:
        all_lines: list[str] = f.readlines()

    lines: list[str] = [s.strip("\n") for s in all_lines]
    message: str = "".join(lines)

    # "rod" is the number of rows. Now, determine number of cols:
    num_cols: int = ceil(len(message) / rod)
    outer_list: list[list[str]] = create_2d_list(message, num_cols)

    col: int = 0
    msg: str = ""
    while col < num_cols:
        for row in range(rod):
            msg += outer_list[row][col]
        col += 1

    print(f'Decrypted message:\n"{msg.strip()}"', sep="")

    with open("decrypted.txt", 'w', encoding="utf-8") as f:
        f.write(msg.strip())


if __name__ == "__main__":
    print()
    cli()
