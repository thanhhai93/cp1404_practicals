
def main():
    for i in range(1,21,2):
        print(i, end=' ')
    print()

    for i in range(0, 101, 10):
        print(i, end=' ')
    print()

    for i in range(20,0,-1):
        print(i, end=' ')
    print()

    star_amount= int(input("Please enter the amount of starts:"))
    for i in range(star_amount):
        print('*', end=' ')

    for i in range(0,star_amount +1):
        print('*'* i)
main()