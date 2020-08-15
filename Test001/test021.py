#!/usr/bin/env python3
import csv


def get_miles_driven():
    while True:
        miles_driven = float(input("Enter miles driven :     "))
        if miles_driven > 0:
            return miles_driven
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue


def get_gallons_used():
    while True:
        gallons_used = float(input("Enter gallons of gas:     "))
        if gallons_used > 0:
            return gallons_used
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue

def weite_trips(list):
    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
        mpg = round((miles_driven / gallons_used), 2)
        print("Miles Per Gallon:\t" + str(mpg))
        print()
        # 将数据保存在列表中
        list.append([miles_driven, gallons_used, mpg])
        # 以写的模式打开文件
        with open("trips.csv", 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # 写入表头
            writer.writerow(['Distance', 'Gallons', 'MPG'])
            # 将数据写入csv文件
            writer.writerows(list)
        list_trips(list)
        more = input("More entries? (y or n): ")

def read_trips(list):
    with open("trips.csv", 'r') as csvfile:
        # 读取csv文件数据
        reader = csv.reader(csvfile)
        for line in reader:
            list.append(line)

def list_trips(list):
    print('Distnce    ','Gallons    ', '  MPG ')
    for i in range(len(list)):
        for j in range(len(list[i])):
            print('%-13s' % list[i][j], end='')
        print()
print()

def main():
    # display a welcome message
    print("The Miles Per Gallon application")
    print()
    list = []
    weite_trips(list)
    read_trips(list)
    print("Bye")


if __name__ == "__main__":
    main()

