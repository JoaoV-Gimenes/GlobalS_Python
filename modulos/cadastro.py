import os
import json

def executar():

    ## Solicita nome, tipo, posição e velocidade do corpo
    nome = input('Nome: ')
    tipo = input('Tipo (satélite ativo ou detrito): ')
    posicao = [
        float(input('Posição X (km): ')),
        float(input('Posição Y (km): ')),
        float(input('Posição Z (km): '))
    ]
    velocidade = [
        float(input('Velocidade X (km): ')),
        float(input('Velocidade Y (km): ')),
        float(input('Velocidade Z (km): '))
    ]
    
    ## Armazena tudo em uma variável
    corpo = {
        'nome': nome,
        'tipo': tipo,
        'posicao': posicao,
        'velocidade': velocidade
    }

    ## Carrega o arquivo com os dados já existentes
    if os.path.exists('dados/objetos.json'):
        with open('dados/objetos.json', 'r') as f:
            objetos = json.load(f)
    else:   
        ## Caso não tenha, cria uma lista vazia
        objetos = []

    ## Adiciona os dados na lista
    objetos.append(corpo)

    ## Salva os dados novos no arquivo
    with open('dados/objetos.json', 'w') as f:
        json.dump(objetos, f, indent=4, ensure_ascii=False)

    print('✅ Objeto cadastrado com sucesso!')
    return True 