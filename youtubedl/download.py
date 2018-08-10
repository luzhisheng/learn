#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import rename
import youtube_dl
import time
import pymongo
from youtube_dl import utils


DEV_SETTING = {
    'host': '47.88.244.133',
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


class GetItem(object):
    def __init__(self):
        self.status = ''

    def rename_hook(self, d):
        # print(d)
        # print(time.time())
        # print("*"*50)
        # 重命名下载的视频名称的钩子
        # if d['total_bytes'] > 10:
        #     return

        if d['status'] == 'finished':
            print(d['filename'])
            file_name = 'video/{}.mp4'.format('http-360p-282956134-worst')
            rename(d['filename'], file_name)
            self.status = d

    def download(self,youtube_url):
        # 定义某些下载参数
        ydl_opts = {
            'format': 'worst',
            'progress_hooks': [self.rename_hook],
            # 格式化下载后的文件名，避免默认文件名太长无法保存
            'outtmpl': '%(id)s%(ext)s',
        }

        # extract_info 提取信息
        # with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        #     result = ydl.extract_info(youtube_url, download=False)

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            # 下载给定的URL列表
            ydl.download([youtube_url])

        # 打印视频长度
        # print('*****')
        # print(result)
        # print(utils.formatSeconds(result['duration']))


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
    # obj = ValueUrl()
    # obj.get_url(source='Dogumentary TV')
    item = GetItem()
    item.download(youtube_url='https://images-cdn.9gag.com/photo/a3Kg675_460sv.mp4')
    # print(item.status)
    # print('*'*300)
    # item.download(youtube_url='https://www.youtube.com/watch?v=fc_MI3MbLPY')
    # print(item.status)
