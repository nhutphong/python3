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


if __name__ == '__main__':
    pass
