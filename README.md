# Summary
This is an intelligent Python chatbot that feeds data from residents into the Floodsight backend for populating the Floodsight citizen reporting application, and allows residents to get relevant inforation by asking questions via SMS.

It's intended to provide residents a low-frequency way to get current emergency information as well as to report on conditions to augment forecasting insights.

It is built in Python, 
Download Docker to your computer
Git clone repository

# To start http server
cd into project root (where the docker-compose.yml is located)
run: docker-compose up

# To interact with bot UI locally
create anaconda or python virtual environment using virtualenv or conda
activate virtual environment
cd into project root (where the requirements.txt is location)
run: pip install -r requirements
run: rasa x
