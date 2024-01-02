import streamlit as st
import os
from data_generator import generate_ddl, generate_dummy_data

def main():
    st.title("Fake Data Machine")

    table_name = st.text_input("Table Name", "my_table")
    num_columns = st.number_input("Number of Columns", min_value=1, max_value=20, value=3)

    columns = []
    for i in range(int(num_columns)):
        col1, col2 = st.columns(2)
        with col1:
            col_name = st.text_input(f"Column {i+1} Name", f"column_{i+1}")
        with col2:
            col_type = st.selectbox(f"Column {i+1} Type", ["VARCHAR", "INTEGER", "NUMBER", "BOOLEAN", "DATE", "TIME", "TIMESTAMP", "VARIANT"], index=0, key=f"type_{i+1}")
            
        columns.append({"name": col_name, "type": col_type})
        

    if st.button("Generate DDL"):
        ddl = generate_ddl(table_name, columns)
        st.text_area("DDL Statement", ddl, height=100)

    num_rows = st.number_input("Number of Rows per File", min_value=1, max_value=1000000, value=100)
    num_files = st.number_input("Number of Files", min_value=1, max_value=10, value=1)
    file_format = st.selectbox("Select File Format", ["CSV", "Parquet", "JSON", "XML"], key="file_format_select")    
    if st.button("Generate Files"):
        os.makedirs('generated_files', exist_ok=True)
        for i in range(int(num_files)):
            df = generate_dummy_data(columns, int(num_rows))
            file_name = f'generated_files/{table_name}_{i}.{file_format.lower()}'
            if file_format == "CSV":
                df.to_csv(file_name, index=False)
            elif file_format == "Parquet":
                df.to_parquet(file_name, index=False)
            elif file_format == "JSON":
                df.to_json(file_name, orient='records')
            elif file_format == "XML":
                df.to_xml(file_name, index=False)
            st.success(f"File {file_name} generated.")

    if st.button("List Generated Files"):
        files = os.listdir('generated_files')
        for file in files:
            st.write(file)
            with open(f'generated_files/{file}', 'rb') as f:
                st.download_button('Download', f, file_name=file)

if __name__ == "__main__":
    main()
