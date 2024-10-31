def initial():
    upper = input("Please enter an upper bound: ")
    while not upper.isdigit() or int(upper) <= 0:
        print("Please enter a positive number!")
        upper = input("Please enter an upper bound: ")
    return int(upper)

upper_bound = initial()
print("The inputted upper bound is:", upper_bound)