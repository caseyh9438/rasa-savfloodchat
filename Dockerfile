# Extend the official Rasa SDK image
FROM rasa/rasa-sdk:latest

# Add a custom system library (e.g. git)
RUN apt-get update && \
    apt-get install -y git

RUN pip install dnspython