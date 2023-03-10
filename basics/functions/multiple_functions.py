def display_ladder(steps):
    for i in range(1, steps + 1):
        print("|   |")
        print("***")
def create_ladder():
    steps = int(input("How many steps do you want to climb? "))
    display_ladder(steps)
create_ladder()