import os
from tkinter import *

tk = Tk()
tk.geometry("700x500")
tk.title("Шифр Цезаря")
tk.resizable(False, False)
tk['bg'] = '#FFE4B5'


def create_file_button1():
    '''Создание файла'''
    my_file = open("text.txt", "w+", encoding='utf-8')
    return my_file


def delete_file_button2():
    '''Удаление файла'''
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'text.txt')
    return os.remove(path)


def Shifr_Cesar():
    '''Шифрование файла'''
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬ'
    words = edit.get()
    key = edit1.get()
    res = []
    ln = len(alphabet)
    n = '.\/[]{}()=-.,;:\'"1234567890~!`@#$%^&*<>?|=+_- '
    for l in words:
        if l not in n:
            res.append(alphabet[(alphabet.find(l) + int(key)) % ln])
        else:
            res.append(l)
    return label.insert(1.0, ('' + ''.join(res) + ' \n'))


def decipher_file_txt():
    '''Расшифровка файла'''
    return f'" "{label.insert(1.0, str(edit.get() + " "))}'


def clearTextInput():
    '''Очистка текстовых полей'''
    label.delete("1.0", "end")
    edit.delete(0)
    edit1.delete(0)


def save_file():
    '''Сохранение в файл'''
    fin = open("text.txt", "at", encoding='utf-8')
    fin.write((edit.get()+" "))

    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬ'
    words = edit.get()
    key = edit1.get()
    res = []
    ln = len(alphabet)
    n = '.\/[]{}()=-.,;:\'"1234567890~!`@#$%^&*<>?|=+_- '
    for l in words:
        if not l in n:
            res.append(alphabet[(alphabet.find(l) + int(key)) % ln])
        else:
            res.append(l)
    fin.write(('' + ''.join(res)))


b1 = Button(tk, text='Создание text.txt', command=create_file_button1, font=('Times New Roman', 10, 'bold'))
b1.place(x=10, y=100, width=120, height=50)

b2 = Button(tk, text='Удалить txt.txt', command=delete_file_button2, font=('Times New Roman', 10, 'bold'))
b2.place(x=155, y=100, width=120, height=50)

b3 = Button(tk, text='Очистить', command=clearTextInput, font=('Times New Roman', 10, 'bold'))
b3.place(x=300, y=100, width=120, height=50)

b4 = Button(tk, text='Шифрование', command=Shifr_Cesar, font=('Times New Roman', 10, 'bold'))
b4.place(x=450, y=100, width=120, height=50)

b5 = Button(tk, text='Расшифрование', command=decipher_file_txt, font=('Times New Roman', 10, 'bold'))
b5.place(x=590, y=100, width=100, height=50)

b6 = Button(tk, text='Сохранить в файл', command=save_file, font=('Times New Roman', 8, 'bold'))
b6.place(x=590, y=160, width=100, height=50)

edit = Entry(tk, width=40, bg='white')  # поле ввода
edit.place(x=300, y=190, width=170, height=20)

lbl1 = Label(tk, text='Шифр Цезаря', bg='#FFF', font=('Times New Roman', 18, 'bold'))
lbl1.place(x=260, y=10, width=200, height=50)

lbl2 = Label(tk, text='Введите текст для его шифрования:', bg='#FFF', font=('Times New Roman', 8, 'bold'))
lbl2.place(x=300, y=160, width=200, height=20)

lbl3 = Label(tk, text='Введите ключ шифрования:', bg='#FFF', font=('Times New Roman', 8, 'bold'))
lbl3.place(x=300, y=240, width=150, height=20)

edit1 = Entry(tk, width=40, bg='white')  # поле ввода
edit1.place(x=300, y=270, width=150, height=20)

label = Text(width=33, height=11)  # поле вывода
label.pack(side=LEFT, padx=15, pady=15)

lbl4 = Label(tk, text='Алгоритм работы с программой', bg='#FFF', font=('Times New Roman', 8, 'bold'))
lbl4.place(x=300, y=320, width=200, height=20)

lbl5 = Label(tk, text='1)Создайте текстовый файл', bg='#FFF', font=('Times New Roman', 8, 'bold'))
lbl5.place(x=300, y=350, width=200, height=20)

lbl6 = Label(tk, text='2)Введите текст', bg='#FFF', font=('Times New Roman', 8, 'bold'))
lbl6.place(x=300, y=380, width=200, height=20)

lbl7 = Label(tk, text='3)Введите ключ шифра', bg='#FFF', font=('Times New Roman', 8, 'bold'))
lbl7.place(x=300, y=410, width=200, height=20)

lbl7 = Label(tk, text='3)Введите ключ шифра', bg='#FFF', font=('Times New Roman', 8, 'bold'))
lbl7.place(x=300, y=410, width=200, height=20)

lbl8 = Label(tk, text='4)Перед выходом удалите файл', bg='#FFF', font=('Times New Roman', 8, 'bold'))
lbl8.place(x=300, y=435, width=200, height=20)

tk.mainloop()
