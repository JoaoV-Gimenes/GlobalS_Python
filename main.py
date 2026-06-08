from modulos import cadastro, listagem, distancia, simulacao, descricao, delete, tle


def menu():
    opcoes = {
        '1': descricao.executar,
        '2': cadastro.executar,
        '3': tle.executar,
        '4': delete.executar,
        '5': listagem.executar,
        '6': distancia.executar,
        '7': simulacao.executar,
    }

    while True:
        print('1 -- Descrição do projeto')
        print('2 -- Cadastrar satélite ativo / detrito')
        print('3 -- Cadastrar TLE')
        print('4 -- Deletar objeto')
        print('5 -- Listar objetos')
        print('6 -- Calcular distância entre corpos')
        print('7 -- Simulação de trajeto')
        print('0 -- Sair')
        opcao = input('\n O que deseja realizar? --- ')

        if opcao == '0':
            print('encerrando...')
            break
        elif opcao in opcoes:
            opcoes[opcao]()
        else:
            print('Opção inválida!')

if __name__ == '__main__':
    menu()