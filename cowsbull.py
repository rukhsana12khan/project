import random
name=input("enter your name")
print('...........', name  ,'............')
print("........... welcome to the cowsbull",name,"........")

def secretnum():
    number=list(range(10))
    random.shuffle(number)
    return number
def cluenum():
    num=secretnum()
    list=[]
    for i in range(4):
        list.append(num[i])
    return list 
def check():
    cows=[]
    bull=[]
    num1=cluenum()
    # print(list)
    i=0
    print(num1)
    maxgue=10
    while maxgue>0:
        guessn=int(input("plz enter your guess number"))
        posi=int(input("enter your position number"))
        if guessn in num1:
            index=num1.index(guessn)
            if index==posi:
                if guessn not in bull:
                    bull.insert(index,guessn)
                    print("bull",bull)
                else:
                    print("you are allready use this number plz try again")
            else:
                cows.append(guessn)  
                print("cows",cows)   
        if bull==num1:
            print(name,"congratulaion you are win")
            break
        maxgue-=1
        print(maxgue,"yor tern is left")
    else:
        print("you are out","loose the game")  
    return bull
check()

def play_again():
    while True:    
        again=input("you want to play again so plz yes==y or no==n")
        if again=="y":
            check()
        else:
            break
play_again()