from main import app
from models import Usuario, db
from flask import render_template, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask import render_template, request, redirect, url_for
from models import db, Resenha

#ROTAS
@app.route("/")    
def homepage():
    resenhas = Resenha.query.order_by(Resenha.idResenha.desc()).all()
    return render_template("index.html", resenhas=resenhas)


@app.route('/criarResenha', methods=["POST"])
def criarResenha():
    titulo = request.form.get("titulo")
    nomeLivro = request.form.get("nomeLivro")
    genero = request.form.get("genero")
    desc = request.form.get("desc")
    nota = float(request.form.get("nota"))

    novaResenha = Resenha(
        titulo= titulo,
        nomeLivro= nomeLivro,
        genero= genero,
        desc= desc,
        nota= nota,
        idUsuario= 1
    )

    db.session.add(novaResenha)
    db.session.commit()
    return redirect("/")


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


@app.route("/auth")
def auth():
    return render_template("cadastro.html")