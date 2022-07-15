import sqlite3 as sql

# Criando banco de dados


class BancoDados:
    def __init__(self):
        self.conexao = sql.connect("mercado_ex.db")
        self.cursor = self.conexao.cursor()
        self.__montar_banco()

    def __montar_banco(self):
        """Monta todas as tabelas do banco de dados."""
        self.__clientes()
        self.__produtos()
        self.__vendas()
        self.__desconectar()

    def __clientes(self):
        """Constrói a tabela de CLIENTES"""
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS clientes ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT,"
            "nome TEXT NOT NULL,"
            "cpf TEXT NOT NULL UNIQUE,"
            "cep TEXT NOT NULL,"
            "estado TEXT NOT NULL,"
            "bairro TEXT NOT NULL,"
            "rua TEXT NOT NULL,"
            "numero INTEGER NOT NULL)"
        )
        self.conexao.commit()

    def __produtos(self):
        """Constrói a tabela de PRODUTOS"""
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS produtos ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT,"
            "nome TEXT NOT NULL,"
            "familia TEXT NOT NULL,"
            "barras TEXT NOT NULL UNIQUE)"
        )
        self.conexao.commit()

    def __vendas(self):
        """Constrói a tabela de VENDAS"""
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS vendas ("
            "quantidade REAL NOT NULL,"
            "unitario REAL NOT NULL,"
            "total REAL NOT NULL,"
            "data TEXT NOT NULL,"
            "cpf TEXT PRIMARY KEY NOT NULL,"
            "barra TEXT NOT NULL)"
        )
        self.conexao.commit()

    def __desconectar(self):
        """Encerra a conexão com o banco de dados."""
        self.cursor.close()
        self.conexao.close()


BancoDados()