import pandas as pd


def calculate_metrics(data):
    """
    Procesa un DataFrame para calcular las metricas en el tiempo.

    Args:
    data (DataFrame): El input data que contiene las metricas de las redes sociales.

    Returns:
    DataFrame: Un DataFrame con métricas calculadas como la tasa total y de crecimiento de seguidores, publicaciones,
    me gusta y comentarios.
    """
    # Asumiendo que la data incluye columnas como 'fecha', 'seguidores', 'posts', 'likes', 'comentarios'
    data['fecha'] = pd.to_datetime(data['fecha'])
    data.sort_values('fecha', inplace=True)

    # Calcular el crecimiento como la diferencia con la entrada anterior.
    data['growth_followers'] = data['seguidores'].diff().fillna(0)
    data['growth_posts'] = data['posts'].diff().fillna(0)
    data['growth_likes'] = data['likes'].diff().fillna(0)
    data['growth_comentarios'] = data['comentarios'].diff().fillna(0)

    return data
