"""Caesar cipher"""
import string
import logging


class Caesar:
    """This class encrypts/decrypts a given text"""

    def __init__(self, key, text):
        """Constructor method"""
        self.key = key
        self.text = text
        self.coded_text = None

    def __encrypt(self, text, key):
        """Returns encrypted text by shifting each letter in the text
         by number of given letters

        :param text: Input text which is encrypted/decrypted
        :param key: Represents the number of letters each 
                    letter in the input text is shifted
        """
        alphabet = list(string.ascii_lowercase)
        text = list(text)
        coded_text = []

        for item in text:
            if item in alphabet:
                i = alphabet.index(item)
                i = (i + key) % len(alphabet)
                coded_text.append(alphabet[i])
            else:
                coded_text.append(item)

        coded_text = "".join(coded_text)
        self.coded_text = coded_text
        return coded_text

    def encrypt(self):
        """Returns encrypted text by shifting each letter in the text 
        by number of given letters

        :return: Encrypted text
        """
        return self.__encrypt(self.text, self.key)

    def decrypt(self):
        """Returns original text by shifting each letter back in the text by number of given letters

        :return: decrypted(original) text
        """
        if not self.coded_text:
            logging.error("Cannot decrypt None")
            raise ValueError('Cannot decrypt none')
        return self.__encrypt(self.coded_text, -1 * self.key)


if __name__ == "__main__":
    input_text = input("Enter a text to encrypt: ")
    input_step = int(input("Enter the number of steps to slide the letters: "))
    caesar = Caesar(input_step, input_text)
    final_text = caesar.encrypt()
    original_text = caesar.decrypt()

    print(f"\nThe coded text: {final_text}")
    print(f"\nThe original text: {original_text}")
