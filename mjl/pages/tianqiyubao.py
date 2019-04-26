from lxml import etree
import requests
import time
import pymysql
from random import random
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import urllib.request

conn = pymysql.connect(host='localhost',user='root',password='123456',db='mjl',port=3306,charset='utf8')
cursor=conn.cursor()    
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5478.400 QQBrowser/10.1.1550.400'}

def get_weather(url):
    proxies={"http": "http://119.102.129.114:9999",
             "https": "http://119.102.129.114:9999"}
    if url=="http://www.weather.com.cn/weather/101010100.shtml":
        city="北京"
    elif url=="http://www.weather.com.cn/weather/101020100.shtml":
        city="上海"
    elif url=="http://www.weather.com.cn/weather/101280601.shtml":
        city="广州"
    elif url=="http://www.weather.com.cn/weather/101280601.shtml":
        city="温州"
    req=urllib.request.Request(url,headers=headers)
    data=urllib.request.urlopen(req)
    data=data.read()
    dammit=UnicodeDammit(data,["utf-8","gbk"])
    data=dammit.unicode_markup
    soup=BeautifulSoup(data,"lxml")
    lis=soup.select("ul[class='t clearfix'] li")
    for li in lis:
        date=li.select('h1')[0].text
        weather=li.select('p[class="wea"]')
        temp=li.select('p[class="tem"] span')[0].text+"/"+li.select('p[class="tem"] i')[0].text
    cursor.execute("insert into page_tianqiyubao (city,date,weather,temp)values(%s,%s,%s,%s)",
                  (str(city),str(date),str(weather),str(temp)))
    
if __name__=='__main__':     
    urls=["http://www.weather.com.cn/weather/101010100.shtml",
          "http://www.weather.com.cn/weather/101020100.shtml",
          "http://www.weather.com.cn/weather/101280601.shtml",
          "http://www.weather.com.cn/weather/101280101.shtml"]     
    for url in urls:
        get_weather(url)  
        time.sleep(random()*2)
    conn.commit()
