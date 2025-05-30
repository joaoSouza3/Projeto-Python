from main import app
from flask import render_template

#ROTAS
@app.route("/")    
def homepage():
    return render_template("index.html")


@app.route("/perfil")
def perfil():
    return render_template("perfil.html")