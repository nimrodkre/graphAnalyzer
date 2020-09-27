import pandas as pd

class csvAnalyzer:
    def __init__(self, filename, x_column_name, y_column_name):
        self.data = pd.read_csv(filename)
        self.x_column_name = x_column_name
        self.y_column_name = y_column_name
