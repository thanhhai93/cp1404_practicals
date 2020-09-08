def main():
    total_price= 0
    item_prices= []
    count= 1
    amount_items = int(input("Number of items:"))

    for i in range(1,amount_items +1 ):
        item_price= float(input("price of item:"))
        item_prices.append(item_price)
        total_price= total_price + item_price

    if total_price > 100:
        total_price = total_price - (total_price * 0.10)
    else:
        pass

    print("Total price for {} items is ${:.2f} ".format(amount_items, total_price))
main()