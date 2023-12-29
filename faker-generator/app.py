import streamlit as st
import os
from data_generator import generate_ddl, generate_dummy_data

def main():
    st.title("Dummy Data Generator")

    table_name = st.text_input("Table Name", "my_table")
    num_columns = st.number_input("Number of Columns", min_value=1, max_value=10, value=3)

    columns = []
    for i in range(int(num_columns)):
        col_name = st.text_input(f"Name of column {i+1}", f"column_{i+1}")
        col_type = st.selectbox(f"Data type of column {i+1}", ["VARCHAR", "INT"], index=0)
        columns.append({"name": col_name, "type": col_type})

    if st.button("Generate DDL"):
        ddl = generate_ddl(table_name, columns)
        st.text_area("DDL Statement", ddl, height=100)

    num_rows = st.number_input("Number of Rows per File", min_value=1, max_value=1000, value=100)
    num_files = st.number_input("Number of Files", min_value=1, max_value=10, value=1)

    if st.button("Generate Files"):
        os.makedirs('generated_files', exist_ok=True)
        for i in range(int(num_files)):
            df = generate_dummy_data(columns, int(num_rows))
            file_name = f'generated_files/{table_name}_{i}.csv'
            df.to_csv(file_name, index=False)
            st.success(f"File {file_name} generated.")

    if st.button("List Generated Files"):
        files = os.listdir('generated_files')
        for file in files:
            st.write(file)
            with open(f'generated_files/{file}', 'rb') as f:
                st.download_button('Download', f, file_name=file)

if __name__ == "__main__":
    main()