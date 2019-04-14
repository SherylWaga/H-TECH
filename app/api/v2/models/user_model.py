from flask import Flask, request
from flask_jwt_extended import JWTManager
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token,get_jwt_identity)

# local imports

from ....database import init_db
app = Flask(__name__)


class Users():
    def __init__(self):
        self.db = init_db()
 
    def save_user(self, first_name, last_name, username,phone, email, password):

        users = {
            'first_name': first_name,
            'last_name': last_name,
            'username': username,
            'phone': phone,
            'email': email,
            'password':password

        }
        query = """INSERT INTO users(first_name,last_name,username,phone,email,password)
          VALUES(%(first_name)s, %(last_name)s,%(username)s, %(phone)s ,%(email)s ,%(password)s)"""
        cur = self.db.cursor()
        cur.execute(query, users)
        self.db.commit()
        return users

    def fetch_user(self):
        dbconn = self.db
        curr = dbconn.cursor()
        curr.execute("""SELECT username FROM users""")
        data = curr.fetchall()
        resp = []

        """Iterate over the index and values of items in 'data'"""
        for i, items in enumerate(data):
            username = items
            datah = dict(
                username=username
            )
            resp.append(datah)
        username = request.json.get('username')
        sname = str(resp)
        if str(username) in sname:
            return True

        
    
    
    

    
