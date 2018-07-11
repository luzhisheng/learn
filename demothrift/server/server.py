# server实现了服务端用于接收客户端发送的数据，并对数据进行大写处理后返回给客户端

__author__ = 'xieyanke'

from demothrift.example import format_data
from demothrift.example import ttypes
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

__HOST = 'localhost'
__PORT = 8080


class FormatDataHandler(object):
    def do_format(self, data):
        return ttypes.Data(data.text.upper())


if __name__ == '__main__':
    handler = FormatDataHandler() #实例化类

    processor = format_data.Processor(handler)
    transport = TSocket.TServerSocket(__HOST, __PORT)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    rpcServer = TServer.TSimpleServer(processor,transport, tfactory, pfactory)

    print('Starting the rpc server at', __HOST,':', __PORT)
    rpcServer.serve()
