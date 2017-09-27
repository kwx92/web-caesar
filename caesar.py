def encrypt(text, rot):
    result = ""
    for letter in text:
        new_character = rotate_character(letter, rot)
        result += new_character
    return result

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]

def alphabet_position(letter):
    letter_lower = letter.lower()
    index = 0
    for let in letters:
        if let == letter_lower:
            return index
        else:
            index +=1

def rotate_character(character, rot):
    if character.isalpha() == False:
        return character
    starting_position = alphabet_position(character)
    number_of_alphabets = 26
    new_position = (starting_position + rot) % number_of_alphabets
    new_character = letters[new_position]
    if character.isupper():
        new_character = new_character.upper()
    return new_character
