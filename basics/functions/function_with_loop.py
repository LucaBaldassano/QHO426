def cross_bridge(distance):
    for step in range(1, distance + 1):
        print("Crossed step.")
        if step > 5:
            print("The bridge is collapsing!")
            break
        elif step == distance:
            print("We made it!")
        else:
            print("We must keep going!")
cross_bridge(3)
cross_bridge(6)