FROM jenkins/jenkins:lts

USER root

# Install Python and other dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip curl && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    apt-get clean

USER jenkins
