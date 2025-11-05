#!/usr/bin/env python3
import pandas as pd
import numpy as np

#TODO: Add shebang line: #!/usr/bin/env python3
# Assignment 5, Question 3: Data Utilities Library
# Core reusable functions for data loading, cleaning, and transformation.
#
# These utilities will be imported and used in Q4-Q7 notebooks.


def load_data(filepath: str) -> pd.DataFrame:
    """
    Load CSV file into DataFrame.
    
    Args:
        filepath: Path to CSV file

    Returns:
        pd.DataFrame: Loaded data

    Example:
        >>> df = load_data('data/clinical_trial_raw.csv')
        >>> df.shape
        (10000, 18)
    """
    pass

    try:
        df = pd.read_csv(filepath) 
        print(f"data loaded with success: {df.shape[0]},rows and {df.shape[1]} columns")
        return df
    except FilenotFoundError:
        print(f"Error:File not found: {filepath}")
        return pd.DataFrame()
    except Exception as e:
        print (f"Errror loasding: {e}")
        return pd.DataFrame()

    

def clean_data(df: pd.DataFrame, remove_duplicates: bool = True,
               sentinel_value: float = -999) -> pd.DataFrame:
    """
    Basic data cleaning: remove duplicates and replace sentinel values with NaN.

    Args:
        df: Input DataFrame
        remove_duplicates: Whether to drop duplicate rows
        sentinel_value: Value to replace with NaN (e.g., -999, -1)

    Returns:
        pd.DataFrame: Cleaned data

    Example:
        >>> df_clean = clean_data(df, sentinel_value=-999)
    """
    pass
    df_copy = df.copy()
    if remove_duplicates: # remove the dublicates
       df_copy = df_copy.drop_duplicates()  
 #replace the sentinel values with NaN
    df_copy = df_copy.replace([-999, -1], np.nan)
    print("data cleaned") 
    print( df.head())
    return df_copy

def detect_missing(df: pd.DataFrame) -> pd.Series:
    """
    Return count of missing values per column.

    Args:
        df: Input DataFrame

    Returns:
        pd.Series: Count of missing values for each column

    Example:
        >>> missing = detect_missing(df)
        >>> missing['age']
        15
    """
    pass
    
#count missing values per column:
    missing = df.isnull().sum()
    print("\nMissing values per column:")
    print(missing)
    return missing

def fill_missing(df: pd.DataFrame, column: str, strategy: str = 'mean') -> pd.DataFrame:
    """
    Fill missing values in a column using specified strategy.

    Args:
        df: Input DataFrame
        column: Column name to fill
        strategy: Fill strategy - 'mean', 'median', or 'ffill'

    Returns:
        pd.DataFrame: DataFrame with filled values

    Example:
        >>> df_filled = fill_missing(df, 'age', strategy='median')
    """
    
    df_copy = df.copy()
    if strategy == 'mean':
        df_copy[column] = df_copy[column].fillna(df_copy[column].mean())
    elif strategy == 'median':
        df_copy[column] = df_copy[column].fillna(df_copy[column].median())
    elif strategy == 'ffill':
        df_copy[column] = df_copy[column].ffill()
    print(f"Filled missing values in column '{column}' using '{strategy}'")
    return df_copy


def filter_data(df: pd.DataFrame, filters: list) -> pd.DataFrame:
    """
    Apply a list of filters to DataFrame in sequence.

    Args:
        df: Input DataFrame
        filters: List of filter dictionaries, each with keys:
                'column', 'condition', 'value'
                Conditions: 'equals', 'greater_than', 'less_than', 'in_range', 'in_list'

    Returns:
        pd.DataFrame: Filtered data

    Examples:
        >>> # Single filter
        >>> filters = [{'column': 'site', 'condition': 'equals', 'value': 'Site A'}]
        >>> df_filtered = filter_data(df, filters)
        >>>
        >>> # Multiple filters applied in order
        >>> filters = [
        ...     {'column': 'age', 'condition': 'greater_than', 'value': 18},
        ...     {'column': 'age', 'condition': 'less_than', 'value': 65},
        ...     {'column': 'site', 'condition': 'in_list', 'value': ['Site A', 'Site B']}
        ... ]
        >>> df_filtered = filter_data(df, filters)
        >>>
        >>> # Range filter example
        >>> filters = [{'column': 'age', 'condition': 'in_range', 'value': [18, 65]}]
        >>> df_filtered = filter_data(df, filters)
    """
    pass
    df_filtered = df.copy()
 #single filters:
    for f in filters: 
        col = f ['column']
        cond = f[ 'condition']
        val = f [ 'value']  
#multiple filters in order:
        if cond == 'equals':
            df_filtered = df_filtered [df [col]==val]
        elif cond == 'greater_than':
            df_filtered = df_filtered [ df [col]>val]
        elif cond == 'les_than':
            df_filtered = df_filtered [ df [col]<val]
        elif cond == 'in range':
            df_filtered = df_filtered[(df_filtered[col] >= val[0]) & (df_filtered[col] <= val[1])]
        elif cond == 'in list':
                df_filtered = df_filtered[df_filtered[col].insn(val)]
        print(f"filtered data with {len(df_filtered)}")
        return df_filtered 

def transform_types(df: pd.DataFrame, type_map: dict) -> pd.DataFrame:
    """
    Convert column data types based on mapping.

    Args:
        df: Input DataFrame
        type_map: Dict mapping column names to target types
                  Supported types: 'datetime', 'numeric', 'category', 'string'

    Returns:
        pd.DataFrame: DataFrame with converted types

    Example:
        >>> type_map = {
        ...     'enrollment_date': 'datetime',
        ...     'age': 'numeric',
        ...     'site': 'category'
        ... }
        >>> df_typed = transform_types(df, type_map)
    """
    pass
    def clean_text(text):
        if placeholders is None:
            placeholders = [ 'NA', 'N/A', 'null', 'None', '']
        if isinstance(text,str):
            cleaned = text.strip().lower()
            if cleaned in placeholders:
                return np.nan
            return cleaned
        return text

    df_copy = df.copy()
    for col, target_type in type_map.items():
        if target_type == 'datetime':
            df_copy[col] = pd.to_datetime(df_copy[col], errors='coerce')
        elif target_type == 'numeric':
                df_copy[col] = pd.to_numeric(df_copy[col],errors='coerce')
        elif target_type == 'catergory':
            df_copy[col] = df_copy[col].astype('category')
        elif target_type == 'string':
            df_copy[col] = df_copy[col].astype(str)
    print("transformed data as type_map")
    return df_copy

    #cleaning and transforming together :

    def clean_and_transform(df, type_map, placeholders=None):
        df_clean = df.copy()
        for col in df_clean.select_dtypes(include=['object']).columns:
            df_clean[col] = df_clean[col].map(lambda x: clean_text(x,placeholders))
        df_transformed = transform_types (df_clean, type_map)
        return df_transformed



def create_bins(df: pd.DataFrame, column: str, bins: list,
                labels: list, new_column: str = None) -> pd.DataFrame:
    """
    Create categorical bins from continuous data using pd.cut().

    Args:
        df: Input DataFrame
        column: Column to bin
        bins: List of bin edges
        labels: List of bin labels
        new_column: Name for new binned column (default: '{column}_binned')

    Returns:
        pd.DataFrame: DataFrame with new binned column

    Example:
        >>> df_binned = create_bins(
        ...     df,
        ...     column='age',
        ...     bins=[0, 18, 35, 50, 65, 100],
        ...     labels=['<18', '18-34', '35-49', '50-64', '65+']
        ... )
    """
    
    df_copy = df.copy()
    if new_column is None:
        new_column = f"(column_binned)"
        df_copy[new_column] = pd.cut(df_copy[column], bins= bins, labels= labels)
        print(f"created binned column '{new_column}'")
        return df_copy
        
    
def summarize_by_group(df: pd.DataFrame, group_col: str,
                       agg_dict: dict = None) -> pd.DataFrame:
    """
    Group data and apply aggregations.

    Args:
        df: Input DataFrame
        group_col: Column to group by
        agg_dict: Dict of {column: aggregation_function(s)}
                  If None, uses .describe() on numeric columns

    Returns:
        pd.DataFrame: Grouped and aggregated data

    Examples:
        >>> # Simple summary
        >>> summary = summarize_by_group(df, 'site')
        >>>
        >>> # Custom aggregations
        >>> summary = summarize_by_group(
        ...     df,
        ...     'site',
        ...     {'age': ['mean', 'std'], 'bmi': 'mean'}
        ... )
    """
    pass
    if agg_dict is None:
        summary = df.groupby(group_col).describe().reset_index()
    else:
        summary =df.groupby(group_col).agg(agg_dict).reset_index()
    print(f"summarized by group '{group_col}")
    return summary



if __name__ == '__main__':
    # Optional: Test your utilities here
      #load the data:
    df = load_data('data/clinical_trial_raw.csv')
    print("  - load_data()")
    print("Data utilities loaded successfully!")
      # clean the data:
    df_clean = clean_data (df)
    print("  - clean_data()")
    print("Data cleaned successfully") 
    # detect missing :
    missing = detect_missing(df_clean)
    print("  - detect_missing()")
    print("Missing values detected successfully") 
    # fill missing:
    df_filled = fill_missing(df_clean, 'age', strategy='median')
    #df_filled = fill_missing(df_filled, 'test_date', strategy='ffill') 
    print("  - fill_missing()")
    print("missing values filled successfully") 
    # Trasform data : 
    type_map ={
        'enrollment_date': 'datetime',
        'age': 'numeric',
        'site': 'category'
    }
    df_typed = transform_types(df_filled, type_map)
    print("data transformed successfully")
    #filtere data:
    filters = [{'column': 'age', 'condition': 'greater_than', 'value': 18}]
    df_filtered = filter_data(df_typed, filters)
    print("  - filter_data()")
    print("data filtered success")
    #create bins:
    df_binned= create_bins(
        df_filtered,
        column= 'age',
        bins=[0, 18, 35, 50, 65, 100],
        labels = [ '<18', '18-34', '35-49', '50-64', '65+']
    )
    print("  - create_bins()")
    print("data binned successfully") 
    #summarize by group:
    summary = summarize_by_group(
        df,
        'site',
        {'age': ['mean', 'std'], 'bmi': 'mean'}
    )
    print("  - summarize_by_group()")
    print("data summarized successfully")


    print("Available functions:")
    print("  - load_data()")
    print("  - clean_data()")
    print("  - detect_missing()")
    print("  - fill_missing()")
    print("  - filter_data()")
    print("  - transform_types()")
    print("  - create_bins()")
    print("  - summarize_by_group()")
    
    # TODO: Add simple test example here
    # Example:
    # test_df = pd.DataFrame({'age': [25, 30, 35], 'bmi': [22, 25, 28]})
    # print("Test DataFrame created:", test_df.shape)
    # print("Test detect_missing:", detect_missing(test_df))