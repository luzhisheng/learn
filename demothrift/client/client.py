# pip install thrift
# sudo apt install thrift-compiler

# client.py 实现了客户端用于发送数据并打印接收到 server 端处理后的数据

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from demothrift.example.format_data import Client
from demothrift.example.format_data import Data

__HOST = 'localhost'
__PORT = 8080

tsocket = TSocket.TSocket(__HOST, __PORT)
transport = TTransport.TBufferedTransport(tsocket)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = Client(protocol)

data = Data('这是我的第一个thrift代码')
transport.open()

print(client.do_format(data).text)
