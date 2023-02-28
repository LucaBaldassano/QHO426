level = int(input("What leve of brightnress do you require?  "))
for i in range(2, level, 2):
    print("Beep's brightness level: ", "*" * i)
    print("Bop's brightness level: ", "*" * i)
    print()
print("Adjustment complete")