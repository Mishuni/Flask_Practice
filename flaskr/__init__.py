import os
from flask import Flask

''' 
Application factory
Any configuration, registration, a
nd other setup the application needs 
will happen inside the function, 
then the application will be returned.
'''

def create_app(test_config=None):
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )

    if test_config is None:
        app.config.from_pyfile('config.py',silent=True)
    else:
        app.config.from_mapping(test_config)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return "Hello, World"
    
    from . import db
    db.init_app(app)

    '''
    Now that init-db has been registered with the app, 
    it can be called using the flask command, 
    similar to the run command 
    $ flask init-db
    '''

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/',endpoint='index')

    return app

    