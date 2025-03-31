# Use Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY requirements.txt .
COPY app.py .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the Flask app
CMD ["python", "app.py"]

