import os
import json
import numpy as np

def valores_posicao():
    while True:
        try:
            x = float(input('Posição X (km): '))
            y = float(input('Posição Y (km): '))
            z = float(input('Posição Z (km): '))
            return x, y, z
        except ValueError:
            print('Digite apenas números / Utilize "." ou invés de "," !')


def valores_velocidade():
    while True:
        try:
            x = float(input('Velocidade X (km/s): '))
            y = float(input('Velocidade Y (km/s): '))
            z = float(input('Velocidade Z (km/s): '))
            return x, y, z
        except ValueError:
            print('Digite apenas números / Utilize "." ou invés de "," !')
    


def salvar_objeto(corpo):
    ## Carrega o arquivo com os dados já existentes
    if os.path.exists('dados/objetos.json'):
        with open('dados/objetos.json', 'r', encoding='utf-8') as f:
            objetos = json.load(f)
    else:   
        ## Caso não tenha, cria uma lista vazia
        objetos = []

    ## Adiciona os dados na lista
    objetos.append(corpo)

    ## Salva os dados novos no arquivo
    with open('dados/objetos.json', 'w', encoding='utf-8') as f:
        json.dump(objetos, f, indent=4, ensure_ascii=False)

    print('✅ Objeto cadastrado com sucesso!')

## Função para cadastro inicial
def cadastro_inicial():
    while True:
        ## Solicita nome, tipo, posição e velocidade do corpo
        nome = input('Nome: ').title()
        tipo = input('Tipo (satélite ou detrito): ').title()
        while tipo not in ['Satelite', 'Satélite', 'Detrito']:
            print('Opção inválida!')
            tipo = input('Tipo (satélite ou detrito): ').title()
        
        x, y, z = valores_posicao()
        posicao = [x, y, z]

        x, y, z = valores_velocidade()
        velocidade = [x, y, z]
        v_magnitude = np.linalg.norm(np.array(velocidade))

        if v_magnitude >= 11.2 :
            print(f'⚠️ Atenção: velocidade de {v_magnitude:.2f} km/s excede a velocidade de escape da Terra (11.2 km/s)!')
            print('Este objeto não estará em órbita terrestre e pode causar erros na simulação.')
            while True:
                Perg_vel = input('Deseja continuar ou refazer cadastro? (C/RC)').lower()
                match Perg_vel:
                    case 'c':
                        return nome, tipo, posicao, velocidade
                    case 'rc':
                        break
                    case _: 
                        print('Operação inválida!')
                        continue
        else:
            return nome, tipo, posicao, velocidade


def executar():

    nome, tipo, posicao, velocidade = cadastro_inicial()

    ## Armazena tudo em uma variável
    corpo = {
        'nome': nome,
        'tipo': tipo,
        'posicao': posicao,
        'velocidade': velocidade
    }

    salvar_objeto(corpo)
    
    return True 