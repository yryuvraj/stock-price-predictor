import csv
file  = open("sharemarket.csv", "r")

file = csv.reader(file)

sector = []
market = []
for i in file:
    market.append(i)
    if i[2] not in sector:
        sector.append(i)
sector = sector[1:]
cont = 'y'
while cont == 'y':
    count =1
    for i in sector:
        print(count, i)
        count +=1

    choice = int(input("Enter your choice: "))
    choice -=1
    chosen = sector[choice]
    print("SECTOR               PRICE")
    for i in market:
        if i[2] == chosen:
            print(i[1], i[6])
    cont = input("do you want to continue (y/n): ")
