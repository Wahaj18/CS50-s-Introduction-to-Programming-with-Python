import sys
from tabulate import tabulate
import csv

def main():
    menu = []

    if(len(sys.argv) < 2):
        sys.exit("Too few command-line arguements")
    elif(len(sys.argv) > 2):
        sys.exit("Too many command-line arguements")
    elif(sys.argv[1].endswith('.csv') ==  False):
        sys.exit("Not a CSV file")
    else:
        try:
            with open(sys.argv[1]) as file:
                reader = csv.reader(file)
                for row in reader:
                    menu.append(row)

        except FileNotFoundError:
            sys.exit("File does not exist")

    print(tabulate(menu, headers="firstrow", tablefmt="grid"))


if __name__ == "__main__":
    main()
