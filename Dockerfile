# Use official Python runtime as base image
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Copy calculator files to container
COPY calculator.py .
COPY test_calculator.py .

# Set environment variable
ENV PYTHONUNBUFFERED=1

# Run the calculator when container launches
CMD ["python3", "calculator.py"]
