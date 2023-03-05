print("What phrase do you see?")
phrase = input()
reverse = ""
for i in range(len(phrase)-1, -1, -1):
    reverse += phrase[i]
print(reverse)
