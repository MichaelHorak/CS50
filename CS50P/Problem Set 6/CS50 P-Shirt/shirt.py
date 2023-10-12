import sys
import os.path
from PIL import Image, ImageOps

# students = []


def main():
    verify_input()

    try:

        # Open the input with Image.open
        image = Image.open(sys.argv[1])
        shirt = Image.open('shirt.png')
        size = shirt.size
        # resize and crop the input with ImageOps.fit
        # using default values for method, bleed, and centering
        image_resized = ImageOps.fit(image, size, method=Image.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
        # overlay the shirt with Image.paste
        image_resized.paste(shirt, box=None, mask=shirt)
        # and save the result with Image.save
        image_resized.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit('Input does not exist')


def verify_input():
    # If the user does not specify exactly two command-line argument
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    # the input’s and output’s names must end in .jpg, .jpeg, or .png, case-insensitively
    # get input & output suffixes
    x = os.path.splitext(sys.argv[1])
    y = os.path.splitext(sys.argv[2])
    # case insensitively
    suf1 = x[1].lower()
    suf2 = y[1].lower()
    # # compare to check if the extensions are the same

    extensions = ['.jpg', '.jpeg', '.png']
    if suf1 in extensions and suf2 in extensions:
        if suf1 == suf2:
            pass
        else:
            sys.exit('Input and output have different extensions')
    else:
        sys.exit('Invalid output')


if __name__ == "__main__":
    main()
