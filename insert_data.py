import pandas as pd
import json
import psycopg2

def insertar_datos(df):
    # Cargar la configuración de la base de datos desde un archivo JSON
    with open('db_config.json', 'r') as file:
        db_config = json.load(file)

    # Conectar al servidor de PostgreSQL especificando la base de datos
    conn = psycopg2.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        dbname="workshop"
    )

    cur = conn.cursor()

    # Preparar la consulta SQL para insertar datos
    insert_query = """
        INSERT INTO candidates (
            first_name, last_name, email, application_date, country, yoe, seniority, technology, code_challenge_score, technical_intrvw_score, hired
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    # Iterar sobre las filas del DataFrame y ejecutar la consulta SQL para cada fila
    for _, row in df.iterrows():
        # Establecer el valor de la columna 'hired' en función de las puntuaciones
        hired = True if row['code_challenge_score'] >= 7 and row['technical_intrvw_score'] >= 7 else False
        
        cur.execute(insert_query, (
            row['first_name'], row['last_name'], row['email'], row['application_date'], row['country'], row['yoe'],
            row['seniority'], row['technology'], row['code_challenge_score'], row['technical_intrvw_score'], hired
        ))

    # Confirmar los cambios en la base de datos
    conn.commit()

    # Cerrar la conexión y el cursor
    cur.close()
    conn.close()

    print("Datos cargados con éxito en la tabla 'candidates'.")

# Cargar el dataset
candidatos = pd.read_csv('candidates.csv', delimiter=';')

# Renombrar las columnas para que coincidan con las de la tabla de base de datos
candidatos.columns = ['first_name', 'last_name', 'email', 'application_date', 'country', 'yoe', 'seniority', 'technology', 'code_challenge_score', 'technical_intrvw_score']

# Llamar a la función insertar_datos
insertar_datos(candidatos)
