def fib(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total


def fib1(n):
    if n == 1:
        return n
    else:
        return n + fib1(n-1)


def for_else(n):
    for r in range(1, n+1):
        print(f"{r:-^10}")
    else:
        print("toi else".center(20, '*'))


def check(n):
    for c in range(2, n):
        for i in range(2, c):
            if c % i == 0:
                print(f"{c:*^15} ko phai la NOOOOOO {i}")
                break
        else:
            print(f"{c:-^20} la ng to kkkkkkkkkkkkkkkk")


def check1(m):
    for n in range(2, m):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)
                break
        else:
         # loop fell through without finding a factor
            print(n, 'is a prime number')


def comprehensions(row, col):
    mang2chieu = [[r, c] for r in range(row) for c in range(col)]
    return mang2chieu


def com1(row):
    ro = [r if r % 2 == 0 else 'chan' for r in range(row)]
    return ro


def try_ex():
    try:
        print("hello try")
        so = input("nhap so: ")
        if not so.isdigit():

            # raise neu khong co except: no se chay va break
            # neu co except thi no nhu label=variable dung trong except
            # v = "2 raise: tao keu nhap so m ngu a: ?????????"
            raise ValueError("2 raise: tao keu nhap so m ngu a: ?????????")
        print("Het TRY")

    except ValueError as v:
        print("except 1: Bị Lỗi Bat dau chay EXCEPT")
        print(v)

    else:
        print("Không có lỗi toi luoc ELSE")

    print("Het Function try_ex()")


def assert_check():
    name = input("Nhap ten ban: ")
    assert name == 'phong', "username khong dung"
    print(f"username cua ban la: {name}")


def process_list(my_list):
    for index in range(len(my_list)):
        my_list[index] *= 2


def process_list_yield(my_list):
    for index in range(len(my_list)):
        yield my_list[index] * 2


def main():
    # a = [1, 3, 5, 7, 9]
    # process_list(a)
    # print(a)

    b = [2, 4, 6, 8, 10]
    for item in process_list_yield(b):
        print(item)


def check_input_int():
    while True:
        try:
            val = int(input("Moi ban nhan so : "))
        except:
            print("Da vao except")
        else:
            print("else : Ban da nhap dung")
            break
        finally:
            print("Da vao finally")

        print("Het try except")


def check_divice_0():
    try:
        num_tren = float(input("nhap so chia: "))
        num_duoi = float(input("so bi chia: "))
        print(f"{num_tren}/{num_duoi} = {num_tren/num_duoi}")

    except (Exception) as err:
        print(f"Loi me roi: {err}")


def ex_raise():
    try:
        your_old = float(input("nhap so tuoi: "))

        if not (0 < your_old < 100):
            raise Exception(your_old)

        print(f"your old: {your_old}")

    except Exception as err:
        print(f"error: invalid your old input {err}")


def main():
    ex_raise()


if __name__ == '__main__':
    main()
