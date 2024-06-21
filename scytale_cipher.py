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

from icecream import ic


def encrypt_str(s: str, rod: int) -> str:
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

    # Characters from "s" are taken one at a time in sequence and added one at a time to each of each sublist (there are "rod" sublists). The first iteration adds a character to index 0 in each sublist. The next iteration adds a character to index 1 in each sublist...and so on.
    char_num: int = 0
    while char_num < len(s):
        for row in range(rod):
            outer_list[row].append(s[char_num])
            char_num += 1
            if char_num >= len(s):
                break

    # Flatten the list of lists so we can create a string with join().
    flat: list[str] = [character for sublist in outer_list for character in sublist]

    return "".join(flat)


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
    s --> 'IRYYMATBHEMVAE HEDL URLP '

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


def decrypt_str(s: str, rod: int) -> str:
    """
    Given a string "s" that was encrypted by encrypt_str(), decrypt the message.

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

    # "rod" is the number of rows. Now, determine number of cols:
    num_cols: int = ceil(len(s) / rod)
    outer_list: list[list[str]] = create_2d_list(s, num_cols)

    col: int = 0
    msg: str = ""
    while col < num_cols:
        for row in range(rod):
            msg += outer_list[row][col]
        col += 1

    return msg


def main(s: str, rod: int, encrypt: bool) -> str:
    """
    Takes a string, "s", and either encrypts it or decrypts it. The length of "s" MUST be evenly divisible by "rod".

    Parameters
    ----------
    s : str -- encrypted or decrypted string
    encrypt : bool, optional -- encrypted "s" if True; default True

    Returns
    -------
    str : either the encrypted or decrypted string
    """

    # The message to encrypt is required to be evenly divisible by "rod".
    if len(s) % rod != 0:
        print(f"Message length ({len(s)}) must be evenly divisible by rod length ({rod}).\nPad message with spaces as necessary.")
        for i in range(5):
            if (len(s) + i) % 5 == 0:
                sp: str = 'space' if i == 1 else 'spaces'
                print(f'Add {i} {sp} to message.')
        exit()

    if encrypt:
        m: str = encrypt_str(s, rod)
    else:
        m: str = decrypt_str(s, rod)

    return m


if __name__ == "__main__":
    # Proof of concept!
    plaintext = "In the café, the bánh mì sandwich is a popular choice among the regulars. The flaky baguette, stuffed with savory grilled pork, pickled daikon and carrots, fresh cilantro, and a dollop of sriracha mayo, is the perfect lunchtime indulgence. As I sipped my matcha latte, I noticed the barista's shirt had a cute ねこ (neko, or cat) graphic on it. It reminded me of the time I visited Tokyo and saw the famous 東京タワー (Tokyo Tower) at night, aglow with colorful lights. The world is full of unique and beautiful symbols, and Unicode makes it possible to express them all in one cohesive language. "

    encrypted = "IRYYATBHMVAEHEDLURLP"
    decrypted = "IAMHURTVERYBADLYHELP"

    encrypted = "IRYYMATBHEMVAE HEDL URLP "
    decrypted = "IAMHURTVERYBADLYHELPME   "

    rod = 5

    msg: str = main(decrypted, rod, True)
    ic(decrypted)
    ic(msg)

    msg: str = main(encrypted, rod, False)
    ic(encrypted)
    ic(msg)

    msg: str = main(plaintext, rod, True)
    print('\n', '=' * 40)
    print(plaintext)
    print('=' * 40)
    print(msg)

    print('=' * 40)
    msg: str = main(msg, rod, False)
    print(msg)
