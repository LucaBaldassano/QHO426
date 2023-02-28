battery_found = False
while (battery_found == False):
    print("where should i look?")
    ax1 = input()
    if ax1 == "in the bedroom":
        print("Where in the bedroom should i look")
        ax2 = input()
        if ax2 == "under the bed":
            print("Found some shoes but no battery")
        else:
            print("Found some mess but no battery")
    elif ax1 == "in the bathroom":
        print("Where in the bathroom should i look?")
        ax2 = input()
        if ax2 == "in the bathub":
            print("Found rubber duck but no battery")
        else:
            print("Found a wet surface but no battery")
    elif ax1 == "in the lab":
        print("Where in the lab should i look?")
        ax2 = input()
        if ax2 == "on the table":
            print("Yes! I found my battery!")
            battery_found = True
    else:
        print("I do not know where that is but i will keep looking")