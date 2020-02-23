import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.messagebox import askyesno
from tkinter import filedialog
from tkinter import messagebox


mapping = (
    u"abvhgdezyijklmnoprstuf'wABVHGDEZYIJKLMNOPRSTUFW",
    u"абвгґдезиійклмнопрстюфьуАБВГҐДЕЗИІЙКЛМНОПРСТЮФУ",
)

pre_processor_mapping = {
    u"His": u"Хіс",
    u"his": u"хіс",
    u"As": u"Ес",
    u"as": u"ес",
    u"Rain": u"Рейн",
    u"rain": u"рейн",
    u"Raid": u"Рейд",
    u"raid": u"рейд",
    u"Rade": u"Рейд",
    u"rade": u"рейд",
    u"wh": u"у",
    u"Light": u"Лайт",
    u"light": u"лайт",
    u"Lite": u"Лайт",
    u"lite": u"лайт",
    u"Air": u"Ейр",
    u"air": u"ейр",
    u"Line": u"Лайн",
    u"line": u"лайн",
    u"Jack": u"Джек",
    u"jack": u"джек",
    u"Hi": u"Хай",
    u"hi": u"хай",
    u"Ive": u"Айв",
    u"ive": u"айв",
    u"Was": u"Уоз",
    u"was": u"уоз",
    u"One": u"Уан",
    u"one": u"уан",
    u"ne": u"н",
    u"Ck": u"К",
    u"ck": u"к",
    u"Ee": u"І",
    u"ee": u"і",
    u"ew": u"ью",
    u"Oi": u"Ой",
    u"oi": u"ой",
    u"Oy": u"Ой",
    u"oy": u"ой",
    u"Ph": u"Ф",
    u"ph": u"ф",
    u"Q": u"Кв",
    u"q": u"кв",
    u"Tch": u"Ч",
    u"tch": u"ч",
    u"Tion": u"Шон",
    u"tion": u"шон",
    u"Ew": u"Ью",
    u"ay": u"ей",
    u"ly": u"лай",
    u"aine": u"ейн",
    u"ye": u"є",
    u"X": u"Кс",
    u"x": u"кс",
    u"zh": u"ж",
    u"yi": u"ї",
    u"kh": u"х",
    u"ts": u"ц",
    u"ch": u"ч",
    u"sh": u"ш",
    u"shch": u"щ",
    u"j": u"джу",
    u"ja": u"я",
    u"Ay": u"Ей",
    u"Aine": u"Ейн",
    u"Ye": u"Є",
    u"Zh": u"Ж",
    u"Yi": u"Ї",
    u"Kh": u"Х",
    u"Ts": u"Ц",
    u"Ch": u"Ч",
    u"Sh": u"Ш",
    u"Shch": u"Щ",
    u"J": u"Джу",
    u"Ly": u"Лай",
    u"Ia": u"Я",
    u"They": u"Зей",
    u"they": u"зей",
    u"The": u"Зе",
    u"the": u"зе",
    u"Th": u"С",
    u"th": u"с",
}

translation_table = {}

for key, val in zip(*mapping):
    translation_table.update({ord(key): ord(val)})


def newfile(event=None):
    mw.title('Нова_Транслітерація')
    field.delete(1.0, END)
    result.delete(1.0, END)


def openfile(event=None):
    filename = filedialog.askopenfilename(filetypes=(('Текстові файли', '*.txt'), ('Усі файли', '*.*')))
    try:
        with open(filename, 'r') as file:
            field.delete(1.0, END)
            field.insert(1.0, file.read())
            mw.title(filename.split('/')[-1])
    except:
        pass


def savefile(event=None):
    filename = filedialog.asksaveasfilename(filetypes=(('Текстові файли', '*.txt'), ('Усі файли', '*.*')))
    if filename != '':
        with open(filename + '.txt', 'w') as file:
            file.write(result.get(1.0, END).rstrip('\n'))
            mw.title(filename.split('/')[-1])


def close(event=None):
    if messagebox.askyesno('Вихід', 'Закрити програму?'):
        mw.quit()


def helps():
    help_win = Toplevel()
    help_win.title('Довідка')
    help_win.geometry('400x420')
    help_win.resizable(False, False)
    text_help = """
    Транслітерація з англійської на українську
    відбувається за словниками, створеними нами
        """
    label_help = Label(help_win, text=text_help, justify=LEFT, width=60)
    label_help.pack()
    btn_close = Button(help_win, text='Ok', command=help_win.destroy)
    btn_close.place(x=320, y=380, width=65)


def about():
    about_win = Toplevel()
    about_win.title('Про програму')
    about_win.geometry('400x420')
    about_win.resizable(False, False)
    text_about = """
            Транслітератор
        _______________________________________________________
        Version 1 (Build 1)
        Design - © Natalie Kulieshova, 2020
        Algorithm - © Vasyl Abramovych, 2020
        _______________________________________________________
        we@we.com
            """
    label_about = Label(about_win, text=text_about, justify=LEFT, width=60)
    label_about.pack()
    btn_close = Button(about_win, text='Ok', command=about_win.destroy)
    btn_close.place(x=320, y=380, width=65)


def transliterate():
    result.delete(1.0, END)
    result.insert(1.0, latinisate(field.get(1.0, END)))


def latinisate(letter):
    for rule in pre_processor_mapping:
        letter = letter.replace(rule, pre_processor_mapping[rule])

    letter = letter.translate(translation_table)

    return letter

root = tk.Tk()
root.geometry("800x600")
root["bg"]='white'
root.resizable(False, False)

mb = Menu()
root.config(menu=mb)
filemenu = Menu(mb, tearoff=0)
filemenu.add_command(label='Новий', command=newfile, accelerator='Ctrl+N')
filemenu.add_command(label='Відкрити', command=openfile, accelerator='Ctrl+O')
filemenu.add_command(label='Зберегти', command=savefile, accelerator='Ctrl+S')
filemenu.add_command(label='Вихід', command=close, accelerator='Ctrl+Q')
helpmenu = Menu(mb, tearoff=0)
helpmenu.add_command(label='Довідка', command=helps)
helpmenu.add_command(label='Про програму', command=about)
mb.add_cascade(label='Файл', menu=filemenu)
mb.add_cascade(label='Допомога', menu=helpmenu)

image1 = tk.PhotoImage(file="header.png")
label = tk.Label(image=image1)
label.pack(side=TOP)

L2 = Label(root, text="Transliteration", fg="#00c6ff", bg="white").place(x=590, y=90)
result = scrolledtext.ScrolledText(root, width=30, height=18, font='Arial 12', wrap='word')

result.place(x=480, y=120)

L1 = Label(root, text="Input", fg="#00c6ff", bg="white").place(x=150, y=90)
field = scrolledtext.ScrolledText(root, width=30, height=18, font='Arial 12', wrap='word')

field.place(x=30, y=120)

image2 = tk.PhotoImage(file="background.png")
label = tk.Label(image=image2)
label.pack(side = BOTTOM)

uabtn = Button(root, text="UK to ENG", activebackground="#00c6ff", width=15).place(x=343, y=125)
engbtn = Button(root, text="ENG to UA", activebackground="#00c6ff", width=15).place(x=343, y=175)
translatebtn = Button(root, text="Transliterate", activebackground="#00c6ff", width=15, command=transliterate).place(x=343, y=225)

root.mainloop()
