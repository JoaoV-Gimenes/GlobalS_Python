import requests
from dotenv import load_dotenv
import os
from sgp4.api import Satrec, WGS84
from astropy.time import Time
import numpy as np
from modulos.cadastro import salvar_objeto

## carrega o .env
load_dotenv() 

URL_LOGIN = 'https://www.space-track.org/ajaxauth/login'
URL_BASE = 'https://www.space-track.org/basicspacedata/query'

## Função para login no site do SPACETRACK
def login():

    session = requests.Session()
    credenciais = {
        'identity': os.getenv('SPACETRACK_USER'),
        'password': os.getenv('SPACETRACK_PASS')
    }

    resposta = session.post(URL_LOGIN, data=credenciais)

    if resposta.status_code == 200:
        print('✅ Login realizado com sucesso!')
        return session
    else:
        print('❌ Erro no login! Verifique suas credenciais.')
        return None

## Função para buscar TLEs reais
def buscar_tle(session, nome_objeto):
    url = f'{URL_BASE}/class/gp/OBJECT_NAME/~~{nome_objeto}/orderby/EPOCH desc/limit/10/format/json'
    resposta = session.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        if dados:
            return dados
        else:
            print(f'Nenhum objeto encontrado com o nome: {nome_objeto}')
            return None
    else:
        print(f'❌ Erro ao buscar dados: {resposta.status_code}')
        return None

## Função para armazenar os dados do TLE 
def tle_para_orbita(dados):
    linha1 = dados[0]['TLE_LINE1']
    linha2 = dados[0]['TLE_LINE2']
    nome = dados[0]['OBJECT_NAME']

    satelite = Satrec.twoline2rv(linha1, linha2)

    ## Tempo atual
    t = Time.now()
    e, r, v = satelite.sgp4(t.jd1, t.jd2)
    
    if e != 0:
        print(f'❌ Erro ao calcular órbita: código {e}')
        return None
    
    return {
        'nome': nome,
        'tipo': 'satélite',
        'posicao': list(r),
        'velocidade': list(v)
    }


def executar():
    session = login()

    if session:
        nome = input('Nome do objeto (ex: ISS, HUBBLE): ').upper()
        dados = buscar_tle(session, nome)
        if dados:
            print(f'Encontrado: {dados[0]["OBJECT_NAME"]}')
            print(f'TLE Line 1: {dados[0]["TLE_LINE1"]}')
            print(f'TLE Line 2: {dados[0]["TLE_LINE2"]}')

            dados_obtidos = tle_para_orbita(dados)
            if dados_obtidos:
                print(f'\nNome: {dados_obtidos["nome"]}')
                print(f'Posição: X={dados_obtidos["posicao"][0]:.2f} Y={dados_obtidos["posicao"][1]:.2f} Z={dados_obtidos["posicao"][2]:.2f} km')
                print(f'Velocidade: X={dados_obtidos["velocidade"][0]:.4f} Y={dados_obtidos["velocidade"][1]:.4f} Z={dados_obtidos["velocidade"][2]:.4f} km/s')

                salvar = input('Deseja salvar esses dados? (s/n)').lower()
                while salvar not in ['s', 'n']:
                    print('Opção inválida!')
                    salvar = input('Deseja salvar este objeto? (s/n) --> ').lower()
                    
                if salvar == 's':
                    salvar_objeto(dados_obtidos)
                    print('✅ Objeto cadastrado com sucesso!')