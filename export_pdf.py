import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from plotting import plot_graph  # Importando a função plot_graph do arquivo plotting.py


# Função para exportar gráficos para PDF
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
        # Exportando cada gráfico para o PDF
        for choice in range(1, 10):
            plt.figure()
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
            pdf.savefig()  # Salva a figura atual no PDF
            plt.close()  # Fecha a figura para liberar memória

    print(f"Resultados exportados para '{pdf_file}'")
