from conta import Conta

class ContaCorrente:
    def __init__(self, titular, senha, limite):
        super().__init__(titular, senha)
        self.limite = limite

    def sacar(self):
        valor_saque = float(input('Digite o valor do saque. '))
        if self.validar_senha():
            if valor_saque < self.__saldo + self.limite:
                print('Saldo insuficiente.')
            else:
                self._Conta__saldo -= valor_saque
                print('Saque realizado com sucesso!')
        else:
            print('Senha incorreta.')