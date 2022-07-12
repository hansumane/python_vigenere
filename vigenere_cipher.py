def vigenere(alphabet_s: str, text_s: str, key_s: str, case: int) -> str:

    alphabet = list(alphabet_s.lower())
    text = list(text_s.lower())
    key = list(key_s.lower())
    result = list()

    i = 0
    while len(key) < len(text):
        try:
            key.append(key[i])
        except IndexError:
            key.append(alphabet[0])
        i += 1

    for i in range(len(text)):
        try:
            result.append(alphabet[(alphabet.index(text[i]) + case * alphabet.index(key[i])) % len(alphabet)])
        except ValueError:
            exit('There is a letter in your text or in your key which is not in the alphabet!')
            return ''

    return ''.join(result)
