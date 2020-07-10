def squirrel(x):
    if x>=0:
        fac = 1
        for i in range(1, x+1):
            fac = fac*i
        faclist = [f for f in str(fac)]
        return int(faclist[0])
    else:
        return None

# print(squirrel(int(input())))