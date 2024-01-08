while True:
    try:
        fuel = input("Fraction: ")
        x,y = fuel.split('/')
        x=int(x)
        y=int(y)
        if(x>y and y!=0):
            continue
        else:
            percentage = round((x / y) * 100)
            if(percentage<=1):
                print("E")
            elif(percentage>=99):
                print("F")
            else:
                print(f"{percentage}"+"%")
            break

    except ValueError:
        print("Please input a valid fraction")
    except ZeroDivisionError:
        print("Cannot divide by zero")
