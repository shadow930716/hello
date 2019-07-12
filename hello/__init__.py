from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import  Moment
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension

app=Flask('hello')
bootstrap=Bootstrap(app)
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db=SQLAlchemy(app)
toolbar=DebugToolbarExtension(app)
moment=Moment(app)


from hello import views,commands