from tkinter import *
from tkinter.messagebox import showerror, showinfo
import re

def insert_digit(window: Tk, digit: str):
    field = window.focus_get()
    if isinstance(field, Entry):
        field.insert(field.index(INSERT), digit)

def is_valide(text):
    return text == "-" or text == "" or re.fullmatch("0|(-?[1-9][0-9]*)", text) is not None

def clear(window: Tk):
    window.focus_get().delete(0, END)

def change_focus(window: Tk, en1: Entry, en2: Entry):
    en2.focus_set() if window.focus_get() == en1 else en1.focus_set()

def calculate(operator: str, en1: Entry, en2: Entry):
    en1 = int(en1.get())
    en2 = int(en2.get())
    if en2 == 0: showerror("Невозможная операция", f"Операция {operator} не определена по отношению к нулю")
    else: showinfo("Результат", f"{en1} {operator} {en2} = {en1 % en2 if operator == 'MOD' else en1 // en2}" if en2 >= 0 else f"{en1} {operator} {en2} = {(-en1) % (-en2) if operator == 'MOD' else (-en1) // (-en2)}")
