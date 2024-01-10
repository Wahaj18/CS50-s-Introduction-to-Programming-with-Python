import sys
import csv

def main():
    biodata = []

    if(len(sys.argv) < 3):
        sys.exit("Too few command-line arguements")
    elif(len(sys.argv) > 3):
        sys.exit("Too many command-line arguements")
    elif(sys.argv[1].endswith('.csv') ==  False or sys.argv[2].endswith('.csv') == False):
        sys.exit("Not a CSV file")
    else:
        try:
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    last_name, first_name = row["name"].split(",")
                    first_name = first_name.lstrip()
                    biodata.append({"first" : first_name, "last" : last_name, "house" : row["house"]})

        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")

        with open(sys.argv[2], "w",newline='') as file:
                writer = csv.DictWriter(file, fieldnames=["first","last","house"])
                writer.writeheader()
                for data in biodata:
                    first = data["first"]
                    last = data["last"]
                    house = data["house"]
                    writer.writerow({"first" : first, "last" : last, "house" : house})

if __name__ == "__main__":
    main()
