# Program allow Beep to pick an adventure
print("Enter the type of adventure")
adv = input()
# Identify the type of adventure
if ((adv == "scary") or (adv == "short")) :
    print("Entering the dark forest!")
else:
    print("Not sure which rouret to take")
adv = input()
if ((adv == "safe") or (adv == "long")) :
    print("Taking the safe route!")
else:
    print("Not sure which route to take")