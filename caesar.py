from sys import argv
#text=str(input("Type a message: "))
#rot = int(argv[1])


from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    new_text = ""

    for char in text:
        if char.isalpha():
            new_text += (rotate_character(char, rot))
        else:
            new_text += char

    return new_text


def user_input_is_valid(argv):
    if  len(argv) >= 2 and argv[1].isdigit(): 
        return True
    return False



