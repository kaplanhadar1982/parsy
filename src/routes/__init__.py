from flask import Blueprint
routes = Blueprint('routes', __name__)

from .health_router import *
from .classes_router import *
from .index_router import *