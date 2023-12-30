# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /usr/src/app

# Install git
RUN apt-get update && apt-get install -y git

# Clone your repository
RUN git clone https://github.com/aek15/fake-data-machine.git .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r faker-generator/requirements.txt

# Make the start.sh file executable
RUN chmod +x faker-generator/start.sh

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Run the start script when the container launches
#CMD ["./faker-generator/start.sh"]
ENTRYPOINT ["streamlit", "run", "faker-generator/app.py", "--server.port=8501", "--server.address=127.0.0.1"]