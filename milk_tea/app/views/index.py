# -*- coding:utf-8 -*-
from flask import Blueprint

index_blueprint = Blueprint('index_blueprint', __name__)


@index_blueprint.route('/')
def index():
    return "index"
