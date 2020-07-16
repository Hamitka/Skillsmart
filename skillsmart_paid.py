def MassVote(N, Votes):
    maxV = max(Votes)
    if Votes.count(maxV)>1:
        return 'no winner'
    maxPercent = round(maxV*100/sum(Votes), 2)
    winner = Votes.index(maxV)+1
    if maxPercent>50:
        return 'majority winner '+ str(winner)
    else:
        return 'minority winner ' + str(winner)

# Vote = [60, 10, 10, 15, 5]
# N = len(Vote)
# print(MassVote(N, Vote))
#
# Vote1 = [10, 15, 11]
# N1 = len(Vote1)
# print(MassVote(N1, Vote1))
#
# Vote2 = [111, 111, 110, 110]
# N2 = len(Vote2)
# print(MassVote(N2, Vote2))
