from prac6.guitar import Guitar

GUITAR_LIST = []


def main():
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        GUITAR_LIST.append(guitar_to_add)
        print(guitar_to_add, "added.")
        name = input("Name: ")

    '''
    List test, uncomment if needed
    '''
    # GUITAR_LIST.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # GUITAR_LIST.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if GUITAR_LIST:
        GUITAR_LIST.sort()
        print("These are my guitars:")
        for i, guitar in enumerate(GUITAR_LIST):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = "(vintage)"
            print("Guitar {0}: {1.name:>30} ({1.year}), worth ${1.cost:10,.2f}\
             {2}".format(i + 1, guitar, vintage_string))
    else:
        print("No guitars :( Quick, go and buy one!")


main()