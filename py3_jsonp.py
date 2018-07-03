import json
import re

jsonp_begin = r'callback('
jsonp_end = r')'


def from_jsonp(jsonp_str):
    '''方法一'''

    jsonp_str = jsonp_str.strip()
    # 是否以指定子字符串开头或者某个字符串结束
    if not jsonp_str.startswith(jsonp_begin) or not jsonp_str.endswith(jsonp_end):
        # 抛出异常
        raise ValueError('Invalid JSONP')
    # 字符串切片[num:-num]
    return json.loads(jsonp_str[len(jsonp_begin):-len(jsonp_end)])


def parse_jsonp(self, response):
    '''方法二'''

    result = response.text
    # findall 全局查找返回列表，取第0个
    item = re.findall(r"jQuery[0-9]+_[0-9]+\((.*)\)", result)[0]
    data_json = json.loads(item)
    return data_json