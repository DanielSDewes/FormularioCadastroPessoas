from flask import Flask, render_template, request, redirect, jsonify
import requests
import sqlite3
import re


app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    pessoas = conn.execute('SELECT * FROM pessoas').fetchall()
    conn.close()
    return render_template('index.html', pessoas=pessoas)

from flask import request, redirect
import re

def validar_cpf(cpf):
    cpf = re.sub(r'[^0-9]', '', cpf)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10 % 11) % 10
    if digito1 != int(cpf[9]):
        return False
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10 % 11) % 10
    if digito2 != int(cpf[10]):
        return False
    return True

@app.route('/add', methods=['POST'])
def add():
    nome = request.form['nome']
    cep = request.form['cep']
    rua = request.form['rua']
    cidade = request.form['cidade']
    estado = request.form['estado']
    cpf = request.form['cpf']

    if not validar_cpf(cpf):
        return 'CPF inválido', 400

    conn = get_db_connection()
    conn.execute('INSERT INTO pessoas (nome, cep, rua, cidade, estado, cpf) VALUES (?, ?, ?, ?, ?, ?)',
                 (nome, cep, rua, cidade, estado, cpf))
    conn.commit()
    conn.close()
    return 'Cadastro realizado com sucesso', 200


@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM pessoas WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/buscar_cep/<cep>')
def buscar_cep(cep):
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    if response.status_code == 200:
        return jsonify(response.json())
    return jsonify({'erro': 'CEP não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
