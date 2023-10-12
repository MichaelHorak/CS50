import sys
import pyfiglet

font_list = pyfiglet.FigletFont.getFonts()

# Zero command-line arguments if the user would like to output text in a random font.
if len(sys.argv) == 1:
    user_input = input("Input: ")
    print(pyfiglet.figlet_format(user_input))

if len(sys.argv) == 2:
    sys.exit('Invalid usage')

if len(sys.argv) == 3:
    # validate input
    user_font1 = sys.argv[1]
    user_font2 = sys.argv[2]
    if user_font1 == '-f' or user_font1 == '-font':
        if user_font2 in font_list:
            user_input = input("Input: ")
            result = pyfiglet.figlet_format(user_input, font=user_font2)
            print(result)
        else:
            sys.exit('Invalid usage')
    else:
        sys.exit('Invalid usage')
    # first str has to be -f or -font
    # second str has to be a font
    # if failed exit via sys.exit with an error message
    # otherwise print in the requested font
    # set the font
    # sys.exit()
