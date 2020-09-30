from GraphBuilder import GraphBuilder
from JsonAnalyzer import JsonAnalyzer
from CsvAnalyzer import CsvAnalyzer
from GraphAnalyzerError import GraphAnalyzerError
import sys
import os
import importlib.util


USAGE_MSG = "Usage: <jsonFileLocation> <Equation.py>"
JSON_ENDING = ".json"
PYTHON_ENDING = "py"
EQUATION_FILE_NAME = "Equation"


def check_data():
    if len(sys.argv) != 3:
        raise GraphAnalyzerError(USAGE_MSG)

    name, extension = os.path.splitext(sys.argv[1])
    if extension != JSON_ENDING:
        raise GraphAnalyzerError(USAGE_MSG)

    name = os.path.basename(sys.argv[2]).split(".")

    try:
        if name[0] != EQUATION_FILE_NAME or name[1] != PYTHON_ENDING:
            raise GraphAnalyzerError(
                "The second argument must be path to Equation.py file")
    except IndexError:
        raise GraphAnalyzerError(USAGE_MSG)

    try:
        file = open(sys.argv[1], 'r')
        file.close()
    except (IOError, FileNotFoundError, FileExistsError) as e:
        raise GraphAnalyzerError("Error while trying to open json file")


if __name__ == "__main__":
    check_data()
    json = JsonAnalyzer(sys.argv[1])
    csv = CsvAnalyzer(json.excel_file_location, json.x_axis_column_name,
                      json.y_axis_column_name, json.x_axis_errors_column_name,
                      json.y_axis_errors_column_name)
    spec = importlib.util.spec_from_file_location("Equation.equation", sys.argv[2])
    equation = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(equation)
    graph = GraphBuilder(json, csv, equation.equation)
    opt = graph.build_graph()
    graph.build_residual_graph(opt)
    graph.print_opt(opt)
