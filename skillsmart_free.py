def PatternUnlock(N, listHits):
    #возможно перемудрил..
    pole = [[6, 1, 9], [5, 2, 8], [4, 3, 7]]
    listXY = []
    listWay = []
    g = 2**0.5

    for k in listHits:
        for x, y in enumerate(pole):
            if k in y:
                listXY +=[[x, y.index(k)]]
    for xy in range(1, len(listXY)):
        if (listXY[xy][0] != listXY[xy-1][0] and listXY[xy][1] != listXY[xy-1][1]):
            listWay+=[g]
        else:
            listWay+=[1]
    listWaystr = [s for s in str("{:.5f}".format(sum(listWay))) if '1'<=s<='9']
    waystr = ""
    return waystr.join(listWaystr)

# hits = [1, 2, 3, 4, 5, 6, 2, 7, 8, 9]
# print(PatternUnlock(10, hits))


