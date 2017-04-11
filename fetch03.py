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

def search_huhupan(query_key):
    
    search_url = 'http://huhupan.com/e/search/index.php'
    data = {
        'keyboard': query_key.decode('utf-8'),
        'show': 'title',
        'tempid': 1,
        'tbname': 'news',
        'mid': 1,
        'dopost': 'search',
        }
    try:
        rsearch = BeautifulSoup(requests.post(url=search_url, headers=headers, data=data).content, 'lxml')
        search_items = rsearch.find_all('a', target='_ablank', href=re.compile('huhupan.com'))
        if rsearch and search_items:
            for item in set(search_items):
                url_huhupan(item['href'])
        else:
            return None
    except:
        pass
        
def url_huhupan(url):
    
    base_url = 'http://huhupan.com'
    try:
        rurl = BeautifulSoup(requests.get(url=url, headers=headers).content, 'lxml')
        url_items = rurl.find_all('a', {'class': 'meihua_btn'})
        if rurl and url_items:
            for item in set(url_items):
                return parse_huhupan(base_url + item['href'])
        else:
            return None
    except:
        pass
    
def parse_huhupan(url):
    
    try:
        purl = BeautifulSoup(requests.get(url=url, headers=headers).content, 'lxml')
        parse_items1 = purl.find_all('a', {'class': 'meihua_btn'}, href=re.compile('pan.baidu.com'))
        parse_items2 = purl.find_all('input', id=re.compile(r'foo[0-9]'))
        if purl and parse_items1:
            print '#url:%s, #pwd: %s' % (parse_items1[0]['href'], parse_items2[0]['value'])
        else:
            return None
    except:
        pass
    
if __name__ == "__main__":
    keyword = raw_input("请输入您要查询资源的关键词：").decode('utf-8').encode('utf-8')
    print "你所搜索的{%s}的结果如下：" % keyword
    search_huhupan(keyword)