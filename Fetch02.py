#-*- coding: UTF-8 -*- 

'''
Created on 2017年4月10日

@author: 0xl00se
'''

import requests
from bs4 import BeautifulSoup
import re

headers = {
    'X-Requested-With' : 'XMLHttpRequest',
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
        rsearch = BeautifulSoup(requests.post(url=search_url, headers=headers, data=data).content, 'lxml')
        items_search = rsearch.find_all('a', target='_blank', href=re.compile("file"))
        href_list1 = []
        if items_search:
            for item in set(items_search):
                href_list1.append(base_url + item['href'])
            result = []
            for iurl in href_list1:
                result.append(url_sobaidupan(iurl))
        else:
            pass
    
def url_sobaidupan(url):
    
    rurl = BeautifulSoup(requests.get(url=url, headers=headers).content, 'lxml')
    items_url = rurl.find_all('a', target='_blank', href=re.compile("down.asp"))
    if items_url:
        for item in set(items_url):
            href_list2 = item['href']
        return parse_sobaidupan(href_list2)
    else:
        return None

def parse_sobaidupan(url):
    
    purl = BeautifulSoup(requests.get(url=url, headers=headers).content, 'lxml')
    item_parse = purl.find_all('meta', content=re.compile("pan.baidu.com"))
    if item_parse:
        for item in set(item_parse):
            href_list3 = item['content']
        print "#url:%s" % href_list3[6:]
    else:
        return None
    

if __name__ == "__main__":
    keyword = raw_input("请输入您要查询资源的关键词：").decode('utf-8').encode('utf-8')
    print "你所搜索的%s的结果如下：" % keyword
    search_sobaidupan("keyword")
