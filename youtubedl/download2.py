from os import rename
import youtube_dl
import json


def download(url):
    def rename_hook(d):
        if d['status'] == 'finished':
            file_name = '1'
            rename(d['filename'], file_name)

    ydl_opts = {
       # 'format': 'worstvideo',
        'progress_hooks': [rename_hook],
        'outtmpl': '%(id)s%(ext)s'
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(url, download=False)
        # ydl.download([url])

    print(json.dumps(result))


if __name__ == '__main__':
    download('https://vimeo.com/246917979')
    # download('https://clips.twitch.tv/ResoluteStrangeTapirNerfBlueBlaster')