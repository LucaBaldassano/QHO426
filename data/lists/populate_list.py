def directions():
    directions_list = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions_list

def menu():
    print("Please select a direction: ")
    directions_list = directions()
    for i in range(len(directions_list)):
        print(f"{i}: {directions_list[i]}")
    responde = int(input())
    return directions_list[responde]

def run():
    route = []
    print("Working out escape route...")
    for i in range(5):
        direction = menu()
        route.append(direction)
    print(f"Escape route: {route}")

run()