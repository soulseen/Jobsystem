#_*_coding:utf-8_*_

class CommonFun(object):
    '''封装了一些公共函数'''

    @staticmethod
    def clear(data):
        return data.strip().replace('\n','').replace('\t','').replace('\r','')