from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from functools import partial

WINS = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7]
]


def take_path(path: list):
    '''Возвращает полный путь к файлу (директории передаются списком)'''
    result = os.getcwd()
    for item in path:
        result = os.path.join(result, item)
    return result


root = Tk()
root.title('Крестики нолики')
root.configure(bg='#ffffff')
# root.iconbitmap(take_path(['icon.ico']))
root.geometry('600x600')

current_player = 'X'

clear_btn_img = ImageTk.PhotoImage(Image.open(
    take_path(['static', 'pictures', 'clear.png'])))
x_btn_img = ImageTk.PhotoImage(Image.open(
    take_path(['static', 'pictures', 'x.png'])))
o_btn_img = ImageTk.PhotoImage(Image.open(
    take_path(['static', 'pictures', 'o.png'])))


def click(button_pos: tuple):
    '''Обрабатывает нажатие на кнопку'''
    global current_player
    if current_player == 'X':
        buttons[button_pos].configure(image=x_btn_img)
        current_player = 'O'
    elif current_player == 'O':
        buttons[button_pos].configure(image=o_btn_img)
        current_player = 'X'
    check()


def isSublist(list1, list2):
    '''Проверяет наличие всех элементов list1 в list2'''
    for elem in list1:
        if elem not in list2:
            return False
    return True


def clear(result):
    '''Очищает игровое поле'''
    global current_player
    for button in buttons.values():
        button.configure(image=clear_btn_img)
        current_player = 'X'


def check():
    '''Проверяет наличие выигрышных комбинаций на поле'''
    global x_btn_img, o_btn_img
    x_btns = []
    o_btns = []
    for button in buttons.items():
        button_number = button[0][0]+1+button[0][1]+button[0][0]*2
        if button[1]['image'] == x_btn_img._PhotoImage__photo.name:
            x_btns.append(button_number)
        elif button[1]['image'] == o_btn_img._PhotoImage__photo.name:
            o_btns.append(button_number)
    for win in WINS:
        if isSublist(win, x_btns):
            result = messagebox.askyesno(title='Игра окончена',
                                         message='Победили крестики!\nХотите сыграть еще раз?')
            if result == 1:
                clear(result)
            elif result == 0:
                root.quit()
        elif isSublist(win, o_btns):
            result = messagebox.askyesno(title='Игра окончена',
                        message='Победили нолики!\nХотите сыграть еще раз?')
            if result == 1:
                clear(result)
            elif result == 0:
                root.quit()


buttons = dict()
for row in range(3):
    for col in range(3):
        current_button = Button(root,
                                image=clear_btn_img,
                                background='#ffffff',
                                highlightbackground='#ffffff',
                                highlightcolor='#ffffff',
                                activebackground='#ffffff',
                                borderwidth=0,
                                width=180,
                                height=180,
                                command=partial(click, (row, col))
                                )
        buttons[row, col] = current_button
        current_button.grid(row=row, column=col, padx=8, pady=8)

root.mainloop()
