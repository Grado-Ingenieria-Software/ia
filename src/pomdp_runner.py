import os

from funcionesEstadistica import *
from models import RockSampleModel, Model
from solvers import POMCP, PBVI
from parsers import PomdpParser, GraphViz
from logger import Logger as log

class PomdpRunner:

    def __init__(self, params):
        self.params = params
        if params.logfile is not None:
            log.new(params.logfile)

    def create_model(self, env_configs):
        """
        Builder method for creating model (i,e, agent's environment) instance
        :param env_configs: the complete encapsulation of environment's dynamics
        :return: concrete model
        """
        MODELS = {
            'RockSample': RockSampleModel,
        }
        return MODELS.get(env_configs['model_name'], Model)(env_configs)

    def create_solver(self, algo, model):
        """
        Builder method for creating solver instance
        :param algo: algorithm name
        :param model: model instance, e.g, TigerModel or RockSampleModel
        :return: concrete solver
        """
        SOLVERS = {
            'pbvi': PBVI,
            'pomcp': POMCP,
        }
        return SOLVERS.get(algo)(model)

    def snapshot_tree(self, visualiser, tree, filename):
        visualiser.update(tree.root)
        visualiser.render('./dev/snapshots/{}'.format(filename))  # TODO: parametrise the dev folder path

    def run(self, numeroEjecuciones,modo, algo, T, **kwargs):
        pasos = []
        recompensas = []
        while numeroEjecuciones != 0:
            params, pomdp = self.params, None
            total_rewards, budget = 0, params.budget
            if modo != "benchmark":
                log.info('~~~ Inicializando ~~~')
            with PomdpParser(params.env_config) as ctx:
                # creates model and solver
                model = self.create_model(ctx.copy_env())
                pomdp = self.create_solver(algo, model)

                # supply additional algo params
                belief = ctx.random_beliefs() if params.random_prior else ctx.generate_beliefs()

                if algo == 'pbvi':
                    belief_points = ctx.generate_belief_points(kwargs['stepsize'])
                    pomdp.add_configs(belief_points)
                elif algo == 'pomcp':
                    pomdp.add_configs(budget, belief, **kwargs)

            # have fun!
            if modo != "benchmark":
                log.info('''
                ++++++++++++++++++++++
                    Estado inicial:  {}
                    Presupuesto inicial:  {}
                    Creencia inicial: {}
                    Horizonte temporal: {}
                    Max Play: {}
                    Modo: {}
                ++++++++++++++++++++++'''.format(model.curr_state, budget, belief, T, params.max_play, modo))

            condicionParada = False
            i = 0
            while not condicionParada:
                # plan, take action and receive environment feedbacks
                pomdp.solve(modo, T)
                action = pomdp.get_action(belief)
                new_state, obs, reward, cost = pomdp.take_action(action)
                
                # update states
                belief = pomdp.update_belief(belief, action, obs)
                total_rewards += reward
                budget -= cost

                # print info
                if modo == "iterativa":
                    log.info('\n'.join([
                    'Accion tomada: {}'.format(action),
                    'Observacion: {}'.format(obs),
                    'Recompensa: {}'.format(reward),
                    'Presupuesto: {}'.format(budget),
                    'Nuevo estado: {}'.format(new_state),
                    'Nueva Creencia: {}'.format(belief),
                    'Prueba numero: {}'.format(i),
                    '=' * 20
                    ]))


                if budget <= 0:
                    log.info('Presupuesto superado.')
                    break

                if params.env == "Tigre.POMDP":
                    condicionParada = action == "open-left" or action == "open-right" or i >= params.max_play
                elif params.env == "TAG.POMDP":
                    condicionParada = action == "Catch"  or i >= params.max_play
                elif params.env == "IndianaJones.POMDP":
                    condicionParada = action == "izquierda" or action == "centro" or action == "derecha"  or i >= params.max_play
                else:
                    condicionParada = i >= params.max_play
                

                i += 1

            if modo != "benchmark":   
                log.info('{} pasos. Recompensa Total = {}'.format(i, total_rewards))
            else:
                log.info('{} | {} pasos. Recompensa Total = {}'.format(numeroEjecuciones, i, total_rewards))
            pasos.append(i)
            recompensas.append(total_rewards)
            numeroEjecuciones -= 1
        if modo == "benchmark":
            log.info('\n'.join([
            '#' * 20,
            'Media de los pasos: {}'.format(media(pasos)),
            'Varianza de los pasos: {}'.format(varianza(pasos)),
            'Desviacion Tipida de los pasos: {}'.format(desviacion_tipica(pasos)),
            '#' * 20
            ]))
            log.info('\n'.join([
            'Media de la recompensa: {}'.format(media(recompensas)),
            'Varianza de la recompensa: {}'.format(varianza(recompensas)),
            'Desviacion Tipida de la recompensa: {}'.format(desviacion_tipica(recompensas)),
            '#' * 20
            ]))
        return pomdp
