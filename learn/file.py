import sys
import os
import shutil
from contextlib import contextmanager

__IMPOTANT__=""" 
    'r': read
    'w': overwrite file or new file if file not exist
    'a': write append => them vao cuoi file
    'rb':read binary
    'wb': write binary
    '+': updating reading and writting, vd: r+, w+, a+
"""
def open_file():
    with open('test.txt') as file_obj:
        # print(file_obj.read(5)) # 5 chu dau tien
        # readline() = đọc tới khi gặp /n (xuống dòng) sẽ dừng
        # print(file_obj.readline())
        # readlines() = ['content1.\n', 'content2.\n', .....]
        print(file_obj.readlines())
        file_obj.seek(0)
        print(type(file_obj.readlines()))
        file_obj.seek(0)
        print(len(file_obj.readlines()))
        file_obj.close()


class ManagedFile:
    def __init__(self, filename, mode='r'):
        self.file_name = filename
        self.mode = mode

    def __enter__(self):
        print("__enter__")

        self.open_file = open(self.file_name, self.mode)
        return self.open_file #iterable(line1, line2, ...,)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")

        if self.open_file:
            self.open_file.close()


class MessageWriter(object): 
    def __init__(self, filename, mode='w'): 
        self.file_name = filename
        self.mode = mode
  
    @contextmanager
    def open_file(self):
        print("open_file")

        try: 
            file = open(self.file_name, self.mode) 
            yield file
        finally: 
            file.close() 


def with_file(file_root, file_new='new_file'):
    with open(file_root,) as f:
        content = f.read()

        with open(file_new, 'w') as new:
            # file=new => cho phep print() tao file tu content xuat ra=prompt
            print(content, 'them noi dung vao cuoi file', file=new)


# Python program for creating a 
# context manager using @contextmanager 
# decorator 
def print_flush_true(content, /, delay=.05):

    print("flush=True")
    # flush=True => in tu tren xuong cho time.sleep xong roi in tiep
    # flush=Flase => cho time.sleep xong roi moi in 1 luc tat ca
    for c in content:
        print(c, end='', flush=True)
        time.sleep(delay)

    print()


@contextmanager
def ContextManager(file, mode='r'): 
    
    # Before yield as the enter method 
    print("__enter__ method called") #1
    f = open(file, mode=mode)

    yield f #2 with as
    
    # After yield as the exit method
    f.close()
    print("__exit__ method called") #3

with ContextManager('zing.txt') as file: #2
    print(f"{'with as start':-^85}")

    content = file.read()
    print_flush_true(content)

    print(f"{'with as end':-^85}")


if __name__ == '__main__':
    pass