import matplotlib.pyplot as plt


def plot_metrics(metrics):
    """
    Traza métricas de series temporales como seguidores, publicaciones, me gusta y comentarios.

    Args:
    metrics (DataFrame): La DataFrame que contiene las metricas a trazar.
    """
    plt.figure(figsize=(14, 7))

    # Trazando cada metrica en el grafico
    plt.plot(metrics['fecha'], metrics['seguidores'], label='Seguidores', marker='o')
    plt.plot(metrics['fecha'], metrics['posts'], label='Posts', marker='o')
    plt.plot(metrics['fecha'], metrics['likes'], label='Likes', marker='o')
    plt.plot(metrics['fecha'], metrics['comentarios'], label='Comentarios', marker='o')

    # Añade los titulos
    plt.title('Análisis de Redes Sociales a lo Largo del Tiempo')
    plt.xlabel('Fecha')
    plt.ylabel('Cantidad')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Muestra el plot
    plt.show()
