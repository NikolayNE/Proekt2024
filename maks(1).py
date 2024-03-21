import tkinter
from tkinter import *
import sys
import os
import subprocess
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk
import tkinter.filedialog as fd

root = Tk()
root.title("Proverka")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))

def menu():
    global root
    root = Tk()
    root.title("Proverka")
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))

    btn1 = Button(root, font='Trebuchet', text="Задача 1",
                  borderwidth=0, bg="aqua")
    btn1.config(command=level1)
    btn1.place(relx=0.35, rely=0.2, relheight=0.05, relwidth=0.3)

    btn2 = Button(root, font='Trebuchet', text="Задача 2",
                  borderwidth=0, bg="yellow")
    btn2.config(command=level2)
    btn2.place(relx=0.35, rely=0.35, relheight=0.05, relwidth=0.3)

    btn3 = Button(root, font='Trebuchet', text="Задача 3",
                  borderwidth=0, bg="green")
    btn3.config(command=level3)
    btn3.place(relx=0.35, rely=0.5, relheight=0.05, relwidth=0.3)
def level1():
    def clic1():
        v = ''

        tests = str('tests1')

        try:
            for test in os.listdir(tests):
                with open(f'{tests}/{test}', 'r', encoding='utf-8') as file:
                    lines = list(map(lambda e: e.strip(), file.readlines()))
                inpt = lines[:lines.index('---')]
                code1 = e1.get("1.0", END).split('\n')
                if len([el for el in code1 if el.strip() != '']) == 0:
                    v += 'нет кода'
                else:
                    my_file = open('code1.py', 'w+', encoding='utf-8')
                    my_file.write('def input():\n\tif len(l) > 0:\n\t\ta = l[0]\n\t\tdel l[0]\n\t\treturn a\n\telse:\n\t\treturn 0\n')
                    my_file.write('def prob():\n')
                    for el in code1:
                        my_file.write('\t' + el + '\n')
                    my_file.write(f'l = {lines[:lines.index("---")]}\n')
                    my_file.write('prob()\n')
                    my_file.close()



                    fl1 = True
                    try:
                        subprocess.check_call([sys.executable, 'code1.py'],
                                              timeout=3)
                    except (subprocess.TimeoutExpired and subprocess.CalledProcessError and NameError and Exception) as e:
                        fl1 = False
                        if e == subprocess.TimeoutExpired:
                            v += f'Превышено время выполнения {test}\n'
                        else:
                            v += f'Ошибка выполнения {test}\n'
                    if fl1:
                        outpt = lines[lines.index('---') + 1:]
                        programm = str('code1.py')
                        ans = list(map(lambda e: e.strip(), os.popen(f'echo {inpt} | python {programm}').readlines()))
                        fl = False
                        print(outpt, ans, inpt)
                        if len(ans) != len(outpt):
                            fl = True
                        else:
                            for i in range(len(ans)):
                                if str(ans[i]) != str(outpt[i]):
                                    fl = True

                        if fl:
                            v += f'Wrong answer test {test}\n'
                        else:
                            v += f'Test {test} passed\n'






        except FileNotFoundError:
            v += 'Такой папки нет\n'
        lab.config(text=v)


    root.withdraw()

    def on_text_change(event):
        e1.config(height=(e1.get("1.0", END).count('\n') + 1))


    l1 = Tk()
    l1
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    l1.geometry("%dx%d" % (width, height))
    scroll_bar = Scrollbar(l1)

    scroll_bar.pack(side=RIGHT,
                    fill=Y)
    l1.title('Сложение')
    e1 = ScrolledText(l1, width=140, height=35)
    e1.pack()
    e1.place(x=0, y=220)

    entry1 = Button(l1, text="Запустить", command=clic1, compound=BOTTOM)
    entry1.pack()
    entry1.place(x=1200, y=200)
    lall1 = Button(l1, text="< Назад", command=lambda: open_level(l1))
    lall1.pack()
    lall1.place(x=1200, y=250)
    f = Label(l1, text='В строку через пробел вводятся два числа, вывести их сумму\n', font="Times 30")
    f.pack()
    f.place(x=10, y=10)
    columns = ('№', 'input', 'output')
    ts = [('1', '5 6', '11'), ('2', '-1 9', '8')]
    tabl = ttk.Treeview(l1, columns=columns, show="headings", height=2)
    tabl.pack()
    tabl.place(x=10, y=80)
    tabl.heading(0, text='№')
    tabl.heading(1, text='input')
    tabl.heading(2, text='output')
    tabl.column("#1", stretch=False, width=100)
    tabl.column("#2", stretch=False, width=100)
    tabl.column("#3", stretch=False, width=100)
    for el in ts:
        tabl.insert("", END, values=el)
    lab = Label(l1, text='Вердикт')
    lab.pack()
    lab.place(x=1200, y=300)

    l1.mainloop()


def level2():
    def clic2():
        v = ''

        tests = str('tests2')

        try:
            for test in os.listdir(tests):
                with open(f'{tests}/{test}', 'r', encoding='utf-8') as file:
                    lines = list(map(lambda e: e.strip(), file.readlines()))
                inpt = lines[:lines.index('---')]
                code1 = e1.get("1.0", END).split('\n')
                if len([el for el in code1 if el.strip() != '']) == 0:
                    v += 'нет кода'
                else:
                    my_file = open('code2.py', 'w+', encoding='utf-8')
                    my_file.write('def input():\n\tif len(l) > 0:\n\t\ta = l[0]\n\t\tdel l[0]\n\t\treturn a\n\telse:\n\t\treturn 0\n')
                    my_file.write('def prob():\n')
                    for el in code1:
                        my_file.write('\t' + el + '\n')
                    my_file.write(f'l = {lines[:lines.index("---")]}\n')
                    my_file.write('prob()\n')
                    my_file.close()



                    fl1 = True
                    try:
                        subprocess.check_call([sys.executable, 'code2.py'],
                                              timeout=3)
                    except (subprocess.TimeoutExpired and subprocess.CalledProcessError and NameError and Exception) as e:
                        fl1 = False
                        if e == subprocess.TimeoutExpired:
                            v += f'Превышено время выполнения {test}\n'
                        else:
                            v += f'Ошибка выполнения {test}\n'
                    if fl1:
                        outpt = lines[lines.index('---') + 1:]
                        programm = str('code2.py')
                        ans = list(map(lambda e: e.strip(), os.popen(f'echo {inpt} | python {programm}').readlines()))
                        fl = False
                        print(outpt, ans, inpt)
                        if len(ans) != len(outpt):
                            fl = True
                        else:
                            for i in range(len(ans)):
                                if str(ans[i]) != str(outpt[i]):
                                    fl = True

                        if fl:
                            v += f'Wrong answer test {test}\n'
                        else:
                            v += f'Test {test} passed\n'



        except FileNotFoundError:
            v += 'Такой папки нет\n'

        lab.config(text=v)


    root.withdraw()

    def on_text_change(event):
        e1.config(height=(e1.get("1.0", END).count('\n') + 1))

    l1 = Tk()
    scroll_bar = Scrollbar(l1)
    l1.geometry("%dx%d" % (width, height))
    scroll_bar.pack(side=RIGHT,
                    fill=Y)
    l1.title('Новая Жизнь')

    e1 = ScrolledText(l1, width=140, height=100)
    e1.pack()
    e1.place(x=0, y=250)
    entry1 = Button(l1, text="Запустить", command=clic2, compound=BOTTOM)
    entry1.pack()
    entry1.place(x=1200, y=300)
    lall1 = Button(l1, text="< Назад", command=lambda: open_level(l1))
    lall1.pack()
    lall1.place(x=1200, y=350)
    f = Text(l1, width=100, height=7, wrap=WORD, font='Times 15')
    f.insert(1.0, 'Мы начали новую жизнь под землей. В нашем городе, в пятистах метрах ниже'
                  ' поверхности земли, хватало места для миллиона с небольшим жителей. Много других'
                  ' городов, точно таких же, находилось в разных местах на всех континентах. '
                  'У человечества не было времени. Все должны были выполнять свою работу, и конца '
                  'ей не предвиделось.Напишите программу для подсчета средней вместительности '
                  'городов-миллионников (население не меньше миллиона). На вход программе подаются'
                  ' числа - населения городов, каждое на отдельной строке. Конец последовательности обозначается словом "end"')
    f.config(state=DISABLED)
    f.pack()
    f.place(x=0, y=10)

    columns = ('№', 'input', 'output')
    ts = [('1', '447067\n4\n861\n1428295\n1465321\n10\nend', '11'), ('2', '11111111\n40\n237465\n10\n228556\nend', '8')]
    style = ttk.Style(l1)
    style.configure('MyStyle1.Treeview', rowheight=105)


    tabl = ttk.Treeview(l1, columns=columns, show="headings", height=2, style='MyStyle1.Treeview')

    tabl.pack()
    tabl.place(x=1200, y=10)
    tabl.heading(0, text='№')
    tabl.heading(1, text='input')
    tabl.heading(2, text='output')
    tabl.column("#1", stretch=False, width=100)
    tabl.column("#2", stretch=False, width=100)
    tabl.column("#3", stretch=False, width=100)
    tabl.tag_configure('oddrow', background='light grey')
    tabl.tag_configure('evenrow', background='white')
    count = 0
    for el in ts:
        if count % 2 == 0:
            tabl.insert("", END, values=el, tags=('oddrow',))
        else:
            tabl.insert("", END, values=el, tags=('enerow',))
        count += 1
    lab = Label(l1, text='Вердикт')
    lab.pack()
    lab.place(x=1200, y=400)

    l1.mainloop()



def level3():
    root.destroy()
    def clic3():
        v = ''

        tests = str(sp[0])

        try:
            for test in os.listdir(tests):
                with open(f'{tests}/{test}', 'r', encoding='utf-8') as file:
                    lines = list(map(lambda e: e.strip(), file.readlines()))
                inpt = lines[:lines.index('---')]
                code1 = e1.get("1.0", END).split('\n')
                if len([el for el in code1 if el.strip() != '']) == 0:
                    v += 'нет кода'
                else:
                    my_file = open('code3.py', 'w+', encoding='utf-8')
                    my_file.write('def input():\n\tif len(l) > 0:\n\t\ta = l[0]\n\t\tdel l[0]\n\t\treturn a\n\telse:\n\t\treturn 0\n')
                    my_file.write('def prob():\n')
                    for el in code1:
                        my_file.write('\t' + el + '\n')
                    my_file.write(f'l = {lines[:lines.index("---")]}\n')
                    my_file.write('prob()\n')
                    my_file.close()



                    fl1 = True
                    try:
                        subprocess.check_call([sys.executable, 'code3.py'],
                                              timeout=3)
                    except (subprocess.TimeoutExpired and subprocess.CalledProcessError and NameError and Exception) as e:
                        fl1 = False
                        if e == subprocess.TimeoutExpired:
                            v += f'Превышено время выполнения {test}\n'
                        else:
                            v += f'Ошибка выполнения {test}\n'
                    if fl1:
                        outpt = lines[lines.index('---') + 1:]
                        programm = str('code3.py')
                        ans = list(map(lambda e: e.strip(), os.popen(f'echo {inpt} | python {programm}').readlines()))
                        fl = False
                        print(outpt, ans, inpt)
                        if len(ans) != len(outpt):
                            fl = True
                        else:
                            for i in range(len(ans)):
                                if str(ans[i]) != str(outpt[i]):
                                    fl = True

                        if fl:
                            v += f'Wrong answer test {test}\n'
                        else:
                            v += f'Test {test} passed\n'



        except FileNotFoundError and Exception and PermissionError:
            v += 'Такой папки с тестами нет\n'
        lab.config(text=v)


    def provp():
        try:
            t = os.listdir(sp[0])
            for el in t:
                    spis = open(sp[0] + '/' + el, encoding='utf-8')
                    spis.close()
            at.delete(1.0, END)
            at.insert(1.0, 'Папка принята')
        except Exception as e:
            print(e)
            at.delete(1.0, END)
            at.insert(1.0, 'Папка не принята')


    def on_text_change(event):
        e1.config(height=(e1.get("1.0", END).count('\n') + 1))


    l1 = Tk()
    scroll_bar = Scrollbar(l1)

    l1.geometry("%dx%d" % (width, height))
    scroll_bar.pack(side=RIGHT,
                    fill=Y)
    l1.config(bg="white")
    l1.title('Задача 3')

    e1 = ScrolledText(l1, width=140, height=100)
    e1.pack()
    e1.place(x=0, y=150)

    entry1 = Button(l1, text="Запустить", command=clic3, compound=BOTTOM)
    entry1.pack()
    entry1.place(x=1200, y=200)
    lall1 = Button(l1, text="< Назад", command=lambda: open_level1(l1))
    lall1.pack()
    lall1.place(x=1200, y=250)
    f = Text(l1, width=100, height=5, wrap=WORD, font='Times 20')
    f.insert(1.0,
             'На данном уровне вы можете решить свою задачу. Для этого выбирите папку с тестами')
    f.config(state=DISABLED)
    f.pack()
    f.place(x=0, y=10)

    at = Text(l1, width=50, height=1)
    s = 'Выберите папку'
    at.insert(1.0, s)
    at.pack()
    at.place(x=150, y=80)
    prov = Button(l1, text='Проверить путь', command=provp, compound=BOTTOM)
    prov.pack()
    prov.place(x=0, y=80)
    lab = Label(l1, text='Вердикт')
    lab.pack()
    lab.place(x=1150, y=300)
    sp = ['']
    def choose_directory():
        directory = fd.askdirectory(title="Открыть папку", initialdir="/")
        sp[0] = directory
    btn_dir = Button(l1, text="Выбрать папку",
                        command=choose_directory, compound=BOTTOM)
    btn_dir.pack()
    btn_dir.place(x=0, y=50)
    l1.mainloop()


def open_level(level_window):
    level_window.withdraw()
    root.deiconify()


def open_level1(level_window):
    level_window.withdraw()
    menu()
    root.deiconify()


btn1 = Button(root, font='Trebuchet', text="Задача 1",
              borderwidth=0, bg="aqua")
btn1.config(command=level1)
btn1.place(relx=0.35, rely=0.2, relheight=0.05, relwidth=0.3)

btn2 = Button(root, font='Trebuchet', text="Задача 2",
              borderwidth=0, bg="yellow")
btn2.config(command=level2)
btn2.place(relx=0.35, rely=0.35, relheight=0.05, relwidth=0.3)

btn3 = Button(root, font='Trebuchet', text="Задача 3",
              borderwidth=0, bg="green")
btn3.config(command=level3)
btn3.place(relx=0.35, rely=0.5, relheight=0.05, relwidth=0.3)

root.mainloop()
