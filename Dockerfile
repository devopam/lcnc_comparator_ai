# Use Python 3.11 as base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create Streamlit config directory
RUN mkdir -p /root/.streamlit

# Copy Streamlit config
COPY .streamlit/config.toml /root/.streamlit/config.toml

# Expose port
EXPOSE 5000

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Initialize database and start Streamlit
CMD python init_db.py && streamlit run main.py --server.port 5000
