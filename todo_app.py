import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_todo(conn, task):
    sql = ''' INSERT INTO todos(title, description, due_date, category_id, is_done)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    conn.close()
    return cur.lastrowid

def create_category(conn, category):
    sql = ''' INSERT INTO categories(name)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, (category,))
    conn.commit()
    conn.close()
    return cur.lastrowid

def update_todo(conn, task):
    sql = ''' UPDATE todos
              SET title = ?, description = ?, due_date = ?, category_id = ?, is_done = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    conn.close()
    
def delete_todo(conn, id):
    sql = 'DELETE FROM todos WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()
    conn.close()
    
def delete_category(conn, id):
    sql = 'DELETE FROM categories WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()
    conn.close()
    
def list_todos(conn, date=None):
    cur = conn.cursor()
    if date:
        cur.execute("SELECT * FROM todos WHERE due_date=?", (date,))
    else:
        cur.execute("SELECT * FROM todos")
    
    rows = cur.fetchall()
    for row in rows:
        print(row)
    conn.close()

def list_categories(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM categories")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    conn.close()
    
def mark_todo_done(conn, id):
    cur = conn.cursor()
    cur.execute("UPDATE todos SET is_done = 1 WHERE id=?", (id,))
    conn.commit()
    conn.close()
