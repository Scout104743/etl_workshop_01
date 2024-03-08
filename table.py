import json
import psycopg2

def crear_tabla(db_config_path='db_config.json'):
    # Cargar la configuración de la base de datos desde el archivo JSON
    with open(db_config_path, 'r') as file:
        db_config = json.load(file)

    # Conectar a la base de datos 'workshop1st'
    conn = psycopg2.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        dbname="workshop"
    )

    # Crear un cursor para ejecutar comandos SQL
    cur = conn.cursor()

    # Crear la tabla con las columnas especificadas
    cur.execute("""
        CREATE TABLE IF NOT EXISTS candidates (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(20),
            last_name VARCHAR(20),
            email VARCHAR(50),
            application_date DATE,
            country VARCHAR(60),
            yoe INTEGER,
            seniority VARCHAR(15),
            technology VARCHAR(50),
            code_challenge_score INTEGER,
            technical_intrvw_score INTEGER,
            hired BOOLEAN
        )
    """)

    # Confirmar los cambios en la base de datos
    conn.commit()

    # Cerrar la conexión y el cursor
    cur.close()
    conn.close()

    print("Tabla creada con éxito.")

# Llamar a la función para crear la tabla
crear_tabla()


