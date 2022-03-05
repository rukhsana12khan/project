import random
def hangman():
    list=["india","rani","rukhsana","prerna","ayushi","nikki","himani"]
    word=random.choice(list)
    turn=10
    g_made=""
    entry=set("abcdefghijklmnopqrstuvwxyz")
    while len(word)>0:
        m_word=""
        for i in word:
            if i in g_made:
                m_word=m_word+i
                # print(m_word)
            else:
                m_word=m_word+" _ "   
        if m_word==word:
            print(m_word)
            print("!!!!!!! you are won !!!!!!")  
            break  
        print("guess the word",m_word)
        guess=input()    
        if guess in entry:
            g_made=g_made+guess
        else:
            print("invalid characters")
            # guess=input()
        if guess not in word:
            turn=turn-1
            if turn==9:
                print("9 turn is left")
                print("*****************") 
                print("_________")
            if turn==8:
                print("8 turn is left")
                print("****************")
                print()
                print("_____________")
                print("      o       ")            
            if turn==7:
                print("7 turn is left")
                print("****************")
                print("______________")
                print("     o      ") 
                print("     |      ")   
            if turn==6:
                print("6 turn is left")
                print("****************")
                print("______________")
                print("     o      ")
                print("     |      ")  
                print("     /      ")  
            if turn==5:
                print("5 turn is left")
                print("****************")
                print("______________")
                print("      o      ")
                print("      |     ")    
                print("     / \     ")
            if turn==4:
                print("4 turn is left")
                print('*****************')
                print("__________________")
                print("        \o       ")
                print("         |        ")
                print("        / \        ")
            if turn==3:
                print("3 turn is left")
                print("****************")
                print("____________________")
                print("         \o/          ")
                print("          |          ")
                print("         / \         ")  
            if turn==2:
                print("2 turn is left")
                print("*******************")
                print("____________________")
                print("       \o/ |         ")
                print("        |       ")  
                print("       / \      ")   
            if turn==1:
                print("last turn is left")
                print("*****************")
                print("__________________")
                print("      \o/_|      ")
                print("       |      ")
                print("      / \        ")
            if turn==0:
                print("****   you are looser   ****")    
                print("yes let a good man die")
                break   
name=input("ENTER YOUR NAME -->") 
print("welcome","***", name ,"***")
print("************************************")
print("try to guess the word in less than 10 attempts")
hangman()
def play_again():
    while True:    
        again=input("you want to play again so plz yes==y or no==n")
        if again=="y":
            hangman()
        else:
            break
play_again()

