# -*- coding: utf-8 -*-

from flask import Blueprint
from .exertion.views import register


bp = Blueprint('api', __name__)

register(bp)
