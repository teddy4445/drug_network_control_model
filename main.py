# library imports
import os
import time
import random
import numpy as np

# project imports
from sim import Simulator
from plotter import Plotter
from multi_sim import MultiSim


class Main:
    """
    Single entry point of the project
    """

    # CONSTS #
    PAPER_PLOTS_FOLDER = "paper_results"
    PAPER_PLOTS_PATH = os.path.join(os.path.dirname(__file__), PAPER_PLOTS_FOLDER)
    # END - CONSTS #

    RESULTS_FOLDER = os.path.join(os.path.dirname(__file__), "results")

    def __init__(self):
        pass

    @staticmethod
    def run():
        """
        Run all the experiments one after the other
        """
        Main.io_prepare()
        Main.simple()

    @staticmethod
    def io_prepare():
        """
        Make sure we have all the IO stuff we need
        """
        try:
            os.mkdir(Main.RESULTS_FOLDER)
        except:
            pass

    @staticmethod
    def simple():
        # TODO: fix later
        pass


if __name__ == '__main__':
    Main.run()
