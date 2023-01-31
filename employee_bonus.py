import csv


with open("EmployeePay.csv", "r") as a:
    
    b = csv.reader(a)

    for row in b:

        dep = row[0]
        fname = row[1]
        lname = row[2]
        sal = row[3]
        bonus = row[4]


        print(f"Department: {dep}")
        print(f"First Name: {fname}")
        print(f"Last Name: {lname}")
        print(f"Salary: ${sal}")
        print(f"Bonus Multiplier: x{bonus}")
        print("\n")
