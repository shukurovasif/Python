import string

alphabet = list(string.ascii_lowercase)

l = len(alphabet)

def cipher(text):
    
    """Encrypt text. 
    
    :param text: Any text that needs to be encoded
    :return: A text encoded by shifting each letter forward by 4 letters"""
    
    text = list(text)
    new_text =[]
    
    for item in text:
        if item in alphabet:
            for i in range(l):
                if alphabet[i] == item:
                    i = (i + 4) % l
                    new_text.append(alphabet[i])
        else:
            new_text.append(item)         
    
    new_text = "".join(new_text)
    
    return(new_text)


while True:
    input_message = input("Enter a text and I will encode it by using Caesar's cipher: ")
    print("Enter 'q' when you want to quit")
    
    if input_message == "q":
        break
    
    
    final_text = cipher(input_message)
    print(final_text)
 
