# Use the official Python 3.9 image as the base image
FROM python:3.9  

# Set the environment variable to ensure Python output is displayed in real-time (useful for debugging)
ENV PYTHONUNBUFFERED 1  

# Set the working directory inside the container to /app
WORKDIR /app  

# Copy the requirements file to the working directory
COPY requirements.txt /app/requirements.txt  

# Install dependencies from the requirements file
RUN pip install -r requirements.txt  

# Copy the entire project directory into the container
COPY . /app  

CMD python3 manage.py runserver 0.0.0.0:8081