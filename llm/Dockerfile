# Base image
FROM python:3.9-slim

# Set work directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt

# Copy application files
COPY . /app

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
