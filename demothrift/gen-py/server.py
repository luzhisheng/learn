from HelloService import HelloService
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


class HelloServiceHanler:

    def __init__(self):
        self.log = {}

    def sayHello(self):
        # sayHello接口的实现
        print('sayhello')

    def getDate(self, input):
        # getDate接口实现
        return input + 'from server 1024'


hanler = HelloServiceHanler()
processor = HelloService.Processor(handler=hanler)
transport = TSocket.TServerSocket(port=9090)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
print('启动服务器......')
server.serve()
print('已完成的....')
