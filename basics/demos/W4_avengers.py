def adding(lista = []):
    new_member = input("Enter new Hero: ")
    lista.append(new_member)

def removing(lista = []):
    rejected = input("Enter Hero to removed ")
    if rejected in lista:
        lista.remove(rejected)

def printing(lista =[]):
    for hero in lista:
        print(f"The mighty {hero} is part of Avengers!")

def run():
    avengers = []
    while True:
        opt = int(input("Avengers, Assamble!\n\n1-Add a member\n2-Remove a member\n3-Check on team\n9-Exit\nOption:"))
        if opt == 1:
            adding(avengers)
        elif opt == 2:
            removing(avengers)
        elif opt == 3:
            printing(avengers)
        elif opt == 9:
            break
        else:
            print("Sort yourselfe out ")

run()