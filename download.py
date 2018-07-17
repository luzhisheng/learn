from os import rename
import youtube_dl
import time
import pymongo


DEV_SETTING = {
    'host': 'xxxx',
    'port': 27017,
    'username': 'xxx',
    'pwd': 'xxx',
    'db': 'xxx',
    'collection': '',
    'source': '',
    'stats': '',
    'producer': '',
}

LOCAL_SETTING = {
    'host': '127.0.0.1',
    'port': 27017,
    'username': 'admin',
    'pwd': '123',
    'db': 'admin',
    'collection': '',
    'source': '',
    'stats': '',
    'producer': '',
}


class MyMongodb(object):
    def __new__(cls, debug=0, *args, **kw):

        if debug == 0:
            if not hasattr(cls, 'db_dic'):
                cls.db_dic = {}

            if kw.get('username', '') not in cls.db_dic:
                instance = pymongo.MongoClient(kw.get('host'), kw.get('port'))
                database = instance[kw.get('db')]
                database.authenticate(
                    kw.get('username'), kw.get('pwd'), source=kw.get('source'))
                cls.db_dic.update({kw.get('username'): database})
            return cls.db_dic.get(kw.get('username'))


class MyLogger(object):
    def debug(self, msg):
        print("---" * 20 + msg)


class GetItem(object):

    def rename_hook(self,d):
        # 重命名下载的视频名称的钩子
        if d['status'] == 'finished':
            file_name = 'video/{}.mp4'.format(int(time.time()))
            rename(d['filename'], file_name)
            print('下载完成{}'.format(file_name))

    def download(self,youtube_url):
        # 定义某些下载参数
        ydl_opts = {
            'progress_hooks': [self.rename_hook],
            # 格式化下载后的文件名，避免默认文件名太长无法保存
            'outtmpl': '%(id)s%(ext)s',
            # 强制打印时间
            'forceduration': 1,
            'logger': MyLogger()
        }

        # with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        #     result = ydl.extract_info(youtube_url,download=False)

        # with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        #     result = ydl.download([youtube_url])

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            result = ydl.process_info(dict(ydl_opts))

        print(result)


class ValueUrl(object):

    def __init__(self):
        self.db_dev = MyMongodb(**DEV_SETTING)
        self.db_local = MyMongodb(**LOCAL_SETTING)

    def get_url(self,source):
        all_source_list = self.db_dev['news'].find({'source': source})
        for item in all_source_list:
            item_url = item.get('url')
            print(item_url)
            item = GetItem()
            item.download(youtube_url=item_url)


if __name__ == '__main__':
    obj = ValueUrl()
    obj.get_url(source='Dogumentary TV')
