# Base image
FROM python:3.9-slim

# Set work directory
WORKDIR /app

# Pre-download torch wheel
COPY torch-2.0.1-cp39-cp39-linux_x86_64.whl /tmp/

# Copy requirements file
COPY requirements.txt /app/

# Install dependencies
RUN pip install /tmp/torch-2.0.1-cp39-cp39-linux_x86_64.whl
RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt

# Copy application files
COPY . /app

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
