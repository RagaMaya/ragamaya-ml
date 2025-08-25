# Use a lightweight Python base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Copy application code
COPY . .

# Expose port
EXPOSE 9013

# Run the app with Gunicorn
# -w 4 = 4 workers (adjust based on CPU cores)
# -k sync = sync workers (good default, can change to gevent for async)
# -b 0.0.0.0:9013 = bind address
CMD ["gunicorn", "-w", "4", "-k", "sync", "-b", "0.0.0.0:9013", "app:app"]
