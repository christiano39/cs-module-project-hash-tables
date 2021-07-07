import itertools

"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

d = {}
for i in q:
    d[i] = f(i)

combs = list(itertools.product(q, repeat=4))

for c in combs:
    if d[c[0]] + d[c[1]] == d[c[2]] - d[c[3]]:
        print(f"f({c[0]}) + f({c[1]}) = f({c[2]}) - f({c[3]})    {d[c[0]]} + {d[c[1]]} = {d[c[2]]} - {d[c[3]]}")