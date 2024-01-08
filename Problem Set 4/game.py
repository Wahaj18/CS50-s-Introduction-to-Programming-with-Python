import random
import sys


def main():
    while True:
        try:
            n = int(input("Level: "))
            if n < 0:
                continue
            r = random.randint(1, n)
            while True:
                try:
                    g = int(input("Guess: "))

                    if g == r:
                        print("Just right!")
                        break
                    elif g < 0:
                        continue
                    elif g < r:
                        print("Too small!")
                    else:
                        print("Too large!")
                except:
                    continue
            break
        except:
            continue

    sys.exit()


main()
