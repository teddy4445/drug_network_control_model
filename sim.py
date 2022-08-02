# library imports
import math
import random
import numpy as np

# project imports
from env.graph import Graph
from population import Population


class Simulator:
    """
    The main class of the project - the simulator
    """

    def __init__(self,
                 population: Population,
                 graph: Graph,
                 max_time: int):
        # sim settings
        self.population = population
        self.graph = graph

        # technical
        self.max_time = max_time

        # operation
        self.step = 0

        # later analysis
        self.epi_dist = []

    # logic #

    def run(self):
        while self.step <= self.max_time:
            self.run_step()

    def run_step(self):
        """
        The main logic of the class, make a single
        """
        # TODO: finish later
        self.step += 1

    # end - logic #

    # analysis #

    # end - analysis #

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Sim: {}/{} ({:.2f}\%)>".format(self.step,
                                                self.max_time,
                                                100 * self.step / self.max_time)
