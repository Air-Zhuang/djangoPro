# -*- coding:utf-8 -*-

import sys
sys.path.append("D:\PyCharm\workspace\www\RequestTest")
from base.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from data.dependent_data import DependdentData
from util.send_email import SendEmail
from util.operation_header import OperationHeader
from util.operation_json import OperationJson
class RunTest(object):
    def __init__(self):
        self.run_method=RunMethod()
        self.data=GetData()
        self.com_util=CommonUtil()
        self.send_mai=SendEmail()
    #程序执行的主入口
    def go_on_run(self):
        res=None
        pass_count=[]
        fail_count=[]
        rows_count=self.data.get_case_lines()
        for i in range(1,rows_count):
            is_run = self.data.get_is_run(i)
            if is_run:
                url=self.data.get_url(i)
                method=self.data.get_request_method(i)
                request_data=self.data.get_data_for_json(i)
                expect=self.data.get_expect_data(i)
                header=self.data.is_header(i)
                depend_case=self.data.is_depend(i)
                res = self.run_method.run_main(method, url, request_data, header)
                print res
                if depend_case !=None:
                    self.depend_data=DependdentData()
                    #获取的依赖相应数据
                    depend_response_data=self.depend_data.get_data_for_key(i)
                    #获取以来的key
                    depend_key=self.data.get_depend_field(i)
                    request_data[depend_key]=depend_response_data
                if header=='write':
                    res=self.run_method.run_main(method,url,request_data)
                    op_header=OperationHeader(res)
                    op_header.write_cookie()
                elif header=='yes':
                    op_json=OperationJson('../dataconfig/cookie.json')
                    cookie=op_json.get_data('apsid')
                    cookies={
                        'apsid':cookie
                    }
                    res=self.run_method.run_main(method,url,request_data,cookies)
                else:
                    res = self.run_method.run_main(method, url, request_data)
                if self.com_util.is_content(expect,res):
                    self.data.write_result(i,'pass')
                    pass_count.append(i)
                    print '测试通过'
                else:
                    self.data.write_result(i,res)
                    fail_count.append(i)
                    print '测试失败'
                # print res
                # if self.com_util.is_equal_dict(expect,res)!=0:
                #     self.data.write_result(i,'pass')
                #     pass_count.append(i)
                #     print '测试通过'
                # else:
                #     self.data.write_result(i,res)
                #     fail_count.append(i)
                #     print '测试失败'
        # self.send_mai.send_main(pass_count,fail_count)
if __name__=='__main__':
    run=RunTest()
    run.go_on_run()




