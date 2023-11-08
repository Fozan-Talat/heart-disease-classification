import pandas as pd

# User-defined functions

def dataset_dimensions(df):
    """
    Show dimensions of the dataframe.
    """
    num_rows, num_columns = df.shape
    print("Dimensions of the dataset:")
    print(f" Number of rows: {num_rows: >9}")
    print(f" Number of columns: {num_columns}\n")

    

def camel_to_snake_case(name):
    """
    Convert a name from CamelCase to snake_case.
    """
    return ''.join(['_' + char.lower() if char.isupper() else char for char in name]).lstrip('_')

def rename_columns(df):
    """
    Rename dataframe columns from CamelCase to snake_case
    """
    df.columns = [camel_to_snake_case(col) if col != 'b_m_i' else 'bmi' for col in df.columns]

    

def column_unique_values(df):
    """
    Show unique values for each column in the dataframe.
    """
    unique_counts = df.nunique()
    print("Unique values in each column:")
    for col, count in unique_counts.items():
        print(f"{col: >24}: {count}")

    

def column_missing_values(df):
    """
    Show the total number of missing values per columns, if they are present.
    """
    missing_values = df.isnull().sum()
    missing_columns = missing_values[missing_values > 0]
    if not missing_columns.empty:
        print("Columns with missing values:")
        print(missing_columns)
    else:
        print('No missing values found!')
    

# Example usage:
if __name__ == '__main__':
    data = {
        'ColumnNameOne': [1, 2, 3],
        'ColumnNameTwo': [4, None, 6],
        'ColumnNameThree': [7, 8, 9]
    }
    df = pd.DataFrame(data)
    
    dataset_dimensions(df)
    rename_columns(df)
    column_unique_values(df)
    column_missing_values(df)
