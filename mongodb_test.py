import pymongo


LOCAL_SETTING = {
    'host': '127.0.0.1',
    'port': 27017,
    'username': 'admin',
    'pwd': '',
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


class spider(object):
    def __init__(self):
        self.db_local = MyMongodb(**LOCAL_SETTING)

    # 查询存在 xx 字段的记录
    def mongo_text(self):
        self.db_local.good.find({"goodId": {"$exists": "true" }})

    # 查询不存在 xx 字段的记录
    def mongo_text_1(self):
        self.db_local.good.find({"textureName": {"$exists": "false"}})

