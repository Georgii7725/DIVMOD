from tkinter import *
from back import *


"ОКНО"
root = Tk()
root.title("Калькулятор")
root.geometry("247x259+200+200")
root.resizable(False, False)
root.iconphoto(False, PhotoImage(file="icon.png"))
root["bg"] = "#7FC7FF"
"ОТСТУП"
l = Label(root)
l["bg"] = "#7FC7FF"
l.grid(row=1, column=1, columnspan=6, sticky=NSEW)


"ПОЛЯ ВВОДА"
check = (root.register(is_valide), "%P")

entry1 = Entry(root, validate="all", validatecommand=check)
entry1["bg"] = "#e1f5fe" 
entry1.grid(row=2, column=1, columnspan=3)
entry1.focus_set()
entry2 = Entry(root, validate="all", validatecommand=check)
entry2["bg"] = "#e1f5fe"
entry2.grid(row=2, column=4, columnspan=3)


"ОТСТУП"
l = Label(root)
l["bg"] = "#7FC7FF"
l.grid(row=3, column=1, columnspan=6, sticky=NSEW)


"КНОПКИ ОПЕРАЦИЙ"
b_DIV = Button(root, text="DIV", command=lambda: calculate(operator="DIV", en1=entry1, en2=entry2))
b_DIV["width"] = 12
b_DIV["bg"] = "#ff4444"
b_DIV.grid(row=4,column=1,columnspan=3)
b_MOD = Button(root, text="MOD", command=lambda: calculate(operator="MOD", en1=entry1, en2=entry2))
b_MOD["width"] = 12
b_MOD["bg"] = "#ff4444"
b_MOD.grid(row=4,column=4,columnspan=3)


"ОТСТУП"
l = Label(root)
l["bg"] = "#7FC7FF"
l.grid(row=5, column=1, columnspan=6, sticky=NSEW)


"КЛАВИАТУРА"
d=1
for i in range(3):
    for j in range(3):
        btn = Button(root, text=str(d), command=lambda arg=d: insert_digit(window=root, digit=str(arg)))
        btn["bg"] = "#039be5"
        btn.grid(row=i+6, column=2*j+1, columnspan=2, sticky=NSEW, padx=1, pady=1)
        d+=1

b_MINUS = Button(root, text="-", command=lambda: insert_digit(window=root, digit="-"), padx=1, pady=1)
b_MINUS.grid(row=9, column=1, columnspan=2, sticky=NSEW)
b_MINUS["bg"] = "#4444ff"
b_0 = Button(root, text="0", command=lambda: insert_digit(window=root, digit="0"), padx=1, pady=1)
b_0.grid(row=9, column=3, columnspan=2, sticky=NSEW)
b_0["bg"] = "#039be5"
b_CLEAR = Button(root, text="CLEAR", command=lambda: clear(window=root), padx=1, pady=1)
b_CLEAR.grid(row=9, column=5, columnspan=2, sticky=NSEW)
b_CLEAR["bg"] = "#FD222A"
b_TAB =Button(root, text="TAB", command=lambda: change_focus(window=root, en1=entry1, en2=entry2), padx=1, pady=1)
b_TAB["height"] = 2
b_TAB["bg"] = "#4444ff"
b_TAB.grid(row=10, column=1, columnspan=6, sticky=NSEW)


"ЗАПУСК"
root.mainloop()