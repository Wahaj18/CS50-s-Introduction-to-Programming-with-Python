def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0:2].isalpha() and (6>= len(s) >=2) and s.isalnum():
        counter = 0
        for i in range(len(s)):
            if(s[i].isalpha() and counter == 0):
                continue
            elif(s[i].isnumeric() and s[i] == "0" and counter == 0):
                return False
            elif((s[i].isnumeric() and s[i] != "0") or (s[i].isnumeric() and counter > 0)):
                counter=counter+1
            elif(s[i].isalpha() and counter > 0):
                return False
            else:
                return True
        return True
    else:
        return False


main()
