# Python 3.9 use kar rahe hain taaki 'Callable' wala error na aaye
FROM python:3.9-slim-bullseye

# System updates and required tools
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    git \
    curl \
    ffmpeg \
    python3-pip \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Node.js (Music bots ke liye Node stable hona chahiye)
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
