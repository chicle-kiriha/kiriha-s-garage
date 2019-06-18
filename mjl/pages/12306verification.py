import re
import requests
import base64
import time
import os
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


class Verificationlogin():

    def getImg(self):
        #构造请求头
        headers = {'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
        }

        road_url = 'https://kyfw.12306.cn/passport/captcha/captcha-image64'    #生成验证码的url
    
        #构造请求表单
        road_parmas = {
            "login_site": "E",
            "module": "login",
            "rand": "sjrand",
            "1560865885873":"",
            "callback": "jQuery19105444643302976442_1560865808951",
            "_": "1560865808960",
        }

        #创建sess对象 保持会话一至
        sess=requests.session()

        #对图片页发送请求
        response=sess.get(url=road_url,params=road_parmas,headers=headers).text
        #获取图片数据
        image_bs64=re.findall('"image":"(.*?)",',response)[0]
        #解码数据
        image=base64.b64decode(image_bs64)
        #保存图片
        with open('Vericode_img.jpg','wb') as f:
            f.write(image)

        self.sess=sess

    def Verification_result(self):
        #验证部分交给了http://littlebigluo.qicp.net:47720/
        road_url_x='http://littlebigluo.qicp.net:47720/'
        sess=requests.session()
        response_x=sess.post(url=road_url_x,data={"type":"1"},files={'pic_xxfile':open('Vericode_img.jpg','rb')})
        result=[]
        #print(response.text)
        try:
            for i in re.findall("<B>(.*)</B>",response_x.text)[0].split(" "):
	            result.append(int(i))
        except:
            print("网站忙")

        #构建像素表单
        coord_data ={
            "1":"40,40",
            "2":"120,40",
            "3":"180,40",
            "4":"250,40",
            "5":"40,100",
            "6":"120,100",
            "7":"180,100",
            "8":"250,100",
        }
        answerlist = []
        print('选中图片为:',result)
        #循环输入的值取出字典相应的坐标
        for i in result:
            answerlist.append(coord_data[str(i)])
        print('坐标为：' + ';'.join(answerlist))
        answer = ','.join(answerlist)
        self.answer=answer
    

    def login(self):
        Vericode_url="https://kyfw.12306.cn/passport/captcha/captcha-check"    #验证验证码的url
        log_url="https://kyfw.12306.cn/passport/web/login"    #登录的url

        Vericode_headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        }
        log_headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin':'https://kyfw.12306.cn',
            'Referer':'https://kyfw.12306.cn/otn/resources/login.html',
            'Accept':'application/json, text/javascript, */*; q=0.01',
        }
        
        username = input('请输入用户名：')
        password = input('请输入密码：')

        #构造data表单
        log_data = {
            "username": username,
            "password": password,
            "appid": "otn",
            #"answer": self.answer,
        }
        #Vericode_url
        log_parmas = {
            "callback": "jQuery19105444643302976442_1560865808951",
            "answer":self.answer, 
            "rand": "sjrand",
            "login_site": "E",
            "_": "1560865808960",          
        }
        #发送图片验证请求
        response_xx=self.sess.get(url=Vericode_url,params=log_parmas,headers=Vericode_headers).text
        #获得图片验证信息
        print(re.findall('"result_message":"(.*?)"',response_xx))

        #增加cookies
        #注意此处的信息一定要及时更变，这关系到登录的成功与否
        self.sess.cookies.update({
            'RAIL_EXPIRATION':'1561202273991',
            'RAIL_DEVICEID':'ab6-pYW9fzg-JDxLuUVxAV4jVsEA1P1Jrk3t_mnz8wqc92wo3iXfhUYw_rh6Us0FZqwnmUT_9mHq426vI9m-yf9i4TKVHAE2Ou2-438l5N-voS1eoYVc-sZ7uqpuKo0aNub9qXjpsC6Sbb3Gq4UWYIBaVEQkOh_3',
        })

        response_xxx=self.sess.post(url=log_url,data=log_data,headers=log_headers)
        #返回编码后的数据
        response_xxx.encoding='utf-8'
        print(re.findall('"result_message":"(.*?)"',response_xxx.text))


    def load(self):
        self.getImg()
        time.sleep(3)
        self.Verification_result()
        time.sleep(10)
        self.login()
        time.sleep(10)

if __name__=="__main__":
    test=Verificationlogin()
    test.load()