import csv

report = open("salesreport.csv", "w")

report.write("Customer ID, Total")

num = int(250)

with open("sales.csv", "r") as a:

    b = csv.reader(a)

    accum = 0

    for row in b:

        i = row[0]

        sub = float(row[3])
        tax = float(row[4])
        freight = float(row[5])
        total = sub - tax + freight

        if i == num:
            accum = accum + total
        else:
            report.write(num + "\n" + accum)
            num = num + 1

report.close()

#help i give up

