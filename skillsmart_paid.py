def TreeOfLife(H, W, N, lstField: list):
    def clearPeerArray(lst: list):
        lstCopy = [x[:] for x in lst]
        for i in range(len(lst)):
            for j in range(len(lst[i])):
                if lstCopy[i][j] >= 3:
                    for di in range(-1, 2):
                        ai = i + di
                        if 0 <= ai < len(lst):
                            lst[ai][j] = 0
                    for dj in range(-1, 2):
                        aj = j + dj
                        if 0 <= aj < len(lst[i]):
                            lst[i][aj] = 0
        return lst

    lstField = [[0 if n == '.' else 1 for n in i] for i in lstField]
    for i in range(1, N + 1):
        lstField = [[i + 1 for i in sublist] for sublist in lstField]
        if i % 2 == 0:
            clearPeerArray(lstField)
    # print (*lstField)
    lstField = [''.join(['.' if i == 0 else '+' for i in sublist]) for sublist in lstField]
    # print(*lstField)
    return lstField

# print(TreeOfLife(3, 4, 12, [".+..","..+.",".+.."]))
# TreeOfLife(3, 4, 12, [".+..",".+..",".+.."])
