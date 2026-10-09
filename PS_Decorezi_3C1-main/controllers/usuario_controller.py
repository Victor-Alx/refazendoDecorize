from flask import Blueprint, jsonify, request, render_template

from models.cliente import Cliente

usuario_bp = Blueprint("usuario", __name__, url_prefix="/usuarios")

@usuario_bp.route("/", methods=["POST"])
def cadastrar_usuario(email, senha):

    if not email or not senha:
        return render_template("Cadastro.html", error="Email e senha são obrigatórios"), 400

    cliente = Cliente.cadastrar_cliente(email=email, senha=senha)
    return render_template("Cadastro.html", cliente=cliente)

@usuario_bp.route("/", methods=["GET", "POST"])
def login_usuario(email, senha):

    if not email or not senha:
        return render_template("Login.html", error="Email e senha são obrigatórios"), 400
    else:
        cliente = Cliente.query.filter_by(email=email, senha=senha).first()
        if cliente:
            return render_template("Login.html", cliente=cliente)
        else:
            return render_template("Login.html", error="Email ou senha inválidos"), 401


