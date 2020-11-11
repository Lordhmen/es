import itertools

q = list(itertools.permutations('пар', r=3))
n = 0
letters_word = []
for i in range(len(q)):
    q[n] = list(q[n])
    n += 1

print(q, len(q))
