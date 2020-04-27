import itertools as it
import operator


names = ['dung', 'thong', 'heo', 'cho']
print('itertools.zip_longest')
zip_longest = it.zip_longest(range(10), names)
print(list(zip_longest))
print()


print('itertools.startmap')
starmap = it.starmap(pow, [(2,3), (3,2), (10,3)] )
print(list(starmap))
print()


#chain
# noi cac iterators
print('itertools.chain')
letters = ['a', 'b', 'c', 'd']
numbers = [1,2,3]
names = ['dung', 'thong']
chain = it.chain(letters, numbers, names)
print(list(chain))
print()


#itertools.islice(iterable, stop)
#itertools.islice(iterable, start, stop[, step])
# lay khoang iterators  [::]
print('itertools.islice')
islice = it.islice(range(10), 1,8,2)
print(list(islice))
print()

print('file with islice')
with open('zing.txt', 'r') as f:
    islice = it.islice(f, 3)

    for line in islice:
        print(line)


#itertools.compress(data, selectors)
print("itertools.compress")
selectors = [True, True, False, True, False]
# selectors = [1, 1, 0, 1, 0]
names = ['dung', 'thong', 'heo', 'cho', 'haha']

compress = it.compress(names, selectors)
print(list(compress))
print()


def lt_2(n):
    if n < 2:
        return True
    else:
        return False


# lay all items la False
print("itertools.filterfalse")
numbers = [0,1,2,3,2,1,0,7]
filterfalse = it.filterfalse(lt_2, numbers)
print(list(filterfalse))
print()


# khi gap False lay het phan items con lai
print('itertools.dropwhile')
dropwhile = it.dropwhile(lt_2, numbers)
print(list(dropwhile))
print()

# khi gap False bo het phan cuoi, tuc lay phan item dau dung
print('itertools.takewhile')
takewhile = it.takewhile(lt_2, numbers)
print(list(takewhile))
print()



# lien quan toi functions.reduce
#itertools.accumulate(iterable[, func, *, initial=None])¶
numbers = [1,2,3,4,5]
print('itertools.accumulate')
mul = it.accumulate(numbers, operator.mul)
print(list(mul))
print()


print('itertools.groupby')
a_list = [("Animal", "cat"),  
          ("Animal", "dog"),  
          ("Bird", "peacock"),  
          ("Bird", "pigeon")] 
groupby = it.groupby(a_list, lambda x : x[0]) 
  
for key, group in groupby: 
    print(f"key: {key}- group: {list(group)}") 


# 
print('itertools.tee')
numbers = [2, 4, 6, 7, 8, 10, 20]  
    
iterators = it.tee(numbers, 3)
iterables = [list(iterator) for iterator in iterators]
print(iterables)