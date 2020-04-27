import itertools as it


"""
product('ABCD', repeat=2)

    AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD

permutations('ABCD', 2) => hoan vi nhung NO duplicate

    AB AC AD BA BC BD CA CB CD DA DB DC 

combinations('ABCD', 2) => NO duplicate va ko hoan vi

    AB AC AD BC BD CD

combinations_with_replacement('ABCD', 2) => them duplicate va NO hoan vi

    AA AB AC AD BB BC BD CC CD DD
"""

def gens(): # vo tan
    n=0
    while True:
        yield n
        n+=2

gen = gens()
print(list(next(gen) for _ in range(5)))