alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(user_text, user_shift):
    user_text_list = user_text.split()
    encrypted_word = []

    for letter in text:
        alpha_index = alphabet.index(letter)

        encrypted_word.append(alphabet[alpha_index + user_shift])

    encrypted_word = ''.join(encrypted_word)
    print(encrypted_word)


encrypt(text, shift)
