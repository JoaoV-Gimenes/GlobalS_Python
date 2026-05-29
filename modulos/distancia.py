from modulos.listagem import carregar_objetos, exibir_objetos
import astropy.units as u
import numpy as np

## Função para tratamento 
def escolha_objeto(mensagem, dados):
    while True:
        try:
            escolha = int(input(mensagem))
            ## verifica se a escolha está entre 1 e a quantidade total de objetos
            if 0 < escolha <= len(dados):
                ## Caso esteja no arquivo
                return dados[escolha - 1]   
            else: 
                ## Caso não esteja
                print(f'Número inválido! Escolha entre 1 e {len(dados)}')
        ## Caso o usuário digite letras
        except ValueError:
            print('Apenas núeros são válidos!')

def executar():
    ## Carrega todos os dados
    objetos = carregar_objetos()

    ## Mostra os dados
    exibir_objetos(objetos)

    while True:
        print('\nPara o cálculo de distância, deverá ser utilizados apenas dois corpos já cadastrados!\n')
    
        ## Solicita os corpos e armazena a posição
        corpo1 = escolha_objeto('Corpo 1 --> ', objetos)
        r1 = np.array(corpo1['posicao']) * u.km

        corpo2 = escolha_objeto('Corpo 2 --> ', objetos)
        r2 = np.array(corpo2['posicao']) * u.km

        ## Calculo de distância entre corpos
        distancia = np.linalg.norm(r1 - r2)
        print(f'\nDistância entre {corpo1["nome"]} e {corpo2["nome"]}: {distancia:.2f}\n')

        ## Verifica se o usuário quer refazer o processo
        cont = input('Fazer outra conta? (s/n) -- ').lower()
        while cont not in ['s', 'n']:
            print('comando inválido')
            cont = input('Fazer outra conta? (s/n) -- ').lower()
        
        match cont:
            case 's':
                continue
            case 'n':
                break