from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


def send_mail(title, content, to_addrs=None, from_addr=None, password=None):

    '''
    发送邮件函数
    :param title: 邮件标题
    :param content: 邮件内容 type: str
    :param to_addrs: 收件人  type: list
    :param from_addr: 寄件人地址
    :param password: 寄件人登录密码
    :return: None
    '''

    if not isinstance(to_addrs, list):
        to_addrs = [to_addrs]

    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))
    if from_addr is None:
        from_addr = 'aiyingfeng110@qq.com'

    if password is None:
        password = 'cccc'

    if to_addrs is None:
        to_addrs = ['aiyingfeng110@qq.com']

    smtp_server = 'smtp.qq.com'
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = _format_addr('发件人 <%s>' % from_addr)
    to_addrs_msg = [_format_addr('收件人 <%s>' % s) for s in to_addrs]
    msg['To'] = ','.join(to_addrs_msg)
    msg['Subject'] = Header(title, 'utf-8').encode()
    server = smtplib.SMTP_SSL(smtp_server, timeout=10)
    server.set_debuglevel(0)
    server.login('aiyingfeng110@qq.com', password)
    server.sendmail(from_addr, to_addrs, msg.as_string())
    server.quit()


if __name__ == '__main__':
    send_mail('', '')
