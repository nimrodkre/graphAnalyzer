import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from GraphAnalyzerError import GraphAnalyzerError
from inspect import getfullargspec
import ctypes


SCALE_LIMIT = 0.25
MAX_FEV = 25000


class GraphBuilder:
    def __init__(self, json_analyzer, csv_analyzer, equation):
        self.json_analyzer = json_analyzer
        self.csv_analyzer = csv_analyzer
        self.x_data = self.csv_analyzer.get_x_data()
        self.y_data = self.csv_analyzer.get_y_data()
        self.equation = equation

    def check_data(self):
        if len(self.x_data) == len(
               self.y_data) == len(
               self.csv_analyzer.get_x_error_data()) == len(
               self.csv_analyzer.get_y_error_data()):
            return True
        raise GraphAnalyzerError(
            "The length of the columns received are not equal")

    def get_xlimit(self):
        """
        If the xlimits are empty than the limits will be according the given
        data.
        Else we will use what the user wanted
        :return:
        """
        return (min(self.x_data) - max(
            self.x_data) * SCALE_LIMIT,
                max(self.x_data) + max(
                    self.x_data) * SCALE_LIMIT)

    def get_ylimit(self):
        return (min(self.csv_analyzer.get_y_data()) - max(
            self.csv_analyzer.get_y_data()) * SCALE_LIMIT,
                max(self.y_data) + max(
                    self.y_data) * SCALE_LIMIT)

    def init_graph(self):
        plt.xlim(self.get_xlimit())
        plt.ylim(self.get_ylimit())
        plt.title(self.json_analyzer.graph_title)
        plt.xlabel(self.json_analyzer.x_scale_label_title)
        plt.ylabel(self.json_analyzer.y_scale_label_title)

    def init_residual_graph(self, y_data):
        plt.xlim(self.get_xlimit())
        plt.ylim((min(y_data)[0] - max(y_data)[0] * SCALE_LIMIT,
                  max(y_data)[0] + max(y_data)[0] * SCALE_LIMIT))
        plt.title(self.json_analyzer.residual_graph_title)
        plt.xlabel(self.json_analyzer.residual_x_scale_label_title)
        plt.ylabel(self.json_analyzer.residual_y_scale_label_title)

    def build_graph(self):
        """
        In charge of building the graph.
        First builds an error bar graph, with the user configuration.
        After that calculates the treadline and builds the relevant graph.
        :return:
        """
        self.init_graph()
        plt.errorbar(self.x_data,
                     self.y_data,
                     xerr=self.csv_analyzer.get_x_error_data(),
                     yerr=self.csv_analyzer.get_y_error_data(), fmt='--o',
                     linestyle='None', ecolor="red", color="black")
        opt, cov = curve_fit(self.equation,
                             np.array(self.x_data),
                             np.array(self.y_data),
                             maxfev=MAX_FEV)
        treadline_x = np.linspace(min(self.x_data),
                                  max(self.x_data),
                                  len(self.x_data) * 10)
        treadline_y = self.equation(treadline_x, *opt)
        plt.plot(treadline_x, treadline_y)
        plt.show()
        plt.clf()
        return opt

    def build_residual_graph(self, opt):
        diff = []
        for i, xval in enumerate(self.x_data):
            diff.append([self.y_data[i] - self.equation(xval, *opt)])
        self.init_residual_graph(diff)
        plt.scatter(self.x_data, diff)
        plt.show()

    def print_opt(self, opt):
        args = getfullargspec(self.equation).args[1:]
        msg = "The variables found are: \n"
        for i in range(len(opt)):
            msg += "{}: {} \n".format(args[i], opt[i])
        ctypes.windll.user32.MessageBoxW(0, msg, "variables", 1)
