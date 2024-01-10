from validator_collection import checkers

def main():
    print(validate(input("What's your email address? ")))


def validate(s):
    is_Valid = checkers.is_email(s)
    if is_Valid == True:
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()
