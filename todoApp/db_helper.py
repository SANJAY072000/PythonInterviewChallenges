import sqlite3
db = 'my_todo.db'
table = 'task'
conn = sqlite3.connect(db)
c = conn.cursor()

def create_table():
    sql = 'CREATE TABLE IF NOT EXISTS ' + table \
    + ' (ID INTEGER PRIMARY KEY AUTOINCREMENT, TASKNAME TEXT)'
    c.excute(sql)

def data_entry(task):
    pass

def print_data():
    pass

def delete_task():
    pass

def close_cursor():
    c.close()
    conn.close()


    








