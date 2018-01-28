from telegram.ext import MessageHandler, CommandHandler, Filters
from telegram.ext import Updater
from telegram import Bot
import logging
import enum

import youtube_downloader


class YoutubeToMp3Arguments(enum.Enum):
    COMMAND_NAME = 0
    YOUTUBE_LINK = enum.auto()
    COUNT = enum.auto()


class TelegramBot:
    def __init__(self, token_filename):
        with open(token_filename, 'rt') as token_file:
            self.token = token_file.read().splitlines()[0]

        self.bot = Bot(token=self.token)

    def launch(self):
        updater = Updater(token=self.token)
        dispatcher = updater.dispatcher
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

        start_handler = CommandHandler('start', TelegramBot.start)
        youtube_to_mp3_handler = CommandHandler('youtube_to_mp3', TelegramBot.youtube_to_mp3_handler)
        dispatcher.add_handler(start_handler)
        dispatcher.add_handler(youtube_to_mp3_handler)

        updater.start_polling(timeout=100)

    @staticmethod
    def start(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="Try /youtube_to_mp3")

    @staticmethod
    def validate_youtube_link_argument(youtube_link_argument):
        # TODO
        return True

    @staticmethod
    def youtube_to_mp3_handler(bot, update):
        try:
            args_list = update.message.text.split()
            chat_id = update.message.chat_id

            if len(args_list) != YoutubeToMp3Arguments.COUNT.value:
                bot.send_message(chat_id=chat_id, text='Invalid arguments count')
                return

            youtube_link = args_list[YoutubeToMp3Arguments.YOUTUBE_LINK.value]

            if not TelegramBot.validate_youtube_link_argument(youtube_link):
                bot.send_message(chat_id=chat_id, text='Invalid argument')
                return

            bot.send_message(chat_id=chat_id, text='Starting to convert video')
            output_file = youtube_downloader.YoutubeDownloader.download_and_convert(args_list[YoutubeToMp3Arguments.YOUTUBE_LINK.value])

            with open(output_file, 'rb') as downloaded_audio:
                bot.send_audio(chat_id=chat_id, audio=downloaded_audio, timeout=100)

        except Exception as e:
            bot.send_message(chat_id=chat_id, text='Error: {}'.format(e))

    @staticmethod
    def youtube_to_mp3(bot, chat_id, text):
        try:
            logging.info("Starting calculate")

            args_list = text.split()

            if len(args_list) != YoutubeToMp3Arguments.COUNT.value:
                bot.send_message(chat_id=chat_id, text='Invalid arguments count')
                return

            logging.info("a")

            youtube_link = args_list[YoutubeToMp3Arguments.YOUTUBE_LINK.value]

            if not TelegramBot.validate_youtube_link_argument(youtube_link):
                bot.send_message(chat_id=chat_id, text='Invalid argument')
                return

            logging.info("b")

            bot.send_message(chat_id=chat_id, text='Starting to convert video')
            output_file = youtube_downloader.YoutubeDownloader.download_and_convert(
                args_list[YoutubeToMp3Arguments.YOUTUBE_LINK.value])

            logging.info("c")

            with open(output_file, 'rb') as downloaded_audio:
                bot.send_audio(chat_id=chat_id, audio=downloaded_audio, timeout=100)

        except Exception as e:
            logging.error("Exception: {}", e)
            bot.send_message(chat_id=chat_id, text='Error: {}'.format(e))
