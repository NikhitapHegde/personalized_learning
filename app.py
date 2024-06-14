# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 23:37:56 2023

@author: poorn
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
