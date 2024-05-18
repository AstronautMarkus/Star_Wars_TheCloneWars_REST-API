import sqlite3
import os

def create_database():
    # Nombre de la base de datos
    db_name = 'clone_wars_quotes.db'

    # Verificar si el archivo de la base de datos existe y eliminarlo si es así
    if os.path.exists(db_name):
        os.remove(db_name)
        print(f"Database '{db_name}' already existed and has been deleted.")

    # Leer el contenido del archivo create_tables.sql
    with open('sql_files/create_tables.sql', 'r') as file:
        create_tables_sql = file.read()

    # Conectar a la base de datos (se crea si no existe)
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Crear las tablas
    cursor.executescript(create_tables_sql)

    # Insertar las citas en distintos idiomas
    languages_path = 'sql_files/languages'
    for filename in os.listdir(languages_path):
        if filename.endswith('.sql'):
            with open(os.path.join(languages_path, filename), 'r') as file:
                insert_quotes_sql = file.read()
                cursor.executescript(insert_quotes_sql)
                print(f"Inserted quotes from '{filename}'")

    # Confirmar los cambios y cerrar la conexión
    conn.commit()
    conn.close()

    print(f"Database '{db_name}' created and tables populated successfully.")

if __name__ == "__main__":
    create_database()
