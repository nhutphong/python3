def outer():
    def inner():
        # chi co effect tren var in function 
        nonlocal x
        x = "nonlocal"
        print("inner:", x) # update x='nonlocal'
        print("inner: id: ", id(x)) # update x='nonlocal'

    x = 'nonlocal'
    print("id: ", id(x))
    inner()
    print("outer:", x) # update x='nonlocal'

print(f"{'nonlocal':-^80}")
outer()
print(f"{'nonlocal':-^80}")


def foo():
    x = 20

    def bar():
        global x # outside function  update x=25
        x = 100
        print("id: ", id(x))
    
    print("Before calling bar: ", x) #  x=20 local
    print("Calling bar now")
    bar()
    print("After calling bar: ", x) # x=20 local
    print("id: ", id(x))

# x = 20
print(f"{'global':-^80}")
foo()
print("x in main: ", x) # outside function x=25
print(f"{'global':-^80}")