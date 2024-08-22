class Conta:
    def __init__(self, titular, senha, saldo=0):
        self.titular = titular
        self.__saldo = saldo
        self.__senha = senha

    def consultar_saldo(self):
        print('='*30)
        print(f'{self.titular} O saldo da sua conta é R${self.__saldo}')
        print('='*30)

    def depositar(self):
        valor_deposito = float(input('Digite o valor do deposito. '))
        if self.validar_senha():
            self.__saldo += valor_deposito
            print('Deposito realizado com sucesso.')
        else:
            print('Senha incorreta.')

    def sacar(self):
        valor_saque = float(input('Digite o valor do saque. '))
        if self.validar_senha():
            if valor_saque > self.__saldo:
                print('Saldo insuficiente.')
            else:
                self.__saldo -= valor_saque
                print('Saque realizado com sucesso!')
        else:
            print('Senha incorreta.')

    def alterar_senha(self):
        senha_digitada = input('Digite sua senha para verificação. ')
        self.__senha = senha_digitada

    def validar_senha(self):
        tentativa = 3
        while tentativa > 0:
            senha_digitada = input('Digite sua senha. ')
            if senha_digitada == self.__senha:
                print('Certo')
                return True
            print('Errado')
            tentativa -= 1
        return False

    def login(self):
        usuario_digitado = input('Digite o usuario. ')
        senha_digitada = input('Digite sua senha.')

        with open('usuario.txt', 'r') as arquivo:
            for linha in arquivo:
                if linha.startswith(f'Titular: {usuario_digitado}'):
                    partes = linha.strip().split(', ')
                    senha_armazenada = partes[1].split(': ')[1]
                    if senha_digitada == senha_armazenada:
                        print('Login bem-sucedido!')
                        return True
                    else:
                        print('Senha incorreta.')
                        return False
        print('Titular não encontrado.')
        return False

    def cadastrar(self):
        titular_digitado = input('Digite o nome do titular da conta. ')
        senha_digitada = input('Cadastre sua senha. ')
        self.titular = titular_digitado
        self.__senha = senha_digitada
        print('Cadastrado com sucesso.')

        with open('usuario.txt', 'a') as arquivo:
            arquivo.write(f'Titular: {self.titular}, Senha: {self.__senha}, Saldo: {self.__saldo}\n')

        return self.titular, self.__senha

    def atualizar(self):
        with open('usuario.txt', 'r') as arquivo:
            linhas = arquivo.readlines()

        with open('usuario.txt', 'w') as arquivo:
            for linha in linhas:
                if linha.startswith(f'Titular: {self.titular}'):
                    linha = f'Titular: {self.titular}, Senha: {self.__senha}, Saldo: {self.__saldo}\n'
                arquivo.write(linha)