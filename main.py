import enum

import telegram_bot
import youtube_downloader
import decorators


def main():
    bot = telegram_bot.TelegramBot('tokens/telegram_token.txt')
    bot.launch()

    # youtube_downloader.YoutubeDownloader.download_and_convert('https://www.youtube.com/watch?v=94BIxqTYJzU')


if __name__ == '__main__':
    main()

