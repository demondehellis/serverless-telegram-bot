import json
from src.telegrambot import *
from src.db_wrapper import DBWrapper

logger = logging.getLogger()
if logger.handlers:
    for handler in logger.handlers:
        logger.removeHandler(handler)
logging.basicConfig(level=logging.INFO)

def random_phrase(tags = []):
    random_phrase = "..."
    return random_phrase

def get_reply(text, params = []):
    reply_text = random_phrase()
    return reply_text

def debug(data):
    logger.debug(data)
    print("")
    print("DEBUG:")
    print(data)
    print("")

def store_update(data):
    telegram_updates_table = os.getenv('TELEGRAM_UPDATES_TABLE')
    db = DBWrapper(telegram_updates_table)
    data['id'] = str(data['update_id'])
    db.put(data)

def webhook(event, context):
    """
    Runs the Telegram webhook.
    """
    logger.info('Event: {}'.format(event))

    if event.get('httpMethod') == 'POST' and event.get('body'): 

        try:
            body_string = event.get('body')
            json_data = json.loads(body_string)
            store_update(json_data)

            bot = configure_telegram()
            update = telegram.Update.de_json(json_data, bot)
            chat_id = update.message.chat.id
            intput_text = update.message.text
            logger.info('Message received: ' + intput_text)

            response_text = get_reply(intput_text)
            response_data = {"text": response_text}        
            reply(chat_id=chat_id, data=response_data)
            logger.info('Message sent: ' + response_text)
            
            response = SuccessResponse('response text: ' + response_text)

        except Exception as e:
            debug(e)
            response = ErrorResponse('(х_х)')
        finally:
            return response.make()        

    response = ErrorResponse('something wrong...')
    return response.make()