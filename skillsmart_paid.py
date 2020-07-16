def Unmanned(L, N, traffic_light):
    def traffLighterRed(wayLenght, traffOneL):
        timeRed = traffOneL[1]
        timeGreen = traffOneL[2]
        way = [i for i in range(1, wayLenght + 1)]
        traff = [list(way[x:x + timeRed]) for x in range(0, wayLenght, timeRed + timeGreen)]
        traffRed = [item for sublist in traff[0::2] for item in sublist]
        return traffRed

    timeWay = 0
    for tl in traffic_light:
        lighter = traffLighterRed(L, tl)
        if tl[0] + timeWay in lighter:
            timeWay += tl[1] - tl[0]

    return timeWay + L


# L1 = 10
# N1 = 1
# traffic_l1 = [[3, 5, 5], [5, 2, 2]]
# traffic_l2 = [[5, 55, 5]]
# print(Unmanned(L1, N1, traffic_l1))
# print(Unmanned(L1, N1, traffic_l2))
