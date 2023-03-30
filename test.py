import unittest
from main import encrypt

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(user_text, user_shift):
    user_text_list = user_text.split()
    encrypted_word = []

    for letter in user_text:
        new_letter_index = alphabet.index(letter) + user_shift

        if new_letter_index > 25:
            new_letter_index = abs(new_letter_index - 26)

        encrypted_word.append(alphabet[new_letter_index])

    encrypted_word = ''.join(encrypted_word)

    return encrypted_word


class EncryptTestCase(unittest.TestCase):
    def test_encrypt_1(self):
        actual = encrypt("zebra", 1)
        expected = "afcsb"
        self.assertEqual(actual, expected)  # add assertion here

    def test_encrypt_2(self):
        actual = encrypt("millionaire", 3)
        expected = "ploolrqdluh"
        self.assertEqual(actual, expected)  # add assertion here

    def test_encrypt_3(self):
        actual = encrypt("xylophone", 5)
        expected = "cdqtumtsj"
        self.assertEqual(actual, expected)  # add assertion here

    if __name__ == '__main__':
        unittest.main()
