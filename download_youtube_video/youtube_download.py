# pip install pytube            -   download youtube
# https://www.ffmpeg.org/         -   обьединение видео и аудио файла в один файл
# pip install ffmpeg-python

from pytube import YouTube
import ffmpeg

URL = 'https://www.youtube.com/watch?v=3ohS3pE3k2E'
DOWNLOAD_DIRECTORY = 'Downloads'


def download_video(url):
    yt = YouTube(url)
    # yt.streams.get_highest_resolution().download(DOWNLOAD_DIRECTORY)
    stream_video = yt.streams.filter(file_extension='mp4').order_by('resolution').desc().first()
    stream_video.download(DOWNLOAD_DIRECTORY, 'video')
    if not stream_video.is_progressive:
        stream_audio = yt.streams.get_audio_only()
        stream_audio.download(DOWNLOAD_DIRECTORY, 'audio')
        combine(DOWNLOAD_DIRECTORY + '/audio.mp4', DOWNLOAD_DIRECTORY + '/video.mp4')


def combine(audio, video):
    audio_stream = ffmpeg.input(audio)
    video_stream = ffmpeg.input(video)
    ffmpeg.output(audio_stream, video_stream, DOWNLOAD_DIRECTORY + '/result.mp4').run()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    download_video(URL)
