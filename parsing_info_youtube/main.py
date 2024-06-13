# pip install google-api-python-client      -   Клиентская библиотека API Google для Python

from conf import KEY
import googleapiclient.discovery

CHANNEL_NAME = "InvestFuture"
KEY = KEY

youtube = googleapiclient.discovery.build(serviceName="youtube", version="v3", developerKey=KEY, )


def channel(channel_name):
    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        forUsername=channel_name,
        maxResults=10
    ).execute()
    return request['items'][0]['id']


def playlists(chan_id):
    request = youtube.playlists().list(
        part="snippet,contentDetails",
        channelId=chan_id,
        maxResults=25
    ).execute()

    for video in request['items']:
        print(video)
        # print(f"Название плейлиста {video['snippet']['title']}, количество видео {video['contentDetails']['itemCount']}")

def playlists_video(play_id):
    request = youtube.playlistItems().list(
        part="snippet,contentDetails",
        playlistId=play_id,
        maxResults=25
    ).execute()
    # for video in request['items']:
    #     print(video)


def video(vid_id):
    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id=vid_id
    ).execute()
    # for video in request['items']:
    #     print(video)
    # print(request['qd4xWVWCyRc']['videoId'])
    # print(request)


if __name__ == "__main__":
    channel_id = channel(CHANNEL_NAME)
    # playlists(channel_id)
    # playlists("UCQmYubm0bFtExa7Q9oHT6Rg")
    playlists_video("PL3gklWqLza7rQ56ZSlFK8xo65yQERTd1O")
    # video('qd4xWVWCyRc')
