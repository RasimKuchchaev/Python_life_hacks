import googleapiclient.discovery


KEY = 'AIzaSyCB1E__gKTv_kKrFBTml3KjGo53VAVofuY'
CHANNEL_NAME = 'myrusakov'

youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=KEY)


def get_video_ids_from_channel(channel_name):
    playlist_id = get_playlist_id(channel_name)
    response = youtube.playlistItems().list(
        part="snippet",
        playlistId=playlist_id,
        maxResults=10
    ).execute()
    ids = []
    for video in response['items']:
        ids.append(video['snippet']['resourceId']['videoId'])
    return ids


def get_playlist_id(channel_name):
    response = youtube.channels().list(
        part="contentDetails",
        forUsername=channel_name
    ).execute()
    return response['items'][0]['contentDetails']['relatedPlaylists']['uploads']


def print_videos_info(video_ids):
    response = youtube.videos().list(
        part='statistics,snippet',
        id=','.join(video_ids)
    ).execute()
    for video in response['items']:
        print('Название:', video['snippet']['title'])
        print('Просмотров:', video['statistics']['viewCount'])
        print('Лайков:', video['statistics']['likeCount'])
        print('Дизлайков:', video['statistics']['dislikeCount'])
        print('------------------------')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    videos = get_video_ids_from_channel(CHANNEL_NAME)
    print_videos_info(videos)