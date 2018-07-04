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


if __name__ == '__main__':
    dirname = 'html_body_str.html'
    test_str(dirname=dirname)