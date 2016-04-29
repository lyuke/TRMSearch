# -*- coding: utf-8 -*-
from flask import Flask,render_template
from recommend.model import recommend,Literature
from recommend.run import run
import  json
app = Flask(__name__)


@app.route('/')
def index():
    result=run.get_recommend("The Use and Utility of High-Level Semantic Features in Video Retrieval")
    print result
    return render_template('index.html')

@app.route('/recommend')
def recommend():
    pass


if __name__ == '__main__':
    app.run(debug=True)
