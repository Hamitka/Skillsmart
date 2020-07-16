def Unmanned(L, N, traffic_light):
    def traffLighterRed(wayLenght, traffOneL):
        time = traffOneL[1]
        way = [i for i in range(1, wayLenght+1)]
        traff  = [list(way[x:x+time]) for x in range(0, wayLenght, time)]
        traffRed = [item for sublist in traff[0::2] for item in sublist]
        return traffRed
    timeWay = 0
    for tl in traffic_light:
        lighter = traffLighterRed(L, tl)
        if tl[0]+timeWay in lighter:
            timeWay+=max(lighter)-tl[0]

    return timeWay+L

# L1 = 10
# N1 = 2
# traffic_l1 = [[5, 5, 5], [2, 2, 2]]
# print(Unmanned(L1, N1, traffic_l1))