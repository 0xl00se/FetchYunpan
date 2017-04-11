#-*- coding: UTF-8 -*- 

'''
Created on 2017年4月10日

@author: 0xl00se
'''

import requests
from bs4 import BeautifulSoup
import re

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2'
    }

def search_sobaidupan(query_key):
    
    search_url = 'http://www.sobaidupan.com/search.asp'
    base_url = 'http://www.sobaidupan.com/'
    data = {
        'r': 0,
        'wd': query_key.decode('utf-8'),
        'p': 0,
        'page': 0,
        }
    for i in range(10)： #页面的数目，1-100
        data['page'] = i
        try:
            rsearch = BeautifulSoup(requests.post(url=search_url, headers=headers, data=data).content, 'lxml')
            items_search = rsearch.find_all('a', target='_blank', href=re.compile("file"))
            if rsearch and items_search:
                for item in set(items_search):
                    url_sobaidupan(base_url + item['href'])
            else:
                pass
        except:
            pass
    
def url_sobaidupan(url):
    
    try:
        rurl = BeautifulSoup(requests.get(url=url, headers=headers).content, 'lxml')
        items_url = rurl.find_all('a', target='_blank', href=re.compile("down.asp"))
        if rurl and items_url:
            for item in set(items_url):
                return parse_sobaidupan(item['href'])
        else:
            return None
    except:
        pass

def parse_sobaidupan(url):
    
    try:
        purl = BeautifulSoup(requests.get(url=url, headers=headers).content, 'lxml')
        item_parse = purl.find_all('meta', content=re.compile("pan.baidu.com"))
        if purl and item_parse:
            for item in set(item_parse):
                print "#url:%s" % item['content'][6:]
        else:
            return None
    except:
        pass

if __name__ == "__main__":
    keyword = raw_input("请输入您要查询资源的关键词：").decode('utf-8').encode('utf-8')
    print "你所搜索的{%s}的结果如下：" % keyword
    search_sobaidupan(keyword)
