def main():
    coke = 50
    accepted = [25, 10, 5]

    # while coke > 0
    while coke > 0:
        # ask for coins
        coin = int(input("Insert Coin: "))
        # check if coins is valid entry (25, 10, 5)
        if coin in accepted:
            # if coin < coke
            if coin < coke:
                #   return coke - coin (Amount Due:)
                coke = coke - coin
                due = str(coke)
                print(f"Amount Due: {due}")
            # if coin >= coke
            else:
                owed = coin - coke
                print(f"Change owed: {owed}")
                break

    #   return Change Owed:
        else:
            print(f"Amount Due: {coke}")

main()
