import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r"src=\"https?://(?:www\.)?(.+?)\.com/embed/([0-9a-zA-Z].+?)\"", s):
        if "youtube" in match.group(1):
            return "https://youtu.be/"+match.group(2)
    else:
        return None

if __name__ == "__main__":
    main()
