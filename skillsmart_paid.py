def Keymaker(k:int) -> str:
    lst_door = ['0' for _ in  range(k)]
    for i in range(1, k+1):
        for j in range(i-1, k, i):
            lst_door[j] = '1' if lst_door[j] == '0' else '0'
    return ''.join(lst_door)

# for i in range(51):
#     print (Keymaker(i))
