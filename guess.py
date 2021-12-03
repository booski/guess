#!/usr/bin/env python3
import os
import random
import uuid

from flask import Flask, Response, flash, redirect, request
from werkzeug.utils import secure_filename

PERMITTED = {'jpg', 'png', 'gif'}

def allowed_file(name):
    return '.' in name and name.rsplit('.', 1)[1].lower() in PERMITTED

def init():
    app = Flask(__name__)
    pictures = os.path.join(app.root_path, 'static/pictures')
    answers = os.path.join(app.root_path, 'answers')
    
    @app.route('/')
    def base():
        return Response(response='REST')

    @app.route('/random')
    def random_pic():
        return {'picture':
                os.path.join(random.choice(os.listdir(pictures)))}

    @app.route('/solution/<string:picture>')
    def solve(picture):
        with open(os.path.join(answers, picture), encoding='UTF-8') as f:
            return {'solution': f.read()}

    @app.route('/upload', methods=['POST'])
    def upload():
        if 'picture' not in request.files:
            return Response(response='No file')
        picture = request.files['picture']
        if picture.filename == '':
            return Response(response='No file provided')
        if not picture or not allowed_file(picture.filename):
            return Response(response='Invalid picture')
            
        if 'answer' not in request.form:
            return Response(response='Invalid form')
        answer = request.form['answer']
        if not answer:
            return Response(response='No answer provided')

        filename = str(uuid.uuid4())
        while filename in os.listdir(pictures):
            filename = str(uuid.uuid4())
        picture.save(os.path.join(pictures, filename))
        with open(os.path.join(answers, filename),
                  'w', encoding='UTF-8') as f:
            f.write(answer+"\n")
        return redirect(request.referrer)
        
    return app
