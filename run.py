import os
# from app.db_config import create_tables

from app import create_app

app = create_app()

if __name__ == '__main__':
    # create_tables
    app.run()

# import os

# from app import create_app
# from flask_jwt_extended import JWTManager


# config_name = os.getenv('FLASK_CONFIG')
# app = create_app(config_name)
# jwt = JWTManager(app)


# if __name__ == '__main__':
# 	app.run()