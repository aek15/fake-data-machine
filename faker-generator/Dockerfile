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

ENV STREAMLIT_STATS_OPT_OUT=true
# Make port 8501 available to the world outside this container
EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "faker-generator/app.py", "--server.port=8501"]