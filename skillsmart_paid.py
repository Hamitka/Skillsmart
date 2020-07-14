def TheRabbitsFoot(s, encode=True):
    def listTransponse(listIn):
        listOut = [[''] * len(listIn) for i in range(len(listIn) + 1)]
        for i in range(len(listIn)):
            for j in range(len(listIn[i])):
                try:
                    listOut[j][i] = listIn[i][j]
                except IndexError:
                    continue
        listOut = [''.join(i) for i in listOut]
        # print(listOut)
        return listOut

    if encode == True:
        s = s.replace(' ', '')
        sqrtS = len(s) ** .5
        upLimit = int(sqrtS + 3 / 10 + 3 / 10 + 3 / 10 + 0.1)
        listMatrixS = [list(s[x:x + upLimit]) for x in range(0, len(s), upLimit)]
        listCode = listTransponse(listMatrixS)

        # print(listMatrixS)
        return ' '.join(listCode)
    else:
        listDeCode = listTransponse(s.split())
        return ''.join(listDeCode)


# s = 'отдай мою кроличью лапку, щенок, она нужна'
# lenS = len(s.replace(' ', ''))
# print(lenS, lenS ** .5)
#
# print(TheRabbitsFoot(s, False))
# print(TheRabbitsFoot(TheRabbitsFoot(s, True), False))
# print (s.replace(' ', '').strip())
# print ((TheRabbitsFoot(TheRabbitsFoot(s, True), False))==(s.replace(' ', '').strip()))
