FROM jenkins/jenkins:lts

USER root

# Install python + dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv curl xvfb xauth && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry && \
    apt-get clean

# Disable Poetry virtualenv creation
RUN poetry config virtualenvs.create false
