"""Caesar cipher with dictionary"""
import string
alphabet = list(string.ascii_lowercase)

def cipher(text,step):
    """Returns encrypted text by shifting it by number of given steps
        :param text: Input text which is encrypted
        :param step: Represents the number of letters each 
                    letter in the input text is shifted
        """
    text = list(text)
    alphabet_dict = {}

    for letter in alphabet:
        i = alphabet.index(letter)
        i = (i + step) % len(alphabet)
        alphabet_dict[letter] = alphabet[i]

    coded_text = [] 
    for item in text:
        if item in alphabet:
            coded_text.append(alphabet_dict[item])
        else:
            coded_text.append(item)

    return "".join(coded_text)
            

input_text = input("Enter a text: ")
input_step = int(input("Enter a step: "))
get_ciphered_text = cipher(input_text,input_step)
print(f"Here is the coded text: {get_ciphered_text}")
