from classes import Mercado as m

mercado = m()
while True:
    x = input('Mercado'
              '\n [1] Cadastrar cliente'
              '\n [2] Editar cliente'
              '\n [3] Excluir cliente'
              '\n [4] Cadastrar produto'
              '\n [5] Editar produto'
              '\n [6] Excluir produto'
              '\n [7] Cadastrar venda'
              '\n [T] Sair e salvar'
              '\n [D] Limpar tabela produtos').lower()

    if x == '1':
        mercado.cadastrar_Cliente(nome=input('Insira seu nome:'),
                                  numero=input('Insira seu numero: '))

    if x == '2':
        mercado.editar_Cliente()

    if x == '3':
        mercado.excluir_cliente(clienteDesejado=input('Escreva o cpf da conta que deseja deletar: '))

    if x == '4':
        mercado.cadastrar_Produto(nome=input('Insira o nome do produto:'),
                                  familia=input('Insira sua familia:'),
                                  barras=input('Insira seu numero de codigo de barras: '))

    if x == '5':
        mercado.editar_Produto()

    if x == '6':
        mercado.excluir_Produto(produtoDesejado=input('Escreva o codigo de barras do produto: '))

    if x == '7':
        mercado.cadastrar_Venda(quantidade=input('Quantidade do produto desejado'),
                                valor=input('Valor unitário do produto: '),
                                cpf=input('Seu cpf cadastrado: '),
                                barras=input('Codigo de barras do produto: '))
    if x == 'd':
        mercado.deletar_produtos()
    if x == 't':
        break


mercado.salvar()
