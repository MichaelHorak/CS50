def einstein(to):
    SOL = 300000000
    Energy = to * pow(SOL, 2)
    print(Energy)


def main():
    einstein(int(input("Please enter mass as an integer: ")))

main()