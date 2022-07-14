from time import sleep


def validar_Cpf():
    validaCPF = True
    while validaCPF:
        cpf = input('Escreva seu CPF: ')
        cpfReal = cpf
        totala = 0
        totalb = 0
        cont = 0
        b = 10
        a = 0
        cpf = ' '.join(filter(str.isalnum, cpf))
        cpf = cpf.split()

        while cont < 9:
            totala = totala + int(cpf[a]) * b
            a += 1
            b -= 1
            cont += 1
        cont = 0
        b = 11
        a = 0
        while cont < 10:
            totalb = totalb + int(cpf[a]) * b
            a += 1
            b -= 1
            cont += 1
        p1 = (totala * 10) % 11
        p2 = (totalb * 10) % 11
        if p1 == int(cpf[9]) and p2 == int(cpf[10]):
            validaCPF = False
            print('Cpf valido')
            sleep(1)
            return cpfReal
        else:
            print("O cpf é inválido")