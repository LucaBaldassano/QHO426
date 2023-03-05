print("How many numbers should i sum up?")
x = int(input())
i = 1
tot = 0
while i <= x:
    print("Please enter number", i, "of", x, ":")
    y = float(input())
    tot += y
    i += 1
print("The answer is", tot)
