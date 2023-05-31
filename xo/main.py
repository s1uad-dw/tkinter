from tkinter import *
from PIL import Image, ImageTk
import os
from functools import partial

root = Tk()
root.title('Крестики нолики')
root.configure(bg='#ffffff')
root.iconbitmap('icon.ico')
root.geometry('600x600')


def take_path(path: list):
    '''Возвращает полный путь к файлу (директории передаются списком)'''
    result = os.getcwd()
    for item in path:
        result = os.path.join(result, item)
    return result


current_player = 'X'

clear_btn_img = ImageTk.PhotoImage(Image.open(
    take_path(['static', 'pictures', 'clear.png'])))
x_btn_img = ImageTk.PhotoImage(Image.open(
    take_path(['static', 'pictures', 'x.png'])))
o_btn_img = ImageTk.PhotoImage(Image.open(
    take_path(['static', 'pictures', 'o.png'])))

def click(button_pos: tuple):
    global current_player
    if current_player == 'X':
        buttons[button_pos].configure(image=x_btn_img)
        current_player = 'O'
    elif current_player == 'O':
        buttons[button_pos].configure(image=o_btn_img)
        current_player = 'X'
    check()


def check():
    global x_btn_img, o_btn_img
    x_summ = []
    o_summ = []
    for button in buttons.items():
        button_number = button[0][0]+1+button[0][1]+button[0][0]*2
        if button[1]['image'] == x_btn_img._PhotoImage__photo.name:
            x_summ.append(button_number)
        elif button[1]['image'] == o_btn_img._PhotoImage__photo.name:
            o_summ.append(button_number)

buttons = dict()
for row in range(3):
    for col in range(3):
        current_button = Button(root,
                                image=clear_btn_img,
                                background='#ffffff',
                                activebackground='#ffffff',
                                borderwidth=0,
                                width=180,
                                height=180,
                                command=partial(click, (row, col))
                                )
        buttons[row, col] = current_button
        current_button.grid(row=row, column=col, padx=9, pady=9)

root.mainloop()
