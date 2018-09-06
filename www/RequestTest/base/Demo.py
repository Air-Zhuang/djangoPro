# -*- coding:utf-8 -*-
import requests
import json

class RunMain(object):
    # def __init__(self,url,method,data=None):
    #     self.res=self.run_main(url,method,data)
    def send_post(self,url,data):
        res=requests.post(url,data).json()
        return json.dumps(res,indent=2,sort_keys=True)
    def send_get(self,url,data):
        res=requests.get(url,data).json()
        return json.dumps(res,indent=2,sort_keys=True)
    def run_main(self,url,method,data=None):
        res=None
        if method=='GET':
            res=self.send_get(url, data)
        else:
            res=self.send_post(url,data)
        return res
if __name__=='__main__':
    post_Data = {
        'username': 'air',
        'password': '123456'
    }
    post_Url = 'http://127.0.0.1:8000/login/'
    get_Data = {
        'username': 'clannad',
        'mobile': '321',
        'data': '英文'
    }
    get_Url = 'http://127.0.0.1:8000/login2?username=air&mobile=123&data=中文'
    get_Url2 = 'http://127.0.0.1:8000/login2'
    run=RunMain().run_main(get_Url2,'GET',get_Data)
    print run
    # run1= RunMain(post_Url,'POST',post_Data)
    # print run1
    # run11=RunMain
    # print run1.res
    # run2 = RunMain(get_Url,'GET')
    # print run2.res
    # run3 = RunMain(get_Url2,'GET',get_Data)
    # print run3.res
