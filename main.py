import enum

import telegram_bot
import youtube_downloader
import decorators


def main():
    bot = telegram_bot.TelegramBot('tokens/telegram_token.txt')
    bot.launch()


if __name__ == '__main__':
    main()

