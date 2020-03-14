class Fib:
    """docstring for Fib"""
    # def __init__(self,n):
    # self.n = n

    def fib(self, n):
        self.n = n
        if self.n == 1:
            return 1
        return self.n * Fib().fib(self.n - 1)


def fib_add_for(n):
    c = 0
    for i in range(1, n + 1):
        c += i
    return c


def fib_multi_for(n):
    c = 1
    for i in range(1, n + 1):
        c *= i
    return c


def fib_add_while(n):
    c = 0
    while n >= 1:
        c += n
        n -= 1
    return c


def fib_multi_while(n):
    c = 1
    while n > 1:
        c *= n
        n -= 1
    return c


def fibo(n):
    a, b = 0, 1
    ls = []
    for _ in range(n):
        ls.append(a)
        c = a+b
        a = b
        b = c
    return ls


def main():
    pass


if __name__ == '__main__':
    pass
