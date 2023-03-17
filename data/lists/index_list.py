def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path

def run ():
    print("Moving...")
    path = movements()
    for i in range(0, len(path), 2):
        direction = path[i]
        steps = path[i+1]
        print(f"{direction} for {steps} steps")
run()