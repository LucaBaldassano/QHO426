def display_box(word):
    border = "+" + "-" * (len(word) + 2) + "+"
    content = "| " + word + " |"
    print(border)
    print(content)
    print(border)

def display_lower_case(word):
    print(word.lower())

def display_upper_case(word):
    print(word.upper())

def display_mirrored(word):
    mirrored_word = word[::-1]
    print(word + " | " + mirrored_word)

def repeat (word):
    num_times = int(input("How many times to repeat the word? "))
    for i in range(num_times):
        if i % 2 == 0:
            print(word.upper())
        else:
            print(word.lower)

def run():
    word = input("Enter a word: ")
    option = int(input("enter an option (1-5): "))
    if option == 1:
        display_box(word)
    elif option == 2:
        display_lower_case(word)
    elif option == 3:
        display_upper_case(word)
    elif option == 4:
        display_mirrored(word)
    elif option == 5:
        repeat(word)
    else:
        print("Invalid option entered.")

run()
