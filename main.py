#coding=utf-8  
__author__ = 'cloudtogo'

from flask import Flask
import sys


app = Flask(__name__)


reload(sys)
sys.setdefaultencoding('utf8')



@app.route('/')
def hello():
    return '恭喜您成功地发布了一个运行在云端的python程序恭喜您成功地发布了一个运行在云端的python程序'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
