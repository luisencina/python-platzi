import os
import random
from datetime import datetime

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        elapsed_time = final_time - initial_time
        print("Terminaste el juego en ", str(elapsed_time.total_seconds()), " segundos")
    return wrapper

def normalize(word):
    replacements = {'á': 'a','é': 'e','í': 'i','ó': 'o','ú': 'u'}
    new_word = ""
    for c in word:
        if c in replacements:
            new_word += replacements[c]
        else:
            new_word += c

    return new_word

 

def read():
    words = []
    with open("./files/data.txt", "r", encoding="utf-8") as f:
        words = [normalize(data.replace("\n", "").lower()) for data in f]

    return random.choice(words)


def unMascarate(character, word, userWord):
    userWord = [c for c in userWord]
    list = [c for c in word]
    c = []

    for i in range(0, len(list)):
        if list[i] == character:
            c.append(i)
    
    for i in c:
        userWord[i] = character

    return ''.join(userWord)

def isCorrect(character, word):
    if character in word:
        return True
    return False


def game(word):

    userWord =  "_" * len(word)
    intentos = 0
    
    while userWord != word:
        os.system('clear')
        # print("N de intentos: ", intentos)
        print(HANGMANPICS[intentos])
        try:
            print(userWord)
            character = str(input("Inserte una letra: "))
            assert character != "", "Debes ingresar una letra" 
            if isCorrect(character, word):
                userWord = unMascarate(character, word, userWord)
            else:
                intentos += 1
            
            if intentos >= 7:
                return print("Perdiste, La palabra era: ", word)
                

        except AssertionError as ae:
            print(ae)
            character = str(input("Inserte una letra: "))
        except KeyboardInterrupt:
            return print("\nAdiós!")
        

    print("Ganaste con "+str(intentos)+" intentos! Palabra: ", word)

@execution_time
def run():
    words = read()
    game(words)
    
    

if __name__ == "__main__":
    run()