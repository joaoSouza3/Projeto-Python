from flask import Flask
from models import db
import secrets

import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url

# Configuration       
cloudinary.config( 
    cloud_name = "dledm0rr0", 
    api_key = "188691393191395", 
    api_secret = "ZbpQ2XzQz5hmd_Nvu6XguqUBJNQ", # Click 'View API Keys' above to copy your API secret
    secure=True
)


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = secrets.token_hex(16)

db.init_app(app)
with app.app_context():
    db.create_all()


from routes import *

if __name__ == "__main__":
    app.run(debug=True)

    