from faker import Faker
import pandas as pd
import json
from datetime import datetime
import random

faker = Faker()

def generate_ddl(table_name, columns):
    ddl = f"CREATE TABLE {table_name} (\n"
    ddl += ",\n".join([f"{col['name']} {col['type']}" for col in columns])
    ddl += "\n);"
    return ddl

def generate_dummy_data(columns, num_rows):
    data = {}
    for col in columns:
        if col['type'] == 'VARCHAR':
            data[col['name']] = [faker.word() for _ in range(num_rows)]
        elif col['type'] == 'INTEGER':
            data[col['name']] = [faker.random_number(digits=5, fix_len=True) for _ in range(num_rows)]
        elif col['type'] == 'NUMBER':
            data[col['name']] = [round(random.uniform(0, 10000), 2) for _ in range(num_rows)]
        elif col['type'] == 'BOOLEAN':
            data[col['name']] = [faker.boolean() for _ in range(num_rows)]
        elif col['type'] == 'DATE':
            data[col['name']] = [faker.date() for _ in range(num_rows)]
        elif col['type'] == 'TIME':
            data[col['name']] = [faker.time() for _ in range(num_rows)]
        elif col['type'] == 'TIMESTAMP':
            data[col['name']] = [datetime.now().strftime("%Y-%m-%d %H:%M:%S") for _ in range(num_rows)]
        elif col['type'] == 'VARIANT':
            data[col['name']] = [json.dumps({"key": faker.word(), "value": faker.word()}) for _ in range(num_rows)]
    return pd.DataFrame(data)
