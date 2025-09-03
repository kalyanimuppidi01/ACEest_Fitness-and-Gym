# Use a lightweight Python base image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements.txt first (better for caching)
COPY requirements.txt .

ENV DOCKER_ENV=1

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the project files
COPY . .

# Run unit tests during build
RUN pytest --maxfail=1 --disable-warnings -q

# Expose port 5000 for Flask
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
