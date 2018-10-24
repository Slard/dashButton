d = {}


def clearPage():
    for i in range(0, 45):
        print()


def createDict(x, y):
    d[x] = y


file = open("loginInfo.txt", 'r')
username = str(file.readline())
password = str(file.readline())
print(username)
createDict(username[0:-1], password)
print(d)


def main():
    global user
    user = input("Enter user name: ")
    if user in d.keys():
        pswrd = input("Enter password: ")
        if pswrd in d[user]:
            clearPage()
            menu()
        else:
            wrongPassword()
    else:
        clearPage()
        yn = input("Would you like to create a new user? Y/N ")
        yn = yn.lower()
        if yn == 'y':
            clearPage()
            newU = input("Enter new username: ")
            newP = input("Enter new password: ")
            createDict(newU, newP)
            print("Now to confirm, please log-in again")
            main()
        if yn == 'n':
            main()

def wrongPassword():
    global n
    global user
    global pswrd
    n = n + 1
    if (n < 3):
        pswrd = input("Please try again")
        if pswrd in d[user]:
            menu()
        else:
            wrongPassword()
    else:
        print("This is now the new password")
        createDict(user, pswrd)
        main()

def setUp():
    print('a')

def changeItems():
    print('b')

def checkItems():
    print('c')

def menu():
    clearPage()
    print("A: Set up Items")
    print("B: Change amount of Items")
    print("C: Check on Items")
    print("D: Exit Program")
    x = input("What would you like to do?: ")
    if x.lower() == 'a':
        setUp()
    elif x.lower() == 'b':
        changeItems()
    elif x.lower() == 'c':
        checkItems()
    elif x.lower() == 'd'
        print("Have a nice day!")
        exit()
    else:
        print("Please enter 'a', 'b', or 'c'")
        menu()

n = 0
main()