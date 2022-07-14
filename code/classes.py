import sqlite3
import arrow
import requests
from funcoes import validar_Cpf

# Conexao com banco de dados
conexao = sqlite3.connect('mercado_ex.db')
cursor = conexao.cursor()


class Mercado:
    def cadastrar_Cliente(self, nome, numero):
        self.cep = input('Qual seu cep? ')
        cep = requests.get('https://cep.awesomeapi.com.br/json/' + self.cep)
        cep_json = cep.json()
        while True:
            cpf = validar_Cpf()
            try:
                cursor.execute('INSERT INTO clientes(nome, cpf, cep, estado, bairro, rua, numero)'
                           'VALUES(?,?,?,?,?,?,?)',
                           (nome, cpf, self.cep, cep_json['state'], cep_json['district'], cep_json['address_name'], numero))
                conexao.commit()
                break
            except:
                print('O cpf já foi cadastrado, cadastre outro.')


    def editar_Cliente(self):
        x = input('Qual cliente deseja editar [CPF]: ')
        infos = [
            '', 'nome', 'cpf', 'cep', 'estado', 'bairro', 'rua', 'numero'
        ]
        cursor.execute(f'SELECT * FROM clientes WHERE cpf={x}')
        for linha in cursor.fetchall():
            print(f'{linha[0]} - {linha[1]} - {linha[2]} - {linha[3]} - {linha[4]} - {linha[5]} - {linha[6]}')
        y = int(input('[1] Nome'
                      '\n[2] CPF'
                      '\n[3] CEP'
                      '\n[4] Estado'
                      '\n[5] Bairro'
                      '\n[6] Rua'
                      '\n[7] Numero'))
        new_info = input('Digite o novo:')
        cursor.execute(f'UPDATE clientes SET {infos[y]}="{new_info}" WHERE cpf={x}')
        conexao.commit()

    def excluir_cliente(self, clienteDesejado):
        cursor.execute(f'DELETE FROM clientes WHERE cpf={clienteDesejado}')
        conexao.commit()

    def cadastrar_Produto(self, nome, familia, barras):
        while True:
            try:
                cursor.execute('INSERT INTO produtos(nome, familia, barras)'
                           'VALUES(?,?,?)',
                           (nome, familia, barras))
                conexao.commit()
                break
            except:
                print('O codigo de barras já está cadastrado')


    def editar_Produto(self):
        x = input('Qual o ID do produto? ')
        infos = [
            '', 'nome', 'familia', 'barras'
        ]
        y = int(input('[1] Nome'
                      '\n[2] Famiia'
                      '\n[3] Barras'))
        new_info = input('Digite o novo:')
        cursor.execute(f'SELECT * FROM produtos WHERE id={x}')
        for linha in cursor.fetchall():
            print(f'{linha[0]} - {linha[1]} - {linha[2]}')
        cursor.execute(f'UPDATE produtos SET {infos[y]}="{new_info}" WHERE id={x}')
        conexao.commit()

    def excluir_Produto(self, produtoDesejado):
        cursor.execute(f'DELETE FROM produtos WHERE barras={produtoDesejado}')
        conexao.commit()

    def cadastrar_Venda(self, quantidade, valor, cpf, barras):

        total = float(quantidade) * float(valor)
        data = arrow.now().format('DD/MM/YYYY')
        cursor.execute('INSERT INTO vendas(quantidade, unitario, total, data, cpf, barras)'
                       'VALUES(?,?,?,?,?,?)',
                        (quantidade, valor, total, data, cpf, barras))
        conexao.commit()

    def deletar_produtos(self):
        cursor.execute('DELETE FROM produtos WHERE id>0')
        conexao.commit()

    def salvar(self):
        cursor.close()
        conexao.close()