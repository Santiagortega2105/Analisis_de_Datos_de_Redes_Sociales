def load_data(filepath):
    """
    Carga los datos de un archivo CSV en un DataFrame de Panda.

    Args:
    filepath (str): El path para el CSV file.

    Returns:
    DataFrame: Pandas DataFrame con la data cargada en el.
    """
    import pandas as pd
    return pd.read_csv(filepath)