from flask import Flask, request, jsonify, render_template, json
from main import ler_dados, atualizar_nota, criar_novo_usuario_e_nota, deletar_usuario
from tabelas import Usuario, Nota
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method=='GET':
        resultado = ler_dados()
        return render_template('index.html',data=resultado)
    elif request.method=='POST':
        data = request.get_data()
        usuario_e_nota = json.loads(data)
        
        user = Usuario( 
                        nome=usuario_e_nota["usuario"],
                        email=usuario_e_nota["email"],
                        senha_hash=usuario_e_nota["senha"])
        note = Nota(
                        titulo=usuario_e_nota["titulo"],
                        conteudo=usuario_e_nota["nota"])
        criar_novo_usuario_e_nota(user, note)
        return jsonify({"message": "Usuário e nota criados com sucesso!"}), 201
    else:
        return jsonify({'error': 'Página não encontrada!'}), 404
    
@app.route("/api/users", methods=["GET"])
def api_users():
    try:
        data = ler_dados()
        return jsonify({"success": True, "data": data}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__=="__main__":
    app.run()