from flask import Flask

from .index import index_blueprint
from .user import user_blueprint


app = Flask(__name__)

app.register_blueprint(index_blueprint)
app.register_blueprint(user_blueprint)
