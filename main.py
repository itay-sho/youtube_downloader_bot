import os
import sys

sys.path.append(os.path.join(os.environ['LAMBDA_TASK_ROOT'], 'env/lib/python3.6/site-packages'))
sys.path.append(os.environ['LAMBDA_TASK_ROOT'])
os.environ['PATH'] += '{old_path}:{new_path}'.format(old_path=os.environ['PATH'], new_path=os.path.join(os.environ['LAMBDA_TASK_ROOT'], 'binaries'))

import json
import logging

import telegram_bot
import youtube_downloader
import decorators


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    try:
        logger.info('Event: {}'.format(event))
        logger.info('Context: {}'.format(context))

        body = json.loads(event['body'])
        chat = body['message']['chat']
        text = body['message']['text']

        logger.info('PATH: {}'.format(os.environ['PATH']))

        logger.info('Body: {}'.format(body))
        logger.info('Chat: {}'.format(chat))
        logger.info('Chat ID: {}'.format(chat['id']))
        logger.info('Message: {}'.format(text))

        bot = telegram_bot.TelegramBot('tokens/telegram_token.txt')

        if text.split()[0] == '/youtube_to_mp3':
            telegram_bot.TelegramBot.youtube_to_mp3(bot.bot, chat, text)
        else:
            bot.bot.send_message(chat_id=chat['id'], text='Ack')
    finally:
        return {}


def main():
    bot = telegram_bot.TelegramBot('tokens/telegram_token.txt')
    bot.launch()


if __name__ == '__main__':
    main()

