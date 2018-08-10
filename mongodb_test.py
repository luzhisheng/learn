import pymongo


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


class Spider(object):
    def __init__(self):
        self.db_local = MyMongodb(**LOCAL_SETTING)
        self.db_dev = MyMongodb(**DEV_SETTING)

    # 查询存在 xx 字段的记录
    def mongo_text(self):
        self.db_local['news'].find({"goodId": {"$exists": "true" }})

    # 查询不存在 xx 字段的记录
    def mongo_text_1(self):
        self.db_local['news'].find({"textureName": {"$exists": "false"}})

    # 查询一条数据记录
    def mongo_find(self, source):
        reseut = self.db_dev['news'].find_one({'source': source})
        print(reseut['domain'])


if __name__ == '__main__':

    source = ('')
    spider = Spider()

    for i in source:
        #print(i)
        spider.mongo_find(i)
