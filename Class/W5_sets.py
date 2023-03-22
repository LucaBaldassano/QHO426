#Initialise empty set
s = set()
#Initialise non-empty set
colours = {"blue," "red", "yellow", "purple", "red"}
print(colours)
#Adding elements into a set
colours.add("green")
colours.add("navy blue")
print(colours)
colours.union({"black", "magenta", "crimson", "brown"})
print(colours)
#Remove item form a set
if "yellow" in colours:
    colours.remove("yellow")
print(colours)
#Sets are heterogeneous and deplicates are not allowed
colours.add(99)
colours.add(True)
print(colours)
#Check membership
if "yellow" in colours:
    print("Yay - I like yellow")
else:
    print("Sad day, no yellow : ")