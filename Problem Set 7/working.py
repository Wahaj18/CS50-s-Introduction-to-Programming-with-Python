import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if match:=re.search(r"^(1[0-2]|0?[1-9]):?([0-5][0-9])?\s(AM|PM)\sto\s(1[0-2]|0?[1-9]):?([0-5][0-9])?\s(AM|PM)$", s, re.IGNORECASE):
        hrs1 = match.group(1)
        minutes1 = match.group(2)
        am_pm1 = match.group(3).lower()
        hr24_1 = ""
        hrs2 = match.group(4)
        minutes2 = match.group(5)
        am_pm2 = match.group(6).lower()
        hr24_2 = ""
        if am_pm1 == "am":
            if(hrs1 == "12"):
                hrs1 = "00"
            if minutes1 == None:
                minutes1 = "00"
            hr24_1 = f"{int(hrs1):02}:{int(minutes1):02}"
        elif am_pm1 == "pm":
            if(hrs1 != "12"):
                hrs1 = int(hrs1) + 12
            if minutes1 == None:
                minutes1 = "00"
            hr24_1 = f"{(int(hrs1)):02}:{int(minutes1):02}"

        if am_pm2 == "am":
            if(hrs2 == "12"):
                hrs2 = "00"
            if minutes2 == None:
                minutes2 = "00"
            hr24_2 = f"{int(hrs2):02}:{int(minutes2):02}"
        elif am_pm2 == "pm":
            if(hrs2 != "12"):
                hrs2 = int(hrs2) + 12
            if minutes2 == None:
                minutes2 = "00"
            hr24_2 = f"{(int(hrs2)):02}:{int(minutes2):02}"

        return f"{hr24_1} to {hr24_2}"

    else:
        raise ValueError

if __name__ == "__main__":
    main()
