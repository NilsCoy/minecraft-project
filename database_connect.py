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
    while row:
        for i in range(len(cols)): print(row[i])
        print('#'*10)
        row = cur.fetchone()

def add_stamp1(line):
    line = line.split(' ')
    conn = psycopg2.connect(CONN_STR)
    cur = conn.cursor()
    cur.execute('select addfunc(%s, %s, %s, %s, %s)', line)
    conn.commit()
    cur.close()
    conn.close()
def edit_adress(line):
    line = line.split(' ')
    conn = psycopg2.connect(CONN_STR)
    cur = conn.cursor()
    cur.execute('select updatefunc(%s, %s)', line)
    conn.commit()
    cur.close()
    conn.close()

def run():
    choice  = 0
    choices = {
        1 : lambda : print_stamp(),
        2 : lambda : add_stamp1(input('enter line: ')),
        3 : lambda : edit_adress(input('enter line: '))
    }
    while (choice != 4):
        print()
        print('1. print stamp')
        print('2. add stamp')
        print('3. edit adress')
        print('4. EXIT')
        print('choose:')
        choice = int(input())
        if choice in choices:
            choices[choice]()

if __name__ == '__main__':
    run()