import json

## Função para leitura dos dados .json
def carregar_objetos():
    ## Leitura dos dados .json
    with open('dados/objetos.json', 'r', encoding='utf-8') as f:
        return json.load(f)
    
## Função para printar as inforações dos objetos no docuento .json
def exibir_objetos(objetos, inicio=0):
    for i, obj in enumerate(objetos, start=inicio):
        print(f'\n[{i+1}] {obj["nome"]} — {obj["tipo"]}')
        print(f'Posição:    X= {obj["posicao"][0]:.2f} Y= {obj["posicao"][1]:.2f} Z= {obj["posicao"][2]:.2f} km')
        print(f'Velocidade: X= {obj["velocidade"][0]:.4f} Y= {obj["velocidade"][1]:.4f} Z= {obj["velocidade"][2]:.4f} km/s')
    
def executar():
    ## leitura de dados 
    objetos = carregar_objetos()

    ## variáveis para manipulação de páginas
    pagina = 0
    por_pagina = 10

    ## loop para visualisação de dados
    while True:

        ## Define inicio e fim da lista (10 por iteração)
        inicio = pagina * por_pagina
        fim = inicio + por_pagina

        ## Printa as inforações de cada objetos no docuento .json
        exibir_objetos(objetos[inicio:fim], inicio=inicio)

        ## Termina o loop caso não tenha mais objetos para mostrar
        if fim >= len(objetos):
            print('\nFim da lista!\n')
            break

        ## Caso tenha mais objetos, verifica se o usuário quer visualisar 
        sequencia = input('Ver mais? (s/n) --  ').lower()

        ## Valida a opção digitada
        while sequencia != 's' and sequencia != 'n':
            print('Comando inválido!')
            sequencia = input('\nVer mais? (s/n) --  \n').lower()
        
        match sequencia:
            case 's':
                pagina += 1
                continue
            case 'n': 
                break