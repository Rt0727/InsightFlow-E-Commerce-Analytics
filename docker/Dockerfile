FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install flask mysql-connector-python

# Copy application files into the container
COPY . /app

# Set the default command to run the Flask app
CMD ["python", "app.py"]
