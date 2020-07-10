def odometer(listOksana):
    listSpeed = [i for i in listOksana[::2]]
    return sum(listSpeed)

# listTest = [10,1,20,2, 30, 3, 40, 4]
# print (odometer(listTest))
# print(squirrel(int(input())))