
def batman_punch(strenght = 5, technique = 8):
    punch_power = strenght * 0.4 + technique * 0.6
    return punch_power

def fight_scene(number = 2, anemy_strenght = 3,):
    total_strenght = number * anemy_strenght
    bat_strenght = batman_punch(randint(0,10)-
    if bat_strenght >= total_strenght:
        return "Batman Wins!"
    else:
        return "Batman Looses!"

def roberry_escape(num_of_cars):
    if num_of_cars > 5:
        return "Batman is caught"
    else:
        return "Batman escape"
def run():
    scene = fight_scene()
    escape = roberry_escape(randint(2,12))
    print(f"After a long fight, {scene}. Afterwards, police chase him and {escape}.")
run()
