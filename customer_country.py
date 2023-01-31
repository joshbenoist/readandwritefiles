import csv


with open("customers.csv", "r") as a:
    b = csv.reader(a)


    with open("customer_country.csv", "w") as c:
        d = csv.writer(c)

        
        for collumn in b:
            d.writerow([collumn[1], collumn[2], collumn[4]])






