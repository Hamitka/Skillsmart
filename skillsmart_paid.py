s = ''
lstChanges = []
lstChangesBackup = lstChanges
varUndo = False

def BastShoe(strCommand):
    global s, lstChanges, lstChangesBackup, varUndo

    def my_add(act, S):
        S += act
        return S

    def my_del(Num, S):
        S = S[:len(S) - int(Num)]
        return S

    def my_get(i, s):
        if i.isdigit():
            i = int(i)
            if i >= len(s):
                return ''
            else:
                return s[i]
        else:
            return s

    def my_undo(lst):
        if len(lst) > 1:
            lst.pop()
            return lst[len(lst) - 1]
        else:
            return lst[0]

    def my_redo(lst, lstBackup):
        deltaLen = (len(lstBackup) - len(lst))
        # print ('list', lst)
        # print ('BU', lstBackup)
        # print(deltaLen)
        if deltaLen > 0:
            lst = lstBackup[:len(lstBackup) - deltaLen + 1]
            return lst[len(lst) - 1], lst
        else:
            return lst[len(lst) - 1], lst

    dctMenu = {'1': my_add, '2': my_del, '3': my_get, '4': my_undo, '5': my_redo}

    N = strCommand[:1]
    strCommand = strCommand[2:].strip()
    if N not in dctMenu.keys():
        # print(s)
        return s
    else:
        if N == '1' or N == '2':
            s = dctMenu[N](strCommand, s)
            if varUndo:
                lstChanges = [lstChanges[len(lstChanges) - 1]]
                varUndo = False
            lstChanges += [s]
            lstChangesBackup = lstChanges[:]
            # print(s)
            return s
        elif N == '3':
            # print(dctMenu[N](strCommand, s))
            return dctMenu[N](strCommand, s)
        elif N == '4':
            s = dctMenu[N](lstChanges)
            varUndo = True
            # print(s)
            return s
        elif N == '5':
            s, lstChanges = dctMenu[N](lstChanges, lstChangesBackup)
            # print(s)
            return s
        # print(lstChanges)

    # while True:
    #     Ncommand = input()
    #     N = Ncommand[:1]
    #     Ncommand = Ncommand[2:]
    #     if N not in dctMenu.keys():
    #         print(s)
    #         return s
    #     else:
    #         if N == '1' or N == '2':
    #             s = dctMenu[N](Ncommand, s)
    #             if varUndo:
    #                 lstChanges = [lstChanges[len(lstChanges) - 1]]
    #                 varUndo = False
    #             lstChanges += [s]
    #             lstChangesBackup = lstChanges[:]
    #             print(s)
    #         elif N == '3':
    #             print(dctMenu[N](Ncommand, s))
    #         elif N == '4':
    #             s = dctMenu[N](lstChanges)
    #             varUndo = True
    #             print(s)
    #         elif N == '5':
    #             s, lstChanges = dctMenu[N](lstChanges, lstChangesBackup)
    #             print(s)
    #         print(lstChanges)

# print (BastShoe('1 ghbdtn'))
# lstTest = []
# lstTest +=[BastShoe('1 Привет ')]   #В текущей строке будет "Привет"
# lstTest +=[BastShoe('1  , Мир!')]   #Привет, Мир!
# lstTest +=[BastShoe('1 ++')]       #Привет, Мир!++
# lstTest +=[BastShoe('2 2')]         #Привет, Мир!
# lstTest +=[BastShoe('4')]           #Привет, Мир!++
# lstTest +=[BastShoe('4')]           #Привет, Мир!
# lstTest +=[BastShoe('1 *')]         #Привет, Мир!*
# lstTest +=[BastShoe('4')]           #Привет, Мир!
# lstTest +=[BastShoe('4 ')]          #Привет, Мир!
# lstTest +=[BastShoe('4')]           #Привет, Мир!
# lstTest +=[BastShoe('3 6')]         #,
# lstTest +=[BastShoe('2 100')]       #
# lstTest +=[BastShoe('1 Привет')]    #Привет
# lstTest +=[BastShoe('1  , Мир!')]   #Привет, Мир!
# lstTest +=[BastShoe('1 ++ ')]       #Привет, Мир!++
# lstTest +=[BastShoe('4')]           #Привет, Мир!
# lstTest +=[BastShoe('4')]           #Привет
# lstTest +=[BastShoe('5')]           #Привет, Мир!
# lstTest +=[BastShoe('4')]           #Привет
# lstTest +=[BastShoe('5')]           #Привет, Мир!
# lstTest +=[BastShoe('5')]           #Привет, Мир!++
# lstTest +=[BastShoe('5')]           #Привет, Мир!++
# lstTest +=[BastShoe('5')]           #Привет, Мир!++
# lstTest +=[BastShoe('4')]           #Привет, Мир!
# lstTest +=[BastShoe('4')]           #Привет
# lstTest +=[BastShoe('2 2')]         #Прив
# lstTest +=[BastShoe('4')]           #Привет
# lstTest +=[BastShoe('5')]           #Прив
# lstTest +=[BastShoe('5')]           #Прив
# lstTest +=[BastShoe('5')]           #Прив
#
# print (*lstTest, sep='\n')