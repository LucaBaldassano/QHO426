import csv
import matplotlib.pyplot as plt

def gather_data(n=1):
    with open("feb_data.csv", "w") as f:
        csv_writer = csv.writer(f)
        for i in range(n):
            h = float(input("Enter height: "))
            w = float(input("Enter weight: "))
            csv_writer.writerow([h,w])

gather_data(3)