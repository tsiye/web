#coding:utf-8
import gevent.monkey
gevent.monkey.patch_all()

import gevent

import crawler

import time

from config import start_url,page_number

import requests

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '86',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': '__utma=142000562.1663982550.1549613237.1549613237.1549613237.1; __utmc=142000562; __utmz=142000562.1549613237.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; 4Oaf_61d6_pc_size_c=0; 4Oaf_61d6_saltkey=AIhELox1; 4Oaf_61d6_lastvisit=1549609805; 4Oaf_61d6_atarget=1; 4Oaf_61d6_forum_lastvisit=D_82_1549613405; 4Oaf_61d6_visitedfid=82; 4Oaf_61d6_lastact=1549613406%09home.php%09misc; 4Oaf_61d6_sendmail=1; __utmb=142000562.16.10.1549613237',
    'Host': 'www.1point3acres.com',
    'Origin': 'https://www.1point3acres.com',
    'Referer': 'https://www.1point3acres.com/bbs/forum-82-1.html',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.98 Chrome/71.0.3578.98 Safari/537.36'}
url = 'https://www.1point3acres.com/bbs/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1'
data = {
    'username': 'tsiye',
    'password': 'fc1601e49487d414c0369fd14e1539da',
    'quickforward':'yes',
    'handlekey': 'ls'}
new_headers = {
    'Host': 'www.1point3acres.com',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.98 Chrome/71.0.3578.98 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'https://www.1point3acres.com/bbs/thread-479854-1-1.html',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cookie':'__utmz=142000562.1539341799.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmc=142000562; _dx_uzZo5y=ead330946b831c182a00e9848a9394283c5cb4766653b40e48e51f848019604a4877421e; _dx_app_captchadiscuzpluginbydingxiang2017=5c5cde35Dy9u5kMSdYZjU0KFHyAZs86hzxQ2U361; _dx_captcha_vid=1CE26433CB2596CB51099006F1F1B1F161D13C5B6634C1A6E191D6C59445FADDC1AEE92877FC61833BE9D9E57CA807633E286283876B862DFDC2612EF648B74AFCE3773D5017914CFDF6C627AFD53FD3; _ga=GA1.2.1838347636.1539341799; PHPSESSID=rossrf0j3ulv5jrh6lnhbobuu2; __utma=142000562.1838347636.1539341799.1549717897.1549761167.8; __utmt=1; 4Oaf_61d6_pc_size_c=0; 4Oaf_61d6_saltkey=h8LyN2iG; 4Oaf_61d6_lastvisit=1549757675; 4Oaf_61d6_hanchuan_tourist=1; 4Oaf_61d6_visitedfid=82; 4Oaf_61d6_viewid=tid_479854; __utmb=142000562.7.10.1549761167; 4Oaf_61d6_lastact=1549761657%09member.php%09logging; 4Oaf_61d6_ulastactivity=1549761657%7C0; 4Oaf_61d6_auth=a69eOTyhGAO8dQ9Mq2Hv8iScrrj9TQi26X14AXQImKG8JqexolQbbA6OqKVzYuSZz9Pc1QJaWeJpNnn7ntqccXRzMUs; 4Oaf_61d6_lastcheckfeed=466369%7C1549761657; 4Oaf_61d6_checkfollow=1; 4Oaf_61d6_lip=39.182.147.195%2C1549761657'}
mysession = requests.session()
response = mysession.post(url, headers = headers, data = data)
#print(response.text)
text = mysession.get('https://www.1point3acres.com/bbs/thread-479854-1-1.html', headers = new_headers).text
#print(text)

def asyn_fetch(url_list, mysession):
    greenlets = []
    for url in url_list:
        greenlets.append(gevent.spawn(crawler.get_data_from_bbs,url, mysession))
    gevent.joinall(greenlets) 

if __name__ == "__main__":
    start_time = time.time()
    
    for number in page_number:
        print (number)
        the_url = start_url + str(number) + ".html"
        print(the_url)
        url_list = crawler.get_link(the_url, mysession)
        print(url_list)
        asyn_fetch(url_list, mysession)

    end_time=time.time()
    
    print ("it cost:",end_time-start_time)
