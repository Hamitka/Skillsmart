def ShopOLAP(N, items):
    items = [int(i) if i.isdigit() else i for s in items for i in s.split()]
    items = [items[x:x+2] for x in range(0, len(items), 2)]
    items = [[str(sublist[0]), sublist[1]] for sublist in items]
    items.sort()
    dictItems = {key[0]: (sum(items[i][1] for i in range(len(items)) if items[i][0] == key[0])) for key in items}
    dictItems = {k: v for k, v in sorted(dictItems.items(), key= lambda x:x[1], reverse=True)}
    listOut = [str(key) + ' ' + str(value) for key, value in dictItems.items()]

    return listOut

# list1 = [['платье1', 5], ['сумка32', 2], ['платье1', 1], ['сумка23', 2], ['сумка128', 4]]
# list1 = ['платье1 5', 'сумка32 2', 'платье1 1', 'сумка23 2', 'сумка128 4']
# N1 = len(list1)
# print(ShopOLAP(N1, list1))
# print (ShopOLAP(5, ["dress1 5", "handbug32 3", "dress2 1", "handbug23 2", "handbug128 4"]))
# print (ShopOLAP(1, []))
# print (ShopOLAP(8, ["123 5", "32 3", "124 5", "128 1", "32 2", "23 4", "128 4", "128 1"]))
