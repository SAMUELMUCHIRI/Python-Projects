import random


def play():
    user=input("What is your choice'r' for rock,'p' for paper,'s'for scissors")
    computer= random.choice(['r','p','s'])
    print(computer)
    if user==computer:
        print ("tie")
    else :
        def is_win():
            if(user=='r' and computer=='s') or (user=='s' and computer=='p') or (user=='p' and computer=='r'):
                print("you won")
            else:
                print("you lost")
        is_win()
play()