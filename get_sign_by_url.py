#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import urlparse as parse
except ImportError:
    from urllib import parse
import hashlib
import base64


def generate_sign(url, name):
    """Generate item sign form url by md5"""
    try:
        sign = base64.urlsafe_b64encode(
            hashlib.md5(check_domain_area(url).encode('utf-8')).digest()).decode('utf-8').replace('==', '')
    except TypeError:
        sign = base64.urlsafe_b64encode(
            hashlib.md5(check_domain_area(url)).digest()).replace('==', '')
    return get_language_type(name) + '_' + sign


def check_domain_area(url):
    """确认域名区域.不对域名区域,协议类型,做ｍｄ５加密"""
    try:
        parsed_uri = parse.urlparse(url)
        uri_netloc = parsed_uri.netloc
        uri_netloc_new = '.'.join(parsed_uri.netloc.split('.')[:-1])
        url = url.replace(uri_netloc, uri_netloc_new).replace('https', '').replace('http', '')
    finally:
        return url


def get_language_type(name):
    """根据爬虫名判断语言类型"""
    language = dict()
    language['Tradchn'] = ['bbc_chinese', 'chinatimes', 'ftchinese', 'hinet', 'hkcna', 'ltn_playing',
                           'ltn', 'master_insight', 'metrodaily', 'nyam', 'takungpao', 'techbang',
                           'teepr', 'tvb', 'wenweipo', 'wsj', 'youtube_hk']
    language['vietnam_'] = ['']

    for language, spider_list in language.items():
        if name in spider_list:
            return 'Tradchn'

    return 'English'


url = 'https://news.abs-cbn.com/business/11/20/18/why-ikea-chose-ph-for-worlds-biggest-store'
name = 'abs_cbn'
a = generate_sign(url, name)
print(a)
