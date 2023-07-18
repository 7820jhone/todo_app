from todo_app import create_connection, create_table, mark_todo_done

def main():
    database = "todo_app.db"

    sql_create_categories_table = """CREATE TABLE IF NOT EXISTS categories (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL UNIQUE
                                );"""
    
    sql_create_todos_table = """CREATE TABLE IF NOT EXISTS todos (
                                id INTEGER PRIMARY KEY,
                                title TEXT NOT NULL,
                                description TEXT,
                                due_date TEXT NOT NULL,
                                category_id INTEGER,
                                is_done INTEGER NOT NULL DEFAULT 0,
                                FOREIGN KEY (category_id) REFERENCES categories (id)
                            );"""
    
    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_categories_table)
        create_table(conn, sql_create_todos_table)

        todo_id = int(input("Digite o ID do TODO que já foi finalizado: "))
        mark_todo_done(conn, todo_id)
        print(f'TODO com ID {todo_id} finalizado com sucesso!')

    else:
        print("Erro! Não foi possível conectar ao banco de dados.")

if __name__ == "__main__":
    main()