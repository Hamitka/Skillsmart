def game():
    listofdictgame = []
    n = int(input())
    for i in range(n):
        c1, g1, c2, g2 = input().split(';')
        listcommand = [c1, c2]
        listgoal = [int(g1), int(g2)]
        # dictgame = dict(zip(listgame[i][::2], listgame[i][1::2]))
        listofdictgame += [dict(zip(listcommand, listgoal))]
    setgame = set([item for d in listofdictgame for item in d])
    dictgame = {key: [0,0,0,0,0] for key in setgame}
    for key1, key2 in [d.items() for d in listofdictgame]:  #каким то макаром получили списки из key+value
        dictgame[key1[0]][0] = dictgame[key1[0]][0]+1   #всего игр 1я команда
        dictgame[key2[0]][0] = dictgame[key2[0]][0]+1   #всего игр 2я команда
        #здесь и далее подсчет результатов игры:
        if key1[1] > key2[1]:
            dictgame[key1[0]][1] = dictgame[key1[0]][1] + 1     #Побед 1я команда
            dictgame[key2[0]][3] = dictgame[key2[0]][3] + 1     #Поражений 2я команда
            dictgame[key1[0]][4] = dictgame[key1[0]][4] + 3    #Очков 1я команда
        elif key1[1] < key2[1]:
            dictgame[key2[0]][1] = dictgame[key2[0]][1] + 1      #Побед 2я команда
            dictgame[key1[0]][3] = dictgame[key1[0]][3] + 1     #Поражений 1я команда
            dictgame[key2[0]][4] = dictgame[key2[0]][4] + 3    #Очков 2я команда
        else:
            dictgame[key1[0]][2] = dictgame[key1[0]][2] + 1      #Ничья 1я команда
            dictgame[key1[0]][4] = dictgame[key1[0]][4] + 1    #Очков 1я команда
            dictgame[key2[0]][2] = dictgame[key2[0]][2] + 1      #Ничья 2я команда
            dictgame[key2[0]][4] = dictgame[key2[0]][4] + 1    #Очков 2я команда
    # print(listofdictgame)
    for key, val in dictgame.items():
        print ((key+':'), *val, end='\n')
    return dictgame
game()
