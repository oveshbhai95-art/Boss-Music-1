# Latest stable Python image (Slim-Bullseye is best for bot deployment)
FROM python:3.10-slim-bullseye

# System updates and required tools
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    git \
    curl \
    ffmpeg \
    python3-pip \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Latest Node.js (Node 20.x is current LTS)
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g npm@latest

# Set working directory
WORKDIR /app

# Upgrade pip
RUN pip3 install --no-cache-dir -U pip

# Copy all files to /app
COPY . .

# Install Python requirements
RUN pip3 install --no-cache-dir -U -r requirements.txt

# Start the bot
CMD ["python3", "main.py"]
