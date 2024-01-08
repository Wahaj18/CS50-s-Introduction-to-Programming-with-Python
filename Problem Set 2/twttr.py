def main():
    s = input("Input: ")
    print("Output:", shorten(s))

def shorten(s):
    short_s = ""
    for c in s:
        if(c.lower() == "a" or c.lower() == "e" or c.lower() == "i" or c.lower() == "o" or c.lower() == "u"):
            pass
        else:
            short_s=short_s+c
    return short_s

if __name__ == "__main__":
    main()
