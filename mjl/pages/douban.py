from lxml import etree
from random import random
import requests
import time
import pymysql   
 
conn = pymysql.connect(host='localhost',user='root',password='123456',db='mjl',port=3306,charset='utf8')
cursor=conn.cursor()    
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5478.400 QQBrowser/10.1.1550.400'}     
 
def get_movies(url):
    proxies = {
        "http": "http://119.102.129.114:9999",
        "https": "http://119.102.129.114:9999",
    }
    res=requests.get(url,headers=headers, proxies=proxies)
    if res.status_code==200:
        selector=etree.HTML(res.text)
        infos=selector.xpath('//tr[@class="item"]')
        for info in infos:
            name=info.xpath('td/div/a/@title')[0]
            url=info.xpath('td/div/a/@href')[0]
            book_infos=info.xpath('td/p/text()')[0]
            author=book_infos.split('/')[0]
            Press=book_infos.split('/')[-3]
            date=book_infos.split('/')[-2]
            price=book_infos.split('/')[-1]
            point=info.xpath('td/div[@class="star clearfix"]/span[2]/text()')[0]
            intro=info.xpath('td/p/span/text()')
            if len(intro)!=0:
                comment=intro[0]
            else:
                comment='空'        
            cursor.execute("insert into page_douban (name,author,Press,date,price,point,intro)values(%s,%s,%s,%s,%s,%s,%s)",
                           (str(name),str(author),str(Press),str(date),str(price),str(point),str(intro)))   
    else:
        print('failed')
 
if __name__=='__main__':     
    urls=['https://book.douban.com/top250?start={}'.format(i*25) for i in range(0,10)]     
    for url in urls:
        get_movies(url)  
        time.sleep(random()*2)
    conn.commit()
