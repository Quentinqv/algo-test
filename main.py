# 1 concours par jour
# Concours consécutifs
# Gain différent pour chaque concours
# N concours consécutifs
# Les concours commencent le 1er du mois
# Au bout de X concours, on doit s'arrêter pour se reposer
from time import sleep

# Il faut retirer les jours déjà joués, et ceux connus comme repos. Il faut ensuite recalculer la row la plus intéressante avec ces paramètres.

tests = [
    [
        [13, 2, 15, 17, 19, 33, 2, 2, 2, 2],
        4
    ],
    [
        [13, 12, 11, 9, 16, 17, 100],
        3
    ],
    [
        [12, 14, 52, 7, 3, 1, 1, 89, 98, 100, 12, 5, 6, 8],
        4
    ],
    [
        [10, 12, 11, 9, 17, 8, 13],
        2
    ],
    [
        [20, 30, 27, 24, 23, 28, 33, 38, 34, 35],
        10
    ]
]

def getBestXRows(gains, x, forbidden):
    """
    For now, returning 0, 0, 0 is when no row is possible
    :param gains:
    :param x:
    :param forbidden:
    :return:
    """
    if len(gains) == x and len(forbidden) == 0:
        return sum(gains), 0, x-1

    copy = gains.copy()
    # replace all forbidden days by -1
    for i in forbidden:
        copy[i] = -1

    # Check if a row of x days is possible with the forbidden days
    isPossible = False
    for i in range(len(gains)-x):
        if i in forbidden:
            continue
        if -1 in copy[i:i+x]:
            continue
        else:
            isPossible = True
            break

    if not isPossible:
        return 0, 0, 0

    # Find the best row with no forbidden days
    best = 0
    minI = 0
    maxI = 0
    for i in range(len(gains)-x+1):
        if i in forbidden:
            continue
        s = sum(gains[i:i+x])
        print("Sum: {}".format(s) + " - " + str(gains[i:i+x]) + " - " + str(i) + " - " + str(i+x))
        if s > best:
            best = s
            minI = i
            maxI = i+x

    return best, minI, maxI-1

def sumGains(gains, forbidden, alreadyWon):
    """
    Sum all gains that are not forbidden but sum the ones that are already won
    :param gains:
    :param forbidden:
    :return:
    """
    listToSum = []
    for i in range(len(gains)):
        if i in forbidden:
            continue
        else:
            listToSum.append(gains[i])


    for i in alreadyWon:
        listToSum.append(gains[i])

    print("List to sum: {}".format(listToSum))
    return sum(listToSum)


for test in tests:
    print("Test: {}".format(test))
    gains = test[0]
    x = test[1]
    forbidden = []
    alreadyWon = []
    best, minI, maxI = getBestXRows(gains, x, forbidden)
    while best != 0:
        print("Best row: {} - {} - {}".format(best, minI, maxI))
        if minI-1 < len(gains):
            forbidden.append(minI-1)
        if maxI+1 < len(gains):
            forbidden.append(maxI+1)
        # ajout des jours interdits entre minI et maxI
        for i in range(minI-1, maxI+1):
            if i not in forbidden:
                forbidden.append(i)
                alreadyWon.append(i)
        best, minI, maxI = getBestXRows(gains, x, forbidden)
        print("Forbidden: {}".format(forbidden))
        print("Already won: {}".format(alreadyWon))
        # sleep(2)
    print("No more rows possible")
    print("Sum of gains: {}".format(sumGains(gains, forbidden, alreadyWon)))
    print()
