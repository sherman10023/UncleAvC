from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import apiai, json
updater = Updater (token = '952376782:AAGilgCGWXhlZ1pb_MMITPGJNPlt_AXVN2o')
dispatcher = updater.dispatcher

def startCommand (bot, update):
    bot.send_message (chat_id = update.message.chat_id, text = 'Hello, Hosehbo?')

def textMessage (bot, update):
    request = apiai.ApiAI ('07cf4955477b4435ab349e6a9cfc56d8').text_request()
    request.lang = 'en'
    request.session_id = 'BatlabAIBot'
    request.query = update.message.text
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech']
    if response:
        bot.send_message (chat_id = update.message.chat_id, text = response)
    else:
        bot.send_message (chat_id = update.message.chat_id, text = "You gong simi lan?")
    
start_command_handler = CommandHandler ('start', startCommand)
text_message_handler = MessageHandler (Filters.text, textMessage)

dispatcher.add_handler (start_command_handler)
dispatcher.add_handler (text_message_handler)

updater.start_polling (clean = True)

updater.idle()