# 定义 Thrift RPC 接口
namespace py example

struct Data {
    1:string text
}

service format_data {
    Data do_format(1:Data data),
}