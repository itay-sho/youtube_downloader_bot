import youtube_dl
import os.path


class YoutubeDownloader:
    OUTPUT_DIR = r'/tmp/'
    YOUTUBE_DL_OPTIONS = {
        'format': 'bestaudio/best',
        'outtmpl': r'/tmp/foo_%(title)s-%(id)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    @staticmethod
    def download_and_convert(youtube_link):
        with youtube_dl.YoutubeDL(YoutubeDownloader.YOUTUBE_DL_OPTIONS) as ydl:
            info = ydl.extract_info(url=youtube_link, download=False)
            output_filename = '{path}{filename}{extension}'.format(
                path=YoutubeDownloader.OUTPUT_DIR,
                filename=ydl.prepare_filename(info),
                extension='mp3'
            )
            output = ydl.download([youtube_link])
            if output == 0:
                output_filename = '{filename}.{extension}'.format(
                    filename=os.path.join(YoutubeDownloader.OUTPUT_DIR, ydl.prepare_filename(info)),
                    extension='mp3'
                )
                return output_filename

        return False
