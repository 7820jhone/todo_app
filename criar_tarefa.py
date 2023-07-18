from todo_app import create_connection, create_table, create_todo

def main():
    database = "todo_app.db"

    sql_create_categories_table ='''CREATE TABLE IF NOT EXISTS categories (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL UNIQUE
                            );'''
    
    sql_create_todos_table = '''CREATE TABLE IF NOT EXISTS todos (
                                id INTEGER PRIMARY KEY,
                                tible  TEXT NOT NULL,
                                description TEXT,
                                due_date TEXT NOT NULL,
                                category_id INTEGER,
                                is_done INTEGER NOT NULL DEFAULT 0,
                                FOREIGN KEY (category_id) REFERENCES categories (id)
                            );'''
    
    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_categories_table)
        create_table(conn, sql_create_todos_table)

        title = input("DIgite o título do TODO: ")
        description = input("Digite a descrição do TODO (pessione Enter se não houver descrição): ")
        due_date = input("DIgite a data de vencimento do TODO (formato: AAA-MM-DD): ")

        new_todo = (title, description, due_date, None, 0)
        todo_id = create_todo(conn, new_todo)
        print(f"TODO criado com sucesso com o ID {todo_id}")

    else:
        print("Erro! Não foi possível conectar ao banco de dados.")

if __name__ == '__main__':
    main()