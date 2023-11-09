

def stoneGameIX(stones: list) -> bool:
    dStones = {0: 0, 1: 0, 2: 0}
    for i in stones:
        dStones[i % 3] += 1

    if dStones[1] + dStones[2] == 0:
        return False    # Alice输

    dStones[0] = dStones[0] % 2
    iMin = min(dStones[1], dStones[2])
    if iMin:
        dStones[1] -= iMin
        dStones[2] -= iMin
        dStones[1] += 1
        dStones[2] += 1

    if dStones[0] == 1:
        if dStones[1] - dStones[2] > 2 or dStones[2] - dStones[1] > 2:
            return True
    elif dStones[1] == 1 and dStones[2] > 0:
        return True
    elif dStones[2] == 1 and dStones[1] > 0:
        return True
    return False


if __name__ == '__main__':
    print(stoneGameIX([19,2,17,20,7,17]))