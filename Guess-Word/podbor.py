from random import randint


def shuffle(arr):
    for n in range(len(arr) - 1):
        rnd = randint(0, (len(arr) - 1))
        val1 = arr[rnd]
        val2 = arr[rnd - 1]

        arr[rnd - 1] = val1
        arr[rnd] = val2

    return arr

podbor = []
q = [randint(0, 3) for i in range(4)]
podbor.append(q)
while len(podbor) != 24:
    q = {randint(0, 3) for i in range(4)}
    while len(q) != 4:
        q |= {randint(0, 3) for i in range(4)}
    q = shuffle(list(q))
    n = 0
    for j in range(len(podbor)):
        if podbor[n] == q:
            break
        n += 1
    if len(podbor) == n:
        podbor.append(q)
print(podbor)

