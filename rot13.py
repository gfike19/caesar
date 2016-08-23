def rot13(mess):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alpha_caps = alphabet.upper()
    encrypted = ''
    for char in mess:
        if not char.isalpha():
            encrypted = encrypted + char
        else:
            rotated_index = alphabet.find(char) + 13
            if rotated_index < 26:
                encrypted = encrypted + alphabet[rotated_index]
            else:
                encrypted = e
