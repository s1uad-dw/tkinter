from tkinter import *
from PIL import Image, ImageTk,ImageDraw, ImageFont
import os
from functools import partial

root = Tk()
root.title('Калькулятор')
root.configure(background='#555555')



def take_path(dirs: list):
    '''Возвращает полный путь к файлу (директории передаются списком)'''
    path = os.getcwd()
    for item in dirs:
        path = os.path.join(path, item)
    return path

root.mainloop()