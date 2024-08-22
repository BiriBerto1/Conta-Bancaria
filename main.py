from conta_poupanca import ContaPoupanca
from conta_corrente import ContaCorrente

def login():
    print("Bem vindo a sua conta bancaria.")
    print('Selecione 1 para se registrar ou 2 para fazer login.')
    opcao_login = int(input(''))
    return opcao_login

def menu():
    print('Selecione o serviço desejado:')
    print('1 - Consultar saldo.')
    print('2 - Depositar.')
    print('3 - Sacar.')
    print('4 - Alterar senha.')
    print('5 - Para sair.')
    opcao_menu = int(input(''))
    return opcao_menu

def main():
    conta = ContaPoupanca('Humberto','9999', 90)
    # opcao_login = login()
    conta.render_juros(0.1)
    conta.consultar_saldo()
    # if opcao_login == 1:
    #     conta.cadastrar()
    # elif opcao_login == 2:
    #     retorno, conta = conta.login()
    #     if retorno:
    #         while True:
    #             opcao_menu = menu()
    #             if opcao_menu == 1:
    #                 conta.consultar_saldo()
    #             elif opcao_menu == 2:
    #                 conta.depositar()
    #                 conta.atualizar()
    #             elif opcao_menu == 3:
    #                 conta.sacar()
    #                 conta.atualizar()
    #             elif opcao_menu == 4:
    #                 conta.alterar_senha()
    #                 conta.atualizar()
    #             elif opcao_menu == 5:
    #                 break
    

main()