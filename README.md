## Data Engineer Workshop:
### This project presents a solution to an interview challenge for the Python Data Engineer role. The challenge aims to evaluate your data management skills and your ability to create meaningful visualizations.

## About the CSV:
### The included CSV file contains simulated data from candidates who participated in selection processes.

## Solution Overview:
### Tools Used:
### Database Management System: PostgreSQL 

### Visualizations: Power BI. To create charts directly from the PostgreSQL database.

## Repository Contents:
### The repository consists of the following components:

## Notebooks Folder:

### eda_candidatos.ipynb: Jupyter notebook for exploratory data analysis.

### visualizations.ipynb: This notebook contains SQL queries designed to generate graphs. While the original plan was to use libraries like matplotlib or seaborn, this notebook ensured that the data visualized in Power BI were consistent with the results obtained here. The prior exploration of visualizations helped validate the accuracy and consistency of results in the final Power BI platform.

### requirements.txt: Lists the library versions utilized in the project.

### db_connection: This file contains a `create_connection` function that establishes a connection to a PostgreSQL database server and creates a new database called "workshop" if it doesn't exist. The function loads the database configuration from a JSON file (`db_config.json`), establishes the connection using the `psycopg2` library, configures the connection to use autocommit mode, and creates a cursor to execute SQL commands. Then, it attempts to create the database and closes the connection and cursor upon completion. If the database already exists, an error message is captured and displayed.

### table.py: This file contains a function `crear_tabla` that creates a table named "candidates" in a PostgreSQL database called "workshop". The function loads the database configuration from a JSON file (`db_config.json`) and establishes a connection to the database using the `psycopg2` library. It then creates a cursor to execute SQL commands and executes a SQL statement to create the "candidates" table with specified columns, including information such as first name, last name, email, application date, country, years of experience, seniority, technology, code challenge score, technical interview score, and a boolean indicating if the candidate was hired. The changes are committed to the database, and the connection and cursor are closed. The function prints a success message upon successful table creation.

### insert_data.py: The file contains a function `insertar_datos` that loads data from a CSV file (`candidates.csv`) into a PostgreSQL database table named "candidates". The function uses the `pandas` library to read the CSV file into a DataFrame and the `psycopg2` library to connect to the database. The database configuration is loaded from a JSON file (`db_config.json`). For each row in the DataFrame, the function prepares an SQL insert query and executes it, inserting the data into the "candidates" table. The `hired` column is calculated based on the values of `code_challenge_score` and `technical_intrvw_score`. After inserting all the rows, the function commits the changes to the database and closes the connection and cursor. The function prints a success message upon successful data insertion.


## Getting Started:
### Follow the next steps:

### - Clone the repository using "https://github.com/Scout104743/etl_workshop_01"
### - Create a virtual environment from your terminal. You can use: "python -m venv environment_name"
### - Activate your virtual environment. You can use: "environment_name/scripts/activate"
### - Install the required tools and modules in the environment. Use: "pip install -r requirements.txt".
### - Set the created environment as kernel.
### - Run db_connection.py, table.py and finaly insert_data.py.
### Now you're ready to use the repository
