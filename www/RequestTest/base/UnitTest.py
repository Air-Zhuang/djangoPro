# -*- coding:utf-8 -*-
import unittest

from Demo import RunMain
import HTMLTestRunner
import time
from mock_demo import mock_test
from mock import mock

class TestMethod(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     print '类执行之前的方法'
    # @classmethod
    # def tearDownClass(cls):
    #     print '类执行之后的方法'
    def setUp(self):
        self.run = RunMain();
        print '-------------Before----------'

    # def tearDown(self):
    #     print 'After'
    def test_01(self):
        post_Data = {
            'username': 'air',
            'password': '123456'
        }
        post_Url = 'http://127.0.0.1:8000/login/'
        #mock使用方法
        # mock_method=mock.Mock(return_value=post_Data)
        # self.run.run_main=mock_method
        #使用自己的封装mock方法
        # res=mock_test(self.run.run_main,post_Data,post_Url,'POST',post_Data)
        res = self.run.run_main(post_Url, 'POST', post_Data)
        print res
        time.sleep(0.5)

    def test_02(self):
        get_Data = {
            'username': 'clannad',
            'mobile': '321',
            'data': '英文'
        }
        get_Url2 = 'http://127.0.0.1:8000/login2'
        res = self.run.run_main(get_Url2, 'GET', get_Data)
        print res
        time.sleep(0.5)


if __name__ == '__main__':
    filePath = '../report/htmlreport.html'
    fp = file(filePath, 'w')
    suite = unittest.TestSuite()
    suite.addTest(TestMethod('test_01'))
    # suite.addTest(TestMethod('test_02'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp)
    runner.run(suite)
    # unittest.TextTestRunner().run(suite)
