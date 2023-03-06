while True:
print("Please choose one of the follwing options: ")
print("1-Nice Message")
print("2-Area of a rectangle")
print("3-Area of triangle")
print("4-Time Table")
opt = int(input())
if opt == 1:
    print("You are so nice today!")
elif opt == 2:
    h = float(input("Enter Height: "))
    b = float(input("Enter the base: "))
    print(f"The area of this rectangle is {h*b} cm2")
elif opt == 3:
    h = float(input("Enter Height: "))
    b = float(input("Enter the base: "))
    print(f"The area of this triangle is {h*b*0.5} cm2")
elif opt == 4:
    n = int(input("Enter whole number: "))
    for i in range(1,17,3):
        print(f"{n}x{i}={n*i}")
    print("DONE!!")
elif opt == 5:
    break
else:
    print("Sorry try again. No such optrion.")
