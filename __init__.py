#This file serves double duty.
#1. It will contain the application factory.
#2. It will tells Python that the flasker directory should be treated as a package.

import os 
from flask import Flask

def create_app(test_config=None):
    #create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    #__name__ : Python moduleの名前で、ディレクトリ内のどこに置かれているか明記する必要がある
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    #This part shows the configuration file is related to the instance file.
    
    #os.path.join → One of the function of os library.パス同士をくっつける ※パス = ファイルがある場所までの道筋の事

    if test_config is None:
    # load the instance config, if it exits, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
    #Load the test cinfig if passed in
        app.config.from_mapping(test_config)
    
    #ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

# a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, world!'
    
    return app