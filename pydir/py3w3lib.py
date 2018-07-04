import os
import w3lib.encoding
import w3lib.html
import w3lib.http
import w3lib.url


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

    # 返回HTML元元素的http-equiv参数，并返回一个元组
    http_equiv = w3lib.html.get_meta_refresh(file_content)
    print(http_equiv)

    # 删除注释
    comments = w3lib.html.remove_comments(file_content)
    print(comments)

    # 仅删除HTML标签,which_ones和keep都是元组，有四种情况
    remove_tag_str = w3lib.html.remove_tags(file_content)
    print(remove_tag_str)

    # 删除标签及其内容
    remove_tag_content_str = w3lib.html.remove_tags_with_content(file_content,which_ones=('html',))
    print('-------------')
    print(remove_tag_content_str)

    # 通过将实体转换为相应的unicode字符，从给定文本中删除实体
    remove_entities = w3lib.html.replace_entities('&lt;')
    print('&lt;')
    print(remove_entities)

    # which_ones是我们要删除的转义字符的元组。默认情况下移除了\n，\t，\r,replace_by是用于替换转义字符的字符串。
    chars = w3lib.html.replace_escape_chars(file_content)
    print(chars)

    # 替换HTML标签, token='' 默认为空
    replace_tag = w3lib.html.replace_tags(file_content)
    print(replace_tag)

    # 去除首尾空格
    whitespace = w3lib.html.strip_html5_whitespace('\n  1111 \n')
    print(whitespace)

    # html实体转义，不是删除
    markup = w3lib.html.unquote_markup('<h1>&lt;')
    print(markup)

    # 客户端应该使用带有“Bearer”HTTP授权方案的“Authorization”请求头部字段发起带有不记名令牌的身份验证请求。资源服务器必须支持此方法。
    Authorization = w3lib.http.basic_auth_header('user','123456')
    print(Authorization)

    # 返回标头的原始HTTP标头表示
    http_head = w3lib.http.headers_dict_to_raw({b'Content-type': b'text/html', b'Accept': b'gzip'})
    print(http_head)

    # 将原始标头（单个多行字节串）转换为字典
    http_dict = w3lib.http.headers_raw_to_dict(http_head)
    print(http_dict)

    # 在给定网址中添加或修改参数
    url = 'www.google.com'
    new_url = w3lib.url.add_or_replace_parameter(url,'id','1')
    new_url_2 = w3lib.url.add_or_replace_parameter(new_url, 'pid', '1')
    print(new_url)
    print(new_url_2)

    # 如果给定路径名，则返回其文件URI，否则返回未修改
    # uri 是一种资源
    uri = w3lib.url.any_to_uri(file_content)
    print(uri)

    print('\n')

    # UTF-8转换 + 非ASCII字符的百分比编码
    ascii_url = w3lib.url.canonicalize_url(u'http://www.example.com/r\u00e9sum\u00e9')
    print(ascii_url)

    # 然后按值对查询参数进行排序
    sort_url = w3lib.url.canonicalize_url('http://www.example.com/do?c=3&b=5&b=2&a=50')
    print(sort_url)




if __name__ == '__main__':
    dirname = 'html_body_str.html'
    test_str(dirname=dirname)