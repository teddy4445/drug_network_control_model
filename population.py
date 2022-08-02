# library imports
import random

# project imports
from env.agent import Agent
from env.graph import Graph


class Population:
    """
    The population in the simulator
    """

    def __init__(self,
                 agents: list):
        self.agents = agents

    def get_size(self):
        return len(self.agents)

    # smart getters #

    def count_node(self,
                   node_id: int):
        return len([True for agent in self.agents if agent.location == node_id])

    # end - smart getters #

    # smart setters #

    # end - smart setters #

    # logic #

    # end - logic #

    @staticmethod
    def random(population_count: int,
               graph: Graph,
               infect_portion: float = 0.02):
        """
        Random amount of individuals, random states, random locations
        """
        # TODO: finish later
        pass

    def __hash__(self):
        return self.agents.__hash__()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Population: size={}>".format(len(self.agents))
