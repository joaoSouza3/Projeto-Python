from main import app
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


@app.route("/auth")
def auth():
    return render_template("cadastro.html")