FROM jenkins/jenkins:lts

USER root

# Install dependencies
RUN apt-get update && \
    apt-get install -y \
    python3 python3-venv python3-pip curl xvfb xauth && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    apt-get clean

# Set up a virtual environment
RUN python3 -m venv /opt/venv

# Activate the venv by default in all shells
ENV PATH="/opt/venv/bin:$PATH"
