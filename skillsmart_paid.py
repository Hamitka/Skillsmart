def Unmanned(L, N, traffic_light):
    timeWay = 0
    for tl in traffic_light:
        if (tl[0] + timeWay)%(tl[1]+tl[2]) in range (1, tl[1]+1):
            timeWay += (tl[1] - (tl[0] + timeWay)%(tl[1]+tl[2]))

    return timeWay + L

#
# L1 = 10
# N1 = 1
# traffic_l1 = [[3, 5, 5], [5, 2, 2]]
# traffic_l2 = [[5, 55, 5]]
# traffic_l3 = [[3, 6, 2], [6, 2, 2]]
# traffic_l4 = [[6, 2, 2]]
# traffic_l5 = [[1, 2, 2]]
# print(Unmanned(L1, N1, traffic_l1))
# print(Unmanned(L1, N1, traffic_l2))
# print(Unmanned(L1, N1, traffic_l3))
# print(Unmanned(L1, N1, traffic_l4))
# print(Unmanned(L1, N1, traffic_l5))
