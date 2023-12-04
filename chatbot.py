from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chatbot
chatbot = ChatBot('MyChatBot')

# Train the chatbot with some conversations
trainer = ListTrainer(chatbot)
trainer.train([
    'Hi',
    'Hello',
    'How are you?',
    'I am good. How about you?',
    'I am also good',
    'That is great to hear',
    'Thank you',
    'You are welcome'
])

# Start a conversation with the chatbot
while True:
    try:
        user_input = input("You: ")
        bot_response = chatbot.get_response(user_input)
        print("Bot: ", bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break























