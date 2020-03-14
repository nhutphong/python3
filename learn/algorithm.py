import math
import os
import sys

""" Tao file algorithm.py
"""

__IMPORTANT__ = """ Tao la algorithm.py
    __private global variable chi dung duoc trong chinh file no
"""

def recursive(n=5):
    if n <= 1:
        return n
    else:
        return n + recursive(n-1)

def add_recursive(n=5):
    if n <= 1:
        return n
    else:
        return add_recursive(n-1) + add_recursive(n-2)

def is_prime(n):
    if n < 2:
        return False
    elif n == 2 or n == 3 or n == 5:
        return True
    elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return False

    for i in range(5, int(n**.5), 2):  # Chỉ kiểm tra các số lẻ n**.5 = can bac 2 cua n
        if n % i == 0:
            return False

    return True


def binary_search(arr, left, right, value):

    # dieu kien arr da duoc sap xep tang
    if left < right:

        mid = left + int((right - left)/2)

        if arr[mid] == value:
            return mid

        elif arr[mid] > value:
            return binary_search(arr, left, mid-1, value)

        else:
            return binary_search(arr, mid+1, right, value)

    else:
        # Element is not present in the array
        return -1

# str.translate


def translate(source, maketran):
    source_list = list(source)

    for old, new in maketran.items():

        for i in range(len(source_list)):
            if ord(source_list[i]) == old:
                source_list[i] = chr(new)

    return ''.join(source_list)

# str.maketrans


def maketrans(old, new):
    old_int = [ord(k) for k in old]
    new_int = [ord(v) for v in new]
    return dict(zip(old_int, new_int))

def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)

        if val not in seen:
            yield item
            seen.add(val)

def invert_dict(dic):
    inverse = dict()
    for key in dic:
        val = dic[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

def percent_of_item(seq):
    total = sum(seq)
    per = 0
    for item in seq:
        per = (item * 100) / total
        per = float(f'{per:,.2f}')
        yield item, per

    yield total,100.00

# sort increase -> buble sort
def sort(iterator, reverse=False):
    if not reverse:
        for current in range(len(iterator)-1):

            for _next in range(current+1, len(iterator)):
                if iterator[current] > iterator[_next]:
                    iterator[current], iterator[_next] = iterator[_next], iterator[current]

            yield iterator[current]

        yield iterator[-1]

    else:

        yield from invert_sort(iterator)

def invert_sort(iterator):
    for current in range(len(iterator)-1):

        for _next in range(current+1, len(iterator)):
            if iterator[current] < iterator[_next]:
                iterator[current], iterator[_next] = iterator[_next], iterator[current]

        yield iterator[current]

    yield iterator[-1]


def clock(delay=1):
    while True:
        current_time = dt.datetime.now()
        current_time_f = current_time.strftime("%H:%M:%S")
        print(current_time_f, end='\r')

        time.sleep(delay)
        

def copy_file_to_file(file_copy, file_append):
    with open(file_copy, 'r') as source:
        copy_source = source.read()

        with open(file_append, 'a+') as file_new:
            print('\n', copy_source, file=file_new)

    return f'{os.path.sep}'.join([os.getcwd(), file_append])


def get_full_files(folder_working):
    files = [file for file in os.listdir(folder_working) if os.path.isfile(file) and not file.startswith('.')]

    return files

def get_files_name_hide_extention(files):
    files_name = [os.path.splitext(filename)[0] for filename in files ]

    return files_name

def get_show_extension_hide_files_name(files):
    extension_names = [os.path.splitext(filename)[1] for filename in files ]

    return extension_names

def set_change_extension_files(files, files_name_hide_ext, new_ext):
    for root_file, file in zip(files, files_name_hide_ext):

        os.rename(root_file, file+new_ext)

def change_extension_files(folder_working, new_ext='.txt'):
    files = get_full_files(folder_working)
    files_name_hide_ext = get_files_name_hide_extention(files)

    set_change_extension_files(files, files_name_hide_ext, new_ext=new_ext)

    return len(files)


def change_name_files(folder_working, new_name):
    files = get_full_files(folder_working)
    count_file = len(files)
    extension_names = get_show_extension_hide_files_name(files)

    set_change_name_files(files, count_file, extension_names, new_name)


def set_change_name_files(files, count_file, extension_names, new_name):
    for file, number, ext in zip(files, range(1,count_file+1), extension_names):
        os.rename(file, new_name + f'_{number}' + ext)


if __name__ == "__main__":
    print(__IMPORTANT__)
    print(__doc__)