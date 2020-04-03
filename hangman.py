import random as rd

  
def word_input():
    '''
    This takes in user input
    '''
    print("\nYour word:")
    user_word=input()
    return user_word

def random_hints(word_pc):
    '''
    This function is the main function that takes in random letters from the word and displays them as hints and leave some letter places blank to guess 
    '''
    r=[]
    l=[]
    hint=[]
    for letter in word_pc:
        r.append(letter)
    no_of_hint=len(r)//2
    l=rd.sample(r,no_of_hint)
    
    for element in r:
        if element in l:
            hint.append(element)
        else:
            hint.append('__')
    print("\n\t\t\t"+ str(hint))

def sentence_hint(word_pc):
    '''
    This function only shows the hint
    '''
    print("\nHINT:")
    print(words.get(word_pc))     

def check(word_pc):
    '''
    This functions checks the user input with the original word
    '''
    j=0
    while(j<4):
         user_word=word_input()
         if user_word==word_pc and j<3:
                print("\nCorrect! you won :)")
                break
         elif(j==3):    
                print("\nYou Lost all your chances!")
                break
         else:
                print("\nTry again")
                
         j=j+1


def play():
    '''
    this function is only used to call all the functions for the game
    '''
    word_pc=rd.choice(list(words))   
    random_hints(word_pc)  
    sentence_hint(word_pc)
    check(word_pc)
    play_again()
          
def play_again():
    '''
    this function is used as a game loop
    '''
    print("\n\tWanna Play again? Press 'Y' or 'y' \n  Press 'N' or 'n' to exit")
    ans=input()
    if ans=='Y' or ans=='y':
        play()
    elif ans=='N' or ans=='n':
        print("\nGoodbye!")
        exit
    else:
        print("\nError! exiting")
        exit 
 

#a dictionary that holds the words as 'key' and hints as its 'value'. More words can be added.
words={'orange':'A color and also a fruit','lion':'The King of Jungle','newyork':'a city that never sleeps'}

#the main funtion
play()

 
  
        
         
