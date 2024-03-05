
import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Import the OpenAI library
import openai

# Set up your OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Define the function to handle the /openai command
def openai_command(update: Update, context: CallbackContext):
    # Check if the message is from a group chat
    if update.message.chat.type != 'group':
        update.message.reply_text("This command only works in group chats.")
        return

    # Get the user input
    user_input = ' '.join(context.args)
    
    # Call the OpenAI API to get a response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=user_input,
        max_tokens=100
    )
    
    # Send the response back to the group chat
    update.message.reply_text(response.choices[0].text)

# Set up the Telegram bot
updater = Updater('YOUR_TELEGRAM_BOT_TOKEN', use_context=True)
dispatcher = updater.dispatcher

# Add the /openai command handler
dispatcher.add_handler(CommandHandler('openai', openai_command))

# Start the bot
updater.start_polling()
updater.idle()






                           
