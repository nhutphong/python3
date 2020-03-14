
from tkinter import *

def command_button():
    Label(text='Tao la command_button()').pack()


def main():
    gui = Tk()
    gui.title('Hello Tkinter')
    my_label = Label(text='label thanh phong', fg='white', bg='red').pack()
    btn1 = Button(text='click', fg='red', bg='green', command=command_button).pack()
    my_text = Entry().pack()
    gui.mainloop()


if __name__ == '__main__':
    main()
