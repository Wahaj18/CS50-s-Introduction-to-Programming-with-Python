def main():
    greeting = input("Greeting: ")
    print(f"{value(greeting)}")

def value(greeting):
    greeting=greeting.lower().strip().split(" ")
    if(greeting[0].startswith('hello')):
        return 0
    elif(greeting[0].startswith('h')):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
