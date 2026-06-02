import json
from modulos.listagem import carregar_objetos, exibir_objetos
from modulos.distancia import escolha_objeto

def executar():
    ## Carrega os dados e mostra para o usuário
    objetos = carregar_objetos()
    exibir_objetos(objetos)


    ## Escolha para qual deletar
    objeto = escolha_objeto('\n Objeto a deletar: ', objetos)
    Perg_remove = input(f'\n Tem certeza que deseja remover {objeto['nome']}? (s/n) --> ').lower()
    while Perg_remove not in ['s', 'n']:
        print('opção inválida!')
        Perg_remove = input(f'\n Tem certeza que deseja remover {objeto['nome']}? (s/n) --> ').lower()

    match Perg_remove:
        case 's':
            ## Acessa o objeto escolhida através do index
            index = objetos.index(objeto)
            print(f'\n Removendo {objeto['nome']}...')
            ## Printa e remove o objeto da lista
            objetos.pop(index)

            with open('dados/objetos.json', 'w', encoding='utf-8') as f:
                json.dump(objetos, f, indent= 4, ensure_ascii=False)

            print('Objeto removido com sucesso!')

        case 'n': 
            print('Operação cancelada')