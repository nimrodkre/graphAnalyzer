import pandas as pd
from graphAnalyzerError import graphAnalyzerError

class csvAnalyzer:
    def __init__(self, filename, x_column_name, y_column_name, x_error_name,
                 y_error_name):
        self.data = pd.read_csv(filename)
        self.x_column_name = x_column_name
        self.y_column_name = y_column_name
        self.x_error_name = x_error_name
        self.y_error_name = y_error_name

    def get_x_data(self):
        try:
            return self.data[self.x_column_name]
        except KeyError:
            raise graphAnalyzerError(
                "The following column does not exist in given csv: {}".format(
                    self.x_column_name))

    def get_y_data(self):
        try:
            return self.data[self.y_column_name]
        except KeyError:
            raise graphAnalyzerError(
                "The following column does not exist in given csv: {}".format(
                    self.x_column_name))

    def get_x_error_data(self):
        try:
            return self.data[self.x_error_name]
        except KeyError:
            raise graphAnalyzerError(
                "The following column does not exist in given csv: {}".format(
                    self.x_error_name))

    def get_y_error_data(self):
        try:
            return self.data[self.y_error_name]
        except KeyError:
            raise graphAnalyzerError(
                "The following column does not exist in given csv: {}".format(
                    self.y_error_name))
