import pandas as pd
from tkinter import Tk, Button, Label, messagebox
from data_analysis import perform_analysis
from plotting import plot_graph
from export_pdf import export_pdf

# Load the Excel file
file_path = "Mega-Sena.xlsx"  # Update the file path as necessary


def main():
    # Perform data analysis and get necessary data
    global mega_sena_data, bola_counts, sem_ganhadores_frequencia, estado_counts, ganhadores_faixa, correlation_matrix, media_numeros, tendencia_acumulado
    (
        mega_sena_data,
        bola_counts,
        sem_ganhadores_frequencia,
        estado_counts,
        ganhadores_faixa,
        correlation_matrix,
        media_numeros,
        tendencia_acumulado,
    ) = perform_analysis(file_path)

    # Create the main window
    root = Tk()
    root.title("Análise da Mega Sena")

    # Create a label
    label = Label(
        root,
        text="Escolha o gráfico que deseja visualizar ou exportar para PDF:",
        font=("Arial", 14),
    )
    label.pack(pady=20)

    # Create buttons for each option
    buttons = [
        ("Números mais sorteados", 1),
        ("Evolução dos valores acumulados ao longo do tempo", 2),
        ("Frequência de concursos sem ganhadores", 3),
        ("Distribuição dos prêmios por estado (principais)", 4),
        ("Quantidade de ganhadores por faixa de prêmio", 5),
        ("Correlação entre os números sorteados", 6),
        ("Média de números sorteados por concurso", 7),
        ("Distribuição dos valores dos prêmios de 6 acertos ao longo do tempo", 8),
        ("Análise de tendência dos prêmios acumulados", 9),
        ("Exportar todos os gráficos para PDF", 10),
    ]

    for text, value in buttons:
        button = Button(
            root,
            text=text,
            command=lambda v=value: on_button_click(v),
            font=("Arial", 12),
            width=50,
        )
        button.pack(pady=5)

    # Create an exit button
    exit_button = Button(
        root, text="Sair", command=root.quit, font=("Arial", 12), width=50
    )
    exit_button.pack(pady=20)

    # Start the main loop
    root.mainloop()


def on_button_click(choice):
    if choice == 10:
        export_pdf(
            mega_sena_data,
            bola_counts,
            sem_ganhadores_frequencia,
            estado_counts,
            ganhadores_faixa,
            correlation_matrix,
            media_numeros,
            tendencia_acumulado,
        )
        messagebox.showinfo("Exportação", "Gráficos exportados para PDF com sucesso!")
    else:
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


if __name__ == "__main__":
    main()
