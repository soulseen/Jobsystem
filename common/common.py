# _*_coding:utf-8_*_

MYSQL_HOST = '127.0.0.1'
MYSQL_DBNAME = 'db'
MYSQL_USER = 'root'
MYSQL_PASSWD = '123456'
MYSQL_PORT = 3306

class CommonFun(object):
    '''封装了一些公共函数'''

    @staticmethod
    def clear(data):
        return data.strip().replace('\n', '').replace('\t', '').replace('\r', '').replace(',', '').replace('.',
                                                                                                           '').replace(
            '!', '').replace('，', '').replace('。', '').replace('！', '').replace('、', '').replace(':', '').replace('：',
                                                                                                                  '').replace(
            ' ', '').replace('"', '').replace('\'', '').replace('“', '').replace('”', '').replace('；', '').replace('(',
                                                                                                                   '').replace(
            ')', '')
