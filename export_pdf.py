import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from plotting import plot_graph


def export_pdf(
    mega_sena_data,
    bola_counts,
    sem_ganhadores_frequencia,
    estado_counts,
    ganhadores_faixa,
    correlation_matrix,
    media_numeros,
    tendencia_acumulado,
):
    pdf_file = "Mega_Sena_Analises.pdf"

    with PdfPages(pdf_file) as pdf:
        for choice in range(1, 10):
            plot_graph(
                choice,
                mega_sena_data,
                bola_counts,
                sem_ganhadores_frequencia,
                estado_counts,
                ganhadores_faixa,
                correlation_matrix,
                media_numeros,
                tendencia_acumulado,
            )
            pdf.savefig()
            plt.close()

    print(f"Resultados exportados para '{pdf_file}'")
