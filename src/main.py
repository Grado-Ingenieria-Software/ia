from funcionesMenu import *
import argparse
import os
import json
import multiprocessing
from pomdp_runner import PomdpRunner
from util import RunnerParams

info = None
#Elegir el Problema
opciones = ["Tigre", "LASER TAG", "Indiana Jones", "Anuncios Web"]
imprimeMenu(opciones, info)
opcionesNormalizadas = ["Tigre", "TAG", "IndianaJones", "AnunciosWeb"]
res = input("Elige un problema: ")
problema = opcionesNormalizadas[int(res)-1]

#Elegir el algoritmo
opciones = ["POMCP", "PBVI"]
if problema == "TAG":
    opciones = ["POMCP"]
    info = """PBVI ha sido desactivado para este problema por motivos
    de eficiencia."""
opcionesNormalizadas = ["pomcp", "pbvi"]
imprimeMenu(opciones, info)
res = input("Elige un algoritmo : ")
algoritmo = opcionesNormalizadas[int(res)-1]

#Elegir el tipo de simulacion
opciones = ["Simulación Iterativa", "Simulación Silenciosa", "Benchmark"]
opcionesNormalizadas = ["iterativa", "silenciosa", "benchmark"]
imprimeMenu(opciones, info)
res = input("Elige un modo de simulación : ")
modo = opcionesNormalizadas[int(res)-1]


# Ejecuta el problema
parser = argparse.ArgumentParser(description='Solve pomdp')
parser.add_argument('--config', type=str, default=algoritmo, help='The file name of algorithm configuration (without JSON extension)')
parser.add_argument('--env', type=str, default=problema+'.POMDP', help='The name of environment\'s config file')
parser.add_argument('--budget', type=float, default=float('inf'), help='The total action budget (defeault to inf)')
parser.add_argument('--snapshot', type=bool, default=False, help='Whether to snapshot the belief tree after each episode')
parser.add_argument('--logfile', type=str, default=None, help='Logfile path')
parser.add_argument('--random_prior', type=bool, default=False, help='Whether or not to use a randomly generated distribution as prior belief, default to False')
parser.add_argument('--max_play', type=int, default=100, help='Maximum number of play steps')

args = vars(parser.parse_args())
params = RunnerParams(**args)

if modo == "benchmark":
    numeroEjecuciones = 30
else:
    numeroEjecuciones = 1


with open(params.algo_config) as algo_config:
    algo_params = json.load(algo_config)
    runner = PomdpRunner(params)
    runner.run(numeroEjecuciones,modo, **algo_params)
