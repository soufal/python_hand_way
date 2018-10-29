#Designing and debugging
#my game
from sys import exit, argv


scipt, user_name = argv

print(f"Hello! {user_name}! The game is begin!")


def kitchen():
    print("You have found the kitchen!")
    print("Good job!")
    print("You are lived and go away!")
    print("The game over!")
    exit(0)

def witch_room():
    print("This is a witch's room!")
    print("You see a witch sat in a chair and smile for you !")
    print("She said: \" There are two choice for you\".")
    print("\"One is give me your all money.\" ")
    print("\"Two is Give me nothing.\" ")
    print("Which one do you choose?")
    print("Money or Nothing?")
    choice = input(">> ")

    if choice == "money":
        kitchen()
    elif choice == "nothing":
        dead("You are dead for witch!")
    else:
        dead("Please input right answer!")

def old_man():
    print("This room have a old man.")
    print("He will dead!")
    print("Do you want to save him?")
    print("Yes or No?")
    choice = input(">> ")

    if choice == "yes":
        print("You are a good man!")
        print("The old man tell you the kitchen where is.")
        print("You saved. Good job!")
    elif choice == "no":
        print("You are so bad!")
        dead("The old man and you all dead!")
    else:
        print("You have no choice.")
        dead("The old man and you all dead!")

def dead(test):
    print(f"{test}, The game failed!")
    exit(0)

def start():
    print("This is a beautiful room!")
    print("You are so hungry!")
    print("You want to find some food.")
    print("There are two doors, which one do you choose? Left os Right?")

    choice = input(">> ")
    if choice == "right":
        witch_room()
    elif choice == "left":
        old_man()
    else:
        dead("You have no choice, you will stumble!")

start()