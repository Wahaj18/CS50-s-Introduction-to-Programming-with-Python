def main():
    inputstr = input("camelCase: ")
    convert_to_camel(inputstr)

def convert_to_camel(s=""):
    for c in s:
        if(c.islower()):
            print(c, end="")
        elif(c.isupper()):
            print("_"+ c.lower(), end="")
    print()

main()
