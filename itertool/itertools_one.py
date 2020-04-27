import itertools as it

"""
    infinite iterators

    itertools.count(start=0, step=1)
    itertools.count(start=0, step=1) (1,2,3,4,5,...) vo han

    itertools.cycle(iterable)
    itertools.cycle([1,2,3]) => (1,2,3, 1,2,3, 1,2,3,....) khoang

    itertools.repeat(object[, times])
    itertools.repeat(4) => duplicates(4,4,4,4,.....) or times=8 gioi han 8 items
"""

#count
print('itertools.count')
count = it.count(start=0, step=2)
print(next(count)) #0
print(next(count)) #2
print(next(count)) #4
print()

count = it.count(start=0, step=3)
for _ in range(4):
    print(next(count))

print()

count = it.count(start=0, step=4)
comp = [next(count) for _ in range(5)]
print(comp)
print()



#cycle
print('itertools.cycle')
cycle = it.cycle([1,3,5])
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print()

cycle = it.cycle(('on', 'off'))
comp = [ next(cycle) for _ in range(5)]
print(comp)
print()


#repeat
print('itertools.repeat')
repeat = it.repeat(3)
print(next(repeat))
print(next(repeat))
print(next(repeat))
print(next(repeat))
print()


squares = map(pow, range(10), it.repeat(3))
print(list(squares))
print()