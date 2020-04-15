

def design(func_name=None, letter='#'):
    def function(func):
        def wrapped(*args, **kwargs):
            print(f"{func_name+ ' START ':{letter}^85}")
            fun = func(*args, **kwargs)
            print(f"{func_name+ ' END ':{letter}^85}", end='\n'*2)
            return fun

        return wrapped
        
    return function