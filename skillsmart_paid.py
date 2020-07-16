def UFO(N, data, octal):
    def from8to10(d):
        list8D =[int(i) for i in str(d)]
        r = len(list8D)
        list10D = [list8D[i]*8**(r-1-i) for i in range(r)]
        return sum(list10D)

    def from16to10(d):
        list16D =[int(i) for i in str(d)]
        r = len(list16D)
        list10D = [list16D[i]*16**(r-1-i) for i in range(r)]
        return sum(list10D)

    if octal:
        return [from8to10(i) for i in data]
    else:
        return [from16to10(i) for i in data]


# data1 = [1234, 1777]
# N1 = len(data1)
# print (UFO(N1, data1, octal=False))
#
# data2 = [1234, 1777]
# N2 = len(data2)
# print (UFO(N2, data2, octal=True))
