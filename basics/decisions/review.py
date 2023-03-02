#Review of programming using decision-making with if/elif/else statements
#Nested decisions and multple conditions with logical operators

#Ask the user to enter their age
age = int(input("Enter your age: "))
#if/elif/else statement to determinate what messagege to display
if age < 1:
    print("invalid age")
elif age < 18:
    print("You are a minor")
elif age >= 18 and age < 65:
    print("You are an adult")
else:
    print("You are a senior citizen")
#Ask the user to enter their gender and age
gender = input("Enter your gender (M/F): ")
age = int(input("Enter your age "))

#Use nested if statement to determinate what messagege to display
if gender == "M" :
    if age < 18:
        print("You are a boy")
    else:
        print("You are a man")
else:
    if age < 18:
        print("You are a girl")
    else:
        print("You are a woman")
#Ask user ti enter a number
num = int(input("Enter a number: "))
#Use and/or operator
if num < 0 or num > 100:
    print("The number is out of range")
elif num >= 50 and num <= 75:
    print("The number is in the middle range")
elif not(num % 2 == 0):
    print("The number is odd")
else:
    print("The number is even")