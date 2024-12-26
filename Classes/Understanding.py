# importing libraries
import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class DataLoader:
    """Class to Load data"""
    def __init__(self):      
        pass

    def read_data(self, file_path):
        _, file_ext = os.path.splitext(file_path)
        """
        Load data from a CSV, TSV, JSON or Excel file
        """
        if file_ext == '.csv':
            return pd.read_csv(file_path, index_col=None)
        
        elif file_ext == '.tsv':
            return pd.read_csv(file_path, sep='\t')

        elif file_ext == '.json':
            return pd.read_json(file_path)

        elif file_ext in ['.xls', '.xlsx']:
            return pd.read_excel(file_path)

        else:
            raise ValueError(f"Unsupported file format:")