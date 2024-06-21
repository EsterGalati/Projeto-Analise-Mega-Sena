import pandas as pd
from data_analysis import perform_analysis
from plotting import plot_graph
from export_pdf import export_pdf

# Load the Excel file
file_path = "Mega-Sena.xlsx"  # Update the file path as necessary


def main():
    # Perform data analysis and get necessary data
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

    # Show the statistics
    print(f"Números mais sorteados:\n{bola_counts.head()}\n")
    print(f"Frequência de concursos sem ganhadores: {sem_ganhadores_frequencia:.2f}%")
    print(f"Distribuição dos prêmios por estado:\n{estado_counts}\n")
    print(f"Quantidade de ganhadores por faixa de prêmio:\n{ganhadores_faixa}\n")
    print(f"Correlação entre os números sorteados:\n{correlation_matrix}\n")
    print(f"Média de números sorteados por concurso:\n{media_numeros}\n")
    print(
        f"Tendência dos prêmios acumulados ao longo dos anos:\n{tendencia_acumulado}\n"
    )

    # Menu for user to select which graph to display or export to PDF
    while True:
        print("\nEscolha o gráfico que deseja visualizar ou exportar para PDF:")
        print("1 - Números mais sorteados")
        print("2 - Evolução dos valores acumulados ao longo do tempo")
        print("3 - Frequência de concursos sem ganhadores")
        print("4 - Distribuição dos prêmios por estado (principais)")
        print("5 - Quantidade de ganhadores por faixa de prêmio")
        print("6 - Correlação entre os números sorteados")
        print("7 - Média de números sorteados por concurso")
        print("8 - Distribuição dos valores dos prêmios de 6 acertos ao longo do tempo")
        print("9 - Análise de tendência dos prêmios acumulados")
        print("10 - Exportar todos os gráficos para PDF")
        print("0 - Sair")

        choice = input("Digite o número da sua escolha: ")

        if choice.isdigit():
            choice = int(choice)
            if choice == 0:
                break
            elif choice == 10:
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
        else:
            print("Entrada inválida. Por favor, digite um número de 0 a 10.")


if __name__ == "__main__":
    main()
