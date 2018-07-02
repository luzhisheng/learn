a = 'aiyingfeng'
a_bytes = a.encode('utf-8')
print(type(a_bytes))

a_str = a_bytes.decode('utf-8')
print(type(a_str))

import base64