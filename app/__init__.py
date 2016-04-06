#!/usr/bin/python
"""
ilmnuri audio website
"""
from flask import Flask, render_template
import logging
from glob import glob
import os

app = Flask(__name__)

logging.basicConfig(filename='/var/log/nginx/ilmnuri.log',
                    format='%(asctime)s  %(funcName)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

log = logging.getLogger(__name__)


@app.route('/')
def index():
    log.info('index page rendered.')
    return render_template("index.html")


@app.route('/dars/<teacher>/')
def first(teacher):

    list_items = glob('{0}/*'.format(teacher))
    new_list = []
    for item in list_items:
        s = item.split('/')
        new_list.append(s[1])

    return render_template('dars.html', new_list=new_list, teacher=teacher)     


@app.route('/dars/<teacher>/<album>/')
def albums(teacher, album):

    list_items = glob('{0}/{1}/*'.format(teacher, album))
    new_list = []
    for item in list_items:
        s = item.split('/')
        new_list.append(s[2])

    return render_template('track.html',
                           new_list=new_list,
                           teacher=teacher,
                           album=album)


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0', debug=True)
