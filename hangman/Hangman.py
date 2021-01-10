from random_words import get_random_word

wrong_attempts = 0
max_wrong_attempts = 5

word = get_random_word()
length = len(word)
word_search = ["__"]
word_search = word_search * length
print(f"You need to find the {length} letters long word by using max number of {max_wrong_attempts} wrong attempts")
print(" ".join(word_search))

used_letter = []

while True:
    
    letter = input("Tell a letter or write the full word if you know: ")
    
    
    if letter in used_letter:
        print("You have already used this letter. Try another one")
        
    elif letter == word:
        print("Congratulations! You won the game!")
        print(f"The word is {word}")
        break
             
    else:
        used_letter.append(letter)
        if letter in word:
            index = [i for i in range(len(word)) if word[i] == letter]
            for i in index:
                word_search[i] = letter
            print(" ".join(word_search))
            if "".join(word_search) == word:
                print("Congratulations! You won the game!")
                print(f"The word is {word}")
                break
        
        else:
            print("This letter is not in the word")
            wrong_attempts += 1
            wrong_attempts_remaining = max_wrong_attempts - wrong_attempts
            print(f"You have {wrong_attempts_remaining} wrong attempts left")
            
            if wrong_attempts == 5:
                print("You lost the game!")
                print(f"The word is {word}")
                break
        


#def check_letter(word, letter):
#    """Summary 
#    
#    :param word: ...
#    :param letter: ...
#    :return: ... 
#    """
#
#
#def get_random_word(): 
#    """generate a random word
#    
#    :return: a random word
#    """
#    ...