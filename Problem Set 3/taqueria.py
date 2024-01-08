def main():
    menu={
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
        }
    t=0

    while True:
        try:
            m=input("Item: ").title()
            if(m==""):
                break
            for k in menu:
                if(m==k):
                    t+=menu[k]
                    print(f"${t:.2f}")
        except KeyError:
            print("wrong key")
            continue

        except EOFError:
            break

main()

