# -*- coding:utf-8 -*-

import json

class CommonUtil(object):
    '''
    判断一个字符串是否在另一个字符串中
    str_one:查找的字符串
    str_two:被查找的字符串
    '''
    def is_content(self,str_one,str_two):
        flag=None
        if isinstance(str_one,unicode):
            str_one=str_one.encode('unicode-escape').decode('string_escape')
        if str_one in str_two:
            flag=True
        else:
            flag=False
        return flag
    def is_equal_dict(self,dict_one,dict_two):
        if isinstance(dict_one,str):
            #json.load()将字符串转换为字典
            dict_one=json.loads(dict_one)
        if isinstance(dict_two,str):
            dict_two=json.loads(dict_two)
        return cmp(dict_one,dict_two)














