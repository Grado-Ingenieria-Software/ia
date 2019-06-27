from tkinter import *
from funcionesMenu import *
import argparse
import os
import json
import multiprocessing
from pomdp_runner import PomdpRunner
from util import RunnerParams


root = Tk()
root.geometry('500x500')
root.title("POMDP | IA | 2018/19")

label_0 = Label(root, text="POMDP | IA | 2018/19",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="Problema:",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

problemas =["Tigre", "TAG", "IndianaJones", "AnunciosWeb"]
problema=StringVar()
dropProblema=OptionMenu(root, problema, *problemas)
dropProblema.config(width=20)
problema.set('Seleccione Problema') 
dropProblema.place(x=240,y=130)


label_2 = Label(root, text="Algoritmo:",width=20,font=("bold", 10))
label_2.place(x=80,y=180)

algoritmos =["pomcp", "pbvi"]
algoritmo=StringVar()
dropalgoritmo=OptionMenu(root, algoritmo, *algoritmos)
dropalgoritmo.config(width=20)
algoritmo.set('Seleccione Algoritmo') 
dropalgoritmo.place(x=240,y=180)


label_3 = Label(root, text="Tipo de simulacion:",width=20,font=("bold", 10))
label_3.place(x=80,y=230)

simulaciones = ["interactiva", "silenciosa", "benchmark"]
simulacion=StringVar()
dropsimulacion = OptionMenu(root, simulacion, *simulaciones)
dropsimulacion.config(width=20)
simulacion.set('Seleccione Simulacion') 
dropsimulacion.place(x=240,y=230)

label_4 = Label(root, text="Pasos maximos:",width=20,font=("bold", 10))
label_4.place(x=80,y=280)

var =IntVar()
var.set(100)
max_pasos = Spinbox(root, from_=0, textvariable=var)
max_pasos.place(x=240,y=280)
max_pasos = 100 if max_pasos == "" else max_pasos


label_5 = Label(root, text="Presupuesto",width=20,font=("bold", 10))
label_5.place(x=80,y=330)

var2 =IntVar()
var2.set(100)
presupuesto = Spinbox(root, from_=0, textvariable=var2)
presupuesto.place(x=240,y=330)
presupuesto = 'inf' if presupuesto == "" else presupuesto

def send(problema, algoritmo, simulacion, max_pasos, presupuesto):
    # Ejecuta el problema
    parser = argparse.ArgumentParser(description='Solve pomdp')
    parser.add_argument('--config', type=str, default=str(algoritmo), help='The file name of algorithm configuration (without JSON extension)')
    parser.add_argument('--env', type=str, default=str(problema)+'.POMDP', help='The name of environment\'s config file')
    parser.add_argument('--budget', type=float, default=float(presupuesto), help='The total action budget (defeault to inf)')
    parser.add_argument('--snapshot', type=bool, default=False, help='Whether to snapshot the belief tree after each episode')
    parser.add_argument('--logfile', type=str, default=None, help='Logfile path')
    parser.add_argument('--random_prior', type=bool, default=False, help='Whether or not to use a randomly generated distribution as prior belief, default to False')
    parser.add_argument('--max_play', type=int, default=max_pasos, help='Maximum number of play steps')

    args = vars(parser.parse_args())
    params = RunnerParams(**args)

    modo = simulacion
    if modo == "benchmark":
        numeroEjecuciones = 30
    else:
        numeroEjecuciones = 1


    with open(params.algo_config) as algo_config:
        algo_params = json.load(algo_config)
        runner = PomdpRunner(params)
        runner.run(numeroEjecuciones,modo, **algo_params)


Button(root, text='Ejecutar',width=20,bg='brown',fg='white', command= lambda: send(problema.get(), algoritmo.get(), simulacion.get(), max_pasos.get(), presupuesto.get())).place(x=180,y=380)

root.mainloop()