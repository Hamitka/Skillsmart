def WordSearch(lenght, s, subs):
    # listS = [s[x:x+lenght] for x in range(0, len(s), lenght)]
    listS = [[word[x:x+lenght] for x in range(0, len(word), lenght)] for word in s.split()]
    listS = [item for sublist in listS for item in sublist ]
    listNewS=[]
    listLenS = [(len(w)+1) for w in listS]

    x=0
    while x < len(listLenS):
        y = 1
        while sum(listLenS[x:x+y]) <= lenght+1:
            y += 1
            if y >= lenght/2:
                break
        listNewS+= [listS[x:x+y-1]]
        x=x+y-1
    listFind = [1 if subs in i else 0 for i in listNewS]

    return listFind

# lenghtE = 12
# s = 'строка разбивается на набор строк     через выравнивание по заданной ширине.'
# subs = 'на'
# print (*WordSearch(lenghtE, s, subs))
