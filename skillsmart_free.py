def SumOfThe(N, listData):
    for i in range(len(listData)):
        if (listData[i] == sum(listData) - listData[i]):
            return listData[i]

# print(SumOfThe(5, [100, -50, 10, -25, 90, -35, 90]))