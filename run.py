# -*- coding: utf-8 -*-

from flask_script import Manager, Server
from flask_app import create_app
import os

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


@app.route('/')
def hello():
    return 'hello'


if __name__ == '__main__':
    manager.add_command("runserver",
                        Server(host="127.0.0.1", port=10011, threaded=True))
    manager.run()
