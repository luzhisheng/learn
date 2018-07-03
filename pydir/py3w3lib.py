import os
import w3lib.encoding
import w3lib.html


def test_str(dirname):
    responses_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(responses_dir, dirname)
    file_content = open(file_path, 'r').read()

    # 返回html正文中元标记中指定的编码，或者None如果找不到合适的编码
    charset = w3lib.encoding.html_body_declared_encoding(file_content)
    print(charset)

    # 将原始html字节转换为unicode
    unicode = w3lib.encoding.html_to_unicode(None,file_content.encode('utf-8'))
    print(unicode)

    # 在content-type标头中提取编码
    content_type = w3lib.encoding.http_content_type_encoding(file_content)
    print(content_type)

    # Python处理以BOM开头的UTF-8编码文件
    bom = w3lib.encoding.read_bom(b'\xef\xbb\xbf')
    print(bom)

    # 返回encoding_alias映射到None 的编码，或者无法解释编码
    encod = w3lib.encoding.resolve_encoding('latin1')
    print(encod)

    # 使用给定的编码将str对象转换为unicode
    unicode = w3lib.encoding.to_unicode(file_content.encode('utf-8'),encoding='utf-8')
    print(unicode)

    # 寻找<base> 标签，为页面上的所有链接规定默认地址或默认目标
    url = w3lib.html.get_base_url(file_content,baseurl='www.google.com',encoding='utf-8')
    print(url)


if __name__ == '__main__':
    dirname = 'html_body_str.html'
    test_str(dirname=dirname)