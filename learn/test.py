import time
import datetime
import os
import tkinter
import random
import sys
import threading
import asyncio
# import scapy.all as scapy
# from scapy.layers import http
# from scapy_http import http

def recursion(start, end):

    if start == end:
        return start

    return start + recursion(start+1, end)


def recursion_pro(start, end):

    if start == end:
        return start

    return start * recursion_pro(start-1, end)


# cuu phap de xem them type cua cac variable va return cua funciton | method
'''def greeting(name: str, x: int, y: int) -> int:
    print(f"Hello {name}")
    print(f"{greeting.__annotations__}")
    return x+y'''


def menu(lw, rw, data={}):
    print('menu'.center(lw+rw, '-'))
    for k, v in data.items():
        print(k.ljust(lw, '.') + str(v).rjust(rw, ' '))


def de(row=['row1', 'row2', 'row3', ], col=6):
    lend = []

    for r in range(len(row)):
        ltemp = []

        for c in range(1, col):
            ltemp.append(c)

        ltemp.insert(0, row[r])
        lend.append(ltemp)
    return lend


def dispatch_dict(key_operator, x, y):
    return {
        'cong': lambda: x+y,
        'tru': lambda: x-y,
        'nhan': lambda: x*y,
        'chia': lambda: x/y,
    }.get(key_operator, lambda: None)()


def print_board(board):
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' | ')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' | ')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' | ')


def print_choice(board):
    choice = int(input('1-9: '))
    if board[choice-1] == ' ':
        board[choice-1] = 'X'


def player_choice(player1=True,):
    if not player1:
        return 'O'
    return 'X'


def control_board():
    board = [' ' for row in range(9)]

    while True:
        print()
        print_board(board)
        print()
        print_choice(board)
        print()


def wrapper_local():
    set_range = 5

    def a():
        for row in range(set_range):
            print(row)
    return a

def check_dir():
    for root, folders, files in list(os.walk('.')):
        print(root)
        print(folders)
        print(files)
        print(end='\n'*2)


def tkin():
    tk = tkinter.Tk()
    frame = tkinter.Frame(tk, relief='ridge', borderwidth=2)
    frame.pack(fill='both',expand=1)

    label = tkinter.Label(frame, text="Hello, World")
    label.pack(fill='x', expand=1)

    button = tkinter.Button(frame,text="Exit",command=tk.destroy)
    button.pack(side='bottom')

    tk.mainloop()


def sort_list_tups(source=[]):
    list_tups = source

    for row1 in range(len(list_tups)-1):
        for row2 in range(row1+1,len(list_tups)):
            if list_tups[row1][1] > list_tups[row2][1]:
                list_tups[row1], list_tups[row2] = list_tups[row2], list_tups[row1]
    return list_tups


def sort_list(source=[]):
    lis = source

    for row1 in range(len(lis)-1):
        for row2 in range(row1+1,len(lis)):
            if lis[row1] > lis[row2]:
                lis[row1], lis[row2] = lis[row2], lis[row1]
    return lis


def check_time(number=1000000):
    start = time.time()
    print(f"Let gooooooo")
    llist = [x**2 for x in range(number)]
    print(f"Total: {time.time() - start}")


def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Dang trong wrapper() -> {args}")
        full_name = args[0] + ' ' + args[1]
        return func(full_name)

    return wrapper


@decorator
def my_name(full_name):
        return f"My name is {full_name}"


def auto_int(start=0, end=10, stop=0):
    is_active = True

    while is_active:
        choice = random.randint(start, end)

        if choice == stop:
            is_active = False
        else:
            print(f"automatic: {choice:-^20}")


def bang_cuu_chuong():
    for row in range(1,10):
        print()

        for col in range(1,10):
            print(f"{row*col:<4}",end='')


def time_test():
    for x in range(100):
        print(f"{x}%", end='\r')
        time.sleep(.1)

def time_test_2():
    sys.stdout.write('['+' '*10+']  0%')
    sys.stdout.flush()
    for i in range(10):
        time.sleep(1)
        sys.stdout.write('\b'*(15-i) + '=')
        if(i < 9):
            sys.stdout.write('>')
        sys.stdout.write(' '*(8-i) + '] ' + str(i+1) + '0%')
        sys.stdout.flush()
    # overwrite the percentage sign and write Done instead
    sys.stdout.write('\b\b\b\bDone!\n')


def clock():
    while True:
        print(datetime.datetime.now().strftime("%H:%M:%S"), end=
            '\r')
        time.sleep(1)


# def sniff(interface):
#     scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


# def process_sniffed_packet(packet):
#     if packet.haslayer(http.HTTPRequest):
#         url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
#         print(url)

#         if packet.haslayer(scapy.Raw):
#             load = packet[scapy.Raw].load
#             keywords = ['username', 'user', 'login', 'password', 'pass']
#             if key in keywords:
#                 if key in load:
#                     print(load)


def find_div(inrange, div_by):
    print(f"start num range({inrange}) / {div_by}")
    located = []

    for i in range(inrange):
            if i%div_by == 0:
                located.append(i)

    print(f"done range({inrange}) / {div_by}")
    return located


def fib_all(stop=10, mode='cong'):
    MODE = "cong tru nhan chia".split()
    choice = mode

    if choice not in MODE:
        raise("error modeeeeeeeeeeeeee")
    if stop==1:
        return 1
    if choice == 'cong':
        return stop + fib_all(stop-1, mode=choice)
    elif choice == 'tru':
        return stop - fib_all(stop-1, mode=choice)
    elif choice == 'nhan':
        return  stop * fib_all(stop-1, mode=choice)
    else:
        return stop / fib_all(stop-1, mode=choice)


def show(rowdf=1000):
    if rowdf <= 1000:
        print(f"{'':=>56}")

        print(' '*6, end='')
        for _ in range(1, 11):
            print(f"{_:>5,}", end='')
        print()

        print(f"{'':->56}")

        for row in range(1,rowdf):

            col_end = row * 10
            col_start = col_end - 10

            print(f"{row:<5}|", end='')
            for col in range(col_start, col_end):
                print(f"{col:>5}",end='')
            print(end='\n'*2)


        print(f"{'':->56}")
    else:
        print(f"{rowdf} > 1000 very big ")

if __name__ == '__main__':
    pass
