# -*- coding:utf-8 -*-
import requests
import json

class RunMethod(object):
    def post_main(self, url, data, cookies=None):
        res = None
        if cookies != None:
            res = requests.post(url=url, data=data, cookies=cookies)
        else:
            res = requests.post(url=url, data=data)
        print res.status_code
        return res.json()

    def get_main(self, url, data=None, cookies=None):
        res = None
        if cookies != None:
            res = requests.get(url=url, data=data, cookies=cookies, verify=False)
        else:
            res = requests.get(url=url, data=data, verify=False)
        print res.status_code
        return res.json()

    def run_main(self, method, url, data=None, cookies=None):
        res = None
        if method == 'post':
            res = self.post_main(url, data, cookies)
        else:
            res = self.get_main(url, data, cookies)
        return json.dumps(res, ensure_ascii=False)
    # return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)
