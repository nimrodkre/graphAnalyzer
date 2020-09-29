from GraphBuilder import GraphBuilder
from JsonAnalyzer import JsonAnalyzer
from CsvAnalyzer import CsvAnalyzer

if __name__ == "__main__":
    json = JsonAnalyzer()
    csv = CsvAnalyzer(json.excel_file_location, json.x_axis_column_name,
                      json.y_axis_column_name, json.x_axis_errors_column_name,
                      json.y_axis_errors_column_name)
    graph = GraphBuilder(json, csv)
    opt = graph.build_graph()
    graph.build_residual_graph(opt)
    GraphBuilder.print_opt(opt)
