import sqlite3
db = 'my_todo.db'
table = 'task'
conn = sqlite3.connect(db)
c = conn.cursor()

def create_table():
    sql = 'CREATE TABLE IF NOT EXISTS ' + table \
          + ' (ID INTEGER PRIMARY KEY AUTOINCREMENT, TASKNAME TEXT)'
    c.execute(sql)

def data_entry(task):
    c.execute('INSERT INTO ' + table + ' (TASKNAME) VALUES (?)', [task])
    print("Task has been added to database")
    conn.commit()

def print_data():
    c.execute('SELECT * FROM ' + table)
    for i in c.fetchall():
        print(i[0], ' ---> ', i[1])


def delete_task(index):
    c.execute('DELETE FROM ' + table + ' WHERE ID=?', (index, ))
    print("Task has been deleted from database")
    conn.commit()

def close_cursor():
    c.close()
    conn.close()











