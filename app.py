# Flask などの必要なライブラリをインポートする
from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import os
import glob
#from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import secure_filename

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    title = "ようこそ"
    message = "welcome"
    return render_template('index.html',
                           message=message, title=title)

@app.route('/post', methods=['GET', 'POST'])
def post():
    title = "こんにちは"
    if request.method == 'POST':
        name = request.form['name']
        return render_template('index.html',
                               name=name, title=title)
    else:
        return redirect(url_for('index'))

@app.route('/image-upload', methods=['GET', 'POST'])
def image_post():
    if request.method == 'POST':
        f = request.files['file']
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            print(os.path.join(os.path.dirname(os.path.abspath(__file__)), "tmp", filename))
            f.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "tmp", filename))
            return filename
        return "file req error"
    return "post error"

@app.route('/fetch-image', methods=['GET', 'POST'])
def fetch_image():
    if request.method == 'GET':
        for fn in glob.glob(os.path.join(os.getcwd(),"tmp","*")):
            print(fn)
    return "fetch image"


if __name__ == '__main__':
    #app.debug = True # デバッグモード有効化
    #port = int(os.environ.get('PORT', 5000))
    #app.run(port=port)
    app.run()
