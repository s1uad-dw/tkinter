'''Модуль, обеспеччивающий работу с графическим интерфейсом'''
from tkinter import Tk, Button, messagebox
import os
from functools import partial
from PIL import ImageTk, Image



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

CURRENT_PLAYER = 'X'

CLEAR_BTN_IMG = ImageTk.PhotoImage(Image.open(
    take_path(['static', 'pictures', 'clear.png'])))
X_BTN_IMG = ImageTk.PhotoImage(Image.open(
    take_path(['static', 'pictures', 'x.png'])))
O_BTN_IMG = ImageTk.PhotoImage(Image.open(
    take_path(['static', 'pictures', 'o.png'])))


def click(button_pos: tuple):
    '''Обрабатывает нажатие на кнопку'''
    global CURRENT_PLAYER
    if CURRENT_PLAYER == 'X':
        buttons[button_pos].configure(image=X_BTN_IMG)
        CURRENT_PLAYER = 'O'
    elif CURRENT_PLAYER == 'O':
        buttons[button_pos].configure(image=O_BTN_IMG)
        CURRENT_PLAYER = 'X'
    check()


def is_sublist(list1, list2):
    '''Проверяет наличие всех элементов list1 в list2'''
    for elem in list1:
        if elem not in list2:
            return False
    return True


def clear():
    '''Очищает игровое поле'''
    global CURRENT_PLAYER
    for button in buttons.values():
        button.configure(image=CLEAR_BTN_IMG)
    CURRENT_PLAYER = 'X'


def check():
    '''Проверяет наличие выигрышных комбинаций на поле'''
    x_btns = []
    o_btns = []
    for button in buttons.items():
        button_number = button[0][0]+1+button[0][1]+button[0][0]*2
        if button[1]['image'] == X_BTN_IMG._PhotoImage__photo.name:
            x_btns.append(button_number)
        elif button[1]['image'] == O_BTN_IMG._PhotoImage__photo.name:
            o_btns.append(button_number)
    for win in WINS:
        if is_sublist(win, x_btns):
            result = messagebox.askyesno(title='Игра окончена',
                        message='Победили крестики!\nХотите сыграть еще раз?')
            if result == 1:
                clear()
            elif result == 0:
                root.quit()
        elif is_sublist(win, o_btns):
            result = messagebox.askyesno(title='Игра окончена',
                        message='Победили нолики!\nХотите сыграть еще раз?')
            if result == 1:
                clear()
            elif result == 0:
                root.quit()


buttons = {}
for row in range(3):
    for col in range(3):
        current_button = Button(
            root,
            image=CLEAR_BTN_IMG,
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
