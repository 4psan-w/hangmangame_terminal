import random 
from worsdf import words
import time as t
def winner():
    print("CONGRATULATIONS")
    print("You Won the game")

def looser():
    print("Better Luck Next time")
    print("You Lost the game")
def tutorial():
    print("*    this is a simple game of vocabulary")
    print("*    you will be given 6 chances (6 stages) before a man gets hanged thus called the game hangman")
    print("*    Upon guessing all the Letters while Not losing all the chances You will win the game")
    print("*    Best of Luck!")


def intro():
    print("THIS IS THE TERMINAL COMMAND LINE HANG-MAN GAME IN PYTHON*")
    print("Press Y to Check the tutorial to the game:")
    if(input("  >").capitalize()=="Y"):
        tutorial()
    print('\n\n')


def gameframe():
    random_word=random.choice(words).upper()
    word_len=len(random_word)
    dashes_words="_" * word_len
    print(f"The Word is {word_len} letters long")
    letters_guessed=[]
    words_guessed=[]
    chances=6
    print(hangman_stages(chances),"   \n    ", dashes_words)
    print("\n")
    guess=False
    while not guess and chances>0:
        guessd_let_word=input("Enter a letter or a word\n>").upper()
        if(len(guessd_let_word)==1 and guessd_let_word.isalpha()):
            if(guessd_let_word in letters_guessed):
                print("You Already Guessed the letter",guessd_let_word)
            elif guessd_let_word not in random_word:
                print(f"The word doesnot contain the letter {guessd_let_word}")
                chances=chances-1
                letters_guessed.append(guess)
            else:
                print(f"The word contains the letter {guessd_let_word}")
                letters_guessed.append(guessd_let_word)
                words_in_list=list(dashes_words)
                indices= [i for i,letter in enumerate(random_word) if( letter == guessd_let_word)]
                for indx in indices:
                    words_in_list[indx]=guessd_let_word
                dashes_words = "".join(words_in_list)
                if("_" not in dashes_words):
                    guess=True
        elif(len(guessd_let_word)==len(random_word) and guessd_let_word.isalpha()):
            if(guessd_let_word in words_guessed):
                print(f"The Word {guessd_let_word} is already Guessed")
            elif guessd_let_word != random_word:
                print("Incorrect guess")
                chances=chances-1
                words_guessed.append(guessd_let_word)
            else:
                guess=True
                dashes_words=random_word
        else:
            print("Invalid Guess")
        print(hangman_stages(chances))
        print(dashes_words)
        print("*"*20,"\n")
    if(guess):
        winner()
    else:
        print(f"The word was :\n{random_word}")
        looser()

def main():
    intro()
    play_again=True
    while play_again:
        in_time=t.time()
        gameframe()
        fin_time=t.time()
        tot_time=fin_time-in_time
        print(f"Total Time of excecution : {tot_time} seconds")
        x=input("Do you want to play it again?\n>(Y/N)")
        if x.capitalize() == 'Y':
            play_again=True
        else:
            play_again=False
    

def hangman_stages(stage):
    st=['''
                +----
                |   | 
                |   O
                |  \\|/
                |   |
                |  / \\
                |
                __+__''',
            '''
                +----
                |   | 
                |   O
                |  \\|/
                |   |
                |  / 
                |
                __+__''',
            ''' 
                +----
                |   | 
                |   O
                |  \\|/
                |   |
                |  
                |
                __+__''',
            '''
                +----
                |   | 
                |   O
                |  \\|
                |   |
                |  
                |
                __+__''',
            '''
                +----
                |   | 
                |   O
                |   |
                |   |
                |  
                |
                __+__''',
            '''
                +----
                |   | 
                |   O
                |  
                | 
                |  
                |
                __+__''',
            '''
                +----
                |   |
                |   
                |  
                | 
                |  
                |
                __+__''']
    return st[stage]


main()
__name__='__main__'