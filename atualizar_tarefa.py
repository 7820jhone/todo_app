from todo_app import create_connection, create_table, update_todo

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

        todo_id = input("Digite o ID do TODO que deseja atualizar: ")
        title = input("Digite o novo título do TODO: ")
        description = input("Digite a nova descrição do TODO (pressione Enter se não houver descrição): ")
        due_date = input("Digite a nova data de vencimento do TODO (formato: AAAA-MM-DD): ")
        categoria_id = input("Qual o ID da Categoria do seu TODO: ")
        is_done = input("Digite 1 se a tarefa estiver concluída ou 0 se não estiver concluída: ")

        updated_todo = (title, description, due_date, int(categoria_id), int(is_done), int(todo_id))
        update_todo(conn, updated_todo)
        print(f"TODO com ID {todo_id} atualizado com sucesso!")

    else:
        print("Error! Não foi possível conectar ao banco de dados.")

if __name__ == '__main__':
    main()