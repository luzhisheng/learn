# py3 str转成bytes
a = 'aiyingfeng'
a_bytes = a.encode('utf-8')
print(type(a_bytes))

# py3 bytes转成str
a_str = a_bytes.decode('utf-8')
print(type(a_str))


import base64
import hashlib


# 哈希加密转码问题
def get_sign(url):
    sign = base64.urlsafe_b64encode(
        hashlib.md5(url).digest())
    sign = str(sign.decode()).replace('==', '')
    return sign


if __name__ == '__main__':
    url = 'www.google.com'
    sign = get_sign(url.encode("utf8"))
    print(sign)