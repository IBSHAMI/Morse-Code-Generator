from morse_code import MORSE_CODE_DICT

MORSE_DICT = MORSE_CODE_DICT


# Use the morse dict to find the letter for each code snippet
def find_letter_from_morse_code(letter_code):
    for key, value in MORSE_DICT.items():
        if value == letter_code:
            return key


# Encrypt the incoming text from user
def encryption(text):
    encrypted_text = ""
    for letter in text:
        if letter != " ":
            encrypted_text += f"{MORSE_DICT[letter]} "
        elif letter == " ":
            encrypted_text += "  "

    return encrypted_text


# decrypt the incoming morse code from user
def decryption(code):
    text = ""
    symbols = ""
    IS_WORD_SPACE = False # A value that turn True if there is a new word
    for code_symbol_index in range(len(code)):
        if code[code_symbol_index] != " ":
            symbols += code[code_symbol_index]
            IS_WORD_SPACE = False
            if code_symbol_index == (len(code) - 1):
                text += find_letter_from_morse_code(symbols)

        elif code[code_symbol_index] == " " and code_symbol_index != (len(code) - 1) and IS_WORD_SPACE == False:
            if code[code_symbol_index + 1] == " ":
                text += find_letter_from_morse_code(symbols)
                text += " "
                symbols = ""
                IS_WORD_SPACE = True

            elif code[code_symbol_index] == " ":
                text += find_letter_from_morse_code(symbols)
                symbols = ""

    if symbols != "":
        text += find_letter_from_morse_code(symbols)

    return text


user_choice = int(input("Do you want to encrypt (press 1) or decrypt (press 2) a message? "))

if user_choice == 1:
    text_to_encrypt = input("Enter your text to encrypt:  ").upper()
    encrypted_text = encryption(text_to_encrypt)
    print(encrypted_text)

elif user_choice == 2:
    code_to_decrypt = input("Enter your code to decrypt:  ")
    decrypted_text = decryption(code_to_decrypt)
    print(decrypted_text)
