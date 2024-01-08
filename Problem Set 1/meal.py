def main():
    hours = convert(input("What time is it? "))
    if (7 <= hours <= 8):
        print("breakfast time")
    elif (12 <= hours <= 13):
        print("lunch time")
    elif (18 <= hours <= 19):
        print("dinner time")
    else:
        print("")

def convert(time):
    hours, minutes = time.split(":")
    mins = ( float(minutes) / 60 )
    hrs = float(hours) + mins
    return hrs

if __name__ == "__main__":
    main()
