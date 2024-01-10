import sys

def main():
    lines = list()
    count = 0

    if(len(sys.argv) < 2):
        sys.exit("Too few command-line arguements")
    elif(len(sys.argv) > 2):
        sys.exit("Too many command-line arguements")
    elif(sys.argv[1].endswith('.py') ==  False):
        sys.exit("Invalid file name")
    else:
        try:
            with open(sys.argv[1], "r") as file:
                lines = file.readlines()
        except FileNotFoundError:
            sys.exit("File does not exist")

    for line in lines:
        if(line.lstrip().startswith('#') or line.isspace()):
            pass
        else:
            count+=1
    print(count)

if __name__ == "__main__":
    main()
