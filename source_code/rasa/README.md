# Building a traditional conversational bot

Building a chatbot with Rasa involves several steps, such as setting up the environment, creating the necessary files, training the bot, and interacting with it. Here's a simple example to help you get started with Rasa:

## Install Rasa

```bash
# First, make sure you have Python 3.6, 3.7, or 3.8 installed on your system. Then, install Rasa using pip:
pip install rasa websockets

# Create a new Rasa project:
# In your terminal or command prompt, run the following command to create a new Rasa project:
rasa init --no-prompt
This will create a new directory called rasa with the necessary files and folders for your Rasa chatbot.
```

## Define intents and entities

Navigate to ``rasa/data`` directory and open the ``nlu.yml`` file - you can define the intents and entities of your chatbot.

## Define the dialogue management

Go to the ``rasa/data`` directory and open the ``stories.yml`` file. Define some conversation examples, so Rasa can learn how to manage the dialogue.

## Define responses

Navigate to the ``rasa/domain.yml`` file, where you define the chatbot's responses. Add the following responses for the greet and goodbye intents:

# Train the chatbot
In your terminal or command prompt, navigate to the root of the rasa directory, and run the following command to train your chatbot:

```bash
rasa train
```

Test the chatbot - After training is complete, you can test the chatbot by running the following command: ``rasa shell``. Now, you can interact with your chatbot by typing messages like "Hello" or "Goodbye" and seeing the corresponding responses.
