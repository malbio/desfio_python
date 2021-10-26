from pessoa import *



def cadastro():
        nome = input('digite seu nome: ')
        idade = input('digite sua idade: ')
        sexo = input('digite seu sexo: ')
        cidade = input('digite sua cidade: ')
        estado = input('digite seu estado: ')

        return nome, idade, sexo, cidade, estado


pc = cadastro()

pessoa1 = pessoa(pc[0], pc[1], pc[2], pc[3], pc[4])

#teste
print(pessoa1.nome,',' ,pessoa1.idade, ',' ,pessoa1.sexo, ',' ,pessoa1.cidade, ',' ,pessoa1.estado)



