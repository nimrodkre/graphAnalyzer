import json
from GraphAnalyzerError import GraphAnalyzerError


class JsonAnalyzer:
    def __init__(self):
        with open("graphDescription.json", "r") as json_data:
            self.graph_data = json.load(json_data, strict=False)
        try:
            self.excel_file_location = self.graph_data["excel_file_location"]
            self.x_axis_column_name = self.graph_data["x_axis_column_name"]
            self.y_axis_column_name = self.graph_data["y_axis_column_name"]
            self.x_axis_errors_column_name = self.graph_data[
                "x_axis_errors_column_name"]
            self.y_axis_errors_column_name = self.graph_data[
                "y_axis_errors_column_name"]
            self.graph_title = self.graph_data["graph_title"]
            self.x_scale_label_title = self.graph_data["x_scale_label_title"]
            self.x_scale_minimum = self.graph_data["x_scale_minimum"]
            self.x_scale_maximum = self.graph_data["x_scale_maximum"]
            self.y_scale_label_title = self.graph_data["y_scale_label_title"]
            self.y_scale_minimum = self.graph_data["y_scale_minimum"]
            self.y_scale_maximum = self.graph_data["y_scale_maximum"]
        except KeyError as err:
            raise GraphAnalyzerError(
                "In the json file you forgot to add a row for {}. \n"
                "Look at the documentation".format(err))

    @property
    def excel_file_location(self):
        return self._excel_file_location

    @property
    def x_axis_column_name(self):
        return self._x_axis_column_name

    @property
    def y_axis_column_name(self):
        return self._y_axis_column_name

    @property
    def x_axis_errors_column_name(self):
        return self._x_axis_errors_column_name

    @property
    def y_axis_errors_column_name(self):
        return self._y_axis_errors_column_name

    @property
    def graph_title(self):
        return self._graph_title

    @property
    def x_scale_label_title(self):
        return self._x_scale_label_title

    @property
    def x_scale_minimum(self):
        return self._x_scale_minimum

    @property
    def x_scale_maximum(self):
        return self._x_scale_maximum

    @property
    def y_scale_label_title(self):
        return self._y_scale_label_title

    @property
    def y_scale_minimum(self):
        return self._y_scale_minimum

    @property
    def y_scale_maximum(self):
        return self._y_scale_maximum

    @excel_file_location.setter
    def excel_file_location(self, location):
        if not type(location) == str:
            raise GraphAnalyzerError("file location must be a string")
        self._excel_file_location = location

    @x_axis_column_name.setter
    def x_axis_column_name(self, col_name):
        if not type(col_name) == str:
            raise GraphAnalyzerError("x axis column name must be a string")
        self._x_axis_column_name = col_name

    @y_axis_column_name.setter
    def y_axis_column_name(self, col_name):
        if not type(col_name) == str:
            raise GraphAnalyzerError("y axis column name must be a string")
        self._y_axis_column_name = col_name

    @x_axis_errors_column_name.setter
    def x_axis_errors_column_name(self, col_name):
        if not type(col_name) == str:
            raise GraphAnalyzerError(
                "x axis errors column name must be a string")
        self._x_axis_errors_column_name = col_name

    @y_axis_errors_column_name.setter
    def y_axis_errors_column_name(self, col_name):
        if not type(col_name) == str:
            raise GraphAnalyzerError(
                "y axis errors column name must be a string")
        self._y_axis_errors_column_name = col_name

    @graph_title.setter
    def graph_title(self, title):
        if not type(title) == str:
            raise GraphAnalyzerError(
                "graph title must be a string")
        self._graph_title = title

    @x_scale_label_title.setter
    def x_scale_label_title(self, title):
        if not type(title) == str:
            raise GraphAnalyzerError(
                "x scale label title must be a string")
        self._x_scale_label_title = title

    @x_scale_minimum.setter
    def x_scale_minimum(self, title):
        if not type(title) in [float, int]:
            raise GraphAnalyzerError(
                "x scale minimum must be a float")
        self._x_scale_minimum = title

    @x_scale_maximum.setter
    def x_scale_maximum(self, title):
        if not type(title) in [float, int]:
            raise GraphAnalyzerError(
                "x scale maximum must be a float")
        self._x_scale_maximum = title

    @y_scale_label_title.setter
    def y_scale_label_title(self, title):
        if not type(title) == str:
            raise GraphAnalyzerError(
                "y scale label title must be a string")
        self._y_scale_label_title = title

    @y_scale_minimum.setter
    def y_scale_minimum(self, title):
        if not type(title) in [float, int]:
            raise GraphAnalyzerError(
                "y scale minimum must be a float")
        self._y_scale_minimum = title

    @y_scale_maximum.setter
    def y_scale_maximum(self, title):
        if not type(title) in [float, int]:
            raise GraphAnalyzerError(
                "y scale maximum must be a float")
        self._y_scale_maximum = title
