def box (word):
    length = len(word)
    print("#*length")
    print("#" + word + #)

def low (word):
    print(word.lower())

def upper(word):
    print(word.upper())

def mirror(word):
    print(word, " / ", word[::-1])

def repeat(word):
    n = int(input("How many time to repeat: "))
    for i in range(n):
        if i % 2 ==  0:
            upper(word)
        else:
            low(word)

def spastic_writing(word):
    for i in range(len(word)):
        if i % 2 == 0:
            print(word[i].upper(), end = "")
        else:
            print(word[i].lower(), end = "")

def run()
    w = input("Enter a word: ")
    print("Choose an option 1 to 6")
    opt = int(input())
    if opt == 1:
        box(w)
    elif opt == 2:
        low(w)
    elif opt == 3:
        upper(w)
    elif opt == 4:
        mirror (w)
    elif opt == 5:
        repeat(w)
    elif opt == 6:
        spastic_writing(w)
