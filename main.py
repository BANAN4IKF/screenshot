from pyautogui import *
from tkinter import *
from tkinter import messagebox


def screen():
    img = screenshot()
    img.save(r"C:/Users/oleg/Pictures/screen.png/screens.png")
    messagebox.showinfo('Оповещение','Скриншот сделан!')



root = Tk()
root.title("Скриншотер")
root.geometry('300x70')
root.resizable(width=False, height=False)

btn = Button(root, text='Сделать скриншот', font=('Comic Sans MS', 15, 'bold'), command=screen)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
