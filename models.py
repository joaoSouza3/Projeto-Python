from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    idUsuario = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(10), nullable=False)



class Resenha(db.Model):
    idResenha = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    nomeLivro = db.Column(db.String(30), nullable=False)
    genero = db.Column(db.String(30), nullable=False)
    desc = db.Column(db.String(400), nullable=False)
    nota = db.Column(db.Float, nullable=False)
    idUsuario = db.Column(db.Integer, db.ForeignKey("usuario.idUsuario"), nullable=False)

    user_rel = db.relationship("Usuario", backref="resenha")

