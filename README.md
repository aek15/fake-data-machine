# Fake Data Machine

This application is designed to generate files with dummy data for database testing purposes. It uses Streamlit for an interactive web interface, allowing users to specify table details and generate corresponding dummy data files using the Faker library.

## Features
- Define table structure including name and columns with types.
- Generate SQL Data Definition Language (DDL) statements.
- Specify the number of rows and files for dummy data generation.
- Download generated dummy data files in CSV format.

## Installation

### Prerequisites
- Docker installed on your machine. Visit [Docker's official website](https://docs.docker.com/get-docker/) for installation instructions.

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/aek15/fake-data-machine.git
   cd fake-data-machine
    ```

2. **Build the Docker Image**
   ```bash
   docker build -t fake-data-machine .
    ```
3. **Run the Docker Container**
   ```bash
   docker run -p 8501:8501 -v ${PWD}/generated_files:/usr/src/app/generated_files fake-data-machine
    ```

After running the above command, the application should be accessible at http://localhost:8501.

## How to use

1. **Accessing the Application**  
Open a web browser and navigate to http://localhost:8501.

2. **Defining the Table Structure**  
Enter the desired table name.
Specify the number of columns.
For each column, provide a name and select a data type.

3. **Generate DDL Statement**  
Click on the "Generate DDL" button to view the SQL DDL statement for the specified table structure.

4. **Generating Dummy Data Files**  
Enter the desired number of rows per file and the total number of files.
Click the "Generate Files" button to create CSV files with dummy data.

5. **Downloading Generated Files**  
After generating files, click the "List Generated Files" button.
Click the "Download" button next to each file to download them.

6. **Modifying the Application**  
The application's code is modular, allowing for easy updates and maintenance:

- **app.py:** Handles the Streamlit frontend interface.
- **data_generator.py:** Contains logic for generating the DDL and dummy data.

## Contributions

Contributions to this project are welcome. Please create a pull request with your proposed changes.