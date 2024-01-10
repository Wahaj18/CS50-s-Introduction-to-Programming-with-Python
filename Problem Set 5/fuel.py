def main():

    fraction = input("Fraction: ")
    try:
        percentage = convert(fraction)
        print(gauge(percentage))
    except:
        print("value or divide by zero error")

def convert(fraction):
    try:
        x,y = fraction.split('/')
        x=int(x)
        y=int(y)
        if(x>y and y!=0):
            raise ValueError
        else:
            percentage = round((x / y) * 100)
            return percentage
    except ValueError:
        print("Please input a valid fraction")
    except ZeroDivisionError:
        print("Cannot divide by zero")

def gauge(percentage):
    if(percentage<=1):
        return "E"
    elif(percentage>=99):
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
