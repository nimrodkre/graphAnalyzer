import json
from graphAnalyzerError import graphAnalyzerError

class jsonAnalyzer:
    def __init__(self):
        with open("graphDescription.json", "r") as json_data:
            self.graph_data = json.load(json_data, strict=False)

        self.excel_file_location = self.graph_data["excel_file_location"]
        self.x_axis_column_name = self.graph_data["x_axis_column_name"]
        self.y_axis_column_name = self.graph_data["y_axis_column_name"]
        self.x_axis_errors_column_name = self.graph_data["x_axis_errors_column_name"]
        self.y_axis_errors_column_name = self.graph_data["y_axis_errors_column_name"]
        self.graph_title = self.graph_data["graph_title"]
        self.x_scale_label_title = self.graph_data["x_scale_label_title"]
        self.x_scale_minimum = self.graph_data["x_scale_minimum"]
        self.x_scale_maximum = self.graph_data["x_scale_maximum"]
        self.y_scale_label_title = self.graph_data["y_scale_label_title"]
        self.y_scale_minimum = self.graph_data["y_scale_minimum"]
        self.y_scale_maximum = self.graph_data["y_scale_maximum"]
        self.graph_equation = self.graph_data["graph_equation"]

    @property
    def excel_file_location(self):
        return self.graph_data["excel_file_location"]

    @property
    def x_axis_column_name(self):
        return self.graph_data["x_axis_column_name"]

    @property
    def y_axis_column_name(self):
        return self.graph_data["y_axis_column_name"]

    @property
    def x_axis_errors_column_name(self):
        return self.graph_data["x_axis_errors_column_name"]

    @property
    def y_axis_errors_column_name(self):
        return self.graph_data["y_axis_errors_column_name"]

    @property
    def graph_title(self):
        return self.graph_data["graph_title"]

    @property
    def x_scale_label_title(self):
        return self.graph_data["x_scale_label_title"]

    @property
    def x_scale_minimum(self):
        return self.graph_data["x_scale_minimum"]

    @property
    def x_scale_maximum(self):
        return self.graph_data["x_scale_maximum"]

    @property
    def y_scale_label_title(self):
        return self.graph_data["x_scale_label_title"]

    @property
    def y_scale_minimum(self):
        return self.graph_data["x_scale_minimum"]

    @property
    def y_scale_maximum(self):
        return self.graph_data["x_scale_maximum"]

    @property
    def graph_equation(self):
        return self.graph_data["graph_equation"]

    @excel_file_location.setter
    def excel_file_location(self, location):
        if not type(location) == str:
            raise graphAnalyzerError("file location must be a string")
        self.excel_file_location = location

    @x_axis_column_name.setter
    def x_axis_column_name(self, col_name):
        if not type(col_name) == str:
            raise graphAnalyzerError("x axis column name must be a string")
        self.x_axis_column_name = col_name

    @y_axis_column_name.setter
    def y_axis_column_name(self, col_name):
        if not type(col_name) == str:
            raise graphAnalyzerError("y axis column name must be a string")
        self.y_axis_column_name = col_name