def odometer(listOksana):
    listSpeed = [i for i in listOksana[::2]]
    listHour = [0] + [i for i in listOksana[1::2]]
    listHour = [listHour[i] - listHour[i-1] for i in range(1, len(listHour))]
    return sum([listSpeed[i]*listHour[i] for i in range(len(listHour))])

# listTest = [20,2,30,6,10,7]
# print (odometer(listTest))
# print(squirrel(int(input())))