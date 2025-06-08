from flask import Flask
from models import db
import secrets

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

    