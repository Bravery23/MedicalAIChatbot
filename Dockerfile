# Base image with Python and pip
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all project files
COPY . /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install pipenv and project dependencies
RUN pip install --no-cache-dir pip --upgrade
RUN pip install --no-cache-dir rasa[full]

# Give execute permission to start script
RUN chmod +x start.sh

# Expose port for Rasa server
EXPOSE 5005

# Start the bot using the shell script
CMD ["./start.sh"]