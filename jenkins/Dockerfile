FROM jenkins/jenkins:lts

USER root

# Install python + dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-venv python3-pip curl xvfb xauth && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    apt-get clean

# Set up a virtual environment
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
