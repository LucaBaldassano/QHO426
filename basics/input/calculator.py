print("Provide 2 numbers")
x1 = float(input())
x2 = float(input())
print(f"{x1} +{x2} = {x1+x2}") #f-string approach
print("{} - {} -{}".format(x1,x2, x1-x2)) #format method
print(str(x1) + " * " + str(x2) + " = " + str(x1*x2)) #String concatenation
print(str(x1), "/", str(x2), "=", str(x1/x2) ) #Comma separeted
