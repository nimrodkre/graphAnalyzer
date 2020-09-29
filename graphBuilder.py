import numpy as np
from csvAnalyzer import CsvAnalyzer
import matplotlib.pyplot as plt
from jsonAnalyzer import JsonAnalyzer
from scipy.optimize import curve_fit
from graphAnalyzerError import graphAnalyzerError
from equation import equation

SCALE_LIMIT = 0.05


class GraphBuilder:
    def __init__(self, json_analyzer, csv_analyzer):
        self.json_analyzer = json_analyzer
        self.csv_analyzer = csv_analyzer

    def check_data(self):
        if len(self.csv_analyzer.get_x_data()) == len(
                self.csv_analyzer.get_y_data()) == len(
            self.csv_analyzer.get_x_error_data()) == len(
            self.csv_analyzer.get_y_error_data()):
            return True
        raise graphAnalyzerError(
            "The length of the columns received are not equal")

    def get_xlimit(self):
        if any([self.json_analyzer.x_scale_minimum,
                self.json_analyzer.x_scale_maximum]):
            return (self.json_analyzer.x_scale_minimum,
                    self.json_analyzer.x_scale_maximum)
        return (min(self.csv_analyzer.get_x_data()) - min(
            self.csv_analyzer.get_x_data()) * SCALE_LIMIT,
                max(self.csv_analyzer.get_x_data()) + max(
                    self.csv_analyzer.get_x_data()) * SCALE_LIMIT)

    def get_ylimit(self):
        if any([self.json_analyzer.y_scale_minimum,
                self.json_analyzer.y_scale_maximum]):
            return (self.json_analyzer.y_scale_minimum,
                    self.json_analyzer.y_scale_maximum)
        return (min(self.csv_analyzer.get_y_data()) - min(
            self.csv_analyzer.get_y_data()) * SCALE_LIMIT,
                max(self.csv_analyzer.get_y_data()) + max(
                    self.csv_analyzer.get_y_data()) * SCALE_LIMIT)

    def init_graph(self):
        plt.xlim(self.get_xlimit())
        plt.ylim(self.get_ylimit())
        plt.title(self.json_analyzer.graph_title)
        plt.xlabel(self.json_analyzer.x_scale_label_title)
        plt.ylabel(self.json_analyzer.y_scale_label_title)

    def build_graph(self):
        self.init_graph()
        plt.errorbar(self.csv_analyzer.get_x_data(),
                     self.csv_analyzer.get_y_data(),
                     xerr=self.csv_analyzer.get_x_error_data(),
                     yerr=self.csv_analyzer.get_y_error_data(), fmt='--o',
                     linestyle='None', ecolor="red", color="black")
        opt, cov = curve_fit(equation,
                             np.array(self.csv_analyzer.get_x_data()),
                             np.array(self.csv_analyzer.get_y_data()),
                             maxfev=25000)
        print(opt)
        treadline_x = np.linspace(min(self.csv_analyzer.get_x_data()),
                                  max(self.csv_analyzer.get_x_data()),
                                  len(self.csv_analyzer.get_x_data()) * 10)
        treadline_y = equation(treadline_x, *opt)
        plt.plot(treadline_x, treadline_y)
        plt.show()


json = JsonAnalyzer()
csv = CsvAnalyzer(json.excel_file_location, json.x_axis_column_name,
                  json.y_axis_column_name, json.x_axis_errors_column_name,
                  json.y_axis_errors_column_name)
graph = GraphBuilder(json, csv)
graph.build_graph()
