import pandas as pd

def load_data(path, file_name):
    """
        Utility function to load csv data

        Arguments:
            path (str)
            file_name (str)
        Returns:
            df (Pandas DataFrame)
    """

    file_name = "native_plants_AL_MI_v_1.csv"
    df = pd.read_csv(f"{path}{file_name}")

    entries = len(df)

    print(f"{entries} entries have been loaded")

    return df

def filter_dataframe(df, filter_dict):
    """
        Utility funciton that filters a dataframe based on a dictionary
        Arguments:
            df (Pandas DataFrame)
            filter_dict (dict)
        Returns:
            df_filtered (Pandas DataFrame)
    """

    df_filtered = df.copy()
    for key, value in filter_dict.items():
        # Case-insensitive comparison for keys
        key_lower = key.lower()
        if key_lower in map(str.lower, df_filtered.columns):
            if isinstance(value, list):  # Handle list filtering
                df_filtered = df_filtered[df_filtered[key_lower].isin(value)]
            else:
                # Case-insensitive comparison for values
                value_lower = str(value).lower()
                df_filtered = df_filtered[df_filtered[key_lower].fillna('').astype(str).str.lower().str.contains(value_lower)]

    return df_filtered