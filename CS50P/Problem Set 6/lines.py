import sys


def main():
    if len(sys.argv) == 1:
        sys.exit('Too few command-line arguments')
    if len(sys.argv) > 2:
        sys.exit('Too many comand-line arguments')

    if len(sys.argv) == 2:
        # len is correct
        name = sys.argv[1]
        if name.endswith('.py'):
            # we have a python file here
            try:
                with open(name, 'r') as file:
                    total = 0
                    for line in file:
                        if line.isspace():
                            pass
                        elif line.lstrip().startswith('#'):
                            pass
                        else:
                            total += 1
                    # stripped_line = line.lstrip()
                    # if stripped_line.startswith('#'):
                    #     pass
                    # elif stripped_line is None:
                    #     pass
                    # else:
                    #     total += 1
                print(total)

            except FileNotFoundError:
                sys.exit('File does not exist')
        else:
            sys.exit('Not a Python file')
    # check if it's a python file
    # check if exists


if __name__ == "__main__":
    main()

