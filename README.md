# Resenhas.Blog


## 📚 Sobre o projeto

**Resenhas.Blog** é uma plataforma Web para leitores compartilharem suas experiências com livros por meio de resenhas. Os usuários podem registrar opiniões, dar notas, e manter um perfil com suas leituras favoritas.
Ideal para quem ama ler e gosta de expor as ideias sobre livros para outras pessoas.

## 🔧 Requisitos:

* Python 3.11

* Flask 3.1.1

* Banco de dados: SQLite3

### 🗃️ Tabela 'Usuario' com os seguintes campos:
```
idUsuario = int, (primary key)
name = string(100), (nullable)
email = string(100), (nullable)
senha = string(255), (nullable)
profile_pic = string(200), (nullable)
```

### 🗃️ Tabela 'Resenha' com os seguintes campos:
```
idResenha = int, (primary key)
titulo = string(120), (nullable)
nomeLivro = string(30), (nullable)
genero = string(30), (nullable)
desc = string(400), (nullable)
nota = float, (nullable)
idUsuario = int, (foreign key)
```

## 🔐 Configuração do banco de dados
```
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
```

## 📁 Estrutura do projeto:
```
projeto/
├── main.py
├── models.py
├── reset_db.py
├── routes.py
├── templates/
│   └── index.html
│   └── perfil.html
│   └── cadastro.html
├── static/
│   └── img/
│   	└── imgLivro.png
│   	└── imgUser.png
│   └── css/
│   	└── index.css
│   	└── perfil.css
│   	└── cadastro.css
└── requirements.txt
```

## 💻 Como rodar o projeto localmente
```
git clone https://github.com/joaoSouza3/Projeto-Python.git

cd Projeto-Python

python -m venv venv

venv\scripts\activate

pip install -r requirements.txt
```

## 🚀 Execute o projeto:
```
python main.py
```
