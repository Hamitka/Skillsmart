def MaximumDiscount(N, price):
    price.sort()
    price = price[::-1]
    lenP = len(price)
    listDiscount = [price[x:x + 3] for x in range(0, lenP, 3)]
    listDiscountSum = [min(sublist) for sublist in listDiscount if len(sublist) == 3]
    # listDiscountSum = [min(sublist) if len(sublist) == 3 else -sum(sublist) for sublist in listDiscount]
    return sum(listDiscountSum)

# price1 = [250, 100, 300, 400, 200, 150, 350]
# N1 = len(price1)
# print(MaximumDiscount(N1, price1))
