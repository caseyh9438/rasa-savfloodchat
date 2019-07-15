# Extend the official Rasa SDK image
FROM rasa/rasa-sdk:latest

# Add a custom system library (e.g. git)
RUN apt-get update && \
    apt-get install -y git

RUN pip install -r requirements.txt

RUN pip install geopy

RUN pip install pymongo

RUN pip install dnspython
