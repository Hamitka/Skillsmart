def SynchronizingTables(N, listID, listSalary):
    dictOfSalary = dict(zip(sorted(listID), sorted(listSalary)))
    return [dictOfSalary[i] for i in listID]

# listOfID = [50, 1, 1024, 2]
# listOfSalary = [20000, 100000, 90000, 20000]
#
# print(SynchronizingTables(3, listOfID, listOfSalary))

