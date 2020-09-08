"""""
Program to calculate and display a users's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over the bonus is 15%.
"""""

sales = float(input("Please enter the users sales: "))

while sales > 0:
    if sales >=1000:
        bonus= sales * 0.15
        print("the total sales is over $1000 giving the user sales to 15% bonus totaling ${}".format(bonus))
        sales = float(input("Please enter the users sales: "))

    elif sales <=1000:
        bonus= sales * 0.10
        print("the total sales is less than $1000 giving the user sales to 10% bonus totaling ${}".format(bonus))

    else:
        print("You have entered an incorrect value. GoodBye.")