FROM mcr.microsoft.com/playwright/python:v1.51.0-noble

WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y xvfb && \
    apt-get clean

# Copy poetry project files
COPY pyproject.toml poetry.lock ./

# Install Poetry (globally)
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# Install dependencies with Poetry (no venv - use system site-packages)
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Copy the rest of the app
COPY . .
