print("Program Started!")
print("Please enter an ASCII code:")
code = int(input().strip())
if code in range(32, 127):
    char = chr(code)
    print(f"The character represented by the ASCII code {code} is: {char}.")
else:
    print("Error: Input must be a positive integer between 32 and 126 (inclusive).")
print("Program Ended!")