import re
import sys

def main():
    print(validate(input("IPv4 Address: ").strip()))

def validate(ip):
    reg_ex = "([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])"
    match = re.search(fr"^{reg_ex}\.{reg_ex}\.{reg_ex}\.{reg_ex}$", ip)
    if match:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
