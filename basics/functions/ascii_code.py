print("Program Started!")
print("Please enter a standard characters:")
letter = input().strip()
if len (letter) == 1:
    value = ord(letter)
    print(f"The ASCII code for {letter} is: {value}")
else:
    print("Error: Input must be a single character.")
print("Program Ended!")
