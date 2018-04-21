# __coding:utf-8__
'''
@Author  : Sun
@Time    :  下午8:52
@Software: PyCharm
@File    : job_run.py
'''

import os
import sys
from scrapy.cmdline import execute

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute(['scrapy', 'crawl', 'zhilian_python', '-o', './export/items.json'])
# execute(['scrapy', 'crawl', 'zhilian_python_beijing'])
# execute(['scrapy', 'crawl', 'zhilian_python_shanghai'])
# execute(['scrapy', 'crawl', 'zhilian_python_shenzhen'])
# execute(['scrapy', 'crawl', 'zhilian_python_hangzhou'])
# execute(['scrapy', 'crawl', 'zhilian_python_guangzhou'])
# execute(['scrapy', 'crawl', 'zhilian_python_chengdu'])

# execute(['scrapy', 'crawl', 'zhilian_tongxin_beijing'])
# execute(['scrapy', 'crawl', 'zhilian_tongxin_guangzhou'])
execute(['scrapy', 'crawl', 'zhilian_tongxin_chengdu'])
# execute(['scrapy', 'crawl', 'zhilian_tongxin_hangzhou'])
# execute(['scrapy', 'crawl', 'zhilian_tongxin_shanghai'])
# execute(['scrapy', 'crawl', 'zhilian_tongxin_shenzhen'])

