import random

def main():
    level = get_level()
    score = 0
    tries = 0
    i=0

    while (i<10):
        if(tries==0):
            x,y = generate_integer(level)
        try:
            z = int(input(f"{x} + {y} = "))
            if(z==(x+y)):
                score+=1
                tries=0
                i+=1
                continue
            else:
                raise ValueError
        except ValueError:
            print("EEE")
            tries+=1
            pass

        if(tries==3):
            print(f"{x} + {y} = {x+y}")
            tries=0
            i+=1
            continue

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if (level == 1 or level == 2 or level == 3):
                return level

        except ValueError:
            continue

def generate_integer(level):
    if(level == 1):
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif(level==2):
        x = random.randint(10,99)
        y = random.randint(10,99)
    elif(level == 3):
        x = random.randint(100,999)
        y = random.randint(100,999)
    return x,y


if __name__ == "__main__":
    main()
