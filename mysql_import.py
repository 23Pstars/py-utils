import pandas as pd
from sqlalchemy import create_engine, text, VARCHAR, FLOAT, INTEGER

# MySQL database connection parameters
db_username = 'winkom'
db_password = 'gakpakepassword'
db_host = 'localhost'
db_port = '3306'  # Change if your MySQL server is running on a different port
db_name = 'unram_sireg'

# Table name in MySQL database
# table_name = '_rapor2024_nilai'
table_name = '_rapor2024_nilai_tambahan'

# CSV file path
csv_file = f'/Users/zaf/Downloads/snbp/rapor/{table_name}.csv'



# Create MySQL database connection
engine = create_engine(f'mysql+mysqlconnector://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}')

# Read a sample of the CSV file to infer column types
df_sample = pd.read_csv(csv_file, nrows=5)

# Define column types for the table
column_types = {
    col: VARCHAR(length=255) if dtype == 'object' else (
        FLOAT() if dtype in ['float64', 'int64'] else INTEGER()
    )
    for col, dtype in df_sample.dtypes.items()
}

# Create MySQL table with predefined column types
with engine.connect() as connection:
    columns = ', '.join([f'{col} {dtype}' for col, dtype in column_types.items()])
    create_table_query = text(f'CREATE TABLE {table_name} ({columns})')
    connection.execute(create_table_query)

print(f"Table '{table_name}' created successfully in MySQL database '{db_name}'.")

# Import data into MySQL table
df = pd.read_csv(csv_file)

# Cast DataFrame columns to match MySQL table column types
df = df.astype({col: dtype.python_type for col, dtype in column_types.items()})

# Insert data into MySQL table
df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)

print(f"Data imported successfully into '{table_name}' table in MySQL database '{db_name}'.")