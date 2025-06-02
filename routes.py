from main import app
from models import Usuario, db
from flask import render_template, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

#ROTAS
@app.route("/")    
def homepage():
    return render_template("index.html")


@app.route("/perfil")
def perfil():
    return render_template("perfil.html")

@app.route("/cadastro", methods=["POST"])
def cadastro():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    senha = data.get("senha")

    if Usuario.query.filter_by(email=email).first():
        return jsonify({"erro": "Email já cadastrado"}), 400

    senha_hash = generate_password_hash(senha)
    novo_usuario = Usuario(name=name, email=email, senha=senha_hash)

    db.session.add(novo_usuario)
    db.session.commit()

    return jsonify({"mensagem": "Usuário criado com sucesso"}), 201

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    senha = data.get("senha")
    user = Usuario.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.senha, senha):
        return jsonify({"erro": "Email ou senha inválidos"}), 401
    return jsonify({"mensagem": "Bem-vindo", "user_id": user.name}), 200