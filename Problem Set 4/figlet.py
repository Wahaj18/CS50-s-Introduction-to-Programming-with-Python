from pyfiglet import Figlet
import sys
import random

def main():

    figlet = Figlet()
    font_list=figlet.getFonts()
    isValid_font = False

    if(len(sys.argv) >= 3):
        for font in font_list:
            if (sys.argv[2] == font):
                isValid_font=True
        if((sys.argv[1] != ("-f" or "--font")) or (isValid_font==False)):
            sys.exit("Invalid usage")
    elif(len(sys.argv) == 2):
        sys.exit("Invalid usage")
    else:
        pass

    s = input()

    if(len(sys.argv)==1):
        f = random.choice(font_list)
        figlet.setFont(font=f)
        print(figlet.renderText(s))

    else:
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(s))



main()

