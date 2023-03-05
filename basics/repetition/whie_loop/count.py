numcab = int(input("How many live cables must I avoid?  "))
livecab = 0
while livecab < numcab:
    print("Avoiding...Done! {} live cable avoided" .format(livecab + 1))
    livecab += 1
print("All live cables have been avoided.")
