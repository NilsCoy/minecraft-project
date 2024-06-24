import tkinter as tk
from tkinter import ttk
import psycopg2
from psycopg2.extensions import register_type, UNICODE
CONN_STR = "host='10.163.31.228' dbname='rpr' user='smirnov_n1' password='bb23770e'"

def print_stamp():
    register_type(UNICODE)
    conn = psycopg2.connect(CONN_STR)
    cur = conn.cursor()
    cur.execute('select * from stamp')
    cols = cur.description
    row = cur.fetchone()
    print(row)
    row = cur.fetchone()
    print(row)
    #while row:
        #for i in range(len(cols)): print(row[i])
        #print('#'*10)
        #row = cur.fetchone()

    
class Main():
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title('База данных')
        self.main_window.geometry('1000x600')
        self.main_window.resizable(width=False, height=False)
        self.addText = tk.Entry(self.main_window, font="Courier 15", width = 20)
        self.editText = tk.Entry(self.main_window, font="Courier 15", width = 20)
        self.addButton = tk.Button(self.main_window, font="Courier 20", text = 'Добавить', command = self.add_line)
        self.editButton = tk.Button(self.main_window, font="Courier 20", text = 'Изменить', command = self.edit_line)
        self.updateButton = tk.Button(self.main_window, font="Courier 20", text = 'Обновить', command = self.update)
        self.addButton.place(x = 5, y = 5)
        self.editButton.place(x = 5, y = 60)
        self.updateButton.place(x = 5, y = 150)
        self.addText.place(x = 170, y = 15)
        self.editText.place(x = 170, y = 70)
        

        self.columns = ('name', 'country','factory', 'address', 'cou')
        self.updateLabel = ttk.Treeview(columns=self.columns, show="headings")
        self.updateLabel.heading("name", text="Имя")
        self.updateLabel.heading("country", text="Страна")
        self.updateLabel.heading("factory", text="Завод")
        self.updateLabel.heading("address", text="Адресс")
        self.updateLabel.heading("cou", text="Кол-во")
        self.updateLabel.column("#1", width=70)
        self.updateLabel.column("#2", width=60)
        self.updateLabel.column("#3", width=100)
        self.updateLabel.column("#4", width=100)
        self.updateLabel.column("#5", width=100)

        self.scrollbar = ttk.Scrollbar(orient="vertical", command=self.updateLabel.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.updateLabel.configure(yscroll=self.scrollbar.set)
        
        self.updateLabel.place(x = 170, y = 150)

        self.update()
        
        self.main_window.mainloop()

    def add_line(self):
        print("Добавление новой строки")
        if self.addText.get() != '':
            line = self.addText.get().split(' ')
            conn = psycopg2.connect(CONN_STR)
            cur = conn.cursor()
            cur.execute('select addfunc(%s, %s, %s, %s, %s)', line)
            conn.commit()
            cur.close()
            conn.close()
            self.update()
        else: print("Ошибка!")
    
    def edit_line(self):
        print("Изменение строки address")
        if self.editText.get() != '':
            line = self.editText.get().split(' ')
            conn = psycopg2.connect(CONN_STR)
            cur = conn.cursor()
            cur.execute('select updatefunc(%s, %s)', line)
            conn.commit()
            cur.close()
            conn.close()
            self.update()
        else: print("Ошибка!")
    
    def update(self):
        print("Получение данных")

        register_type(UNICODE)
        conn = psycopg2.connect(CONN_STR)
        cur = conn.cursor()
        cur.execute('select * from stamp')
        cols = cur.description
        row = cur.fetchone()
        #line = 'name | country | factory | address | cou\n'
        #while row:
        #    for i in range(len(row)):
        #        line += str(row[i])
        #        if i != len(row):
        #            line += ' | '
        #    line += '\n'
        #    row = cur.fetchone()
        data = []
        while row:
            data.append(row)
            row = cur.fetchone()
        self.updateLabel = ttk.Treeview(columns=self.columns, show="headings")
        self.updateLabel.heading("name", text="Имя")
        self.updateLabel.heading("country", text="Страна")
        self.updateLabel.heading("factory", text="Завод")
        self.updateLabel.heading("address", text="Адресс")
        self.updateLabel.heading("cou", text="Кол-во")
        self.updateLabel.column("#1", width=100)
        self.updateLabel.column("#2", width=100)
        self.updateLabel.column("#3", width=100)
        self.updateLabel.column("#4", width=100)
        self.updateLabel.column("#5", width=100)
        for dt in range(len(data)):
            self.updateLabel.insert("", str(dt), values=tuple(data[dt]))
        self.updateLabel.configure(yscroll=self.scrollbar.set)
        self.updateLabel.place(x = 170, y = 150)
start = Main()
#print_stamp()