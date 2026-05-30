from modulos import cadastro, listagem, distancia, simulacao, descricao


def menu():
    opcoes = {
        '1': descricao.executar,
        '2': cadastro.executar,
        '3': listagem.executar,
        '4': distancia.executar,
        '5': simulacao.executar,
        '0': None
    }

    while True:
        print('1 -- Descrição do projeto')
        print('2 -- Cadastrar satélite ativo')
        print('3 -- Listar detritos')
        print('4 -- Calcular distância entre corpos')
        print('5 -- Simulação de trajeto')
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