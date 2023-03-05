print("How many bars should be charged?")
bars = int(input())
bar_char = 0
while bar_char < bars:
    bar_char += 1
    print("Charging:", "@" * bar_char)
print("The battery is fully charged.")