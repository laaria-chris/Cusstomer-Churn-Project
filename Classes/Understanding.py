# importing libraries
import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display, HTML


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

class DataInfo:
    """Class to get dataset information """
    def __init__(self):      
        pass

    def info(self, df): 
        """
        Displaying Relevant Information on the the Dataset Provided
        """    
        # Counting no of rows 
        print('=='*20 + f'\nShape of the dataset : {df.shape} \n' + '=='*20 + '\n')
        
        # Extracting column names
        column_name =  df.columns 
        print('=='*20 + f'\nColumn Names\n' + '=='*20 +  f'\n{column_name} \n \n')
        
        # Data type info
        print('=='*20 + f'\nData Summary\n' + '=='*20 )
        data_summary = df.info() 
        print('=='*20 +'\n')

        # Descriptive statistics
        describe =  df.describe() 
        print('=='*20 + f'\nDescriptive Statistics\n' + '=='*20  )
        display(describe)
        
        #Display the dataset
        print('=='*20 + f'\nDataset Overview\n'+ '=='*20 )
        return df.head(3)
class DataChecks:
    """Class to Perform various checks on the dataset"""
    def __init__(self, df):
        self.df =df
        self.categorical_columns = [] 
        self.numerical_columns =[]
        self._identify_columns()

    def _identify_columns(self):
        """
        Identify numerical and categorical columns.
        """
        for col in self.df.columns:
            if self.df[col].dtype == object:
                self.categorical_columns.append(col)
            else:
                self.numerical_columns.append(col)
        
    def check_duplicates(self):
        """
        Displaying the duplicated rows for visual assesment
        """
        df_sorted = self.df.sort_values(by=self.df.columns.tolist())

        # Find duplicated rows
        duplicates = df_sorted[df_sorted.duplicated(keep=False)]

        if not duplicates.empty:
            # Display the duplicated rows as HTML
            display(HTML(duplicates.to_html()))
        else:
            print("NO DUPLICATES FOUND")

    def check_missing(self):
        """
        Identify Null values in dataset as value count and percentage 
        """
        # Get features with null values
        null_features = self.df.columns[self.df.isnull().any()].tolist()
        
        if null_features:
            # Calculate the number of missing values for each feature
            null_counts = self.df[null_features].isnull().sum()
            
            # Calculate the percentage of missing data for each feature
            null_percentages = self.df[null_features].isnull().mean() * 100
            
            # Create a DataFrame to display the results
            null_info = pd.DataFrame({
                'Column Names': null_features,
                'Missing Values': null_counts,
                'Percentage Missing': null_percentages
            }).reset_index(drop=True)
            
            # Display the results
            display(null_info)
        else:
            print("NO NULL VALUES FOUND")  
   # check for outliers in restaurant dataset
    def check_outliers_and_plot(self):
      outlier_columns = [...]  # Your logic to determine outlier columns
      num_rows = len(outlier_columns) // 3 + (len(outlier_columns) % 3 > 0)
      num_cols = min(len(outlier_columns), 3)
    
      fig, axes = plt.subplots(nrows=num_rows, ncols=num_cols, figsize=(20, 8))
    
    # If there's only one subplot, axes will not be an array
      if num_rows == 1 and num_cols == 1:
        axes = [axes]  # Convert to a list for consistency
      elif num_rows == 1:
        axes = axes.flatten()  # This will work if there's more than one column
      elif num_cols == 1:
        axes = axes.flatten()  # This will work if there's more than one row
      else:
        axes = axes.flatten()  # This will work for multiple rows and columns

      for i, column in enumerate(outlier_columns):
        sns.boxplot(x=self.df[column], ax=axes[i])
    
      plt.tight_layout()
      plt.show()
