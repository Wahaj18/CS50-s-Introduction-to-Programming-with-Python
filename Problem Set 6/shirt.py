import sys
from PIL import Image
from PIL import ImageOps
import os


def main():
    if verify():
        edit(sys.argv[1], sys.argv[2])

def verify():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguements")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguements")
    else:
        first = os.path.splitext(sys.argv[1])
        first = first[1]
        second = os.path.splitext(sys.argv[2])
        second = second[1]

    valid_ext = [".jpg", ".jpeg", ".png"]
    if first.lower() not in valid_ext:
        sys.exit("Invalid output")
    elif first.lower() not in valid_ext:
        sys.exit("Invalid output")
    elif first.lower() != second.lower():
        sys.exit("Input and output have different extensions")
    else:
        return True


def edit(before, after):
    try:
        shirt = Image.open("shirt.png")
        size = shirt.size
        with Image.open(before) as before:
            before_fit = ImageOps.fit(before, size)
            before_fit.paste(shirt, shirt)
            before_fit.save(after)
    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
