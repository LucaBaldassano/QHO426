def sum_weight(w_Beep, w_Bop):
    total_w = w_Beep + w_Bop
    return total_w

def calc_avg_weight(w_Beep, w_Bop):
    total_w = sum_weight(w_Beep, w_Bop)
    avg_weight = total_w / 2
    return avg_weight

def run():
    w_Beep = float(input("Enter weight of Beep: "))
    w_Bop= float(input("Enter weight of Bop: "))
    operation = input("Enter SUM or AVERAGE: ")
    if operation == "sum":
        total_weight = sum_weight(w_Beep,w_Bop)
        print("Total weight is: ", total_weight)
    elif operation == "average":
        avg_weight = calc_avg_weight(w_Beep,w_Bop)
        print("Average weight is:", avg_weight)
    else:
        print("Invalid operation entered.")
run()
