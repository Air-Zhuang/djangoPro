# -*- coding:utf-8 -*-
import MySQLdb.cursors
import json

class OperationMysql(object):
    def __init__(self):
        self.conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='test',
            charset='utf8',
            #将结果返回成字典格式
            cursorclass=MySQLdb.cursors.DictCursor
        )
        self.cur = self.conn.cursor()
    def search_one(self,sql):
        self.cur.execute(sql)
        result=self.cur.fetchone()
        result=json.dumps(result)
        return result

if __name__ == '__main__':
    op_mysql=OperationMysql()
    res=op_mysql.search_one("select * from table1 where name='first'")
    print res










