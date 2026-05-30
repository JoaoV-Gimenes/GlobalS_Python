from modulos.distancia import escolha_objeto
from modulos.listagem import exibir_objetos, carregar_objetos
from astropy import units as u
from poliastro.bodies import Earth
from poliastro.twobody import Orbit
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import os

def calc_orbita(corpo):
    r = np.array(corpo['posicao']) * u.km
    v = np.array(corpo['velocidade']) * u.km / u.s
    orb = Orbit.from_vectors(Earth, r, v)
    return orb

def tempo():
    while True:
        try:
            horas = float(input('Tempo de simulação (horas) --> '))
            intervalo = int(input('Intervalo de verificação (minutos) -->'))

            if horas <= 0 or intervalo <= 0:
                print('Os números deve ser maiores que 0')
                continue

            if intervalo > horas*60:
                print('O intervalo não pode ser maior que o tempo total!')
                continue

            minutos_total = int(horas * 60)
            return minutos_total, intervalo

        except ValueError:
            print('Digite apenas números!')

def executar():
    ## Carrega os dados
    objetos = carregar_objetos()

    ## Exibe os dados
    exibir_objetos(objetos)

    print('\nPara a simulação de órbita, deverá ser utilizados apenas dois corpos já cadastrados!\n')

    ## Armazena as informações dos corpos e calcula suas órbitas
    corpo1 = escolha_objeto('Corpo 1 --> ', objetos)
    orbita1 = calc_orbita(corpo1)

    corpo2 = escolha_objeto('Corpo 2 --> ', objetos)
    orbita2 = calc_orbita(corpo2)

    ## obtem o tempo total e o intervalo de tempo para calculo da rota dos corpos
    minutos_total, intervalo = tempo()

    ## Solicita o limiar de alerta
    while True:
        try:
            limiar = float(input('Limiar de alerta (km) --> '))
            break
        except ValueError:
            print('Digite apenas números!')
    
    ## Listas para armazenar as informações
    distancias = []
    minutos = []

    ## Loop para análise das rotas
    for i in range(0, minutos_total, intervalo):

        ## posição futura de cada corpo no minuto i
        futuro1 = orbita1.propagate(i * u.min)
        futuro2 = orbita2.propagate(i * u.min)
        
        ## calcula distancia entre eles em certo ponto (i min)
        distancia = np.linalg.norm(futuro1.r - futuro2.r)

        ## Gera alerta caso possível colisão
        if distancia.value <= limiar:
            print(f'Possível colisão encontrada! distancia --> {distancia:.2f} / minuto --> {i}')
        
        ## adiciona as informações na lista
        distancias.append(distancia)
        minutos.append(i)

    ## Conclusão
    print(f'Simulação finalizada')
    print(f'Menor distância detectada: {min(distancias)}')
    print(f'minuto: {minutos[distancias.index(min(distancias))]}')

    ## Geração do gráfico
    valores = [d.value for d in distancias]
    plt.figure(figsize=(10, 5))
    plt.plot(minutos, valores, color='blue', label='Distância')
    plt.axhline(y=limiar, color='red', linestyle = '--', label=f'Limiar de alerta ({limiar} km)')
    plt.xlabel("Tempo (min)")
    plt.ylabel("Distância (km)")
    plt.title(f'Simulação: {corpo1['nome']} x {corpo2['nome']}')
    plt.legend()
    plt.grid(True)
    plt.figtext(0.1, 0.02, 
                f'Corpo 1: {corpo1['nome']}  |  Corpo 2: {corpo2['nome']}\n'
                f'Menor distância: {min(valores):.2f} km  |  Minuto de menor distância: {minutos[distancias.index(min(distancias))]} min\n'
                f'Limiar de alerta: {limiar} km  |  Tempo simulado: {minutos_total} min',
                fontsize=9,
                bbox=dict(facecolor='lightyellow', edgecolor='gray', boxstyle='round'))
    plt.tight_layout() # ajusta o layout para o texto não sobrepor o gráfico

    ## Salva o gráfico em png caso o usuário queira
    while True:
        salvar = input('Deseja salvar o gráfico para relatório? (s/n): ').lower()
        match salvar:
            case 's':
                os.makedirs('relatorios', exist_ok=True)
                nome_grafico = f'relatorios/relatorio_{datetime.now().strftime('%d%m%Y_%H%M%S')}.png'
                plt.savefig(nome_grafico)
                print(f'✅ Relatório salvo em {nome_grafico}')
                break
            case 'n':
                break
            case _:
                print('Operação Inválida!')
    plt.show()