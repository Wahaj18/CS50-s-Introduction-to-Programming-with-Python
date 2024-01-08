import inflect

def main():
    p = inflect.engine()
    names = list()
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            break

    print("\nAdieu, adieu, to", p.join(names))
  
main()
