# Install the required library
# pip install chatterbot==1.0.5 chatterbot_corpus flask

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask, request, jsonify

# Step 1: Create and train the chatbot
chatbot = ChatBot('VirtualAssistant')

# Train the chatbot using English corpus
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

# Step 2: Set up a Flask app for interaction
app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    # Get a response from the chatbot
    bot_response = chatbot.get_response(user_message)
    return jsonify({'response': str(bot_response)})

# Step 3: Run the app
if __name__ == '__main__':
    app.run(debug=True)
