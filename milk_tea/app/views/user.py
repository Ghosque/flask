# -*- coding:utf-8 -*-
from flask import Blueprint

user_blueprint = Blueprint('user_blueprint', __name__, url_prefix='/user')


@user_blueprint.route('/register')
def register():
    return "register"


@user_blueprint.route('/login')
def login():
    return "login"
