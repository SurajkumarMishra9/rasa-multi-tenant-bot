This repository contains the code for a multi-chatbot dispatcher built using Python's Flask framework. It allows you to run two separate chatbots with individual models and configurations and route user requests to the appropriate chatbot.


**Features:**

Supports two chatbots with independent models and configurations.

Listens on port 5000 for incoming user requests.

Identifies the target chatbot based on the bot ID included in the endpoint URL.

Routes requests to the appropriate chatbot running on port 5005 (binary) or 5006 (Suraj).

Returns the chatbot's response to the user.



**Requirements:**

Python 3.8

Flask (https://flask.palletsprojects.com/)



**Setup:**

Clone this repository.
Install required dependencies: pip install rasa & pip install Flask.

The individual chatbots (binary and Suraj) are preconfigured with their respective models and YAML files.

Run the chatbots with API enabled from their respecitve directory and on respective ports (5005 for binary and 5006 for Suraj).



**Usage:**

Run the dispatcher: python dispatcher.py

Send a POST request to http://localhost:5000/suraj or http://localhost:5000/binary with a JSON body containing the message,

The dispatcher will route the request to the specified chatbot and return the response.
