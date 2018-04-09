#-*- coding: utf-8 -*-

from flask_script import Manager, Server
from flask_app import create_app
import os
import sys
from scrapy.cmdline import execute

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
#execute(['scrapy', 'crawl', 'zhilian_python','-o','./export/items.json'])
execute(['scrapy', 'crawl', 'zhilian_python'])


# app = create_app(os.getenv('FLASK_CONFIG') or 'default')
# manager = Manager(app)
#
#
# @app.route('/')
# def hello():
#     return 'hello'
#
#
# if __name__ == '__main__':
#     manager.add_command("runserver",
#                         Server(host="0.0.0.0", port=10011, threaded=True))
#     manager.run()

