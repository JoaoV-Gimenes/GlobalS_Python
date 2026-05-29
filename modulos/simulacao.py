from modulos.distancia import escolha_objeto
from modulos.listagem import exibir_objetos, carregar_objetos
from astropy import units as u
from poliastro.bodies import Earth
from poliastro.twobody import Orbit
import numpy as np

def executar():
    ## Carrega os dados
    objetos = carregar_objetos()

    ## Exibe os dados
    exibir_objetos(objetos)

    