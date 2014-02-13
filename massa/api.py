# -*- coding: utf-8 -*-

from flask import Blueprint
from .views import entity_not_found_handler, invalid_input_handler
from .errors import EntityNotFoundError, InvalidInputError
from .exertion.views import register


bp = Blueprint('api', __name__)
bp.app_errorhandler(EntityNotFoundError)(entity_not_found_handler)
bp.app_errorhandler(InvalidInputError)(invalid_input_handler)

register(bp)
