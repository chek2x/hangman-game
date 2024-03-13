import random
import string

# Introduction as a function to not make the main loop code too long.
def introduction():
    print
    input("Press Enter to continue...")
    print()
    input("A game by TATAK L. Productions")
    print()
    input("Welcome to...")
    print()
    print()
    print()
    print("88                                                                                       ")
    print("88                                                                                       ")
    print("88                                                                                       ")
    print("88,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYb,d8 88,dPYba,,adPYba,  ,adPPYYba,  8b,dPPYba, ")
    print("88P'     8a a       a  88P      8a a8a      Y8 88P     88      8* a       Y8  88P      8a")
    print("88       88 ,adPPPPP88 88       88 8b       88 88      88      88 ,adPPPPP88  88       88")
    print("88       88 88,    ,88 88       88  88a,   ,d8 88      88      88 88,    ,88  88       88")
    print("88       88  a8bbdP Y8 88       88   aYbbdP Y8 88      88      88  a8bbdP Y8  88       88")
    print("                                    aa,   , 88                                           ")
    print("                                      Y8bbdP                                             ")
    print()
    print()
    print()


#Constructors
givenWord = ""
currentWord = ""

# Categories
unitsDI = ["byte", "kilobyte", "megabyte", "gigabyte", "terabyte"]
pc_peripheral = ["microphone", "keyboard", "mouse", "monitor", "speakers"]
dataTypes = ["string", "character", "integer", "float", "boolean"]
compViruses = ["trojan", "spyware", "adware", "rootkit", "woprm"]
progElems = ["input", "output", "conditionals", "operations", "variables"]

# Reveals correct letter.
def reveal(hidden, letter):
    j = 0
    newVer = list(hidden).copy()
    for x in givenWord[:]:
        if x == letter:
            newVer[j] = letter
        j += 1

    return newVer

# Turns the array into a string with spaces inbetween letters.
def arrayToString(array):
    x = " "
    return (x.join(array))

# Displays the letters as underscores in the form of an array.
def hideSlct(word):
    word = list(word)
    i = 0
    while i < len(word):
        word[i] = "_"
        i += 1

    return word

# This method randomly picks a word from the tuples above depending on which category is chosen.
def wordSlct(category):
    switcher = {
        0 : random.choice(unitsDI),
        1 : random.choice(pc_peripheral),
        2 : random.choice(dataTypes),
        3 : random.choice(compViruses),
        4 : random.choice(progElems)
    }

    return switcher.get(category)

# Cheks (hehe) the state of the input whether it's the wrong
def correctCheck(letter):
    if letter in givenWord[:]:
        return True
    elif letter not in givenWord[:]:
        return False
    

# The different states per life spent for the game.
def state(num):
    def state0():
        return (r"""









|W|
| |
| |
| |
| |
| |
| |
| |
|_|
            """)

    def state1():
        return (r"""
 _____________________
| .__________________|
| | / /
| |/ /
| | /
| |/
| |
| |
| |
| |
| |
| |
| |
| |
| |
| |
| |
|_|
            """)

    def state2():
        return (r"""
____________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||
| |/         ||
| |          ||
| |          ||
| |          ||
| |          ||
| |          ||
| |          ||
| |          ()
| |
| |
| |
| |
|_|
            """)

    def state3():
        return (r"""
 ____________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |           `--'
| |
| |
| |
| |
| |
| |
| |
| |
|_|
            """)

    def state4():
        return (r"""
 ____________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |          -`--'
| |          |   |
| |          |   |
| |          |   |
| |          | _ |
| |
| |
| |
| |
|_|
            """)

    def state5():
        return (r"""
  ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y     Y\
| |       // |   | \\
| |      //  |   |  \\
| |     ')   | _ |   (`
| |
| |
| |
| |
|_|
            """)

    def state6():
        return (r"""
  ___________.._______           
| .__________))______|          
| | / /      ||               
| |/ /       ||                
| | /        ||.-''.            
| |/         |/  _  \          
| |          ||  `/,|        
| |          (\\`_.'         
| |         .-`--'.           
| |        /Y     Y\           
| |       // |   | \\       
| |      //  |   |  \\        
| |     ')   | _ |   (`        
| |          || ||             
| |          || ||              
| |          || ||              
| |          || ||               
|_|         / | | \  
            """)

    switcher = {
        0 : state0,
        1 : state1,
        2 : state2,
        3 : state3,
        4 : state4,
        5 : state5,
        6 : state6
    }

    return switcher.get(num)()

# This method is for starting/restarting purposes.
def start():
    while True:
        ans = input("> ").lower()

        if ans == 'y':
            value = True
            break
        elif ans == 'n':
            value = False
            break
        else:
            print("Invalid input")
            continue
    
    return value