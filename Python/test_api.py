# coding:utf-8
import requests
bad_headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
           'Host': 'kindmark.com',
           'Upgrade-Insecure-Requests': 1,
           'Accept-Encoding': 'gzip, deflate, sdch',
           'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6'}
good_headers = {           
            'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.3.22 NetType/WIFI Language/en',
           'Host': 'kinmark.com',
           'Upgrade-Insecure-Requests': 1,
           'Accept-Encoding': 'gzip, deflate, sdch',
            'x-openid':'aaaa-aaa',
           'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6'}
test_url = "http://192.168.1.109:8001/api/products/trust/"
result_url = "http://192.168.1.109:8001/api/accounts/profile/"
test_fucker = requests.Session()
test_organism = test_fucker.get(test_url,headers=good_headers)
result = test_fucker.get(result_url,headers=good_headers)
#  test_organism2 = test_fucker.get(test_url,headers=bad_headers)
with open("result_url.html","wb") as f:
    f.write(result.content)
print test_organism.content
print result.content

