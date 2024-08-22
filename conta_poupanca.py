from conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, titular, senha, saldo=0):
        super().__init__(titular, senha, saldo)

    def render_juros(self, porcentagem):
        rendimento = self._Conta__saldo * (porcentagem/100)
        self._Conta__saldo += rendimento