import json
from GraphAnalyzerError import GraphAnalyzerError


class JsonAnalyzer:
    def __init__(self, filelocation):
        with open(filelocation, "r") as json_data:
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
            self.residual_graph_title = self.graph_data["residual_graph_title"]
            self.x_scale_label_title = self.graph_data["x_scale_label_title"]
            self.y_scale_label_title = self.graph_data["y_scale_label_title"]
            self.residual_x_scale_label_title = self.graph_data[
                "residual_x_scale_label_title"]
            self.residual_y_scale_label_title = self.graph_data[
                "residual_y_scale_label_title"]
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
    def residual_graph_title(self):
        return self._residual_graph_title

    @property
    def x_scale_label_title(self):
        return self._x_scale_label_title

    @property
    def y_scale_label_title(self):
        return self._y_scale_label_title    \

    @property
    def residual_x_scale_label_title(self):
        return self._residual_x_scale_label_title

    @property
    def residual_y_scale_label_title(self):
        return self._residual_y_scale_label_title

    @excel_file_location.setter
    def excel_file_location(self, location):
        if not type(location) == str:
            raise GraphAnalyzerError("File location must be a string")
        try:
            file = open(location, 'r')
            file.close()
        except (IOError, FileNotFoundError, FileExistsError) as e:
            raise GraphAnalyzerError("Csv file was not found")
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
        self._graph_title = title    \

    @residual_graph_title.setter
    def residual_graph_title(self, title):
        if not type(title) == str:
            raise GraphAnalyzerError(
                "residual graph title must be a string")
        self._residual_graph_title = title

    @x_scale_label_title.setter
    def x_scale_label_title(self, title):
        if not type(title) == str:
            raise GraphAnalyzerError(
                "x scale label title must be a string")
        self._x_scale_label_title = title

    @y_scale_label_title.setter
    def y_scale_label_title(self, title):
        if not type(title) == str:
            raise GraphAnalyzerError(
                "y scale label title must be a string")
        self._y_scale_label_title = title    \

    @residual_x_scale_label_title.setter
    def residual_x_scale_label_title(self, title):
        if not type(title) == str:
            raise GraphAnalyzerError(
                "residual x scale label title must be a string")
        self._residual_x_scale_label_title = title

    @residual_y_scale_label_title.setter
    def residual_y_scale_label_title(self, title):
        if not type(title) == str:
            raise GraphAnalyzerError(
                "residual y scale label title must be a string")
        self._residual_y_scale_label_title = title
