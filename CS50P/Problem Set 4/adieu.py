import inflect

p = inflect.engine()

mylist = []

while True:
    try:
        item = input("Name: ")
        mylist.append(item)
        # prompt user for names, one per line,
        # until the user inputs ctr+d
    except EOFError:
        # for x in mylist:
        #     print(x)
        print('Adieu, adieu, to ' + p.join(mylist))
        break

        # code to execute once user inputs ctrl+d
        #
        # JOIN WORDS INTO A LIST:
        #
        # mylist = p.join(("apple", "banana", "carrot"))
        # "apple, banana, and carrot"
        #
        # mylist = p.join(("apple", "banana"))
        # "apple and banana"
        #
        # mylist = p.join(("apple", "banana", "carrot"), final_sep="")
        # "apple, banana and carrot"
