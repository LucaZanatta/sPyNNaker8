from spynnaker8.utilities import exceptions


class FailedState(object):
    def __init__(self):
        pass

    @staticmethod
    def run(simtime, callbacks=None):
        raise exceptions.Spynnaker8Exception(
            "You cannot call run until you have called setup. durrrr!")

    @staticmethod
    def exit():
        raise exceptions.Spynnaker8Exception(
            "You cannot call exit until you have called setup. durrrr!")

    @staticmethod
    def stop():
        raise exceptions.Spynnaker8Exception(
            "You cannot call stop until you have called setup. durrrr!")

    @staticmethod
    def reset(annotations=None):
        raise exceptions.Spynnaker8Exception(
            "You cannot call reset until you have called setup. durrrr!")

    @staticmethod
    def run_until(time_point, callbacks=None):
        raise exceptions.Spynnaker8Exception(
            "You cannot call run_until until you have called setup. durrrr!")

    @staticmethod
    def run_for(simtime, callbacks=None):
        raise exceptions.Spynnaker8Exception(
            "You cannot call run_for until you have called setup. durrrr!")

    @staticmethod
    def get_current_time():
        raise exceptions.Spynnaker8Exception(
            "You cannot call get_current_time until you have called setup. "
            "durrrr!")

    @staticmethod
    def get_time_step():
        raise exceptions.Spynnaker8Exception(
            "You cannot call get_time_step until you have called setup. "
            "durrrr!")

    @staticmethod
    def get_min_delay():
        raise exceptions.Spynnaker8Exception(
            "You cannot call get_min_delay until you have called setup. "
            "durrrr!")

    @staticmethod
    def get_max_delay():
        raise exceptions.Spynnaker8Exception(
            "You cannot call get_max_delay until you have called setup. "
            "durrrr!")

    @staticmethod
    def num_processes():
        raise exceptions.Spynnaker8Exception(
            "You cannot call num_processes until you have called setup. "
            "durrrr!")

    @staticmethod
    def rank():
        raise exceptions.Spynnaker8Exception(
            "You cannot call rank until you have called setup. durrrr!")

    @staticmethod
    def initialize(cells, **initial_values):
        raise exceptions.Spynnaker8Exception(
            "You cannot call initialize until you have called setup. durrrr!")

    @staticmethod
    def create(ellclass, cellparams=None, n=1):
        raise exceptions.Spynnaker8Exception(
            "You cannot call create until you have called setup. durrrr!")

    @staticmethod
    def connect(
            pre, post, weight=0.0, delay=None, receptor_type=None, p=1,
            rng=None):
        raise exceptions.Spynnaker8Exception(
            "You cannot call connect until you have called setup. durrrr!")

    @staticmethod
    def record(variables, source, filename, sampling_interval=None,
               annotations=None):
        raise exceptions.Spynnaker8Exception(
            "You cannot call record until you have called setup. durrrr!")
