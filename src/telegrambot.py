import os
import telegram
import logging
from src.responses import SuccessResponse
from src.responses import ErrorResponse

logger = logging.getLogger()
if logger.handlers:
    for handler in logger.handlers:
        logger.removeHandler(handler)
logging.basicConfig(level=logging.INFO)

def configure_telegram():
    """
    Configures the bot with a Telegram Token.

    Returns a bot instance.
    """

    TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
    if not TELEGRAM_TOKEN:
        logger.error('The TELEGRAM_TOKEN must be set')
        raise NotImplementedError

    return telegram.Bot(TELEGRAM_TOKEN)

def set_webhook(event, context):
    """
    Sets the Telegram bot webhook.
    """

    logger.info('Event: {}'.format(event))
    bot = configure_telegram()
    url = 'https://{}/{}/'.format(
        event.get('headers').get('Host'),
        event.get('requestContext').get('stage'),
    )
    webhook = bot.set_webhook(url)

    if webhook:
        response = SuccessResponse('ok')
        return response.make()

    response = ErrorResponse('something wrong')
    return response.make()

def reply(chat_id, data, params = []):

    try:
        bot = configure_telegram()
        if os.environ.get('STAGE') != 'local':
        
            if 'text' in data:
                response_text = data['text']

                if response_text is not None:
                    bot.sendMessage(chat_id=chat_id, text=response_text)
                    logger.info('Message sent: ' + response_text)
    except Exception as e:
        logger.error(e)
    