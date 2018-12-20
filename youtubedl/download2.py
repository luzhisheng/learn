import youtube_dl


def download(youtube_url):
    # 定义某些下载参数
    ydl_opts = {
        'format': '133+m4a',
        'outtmpl': '%(id)s%(ext)s'
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])


if __name__ == '__main__':
    download('https://www.youtube.com/watch?v=cQgn9TYeejs')