def TransformTransform(lst:list, N:int):
    def sA(lstA:list):
        lstB = []
        N = len(lstA)
        for i in range(N):
            for j in range(N-i):
                k = i + j
                lstB += [max(lstA[j:k+1])]
        return lstB
    return sum(sA(sA(lst)))%2 == 0

# print(TransformTransform([1, 2, 3, 4, 5, 6, 7], 7))
# print(TransformTransform([3, 2, 1], 7))