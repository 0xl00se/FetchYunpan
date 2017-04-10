#-*- coding: UTF-8 -*- 

'''
Created on 2017年4月10日

@author: 0xl00se
'''

import requests

headers = {
    'X-Requested-With' : 'XMLHttpRequest',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2'
    }

def fetch_pansou(query_key):
    
    url = 'http://api.pansou.com/search_new.php?q=%s' % query_key.decode('utf-8')
    j = requests.get(url, headers=headers).json()
    if j['listcount'] > 0:
        items = j['list']['data']
        if items:
            return [item['link'] for item in items if item['host'] == 'pan.baidu.com' or item['host'] == 'yun.baidu.com']
        else:
            return None
    else:
        return None
    
def search_movie(keyword):
    
    query_key = keyword
    result_list = []
    try:
        result_pansou = fetch_pansou(query_key)
        if result_pansou:
            print u"你所搜索的%s的结果如下：" % keyword
            for list in range(len(result_pansou)):
                print u"#%s   url:%s" % (list, result_pansou[list])
        else:
            print u"请输入正确的关键词！"
    except:
        pass
if __name__ == "__main__":
    keyword = raw_input(u"请输入您要查询资源的关键词：").encode('utf-8')
    search_movie(keyword);