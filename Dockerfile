FROM mcr.microsoft.com/playwright/python:v1.51.0-noble

WORKDIR /app

# Install python libraries
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install additional dependencies
RUN apt-get update && \
    apt-get install -y xvfb && \
    apt-get clean
