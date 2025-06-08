from main import app
from models import Usuario, db
from flask import render_template, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask import render_template, request, redirect, url_for
from models import db, Resenha
from flask_login import LoginManager
from flask_login import login_required, current_user
from flask_login import login_user
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "cadastro"


@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

#ROTAS
@app.route("/")    
def homepage():
    resenhas = Resenha.query.order_by(Resenha.idResenha.desc()).all()
    return render_template("index.html", resenhas=resenhas)


@app.route('/criarResenha', methods=["POST"])
@login_required
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
        idUsuario= current_user.id
    )

    db.session.add(novaResenha)
    db.session.commit()
    return redirect("/")


@app.route("/perfil")
@login_required
def perfil():
    resenhas_usuario = current_user.resenha
    return render_template("perfil.html", name=current_user.name, email=current_user.email, resenhas=resenhas_usuario)

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    #data = request.get_json()
    name = request.form.get("name")
    email = request.form.get("email")
    senha = request.form.get("senha")

    if Usuario.query.filter_by(email=email).first():
        return jsonify({"erro": "Email já cadastrado"}), 400

    senha_hash = generate_password_hash(senha)
    novo_usuario = Usuario(name=name, email=email, senha=senha_hash)

    db.session.add(novo_usuario)
    db.session.commit()

    print(f"Usuário encontrado: {novo_usuario.email}, senha hash no banco: {novo_usuario.senha}")
    return redirect("/")
    #return jsonify({"mensagem": "Usuário criado com sucesso"}), 201

@app.route("/login", methods=["POST"])
def login():
    #data = request.form.get()
    email = request.form.get("email")
    senha = request.form.get("senha")
    user = Usuario.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.senha, senha):
        return jsonify({"erro": "Email ou senha inválidos"}), 401

    login_user(user)    
    return redirect("/perfil")


@app.route("/auth")
def auth():
    return render_template("cadastro.html")