#!/usr/bin/env python3
from vigenere_cipher import vigenere


if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        file = f.read().split('\n')

    try:
        alphabet, text, key, case = file[0], file[1], file[2], file[3]
    except IndexError:
        exit('Wrong data in input.txt')

    if case.lower() == 'encrypt':
        result = vigenere(alphabet, text, key, 1)
    elif case.lower() == 'decrypt':
        result = vigenere(alphabet, text, key, -1)
    else:
        exit('Wrong encrypt/decrypt argument!')

    print(result)
    with open('output.txt', 'w') as f:
        f.write(result + '\n')
