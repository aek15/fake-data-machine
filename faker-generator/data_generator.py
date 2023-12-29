from faker import Faker
import pandas as pd

faker = Faker()

def generate_ddl(table_name, columns):
    ddl = f"CREATE OR REPLACE TABLE {table_name} (\n"
    ddl += ",\n".join([f"{col['name']} {col['type']}" for col in columns])
    ddl += "\n);"
    return ddl

def generate_dummy_data(columns, num_rows):
    data = {col['name']: [faker.pystr() if col['type'] == 'VARCHAR' else faker.random_number() for _ in range(num_rows)] for col in columns}
    return pd.DataFrame(data)
