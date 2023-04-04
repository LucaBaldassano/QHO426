#HOW TO FIND THE PATH
import os
path=os.getcwd()
print(f"My path is {path}")
path=path + "\\"+"students"
print(path)
#Relative
for file in os.listdir(path):
    print(file)

