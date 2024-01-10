def main():
    s = input("Input: ").lower()
    print("Output:", shorten(s))

def shorten(s):
    short_s = ""
    for c in s:
        if(c == "a" or c == "e" or c == "i" or c == "o" or c == "u"):
            pass
        else:
            short_s=short_s+c
    return short_s

if __name__ == "__main__":
    main()
