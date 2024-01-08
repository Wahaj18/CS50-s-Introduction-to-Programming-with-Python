import emoji

def main():
    e = input("Input: ").lower().strip()
    print("Output:", emoji.emojize(e,language='alias'))


main()
