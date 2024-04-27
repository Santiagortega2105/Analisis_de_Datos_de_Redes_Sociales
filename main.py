from utils import load_data, calculate_metrics, plot_metrics


def main():
    # Ruta al archivo CSV que contiene los datos
    filepath = 'utils/social_media_data.csv'

    # Cargar los datos
    data = load_data(filepath)

    # Calcular las métricas necesarias
    metrics = calculate_metrics(data)

    # Generar y mostrar los gráficos
    plot_metrics(metrics)


if __name__ == '__main__':
    main()
