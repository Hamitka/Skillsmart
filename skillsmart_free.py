def ConquestCampaign(N, M, L, list):
    pole = [[0 for x in range(M)] for y in range(N)]
    batx = [i - 1 for i in list[::2]]
    baty = [i - 1 for i in list[1::2]]

    for i in range(len(batx)):
        pole[batx[i]][baty[i]] = 1

    for d in range(1, N + M - 1):
        for i in range(N):
            for j in range(M):
                if pole[i][j] == d:
                    for di in range(-1, 2, 2):
                        ai = i + di
                        if 0 <= ai < N and pole[ai][j] == 0:
                            pole[ai][j] = d + 1
                    for dj in range(-1, 2, 2):
                        aj = j + dj
                        if 0 <= aj < M and pole[i][aj] == 0:
                            pole[i][aj] = d + 1
    # [print(i) for i in pole]
    return max([max(i) for i in pole])

# N = 30
# M = 4
# L = 2
# battalion = [2,2, 3,4]
#
# print (ConquestCampaign(N, M, L, battalion))