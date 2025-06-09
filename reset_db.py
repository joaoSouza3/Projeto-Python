# reset_db.py
from main import app, db

with app.app_context():
    db.drop_all()
    db.create_all()
    print("Banco de dados resetado com sucesso!")
