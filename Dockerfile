# Use Python base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Install system dependencies (important for PostgreSQL and other C extensions)
RUN apt-get update && apt-get install -y libpq-dev gcc

# Copy project files
COPY . .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt  # No need for virtualenv activation!

# Expose the Flask app port
EXPOSE 5000

# Run the Flask application
CMD ["python", "run.py"]
