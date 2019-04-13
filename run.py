import os
from app.database import create_table

from app import create_app

app = create_app()

if __name__ == '__main__':
    create_table
    app.run()

# import os

# from app import create_app
# from flask_jwt_extended import JWTManager


# config_name = os.getenv('FLASK_CONFIG')
# app = create_app(config_name)
# jwt = JWTManager(app)


# if __name__ == '__main__':
# 	app.run()