from flask_restful import Resource

import psycopg2
from flask_jwt_extended import (create_access_token, jwt_required, 
                                get_jwt_identity, get_current_user, get_raw_jwt, JWTManager)

connection = psycopg2.connect(dbname='htech', user='postgres', password='refuge', host='localhost')
curr = connection.cursor()