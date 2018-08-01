from os import rename
import youtube_dl


def download(youtube_url):
    """
    download the video from the given url
    """

    def rename_hook(d):
        """
        youtube-dl's hook to rename the downloaded video name
        """

        if d['status'] == 'finished':
            file_name = '1'
            rename(d['filename'], file_name)

    # 定义某些下载参数
    ydl_opts = {
        # 'format': 'bestaudio/best',
        'progress_hooks': [rename_hook],
        # outtmpl 格式化下载后的文件名，避免默认文件名太长无法保存
        'outtmpl': '%(id)s%(ext)s'
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])


if __name__ == '__main__':
    download('https://www.youtube.com/watch?v=VUOAszEiR8I')
