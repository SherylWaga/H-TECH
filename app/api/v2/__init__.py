from flask import Blueprint
from flask_restful import Api


from .views.system import Home, Register,Tests

# from .views.instance_views import Create_incident, Specific, Admin
version_2 = Blueprint('api_v2', __name__, url_prefix='/api/v2')
api = Api(version_2)

api.add_resource(Home, '/')
api.add_resource(Register, '/create/patient')
api.add_resource(Tests, '/create/test')