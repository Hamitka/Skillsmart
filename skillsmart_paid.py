def MatrixTurn(lst:list, M:int, N:int, T:int):
    # print (id(lst), *lst, sep='\n')
    # print()
    lstRotate = [list(i) for i in lst]
    # print(*lstRotate, sep='\n')

    def kontur(lst):
        n, m = len(lst), len(lst[0])
        numK = min(n, m)//2
        lstOfKontur = [[] for _ in range(numK)]
        lstOfXYKontur = [[] for _ in range(numK)]
        for k in range(numK):
            dx, dy = n-k-1, m-k-1
            for i in range(k, dx):
                lstOfKontur[k] += lst[i][k]
                lstOfXYKontur[k] += [(i, k)]
            for j in range(k, dy):
                lstOfKontur[k] += lst[dx][j]
                lstOfXYKontur[k] += [(dx, j)]
            for i in range(dx, k, -1):
                lstOfKontur[k] += lst[i][dy]
                lstOfXYKontur[k] +=[(i, dy)]
            for j in range(dy, k, -1):
                lstOfKontur[k] += lst[k][j]
                lstOfXYKontur[k] += [(k, j)]
        return lstOfKontur, lstOfXYKontur
    lstKontur, lstXYKontur = kontur(lstRotate)
    lstKontur = [sublist[T:]+sublist[:T] for sublist in lstKontur]

    for k, val in enumerate(lstXYKontur):
        for u, tup in enumerate(val):
            lstRotate[tup[0]][tup[1]] = lstKontur[k][u]
    # print(*lstRotate, sep='\n')
    lst[:]= [''.join(sublist) for sublist in lstRotate]
#     print(id(lst), *lst, sep='\n')
#     print()
#
# listTest = ["023456", "234567", "345678", "156789"]
# MatrixTurn(listTest, 4, 6, 3)
# print (id(listTest), *listTest, sep='\n')
