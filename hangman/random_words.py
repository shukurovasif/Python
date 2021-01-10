import random

filename = "HangmanWords.txt"
with open(filename) as f:
    lines = f.readlines()

words = []

for line in lines:
    line = line.strip()
    words.append(line)
    
def get_random_word():
    return random.choice(words)