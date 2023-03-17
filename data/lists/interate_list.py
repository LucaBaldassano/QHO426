def directios():
    directios_list = ["Move Forward", "Move Backward", "Turn left", "turn Right"]
    return directios_list

def menu():
    print("Please select a direction:")
    directions_list = directios()
    for i in range(len(directions_list)):
        print(f"{i}: {directions_list[i]}")

def run():
    menu()
run()